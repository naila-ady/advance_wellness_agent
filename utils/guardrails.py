# from agents import input_guardrail, GuardrailFunctionOutput, InputGuardrailTripwireTriggered

# class HealthguardOutput(BaseModel)
    # is_addicted:bool
    # reasoning:str
    # answer:str
# guardrail_agent=Agent(
    # name=Guradrail_check,
    # instructions="Check if the user is asking for steroids,injections or direcctly asking for high dose of medicine",
    # output_type=HealthguardOutput
    # )

# @input_guardrail
# async def guard_health_input(context:RunContextWrapper[None], Agent, input: str|list[TresponseInputItem]
# ) -> GuardrailFunctionOutput:
#     

#     if any(word in lowered for word in blocked_keywords):
#         return InputGuardrailTripwireTriggered(
#             "🚫 Your message contains unsafe or inappropriate content. Please rephrase it."
#         )

#     return GuardrailFunctionOutput(
#         output_info=user_input,
#         tripwire_triggered=False
#     )
