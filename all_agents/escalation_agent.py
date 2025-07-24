from agents import Agent


escalation_agent = Agent(
    name="escalation_agent",
    instructions="You handle requests where the user wants to talk to a human coach or trainer. Acknowledge their request, inform them someone will reach out soon, and say 'take care'.",
    # handoff_description="Handles escalation to a human coach or trainer.",
    
)
