#!/usr/bin/env python
import sys
import warnings

from idea_stress_tester.crew import IdeaStressTester

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew.
    """
    inputs = {
        'idea': 'An AI-powered automated smart pantry inventory tracker that orders groceries before they expire.'
    }

    try:
        result = IdeaStressTester().crew().kickoff(inputs=inputs)
        print("\n" + "="*50)
        print("🎯 FINAL EXECUTIVE VERDICT & SCORE")
        print("="*50 + "\n")
        print(result)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    idea_input = input("Enter the startup idea for training: ")
    inputs = {
        "idea": idea_input
    }
    try:
        IdeaStressTester().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        IdeaStressTester().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "idea": "An AI-powered personalized diet and nutrition planner."
    }
    try:
        IdeaStressTester().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")


def run_with_trigger():
    """
    Run the crew with trigger payload.
    """
    import json

    if len(sys.argv) < 2:
        raise Exception("No trigger payload provided. Please provide JSON payload as argument.")

    try:
        trigger_payload = json.loads(sys.argv[1])
    except json.JSONDecodeError:
        raise Exception("Invalid JSON payload provided as argument")

    inputs = {
        "crewai_trigger_payload": trigger_payload,
        "idea": trigger_payload.get("idea", "Default business idea")
    }

    try:
        result = IdeaStressTester().crew().kickoff(inputs=inputs)
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew with trigger: {e}")


if __name__ == "__main__":
    run()