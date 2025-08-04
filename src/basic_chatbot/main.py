from config import MODEL_SPECS, GROQ_API_KEY
from helper import logger
from langchain_groq import ChatGroq


llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model=MODEL_SPECS["model"],
    max_tokens=MODEL_SPECS["max_tokens"],
    timeout=MODEL_SPECS["timeout"],
    max_retries=MODEL_SPECS["max_retries"],
)


def run_llm(messages):
    """Runs the language model with the given messages and returns the response."""
    response = llm.invoke(messages)

    meta_data = response.response_metadata

    logger.info(meta_data)

    logger.info(f"Model name: {meta_data['model_name']}")
    logger.info(f"Input tokens: {meta_data['token_usage']['prompt_tokens']}")
    logger.info(f"Output tokens: {meta_data['token_usage']['completion_tokens']}")
    logger.info(f"Time taken: {meta_data['token_usage']['total_time']}")

    return response.content
