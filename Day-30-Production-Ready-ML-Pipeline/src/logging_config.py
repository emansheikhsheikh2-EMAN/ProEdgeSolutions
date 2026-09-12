import logging

from src.config import LOG_PATH, LOG_LEVEL


def setup_logging():
    """Configure application logging."""

    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        level=getattr(logging, LOG_LEVEL.upper(), logging.INFO),
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        handlers=[
            logging.FileHandler(LOG_PATH, encoding="utf-8"),
            logging.StreamHandler(),
        ],
        force=True,
    )

    logging.getLogger(__name__).info(
        "Logging system initialized."
    )