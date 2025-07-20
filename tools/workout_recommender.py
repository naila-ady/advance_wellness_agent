              
    
from agents import function_tool

@function_tool
async def workout_plan(plan: str) -> str:
    """
    Suggest a fitness workout plan based on the user's fitness level beginner or advance.
    once u gave the plan call the tracker tool
    """

    work_plan = plan.lower()

    if "beginner" in work_plan or "weightloss"  in work_plan:
    
        return (
            "🏋️ Beginner Weight Loss Plan:\n"
            "1. Brisk 30-minute walk (outdoors or treadmill)\n"
            "2. 10 minutes of stretching\n"
            "3. Jumping jacks (30 seconds)\n"
            "4. Squats (30 seconds)"
        )

    elif "advance" in work_plan or "Obesity" in work_plan :
        return (
            "💪 Advanced Weight Loss Plan:\n"
            "1. Brisk 30-minute walk (outdoors or treadmill)\n"
            "2. 10 minutes of stretching\n"
            "3. Sets of push-ups\n"
            "4. Dumbbell rows\n"
            "5. Wall sits (30-second hold)"
        )

    else:
        return (
            "🚶‍♂️ General Fitness Tip:\n"
            "Start with a brisk 20-minute walk daily, and gradually add 10 more minutes every week."
        )
