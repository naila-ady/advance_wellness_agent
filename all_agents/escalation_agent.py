# from agents import Agent
# escalation_agent = Agent(
#     name="Escalation_Agent",
#     instructions="work according to your main agent"
#     # "You are a handoff agent. When a user wants to speak to a human trainer or coach, you acknowledge their request and inform them that a real person will follow up shortly after that say takecare."
# )


from agents import Agent


escalation_agent = Agent(
    name="escalation_agent",
    instructions="You handle requests where the user wants to talk to a human coach or trainer. Acknowledge their request, inform them someone will reach out soon, and say 'take care'.",
    handoff_description="Handles escalation to a human coach or trainer.",
    
)
