import argparse
import json

from ssg.generator import generator


def get_args() -> argparse.Namespace:
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-f")

    return args.parse_args()


def load_json(file_name: str):
    with open(file_name) as file_pointer:
        return json.load(file_pointer)


if __name__ == "__main__":
    args = get_args()
    config = load_json(args.config)
    generator.generate_pages(
        config["markdown_folder"],
        config["base_template"],
        config["css_file"],
        config["output_folder"],
    )
