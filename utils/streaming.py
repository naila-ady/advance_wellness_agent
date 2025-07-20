# from agents import Runner
# from core_agent import wellness_agent
# from context import UserSessionContext
# from runconfig import config


# async def stream_user_input(user_input:str ,ctx:UserSessionContext):
#     response= await Runner.run(
#         starting_agent=wellness_agent,
#         input=user_input,               
#         context=ctx,                
#         run_config=config           
#     )
#     return(response.final_output)       


# print("=== Run starting ===")
    # async for event in result.stream_events():
    # # We'll ignore the raw responses event deltas
    #     if event.type == "raw_response_event":
    #         continue
    #     elif event.type == "agent_updated_stream_event":
    #         print(f"Agent updated: {event.new_agent.name}")
    #         continue
    #     elif event.type == "run_item_stream_event":
    #         if event.item.type == "tool_call_item":
    #             print("-- Tool was called")
    #     elif event.item.type == "tool_call_output_item":
    #         print(f"-- Tool output: {event.item.output}")
    #     elif event.item.type == "message_output_item":
    #         print(f"-- Message output:\n {ItemHelpers.text_message_output(event.item)}")
    #     else:
    #         pass  # Ignore other event types


