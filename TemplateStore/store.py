import os
import json
from typing import Optional
from TemplateStore.models import Template


class TemplateStore:
    def __init__(self, base_dir: str = "templates"):
        self.base_dir = base_dir

    def load(self, template_id: str) -> Optional[Template]:
        file_path = os.path.join(self.base_dir, f"{template_id}.json")
        if not os.path.isfile(file_path):
            print(f"Template '{template_id}' not found.")
            return None

        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return Template(**data)

    def save(self, template: Template) -> None:
        file_path = os.path.join(self.base_dir, f"{template.id}.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(template.model_dump(), f, indent=2)
        print(f"✅ Template '{template.id}' saved to '{file_path}'.")

    # List all .json files in the templates/ directory
    #
    # Attempt to load each one as a Template
    #
    # Return a list of Template objects

    def list(self) -> list[Template]:
        templates = []
        for file in os.listdir(self.base_dir):
            if file.endswith(".json"):
                template_id = os.path.splitext(file)[0]
                template = self.load(template_id)
                if template:
                    templates.append(template)
        return templates

    def delete(self, template_id: str) -> bool:
        file_path = os.path.join(self.base_dir, f"{template_id}.json")
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"🗑️ Deleted template '{template_id}'.")
            return True
        else:
            print(f"⚠️ Template '{template_id}' not found.")
            return False
