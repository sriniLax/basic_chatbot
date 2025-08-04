import os
import helper

from keyvault import keyvault  # type: ignore
from dotenv import load_dotenv

load_dotenv()

logger = helper.logger
MODEL_SPECS = {
    "model": os.getenv("MODEL"),
    "temperature": float(os.getenv("TEMPERATURE")),
    "top_p": float(os.getenv("TOP_P")),
    "max_tokens": int(os.getenv("MAX_TOKENS", 2048)),
    "timeout": int(os.getenv("TIMEOUT", 600)),
    "max_retries": int(os.getenv("MAX_RETRIES", 2)),
    "response_format": os.getenv("RESPONSE_FORMAT", None),
    # "seed": int(os.getenv("SEED", 42)),
}


GROQ_API_KEY = keyvault.GROQ_API_KEY
if GROQ_API_KEY:
    logger.info("GROQ API Key loaded successfully.")
else:
    logger.warning("GROQ API Key not found. Please check your keyvault setup.")
