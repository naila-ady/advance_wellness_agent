# from agents import Agent
# from tools import meal_planner

# nutrition_agent = Agent(
#     name="nutrition_agent",
#     instructions=("You assist users with dietary advice. Use the meal planner tool for detailed diet plans."
#                 " Support users with allergies, diabetes, or dietary preferences."),
#     # handoff_description="Handles personalized dietary and nutrition planning."
#     tools=[meal_planner]
    
# )

from agents import Agent
from tools import meal_planner

nutrition_agent = Agent(
    name="nutrition_agent",
    instructions=(
        "You are a dietary planning assistant."
        "1. If the user gives a dietary preference (e.g., vegan, vegetarian, non-veg, gluten-free, high-protein),acknowledge it and pass it to the `meal_planner` tool."
        "2.If the user is unclear, ask them to specify their preference."
        "3. Always use the `meal_planner` tool to generate a meal plan."
        "4. Do not answer from your own knowledge — use the tool."
    ),
    
)
