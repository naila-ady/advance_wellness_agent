
from agents import function_tool

@function_tool
async def schedule(followup_time: str) -> str:
    """
    ⏰ Schedule a preferred time for the user to revisit weekly for health and progress check.
    Suggest a time with an 7 day interval along with the date . If the user agrees to the day, confirm.
    Otherwise, ask the user to select their own convenient time.once selected ask user want any more help or want to exit .
    Ask user to type exit or quit
    """
    time_slot = followup_time.lower()
    valid_days = {"monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"}

    # Check if user mentioned a valid day
    if any(day in time_slot for day in valid_days):
        return f"✅ Your checkup is scheduled every 7 days you have to reviit me on {followup_time.title()}."
    else:
        return (
            "❌ The provided time is unclear or doesn't include a valid weekday.\n"
            "Please mention a day like 'Monday morning' or suggest your own convenient time."
        )
