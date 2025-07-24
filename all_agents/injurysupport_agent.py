from agents import Agent
from tools import workout_recommender

injury_support_agent = Agent(
    name="injury_support_agent",
    instructions="You assist users with joint pain or injuries",
    # handoff_description="Helps with joint pain, swelling, or physical injury concerns.",
    tools=[workout_recommender]
    
)
