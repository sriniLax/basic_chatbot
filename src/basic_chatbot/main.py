from config import MODEL_SPECS, GEMINI_API_KEY
from helper import logger
from langchain_google_genai import ChatGoogleGenerativeAI


llm = ChatGoogleGenerativeAI(
    api_key=GEMINI_API_KEY,
    model=MODEL_SPECS["model"],
    max_tokens=MODEL_SPECS["max_tokens"],
    timeout=MODEL_SPECS["timeout"],
    max_retries=MODEL_SPECS["max_retries"],
)


def run_llm(messages):
    """Runs the language model with the given messages and returns the response."""
    response = llm.invoke(messages)

    # meta_data = response.response_metadata

    logger.info(response.usage_metadata)

    logger.info(f"Model name: {MODEL_SPECS['model']}")
    logger.info(f"Input tokens: {response.usage_metadata['input_tokens']}")
    logger.info(f"Output tokens: {response.usage_metadata['output_tokens']}")
    # logger.info(f"Time taken: {meta_data['token_usage']['total_time']}")

    return response.content
