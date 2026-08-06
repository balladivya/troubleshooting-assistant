from src.config.settings import get_settings


def test_default_settings() -> None:
    settings = get_settings()

    assert settings.app_name == "Manufacturing Troubleshooting Assistant"
    assert settings.app_env == "development"