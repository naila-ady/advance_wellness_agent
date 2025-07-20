# from agents import Agent
# injury_support_agent=Agent(
#     name = "Injury Support Agent",
#     instructions = "Handles user request to examine physical issues\n You are handoff agent.If user concerns about bones injury , jointPain, or any physical limitation ,you provide them with guidence and traetment and then say takecare",
    
# )

from agents import Agent


injury_support_agent = Agent(
    name="injury_support_agent",
    instructions="You help users who have physical injuries or limitations such as bone issues, joint pain, or strains. Give safe guidance and basic recovery advice.",
    handoff_description="Supports users with physical injury concerns or pain.",
    
)
