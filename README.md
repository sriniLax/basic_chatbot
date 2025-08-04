# Basic Chatbot

This project demonstrates a basic question-answering chatbot built using Langchain, Groq, and Streamlit. It allows users to interact with a language model through a simple chat interface.

## Overview

The chatbot utilizes the following components:

*   **Langchain:** A framework for building applications powered by language models.
*   **Groq:** A fast LLM API.
*   **Streamlit:** A Python library for creating interactive web applications.

The application consists of two main files:

*   `main.py`: This file defines the core logic for interacting with the Groq language model. It initializes the ChatGroq object with API key and model specifications and includes a function `run_llm` that takes messages as input, interacts with the LLM, and returns the response.
*   `stream_chat.py`: This file contains the Streamlit application that provides the user interface for the chatbot. It handles displaying the chat history, getting user input, and managing the chat flow.

## Functionality

*   **Chat Interface:** Users can type messages into the input box and receive responses from the language model.
*   **Chat History:** The chat history is displayed in the Streamlit app, allowing users to see the ongoing conversation.
*   **System Message:** The chatbot initializes with a system message that sets the tone for the conversation.
*   **Basic "exit" functionality:** User can type "exit" to end the chat.

## Getting Started

To run this chatbot, you'll need to:

1.  Install the required Python packages.
2.  Set up a Groq API key.
3.  Run the Streamlit application.

### Installation

First, clone the repository.  Then, install the necessary Python packages:

```bash
pip install langchain langchain-groq streamlit
```

### Configuration

Set the `GROQ_API_KEY` environment variable with your Groq API key. You will also need to configure the `MODEL_SPECS` in `config.py`. Example:

```python
MODEL_SPECS = {
    "model": "mixtral-8x7b-32768",
    "max_tokens": 1024,
    "timeout": 30,
    "max_retries": 3,
}
```

### Running the Application

To start the Streamlit application, run the following command:

```bash
streamlit run src/basic_chatbot/stream_chat.py
```

This will open the chatbot in your web browser.
