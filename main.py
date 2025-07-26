# import asyncio
# from openai.types.responses import ResponseTextDeltaEvent
# from runconfig import config
# from agents import Runner, Agent
# from all_agents.escalation_agent import escalation_agent
# from all_agents.injurysupport_agent import injury_support_agent
# from all_agents.nutrition_agent import nutrition_agent
# from tools.goal_analyzer import goal_analyzer
# from tools.meal_planner import meal_planner
# from tools.scheduler import schedule
# from tools.tracker import progress_tracker
# from tools.workout_recommender import workout_plan
# from context import user_info



# Orchestrator_agent = Agent(
#     name="Orchestrator_agent",
#     instructions=(
#         "1.Ask about goals by using goal_analyzer tool,fitness level, meal plans, injury support, workout or any challenges."
#         "Please choose your goal category:\n"
#         "- 🍽️ Nutrition Diet / Meal Planner\n"
#         "- 🏥 Fitness Training / Gym / Workout\n"
#         "- 🧠 Mental Health\n"
#         "- 🤕 Injury Support\n"
#         "- 👋 exit"
#         "2. Analyze input to determine the most appropriate support."
#         "3. Use tools if needed: Goal Analyzer, Meal Planner, Workout Recommender, etc."
#         "4. Hand off to specialized agents when appropriate: NutritionExpertAgent, InjurySupportAgent, EscalationAgent"
#     ),
        
#     tools=[
#         escalation_agent.as_tool(
#             tool_name="give_escalation",
#             tool_description="Handles requests to speak with a human coach."
#         ),
#         injury_support_agent.as_tool(
#             tool_name="give_injurysupport",
#             tool_description="Supports users with injury concerns like joint pain or muscle issues."
#         ),
#         nutrition_agent.as_tool(
#             tool_name="give_nutrition",
#             tool_description="Provides diet guidance using meal planning tools."
#         ),
#         goal_analyzer,
#         meal_planner,
#         schedule,
#         progress_tracker,
#         workout_plan
#     ],
# )



# async def main():
#     name_input = input("Enter your name: ").strip()
#     uid_input = input("Enter your User ID (just a number): ").strip()
#     try:
#         uid=int(uid_input)
#     except ValueError:
#         print("❌ Invalid UID. Please enter a numeric value.")
#         return
    
        
#     context = user_info(name=name_input, uid=uid)

#     print("\n💬 Welcome to the Health & Wellness Planner!")
    
#     print(""" 
#         Please choose your goal category
#         🍽️ Nutrition Diet / Meal Planner
#         🏥 Fitness Training / Gym / Workou
#         🧠 Mental Health
#         🤕 Injury Support
#         👋 exit
# """)

#     while True:
#         user_input = input("You: ").strip()
#         if user_input.lower() in {"exit", "quit"}:
#             print("👋 Goodbye! Take care.")
#             break
#         result = Runner.run_streamed(
#             Orchestrator_agent,
#             input=user_input,
#             run_config=config,
#             context=context
#         )
#         full_response = ""
#         async for event in result.stream_events():
#             if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
#                 delta = event.data.delta
#                 print(delta, end="", flush=True)
#                 full_response += delta
#         print() 
# if __name__ == "__main__":
#     asyncio.run(main())

import asyncio
from runconfig import config
from agents import Runner, Agent
from context import user_info
from all_agents.escalation_agent import escalation_agent
from all_agents.injurysupport_agent import injury_support_agent
from all_agents.nutrition_agent import nutrition_agent
from tools.goal_analyzer import goal_analyzer
from tools.meal_planner import meal_planner
from tools.scheduler import schedule
from tools.tracker import progress_tracker
from tools.workout_recommender import workout_plan
from utils.streaming import stream_agent_response  

Orchestrator_agent = Agent(
    name="Orchestrator_agent",
    instructions=(
        "1. Ask about goals by using goal_analyzer tool, fitness level, meal plans, injury support, workout or any challenges.\n"
        "2. Analyze input to determine the most appropriate support.\n"
        "3. Use tools if needed: Goal Analyzer, Meal Planner, Workout Recommender, etc.\n"
        "4. Hand off to specialized agents when appropriate: NutritionExpertAgent, InjurySupportAgent, EscalationAgent.\n"
        "Please choose your goal category:\n"
        "- 🍽️ Nutrition Diet / Meal Planner\n"
        "- 🏥 Fitness Training / Gym / Workout\n"
        "- 🧠 Mental Health\n"
        "- 🤕 Injury Support\n"
        "- 👋 exit"
    ),
    tools=[
        escalation_agent.as_tool(
            tool_name="give_escalation",
            tool_description="Handles requests to speak with a human coach."
        ),
        injury_support_agent.as_tool(
            tool_name="give_injurysupport",
            tool_description="Supports users with injury concerns like joint pain or muscle issues."
        ),
        nutrition_agent.as_tool(
            tool_name="give_nutrition",
            tool_description="Provides diet guidance using meal planning tools."
        ),
        goal_analyzer,
        meal_planner,
        schedule,
        progress_tracker,
        workout_plan
    ],
)


async def main():
    name_input = input("Enter your name: ").strip()
    uid_input = input("Enter your User ID (just a number): ").strip()
    try:
        uid = int(uid_input)
    except ValueError:
        print("❌ Invalid UID. Please enter a numeric value.")
        return

    context = user_info(name=name_input, uid=uid)

    print("\n💬 Welcome to the Health & Wellness Planner!")
    print(""" 
        Please choose your goal category
        🍽️ Nutrition Diet / Meal Planner
        🏥 Fitness Training / Gym / Workout
        🧠 Mental Health
        🤕 Injury Support
        👋 exit
""")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in {"exit", "quit"}:
            print("👋 Goodbye! Take care.")
            break

        result = Runner.run_streamed(
            Orchestrator_agent,
            input=user_input,
            run_config=config,
            context=context
        )

        await stream_agent_response(result)


if __name__ == "__main__":
    asyncio.run(main())
