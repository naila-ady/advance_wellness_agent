# from agents import Agent

# nutrition_agent = Agent(
#     name = "Nutritionist",
#     instructions = "work according to your main agent"
#     # "you are a handoff agent,you guide user about their diet plans by taking plans from meal planner,once plan is given say takecare",
#     # handoff_description = "Handles users with special dietary needs such as diabetes, allergies, or gluten intolerance."
# )

from agents import Agent

nutrition_agent = Agent(
    name="nutrition_agent",
    instructions="You assist users with dietary advice. Use the meal planner tool for detailed diet plans. Support users with allergies, diabetes, or dietary preferences.",
    handoff_description="Handles personalized dietary and nutrition planning.",
    
)
