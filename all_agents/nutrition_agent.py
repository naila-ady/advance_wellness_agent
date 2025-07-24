from agents import Agent
from tools import meal_planner

nutrition_agent = Agent(
    name="nutrition_agent",
    instructions=("You assist users with dietary advice. Use the meal planner tool for detailed diet plans."
                " Support users with allergies, diabetes, or dietary preferences."),
    # handoff_description="Handles personalized dietary and nutrition planning."
    tools=[meal_planner]
    
)
