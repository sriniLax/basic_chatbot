import logging
import sys
from pathlib import Path


logger = logging.getLogger(__name__)

# Initialize logger
# Using INFO level is generally better for production than DEBUG.
logging.basicConfig(
    level=logging.INFO, format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
)

parent_dir = Path(__file__).resolve().parent.parent.parent.parent
# logger.info(parent_dir)
# Add the parent directory to sys.path
sys.path.append(str(parent_dir))
