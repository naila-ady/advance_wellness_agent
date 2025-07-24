from agents import function_tool, RunContextWrapper
from context import user_info

@function_tool
async def goal_analyzer(context: RunContextWrapper[user_info],user_input: str) -> str:
    """
    Analyze the user's input and set their goal category (only once).
    when user is provided with answer just give him schedue to revisit.
    After schedule is provided ask him to 
    """

    user_input = user_input.lower().strip()
   
    if not context.goal:
        context.goal = {"menu_shown": True}
        return (
            "Please choose your goal category:\n"
            "- 🍽️ Nutrition Diet / Meal Planner\n"
            "- 🏥 Fitness Training / Gym / Workout\n"
            "- 🧠 Mental Health\n"
            "- 🤕 Injury Support\n"
            "- 👋 exit"
        )

    if "type" not in context.goal:
        if any (word  in user_input for word in[ "nutrition" ,"meal plan" ,"food" "diet"] ):
            context.goal["type"] = "meal plan"
            return "✅ Goal set: Meal plan."
        elif any (word in user_input for  word in ["gym", "workout" ,"excercise","fitness" ,"workout"]):
            context.goal["type"] = "fitness"
            return "✅ Goal set: Fitness."
        elif any(word in user_input for word in ["injury", "pain", "treatment", "accident"]):
            context.goal["type"] = "injury support"
            return "✅ Goal set: injury support."
        elif any(word in user_input for word in ["mental", "stress", "depression", "anxiety"]):
            context.goal["type"] = "mental support"
            return "✅ Goal set: Mental Health."
        elif "exit" in user_input:
            context.goal["type"] = "exit"
            return("👋bye")
        else:
            return (
                "❌ Sorry, I didn't understand.\n"
                "Please choose: Nutrition, Fitness, Mental Health, or Injury Support."
            )

    return (
         f"🎯"
        # Your goal is already set to: {context.goal['type'].replace('_', ' ').title()}.\n"
        # "✅ Would you like help with anything else (like a meal plan, schedule, or nutrition)?\n"
        # "Type your next request or say 'exit' to leave."
    )
   
    