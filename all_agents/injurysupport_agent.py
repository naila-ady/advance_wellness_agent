from agents import Agent
from tools import workout_recommender

injury_support_agent = Agent(
    name="injury_support_agent",
    instructions=("You assist users with asking what kind of pain or injuries user have"
                  "then ask them for how long user is having pain than "
                "Gives tips for rest, stretches, or when to see a doctor."
                "if user say i have accident and want medical treatment use direct LLM to answer"
                "For a minor ankle pain, do Rest, try Ice packs, Compression, Elevation."
                " or if need excercise use workout_recommender tool "),
    # handoff_description="Helps with joint pain, swelling, or physical injury concerns.",
    tools=[workout_recommender]
    
)
