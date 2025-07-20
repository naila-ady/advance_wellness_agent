# from agents import input_guardrail, GuardrailFunctionOutput, InputGuardrailTripwireTriggered

# @input_guardrail
# async def guard_health_input(context, agent, user_input: str) -> GuardrailFunctionOutput:
#     lowered = user_input.lower()
#     blocked_keywords = [
#         "suicide", "xxx", "drugs", "steroids", "inject", "hack", "body pack"
#     ]

#     if any(word in lowered for word in blocked_keywords):
#         return InputGuardrailTripwireTriggered(
#             "🚫 Your message contains unsafe or inappropriate content. Please rephrase it."
#         )

#     return GuardrailFunctionOutput(
#         output_info=user_input,
#         tripwire_triggered=False
#     )
