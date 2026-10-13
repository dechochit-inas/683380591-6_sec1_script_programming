
import json
import os


class ConfigParser:
    def __init__(self, config_path):
        self.config_path = config_path
        self.config = {}

    def load_config(self):
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(
                f"Configuration file not found: {self.config_path}"
            )

        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                self.config = json.load(f)

        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format: {e}")

        self._validate_config()
        print(f"Configuration loaded successfully from {self.config_path}")
        return self.config

    def _validate_config(self):
        required_fields = [
            "start_url",
            "pagination_selector",
            "item_container_selector",
            "item_data_selectors"
        ]

        for field in required_fields:
            if field not in self.config:
                raise ValueError(
                    f"Missing required field in config: '{field}'"
                )

        if not isinstance(self.config["start_url"], str):
            raise ValueError("start_url must be a string.")

        for field in ["pagination_selector", "item_container_selector"]:
            if not isinstance(self.config[field], str):
                raise ValueError(f"{field} must be a string.")

        selectors = self.config["item_data_selectors"]

        if not isinstance(selectors, dict):
            raise ValueError("item_data_selectors must be a dictionary.")

        for field in ["name", "price"]:
            if field not in selectors:
                raise ValueError(
                    f"Missing required item data selector: '{field}'"
                )

        for key, value in selectors.items():
            if value is not None and not isinstance(value, str):
                raise ValueError(
                    f"Item data selector '{key}' must be a string or null."
                )

        print("Configuration validated.")
