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
from agents import Runner, Agent,enable_verbose_stdout_logging,set_tracing_disabled,ModelSettings
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
from hooks import hooks 


# enable_verbose_stdout_logging()
# set_tracing_disabled(disabled=True)

Orchestrator_agent= Agent(
    name="Health_wellness_Agent",
    # instructions=(
        # "1. Ask about goals by using goal_analyzer tool, fitness level, meal plans, injury support, workout or any challenges.\n"
        # "2. Analyze input to determine the most appropriate support.\n"
        # "3. Use tools if needed: Goal Analyzer, Meal Planner, Workout Recommender, etc.\n"
        # "4. Hand off to specialized agents when appropriate: NutritionExpertAgent, InjurySupportAgent, EscalationAgent.\n"
    instructions=(
            "You're a wellness assistant helping users with fitness, nutrition, and recovery.\n"
            "1. First, use `goal_analyzer` to understand the user's wellness goal.\n"
            "2. Then according to user goal, use other tools:\n"
            "- Use `meal_planner` for meal planning.\n"
            "- Use `schedule` to schedule health activities.\n"
            "- Use `progress_tracker` to track user's health journey.\n"
            "- 🏋️‍♂️ Use `workout_plan` when the user says 'beginner', 'advanced', 'gym', 'workout', 'fitness routine', or asks for a fitness plan.\n"
            "- Use `give_nutrition` for dietary goals.\n"
            "- Use `give_injurysupport` for pain, injury, or joint issues.\n"
            "- Use `give_escalation` if they want to speak with a human coach.\n"
            "Be proactive — prefer tools over answering yourself."
            "Please choose your goal category:\n"
            "- 🍽️ Nutrition Diet / Meal Planner\n"
            "- 🏥 Fitness Training / Gym / Workout\n"
            "- 🧠 Mental Health\n"
            "- 🤕 Injury Support\n"
            "- 👋 exit"
            ),
    # instructions=(
    #             # "if User: I want to lose 5kg in 2 months, transfer to workout_recommender "
    #             # "if User: I’m vegetarian transfer to MealPlannerTool provides meal plans after asking their choice"
    #     ),
            
    
        
        
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
        model_settings=ModelSettings(tool_choice="required"),
        reset_tool_choice=True
    )

conversation_state = {}

async def main():
    name_input = input("Enter your name: ").strip()
    uid_input = input("Enter your User ID (just a number): ").strip()
    try:
        uid = int(uid_input)
    except ValueError:
        print("❌ Invalid UID. Please enter a numeric value.")
        return

    context = user_info(name=name_input, uid=uid,conversation_state={})
    


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
            hooks=hooks,
            run_config=config,
            context=context,
            
        )

        await stream_agent_response(result)


if __name__ == "__main__":
    asyncio.run(main())
