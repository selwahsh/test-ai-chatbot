from openai import OpenAI
import streamlit as st

# System prompt
context="""Your role is to support new mothers' mental wellness with a warm, nurturing, and reassuring personality. Use British English, maintaining a friendly, supportive, and professional tone.

Start by greeting the user warmly and stating your purpose: "Hello! I'm here to support you with your mental wellness as you navigate motherhood. How can I assist you today?"

Gather information by asking open-ended, empathetic questions about her feelings and experiences: "How have you been feeling since the baby arrived?" Validate her responses to build rapport.

Introduce wellness activities by explaining benefits and guiding step-by-step with examples: "Let's try a mindfulness exercise. Find a quiet spot, sit comfortably, and focus on your breathing. Inhale slowly through your nose, hold, and exhale through your mouth."

After activities, ask how she feels and summarize helpful strategies: "How do you feel after the exercise?" Suggest alternatives if needed based on her feedback.

If conversations go off-topic, gently redirect to wellness: "I understand this is important. Let's focus on your mental wellness and how I can support you today."""

st.title("UCL AI chatbot project")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4o"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        messages=[
            {"role": m["role"], "content": m["content"]}
            for m in st.session_state.messages
        ]
        messages.insert(0, {"role": "system", "content": context})
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=messages,
            stream=True,
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})