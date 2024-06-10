import streamlit as st
import random

# Psychiatrist's responses
psychiatrist_responses = {
    "greetings": ["Hello! How can I help you today?", "Hi there! What's on your mind?"],
    "feelings": ["Tell me more about how you're feeling.", "How does that make you feel?"],
    "thanks": ["You're welcome!", "Glad I could help."],
    "answer": ["I am psychiatrist", "what is your role"],
    "farewell": ["Goodbye. Take care!", "See you later!"],
    "fallback": ["Could you please elaborate?", "I'm not sure I understand. Can you provide more details?"]
}

# Function to generate response
def generate_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return random.choice(psychiatrist_responses["greetings"])
    elif "feel" in user_input or "sad" in user_input or "happy" in user_input:
        return random.choice(psychiatrist_responses["feelings"])
    elif "thank" in user_input:
        return random.choice(psychiatrist_responses["thanks"])
    elif "bye" in user_input or "goodbye" in user_input:
        return random.choice(psychiatrist_responses["farewell"])
    elif "who" in user_input or "role" in user_input:
        return random.choice(psychiatrist_responses["answer"])
    else:
        return random.choice(psychiatrist_responses["fallback"])

# Streamlit app
def main():
    st.title("Psychiatrist Chatbot")

    # Text input for user's message
    user_input = st.text_input("You:", "")

    # Chat history
    st.subheader("Chat History")

    if st.button("Send"):
        if user_input.strip() == "":
            st.warning("Please type something...")
        else:
            st.write("User:", user_input)
            response = generate_response(user_input)
            st.write("Psychiatrist:", response)

if __name__ == "__main__":
    main()
