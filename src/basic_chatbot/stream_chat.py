import streamlit as st
from main import run_llm  # Import the main function from main.py
import io


def display_chat(history):
    """Displays the chat history in the Streamlit app."""
    for entry in history:
        if entry["role"] == "user":
            with st.chat_message("user"):
                st.write(entry["content"])
        elif entry["role"] == "assistant":
            with st.chat_message("assistant"):
                st.write(entry["content"])


def get_user_input():
    """Gets user input from the Streamlit input box."""
    return st.chat_input("Enter your message here...")


def initialize():
    if "start_flag" not in st.session_state:
        st.session_state.start_flag = False
    # Initialize chat history in session state
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            {"role": "system", "content": "Please answer any question respectfully"}
        ]


def main():
    st.title("Simple Chatbot")

    initialize()

    # Display chat history
    display_chat(st.session_state.chat_history)

    # Get user input
    user_input = get_user_input()

    if user_input and user_input.lower() != "exit":
        st.session_state.start_flag = True
        # Append user message to chat history
        st.session_state.chat_history.append({"role": "user", "content": user_input})

        # Prepare messages for the LLM in the format it expects (Langchain messages)
        messages = [
            (entry["role"], entry["content"]) for entry in st.session_state.chat_history
        ]

        # Get the LLM's response
        llm_response = run_llm(messages)

        # Append the LLM's response to the chat history
        st.session_state.chat_history.append(
            {"role": "assistant", "content": llm_response}
        )
    elif st.session_state.start_flag and user_input and user_input.lower() == "exit":
        markdown_text = ""
        for entry in st.session_state.chat_history:
            if entry["role"] == "user":
                markdown_text += f"**User:** {entry['content']}\n\n"
            elif entry["role"] == "assistant":
                markdown_text += f"**Assistant:** {entry['content']}\n\n"

        # Convert to bytes
        markdown_bytes = markdown_text.encode()

        # Create a BytesIO object
        markdown_file = io.BytesIO(markdown_bytes)

        st.session_state.markdown_file = markdown_file  # store to use later

        st.download_button(
            label="Download Chat History",
            data=st.session_state.markdown_file,
            file_name="chat_history.md",
            mime="text/markdown",
            key="download_button",
            on_click=initialize(),
        )
        st.session_state.start_flag = False

    if st.session_state.start_flag:
        # Display the updated chat history
        display_chat(st.session_state.chat_history)


if __name__ == "__main__":
    main()
