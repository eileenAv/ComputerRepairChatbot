import streamlit as st
from openai import OpenAI

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    # "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    # "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"

st.title("💬 Computer Repair Chatbot")
st.text("Hi! I am an AI assistant specialized in computer repair. Please start by writing your computer model and problem.")

# Custom system prompt
if "messages" not in st.session_state:
    st.session_state["messages"] = [{
        "role": "system",
        "content": (
            "You are an expert in computer repair. You answer user questions by referencing official help forums "
            "for their specific device model. Always ask for the exact model if it’s not provided. Once provided, "
            "you source your response from the official forum for that model (e.g., 'Acer Community Help Forum') "
            "and then give short, precise steps to fix the issue. Always show the source before your advice. "
            "Never forget the model once it is mentioned in the chat."
        )
    }]

# Display the full conversation
for msg in st.session_state.messages[1:]:  # Skip system message
    st.chat_message(msg["role"]).write(msg["content"])

# Handle new user input
if prompt := st.chat_input("Ask a computer question..."):
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    client = OpenAI(api_key=openai_api_key)

    # Add user message to chat
    st.session_state["messages"].append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Get assistant reply
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # or "gpt-3.5-turbo" if you don't have access
        messages=st.session_state.messages
    )

    reply = response.choices[0].message.content
    st.session_state["messages"].append({"role": "assistant", "content": reply})
    st.chat_message("assistant").write(reply)
