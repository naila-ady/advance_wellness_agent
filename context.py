from dataclasses import dataclass
from agents import RunContextWrapper,function_tool
from pydantic import BaseModel

from typing import Optional,List,Dict

# @dataclass
class user_info(BaseModel):
    name :str
    uid  :int
    goal: dict= {}
    diet_preferences: Optional[str] = None
    workout_plan: Optional[dict] = None
    meal_plan: Optional[List[str]] = None
    injury_notes: Optional[str] = None
    handoff_logs: List[str] = []
    progress_logs: List[Dict[str, str]] = []


    

@function_tool
async def fetch_user_info(wrapper:RunContextWrapper[user_info])->str:
    return f"user{wrapper.context.name} has UID {wrapper.context.uid}"
    



