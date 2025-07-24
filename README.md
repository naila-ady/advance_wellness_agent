# 💬 Health & Wellness Planner Agent (Streamlit + OpenAI Agents SDK)

An intelligent conversational health planner powered by OpenAI's multi-agent SDK and Streamlit UI. It supports personalized meal planning, injury support, workout recommendations, and goal tracking.
  Features
- 🧠 Goal analysis (via Goal Analyzer tool)
- 🍽️ Meal planning & nutrition advice
- 🏋️‍♂️ Workout recommendations
- 🤕 Injury support agent
- 📆 Scheduling + progress tracking
- 🧑‍💻 Escalation to human coach (if needed)
- 🔁 Live chat UI built with Streamlit

Code Structure
advance_wellness_agent/
├── all_agents/
│   ├── escalation_agent.py
│   ├── injurysupport_agent.py
│   └── nutrition_agent.py
├── tools/
│   ├── goal_analyzer.py
│   ├── meal_planner.py
│   ├── workout_recommender.py
│   ├── scheduler.py
│   └── tracker.py
├── context.py             
├── runconfig.py          # run_config for SDK
├── streamlit_chat_ui.py  # Streamlit UI
├── main.py               # CLI interface 
└── README.md             
