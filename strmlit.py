import streamlit as st
import asyncio
from runconfig import config
from agents import Runner, Agent
from all_agents.escalation_agent import escalation_agent
from all_agents.injurysupport_agent import injury_support_agent
from all_agents.nutrition_agent import nutrition_agent
from tools.goal_analyzer import goal_analyzer
from tools.meal_planner import meal_planner
from tools.scheduler import schedule
from tools.tracker import progress_tracker
from tools.workout_recommender import workout_plan
from context import user_info
from openai.types.responses import ResponseTextDeltaEvent

# Define Orchestrator Agent
Orchestrator_agent = Agent(
    name="Orchestrator_agent",
    instructions=(
        "1. Ask about goals using goal_analyzer tool, fitness level, meal plans, injury support, workout or challenges.\n"
        "2. Analyze input to determine the most appropriate support.\n"
        "3. Use tools if needed: Goal Analyzer, Meal Planner, Workout Recommender, etc.\n"
        "4. Hand off to specialized agents when appropriate: NutritionExpertAgent, InjurySupportAgent, EscalationAgent."
    ),
    tools=[
        escalation_agent.as_tool("give_escalation", "Handles requests to speak with a human coach."),
        injury_support_agent.as_tool("give_injurysupport", "Supports users with injury concerns."),
        nutrition_agent.as_tool("give_nutrition", "Provides diet guidance."),
        goal_analyzer,
        meal_planner,
        schedule,
        progress_tracker,
        workout_plan
    ],
)

st.set_page_config(page_title="Health & Wellness Chat", page_icon="💬")
st.title("Health & Wellness Planner Agent")
st.markdown("""
💬 **Welcome to the Health & Wellness Planner!**

Please choose your goal category:

- 🍽️ Nutrition Diet / Meal Planner  
- 🏥 Fitness Training / Gym / Workout  
- 🧠 Mental Health  
- 🤕 Injury Support  
- 👋 exit
""")
if "messages" not in st.session_state:
    st.session_state.messages = []
if "context" not in st.session_state:
    with st.sidebar:
        st.subheader("User Setup")
        name_input = st.text_input("Enter your name")
        uid_input = st.text_input("Enter your User ID (number)", value="1")
        if name_input and uid_input.isdigit():
            st.session_state.context = user_info(name=name_input, uid=int(uid_input))
            st.success("User context initialized.")
        else:
            st.warning("Please enter valid user info to begin.")
            
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


user_input = st.chat_input("Ask me anything about your health goals...")

if user_input and "context" in st.session_state:
    
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    
    assistant_box = st.chat_message("assistant")
    assistant_stream = assistant_box.empty()
    st.session_state.messages.append({"role": "assistant", "content": ""}) 

    async def get_agent_response():
        result = Runner.run_streamed(
            Orchestrator_agent,
            input=user_input,
            run_config=config,
            context=st.session_state.context,
        )
        full_response = ""
        async for event in result.stream_events():
            if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
                delta = event.data.delta
                full_response += delta
                assistant_stream.markdown(full_response + "▌")
        assistant_stream.markdown(full_response)
        st.session_state.messages[-1]["content"] = full_response

    asyncio.run(get_agent_response())

elif user_input:
    st.warning("⚠️ Please enter user name and ID in the sidebar first.")

