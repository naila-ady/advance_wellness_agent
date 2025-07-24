from agents import Agent
from tools import workout_recommender

injury_support_agent = Agent(
    name="injury_support_agent",
    instructions=("You assist users with joint pain or injuries"
                "Gives tips for rest, stretches, or when to see a doctor."
                "For a minor ankle pain, do Rest, try Ice packs, Compression, Elevation."
                "move to workout_recommender tool "),
    # handoff_description="Helps with joint pain, swelling, or physical injury concerns.",
    tools=[workout_recommender]
    
)
