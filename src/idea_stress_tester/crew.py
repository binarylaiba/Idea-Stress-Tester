import os
from dotenv import load_dotenv  # type: ignore
from crewai import Agent, Crew, Process, Task, LLM  # type: ignore
from crewai.project import CrewBase, agent, crew, task  # type: ignore

load_dotenv()

# Google Gemini LLM with auto-retries for demand spikes
gemini_llm = LLM(
    model="gemini/gemini-3.6-flash",
    api_key=os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY"),
    max_retries=5,
    timeout=120
)

@CrewBase
class IdeaStressTester:
    """IdeaStressTester crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def optimist_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['optimist_agent'],  # type: ignore
            llm=gemini_llm,
            verbose=True
        )

    @agent
    def critic_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['critic_agent'],  # type: ignore
            llm=gemini_llm,
            verbose=True
        )

    @agent
    def arbiter_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['arbiter_agent'],  # type: ignore
            llm=gemini_llm,
            verbose=True
        )

    @task
    def optimist_task(self) -> Task:
        return Task(
            config=self.tasks_config['optimist_task']  # type: ignore
        )

    @task
    def critic_task(self) -> Task:
        return Task(
            config=self.tasks_config['critic_task']  # type: ignore
        )

    @task
    def arbiter_task(self) -> Task:
        return Task(
            config=self.tasks_config['arbiter_task']  # type: ignore
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,  # type: ignore
            tasks=self.tasks,  # type: ignore
            process=Process.sequential,
            verbose=True,
        )