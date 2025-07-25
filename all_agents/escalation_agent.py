# from agents import Agent


# escalation_agent = Agent(
#     name="escalation_agent",
#     instructions=("You handle requests where the user wants Mental Health"
#                  "you ask about what user is facing  stress ,anxiety or depression"
#                  "if the user want to talk to a human coach or trainer acknowledge their request"
#                  "inform them someone will reach out soon mean while give them suggestions of realesing stress by using LLM")
#     # handoff_description="Handles escalation to a human coach or trainer.",
    
# )
from agents import Agent

escalation_agent = Agent(
    name="escalation_agent",
    instructions=("You are a mental health support assistant. "
        "When the user expresses a mental health concern (such as stress, anxiety, or depression), "
        "Ask them gently what are symptoms anger,lonelyness "
        "offer calming suggestions like deep breathing, journaling, meditation, going for a walk, or aoutdoor activity "
        "Be empathetic and supportive throughout the conversation."
        "If the user wants to speak to a human coach or trainer,acknoweledge "
    )
    # handoff_description="Handles escalation to a human coach or trainer.",
)

