import logging

from src.config.settings import get_settings
from src.observability.logging_config import configure_logging


def main() -> None:
    """Start the Manufacturing Troubleshooting Assistant."""

    settings = get_settings()
    configure_logging(settings.log_level)

    logger = logging.getLogger(__name__)

    logger.info("Starting %s", settings.app_name)
    logger.info("Environment: %s", settings.app_env)
    logger.info("Project setup is working")


if __name__ == "__main__":
    main()