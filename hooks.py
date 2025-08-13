from typing import Any
from agents import Agent, RunHooks,RunContextWrapper,Tool
from context import user_info



# class MyCustomHooks(RunHooks):
    
    # async def on_agent_start(self, context:RunContextWrapper[user_info], agent:Agent):
    #     print(f"🔵 {agent.name} started checking for user {context.context.name} having UserID 00{context.context.uid}")
        
    # async def on_tool_start(self, context: RunContextWrapper[user_info], agent: Agent, tool:Tool):
    #     print(f"🟡 {agent.name} is now calling tool {tool.name} to address the user {context.context.name} issue.")
        
    # # async def on_handoff(self, context: RunContextWrapper[user_info], from_agent: Agent[Any], to_agent: Agent[Any]):
    # #     # return await super().on_handoff(context, from_agent, to_agent)
    # #     print(f"🟢handoff")
    # async def on_tool_end(self, context: RunContextWrapper[user_info], agent: Agent, tool: Tool, result: str):
    #     # print(f"🟣 {tool.name} tool completed its works ")
    #     print(f"🟣 '{tool.name}' is called,")

        
    # async def  on_agent_end(self,context:RunContextWrapper[user_info],agent:Agent,output:Any):
    #     print(f"🟤 {agent.name}  completed request for {context.context.name} ")

class MyCustomHooks(RunHooks):

    async def on_agent_start(self, context: RunContextWrapper[user_info], agent: Agent):
        print(f"🔵 {agent.name} is now working on a new request for {context.context.name} (User ID: {context.context.uid:03})")

    async def on_tool_start(self, context: RunContextWrapper[user_info], agent: Agent, tool: Tool):
        print(f"🟡 Using tool: {tool.name} to continue with {context.context.name}'s request...")
    
   
    async def on_tool_end(self, context: RunContextWrapper[user_info], agent: Agent, tool: Tool, result: str):
        print(f"🟣 Finished using {tool.name}. Proceeding with the next step...")

    async def on_agent_end(self, context: RunContextWrapper[user_info], agent: Agent, output: Any):
        # print(f"🟤 {agent.name} has successfully completed this request for {context.context.name}.")
        return("")

    async def on_handoff(self, context: RunContextWrapper[user_info], from_agent: Agent, to_agent: Agent):
        print(f"🟢 Handing over from {from_agent.name} to {to_agent.name} for specialized support.")

hooks=MyCustomHooks()
        