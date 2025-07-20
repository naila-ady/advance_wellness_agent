import asyncio
from openai.types.responses import ResponseTextDeltaEvent
from runconfig import config
from agents import Runner ,Agent 
from all_agents.escalation_agent import escalation_agent
from all_agents.injurysupport_agent import injury_support_agent
from all_agents.nutrition_agent import nutrition_agent
from tools.goal_analyzer import goal_analyzer
from tools.meal_planner import meal_planner
from tools.scheduler import schedule
from tools.tracker import progress_tracker
from tools.workout_recommender import workout_plan
from context import user_info




name_input = input("👤 Enter your name: ").strip()
uid_input = input("🆔 Enter your User ID (just a number): ").strip()

try:
    uid = int(uid_input)
except ValueError:
    print("❌ Invalid UID. Please enter a numeric value.")
    exit()

context = user_info(name=name_input, uid=uid)


Orchestrator_agent=Agent(
    name="Orchestrator_agent",
    # instructions="""You are a health and wellness agent ,You use tools given to you to analyze goals,
    # give users meal plans,schedule their revisit,give them work out and track their progress.If ask for
    # multiple tsk you use tools and never perform any function .Always use provided tools """,
    instructions="you are health wellness agent",    


tools=[
    escalation_agent.as_tool(
        tool_name="give_escalation",
        tool_description="""You  When a user wants to speak to a human trainer or coach,
        you acknowledge their request and inform them that a real person will follow up shortly ."""
),
    injury_support_agent.as_tool(
        tool_name="give_injurysupport",
        tool_description="""Handles user request to examine physical issues.If user 
        concerns about bones injury , jointPain, or any physical limitation ,you provide them with guidence 
        and treatment """,
    ),
    nutrition_agent.as_tool(
        tool_name="give_nutrition",
        tool_description="""you guide user about their diet plans by taking plans from meal planner,Handles users 
        with special dietary needs such as diabetes, allergies, or gluten intolerance."""

    ),
    goal_analyzer,
    meal_planner,
    schedule,
    progress_tracker,
    workout_plan 
],

handoffs=[
    escalation_agent,
    nutrition_agent,
    injury_support_agent
  
]
)

async def main():
    result=Runner.run_streamed(
        Orchestrator_agent,
        input="I want to get guided with wellness agent about fitness and health",
        run_config=config,
        context= context
        )
    
    
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            print(event.data.delta, end="", flush=True)
    
if __name__ == "__main__":
    asyncio.run(main())

