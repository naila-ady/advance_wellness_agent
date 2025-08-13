from agents import function_tool, RunContextWrapper
from context import user_info

@function_tool
async def goal_analyzer(context: RunContextWrapper[user_info], user_input: str) -> str:
    """
    Analyze the user's input and set their goal category (only once).
    After the goal is set, transfer it to the orchestrator agent  it won't ask again.
    """
    user_input = user_input.lower().strip()
    context = context.context

    
    if not context.goal:
        context.goal = {"menu_shown": True}
        return (
            # "Please choose your goal category:\n"
            # "- 🍽️ Nutrition Diet / Meal Planner\n"
            # "- 🏥 Fitness Training / Gym / Workout\n"
            # "- 🧠 Mental Health\n"
            # "- 🤕 Injury Support\n"
            # "- 👋 exit"
        )

    # If goal type not yet selected, analyze user input
    if "type" not in context.goal:
        if any(word in user_input for word in ["nutrition", "meal plan", "food", "diet"]):
            context.goal["type"] = "meal plan"
            return "✅ Goal set: Meal plan."
        elif any(word in user_input for word in ["gym", "workout", "exercise", "fitness"]):
            context.goal["type"] = "fitness"
            return "✅ Goal set: Fitness."
        elif any(word in user_input for word in ["injury", "pain", "treatment", "accident"]):
            context.goal["type"] = "injury support"
            return "✅ Goal set: Injury Support."
        elif any(word in user_input for word in ["mental", "stress", "depression", "anxiety"]):
            context.goal["type"] = "mental health"
            return "✅ Goal set: Mental Health."
        elif "exit" in user_input:
            context.goal["type"] = "exit"
            return "👋 Bye!"
        else:
            return (
                "❌ Sorry, I didn't understand.\n"
                "Please choose: Nutrition, Fitness, Mental Health, or Injury Support."
            )

    
    return f"🎯 Your current goal is: {context.goal['type']}."

    