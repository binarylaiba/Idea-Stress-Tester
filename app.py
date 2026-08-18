import streamlit as st
from idea_stress_tester.crew import IdeaStressTester

st.set_page_config(page_title="Ideas Stress Tester", page_icon="🧠", layout="wide")

st.title("🧠 AI Startup & Idea Stress Tester")
st.caption("Powered by Multi-Agent AI (CrewAI + Gemini)")

idea_input = st.text_area("💡 Enter Your Startup / Business Idea:", placeholder="e.g. Smart automated pantry tracker...", height=120)

if st.button("🚀 Run Stress Test", type="primary", use_container_width=True):
    if not idea_input.strip():
        st.warning("Please enter an idea first.")
    else:
        with st.spinner("Analyzing your idea with 3 AI agents..."):
            try:
                res = IdeaStressTester().crew().kickoff(inputs={"idea": idea_input.strip()})
                st.success("Analysis Complete!")
                st.markdown("---")
                st.markdown(res.raw)
            except Exception as e:
                st.error(f"Error: {e}")

