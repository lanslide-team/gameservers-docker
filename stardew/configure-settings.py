#!/usr/bin/env python3

import json
import os
import shutil
import re
from pathlib import Path


DEFAULT_SETTINGS = Path(
    "/defaults/server-settings.json"
)

SETTINGS_PATH = Path(
    os.environ.get(
        "SETTINGS_PATH",
        "/data/settings/server-settings.json"
    )
)


def convert(value, current, key=None):
    """Convert environment values to the appropriate JSON type."""

    # FarmType supports numeric IDs or named farms.
    if key == "FarmType":
        try:
            return int(value)
        except ValueError:
            return value

    # Null values, such as RandomSeed.
    if current is None:
        if value.strip().lower() in ("", "null"):
            return None

        try:
            return json.loads(value)
        except json.JSONDecodeError:
            return value

    # Boolean values.
    if isinstance(current, bool):
        normalized = value.strip().lower()

        if normalized in ("1", "true"):
            return True

        if normalized in ("0", "false"):
            return False

        raise ValueError(
            f"Invalid boolean value for {key}: {value!r}. "
            "Expected 0, 1, false, or true."
        )

    # Integer values.
    if isinstance(current, int):
        return int(value)

    # Floating-point values.
    if isinstance(current, float):
        return float(value)

    # JSON arrays.
    if isinstance(current, list):
        value = value.strip()

        if not value:
            return []

        try:
            result = json.loads(value)
        except json.JSONDecodeError:
            result = [
                item.strip()
                for item in value.split(",")
                if item.strip()
            ]

        if not isinstance(result, list):
            result = [value]

        return [str(item) for item in result]


    # JSON objects.
    if isinstance(current, dict):
        result = json.loads(value)

        if not isinstance(result, dict):
            raise ValueError(
                f"Expected JSON object for {key}"
            )

        return result

    # String values.
    return value


def load_settings():
    """Load existing settings or initialise from defaults."""

    SETTINGS_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    if not SETTINGS_PATH.exists():
        if not DEFAULT_SETTINGS.exists():
            raise FileNotFoundError(
                f"Default settings not found: {DEFAULT_SETTINGS}"
            )

        shutil.copyfile(
            DEFAULT_SETTINGS,
            SETTINGS_PATH
        )

        print(
            f"Created default settings: {SETTINGS_PATH}"
        )

    with SETTINGS_PATH.open(
        "r",
        encoding="utf-8"
    ) as f:
        return json.load(f)


def apply_environment(config):
    """Apply SDV_GAME_* and SDV_SERVER_* overrides."""

    for section in ("Game", "Server"):

        settings = config.get(section, {})

        for key, current in settings.items():

            env_name = (
                f"SDV_{section}_{re.sub(r'(?<!^)(?=[A-Z])', '_', key)}"
            ).upper()

            if env_name not in os.environ:
                continue

            value = os.environ[env_name]

            converted = convert(
                value,
                current,
                key
            )

            config[section][key] = converted

            print(
                f"Override: {section}.{key} = "
                f"{json.dumps(converted)}"
            )

    return config


def save_settings(config):
    """Write settings atomically."""

    temp_path = SETTINGS_PATH.with_suffix(".tmp")

    try:
        with temp_path.open(
            "w",
            encoding="utf-8"
        ) as f:
            json.dump(
                config,
                f,
                indent=2,
                ensure_ascii=False
            )

            f.write("\n")

        os.replace(
            temp_path,
            SETTINGS_PATH
        )

    finally:
        if temp_path.exists():
            temp_path.unlink()

    print(
        f"Settings saved: {SETTINGS_PATH}"
    )


def main():

    print("Configuring Stardew Valley server...")

    config = load_settings()

    config = apply_environment(config)

    save_settings(config)

    print("Configuration complete.")


if __name__ == "__main__":
    main()

