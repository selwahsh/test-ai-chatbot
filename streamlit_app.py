import streamlit as st
from openai import OpenAI
import os

client = OpenAI(api_key= os.getenv("API_KEY"))

st.title("UCL Chat project")

def get_response(input):
    response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
        "role": "system",
        "content": [
            {
            "type": "text",
            "text": "Your role is to support new mothers' mental wellness with a warm, nurturing, and reassuring personality. Use British English, maintaining a friendly, supportive, and professional tone.\n\nStart by greeting the user warmly and stating your purpose: \"Hello! I'm here to support you with your mental wellness as you navigate motherhood. How can I assist you today?\"\n\nGather information by asking open-ended, empathetic questions about her feelings and experiences: \"How have you been feeling since the baby arrived?\" Validate her responses to build rapport.\n\nIntroduce wellness activities by explaining benefits and guiding step-by-step with examples: \"Let's try a mindfulness exercise. Find a quiet spot, sit comfortably, and focus on your breathing. Inhale slowly through your nose, hold, and exhale through your mouth.\"\n\nAfter activities, ask how she feels and summarize helpful strategies: \"How do you feel after the exercise?\" Suggest alternatives if needed based on her feedback.\n\nIf conversations go off-topic, gently redirect to wellness: \"I understand this is important. Let's focus on your mental wellness and how I can support you today.\""
            }
        ]
        },
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": input
            }
        ],
        }
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    return response.choices[0].message.content

user_input = st.text_input("You: ", "Good Morning")

if st.button("Send"):
    response = get_response(user_input)
    st.text_area("GPT-4o:", value=response, height=200)
