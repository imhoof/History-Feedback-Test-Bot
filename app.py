import streamlit as st
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]

system_prompt = """
You are a helpful and encouraging writing coach for college students in introductory history classes.
When a student shares a paragraph, provide specific feedback on clarity, historical argument, use of evidence, and structure.
Be constructive, supportive, and focused on improving historical thinking.
"""

st.title("📜 History Writing Feedback Bot")
st.write("Paste your paragraph below and get detailed, helpful feedback.")

user_input = st.text_area("Enter your paragraph here:", height=200)

if st.button("Get Feedback") and user_input:
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input}
    ]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages,
            temperature=0.7
        )
        feedback = response["choices"][0]["message"]["content"]
        st.subheader("🧠 Writing Coach Feedback")
        st.write(feedback)
    except Exception as e:
        st.error(f"Error: {e}")
