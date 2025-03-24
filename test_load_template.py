from TemplateStore.store import TemplateStore
from TemplateStore.models import Template

if __name__ == "__main__":
    store = TemplateStore(base_dir="templates")
    template = store.load("template_001")

    if template:
        print("✅ Template loaded successfully:")
        print(template)

        # Save a modified copy
        new_template = template.model_copy(update={"id": "template_001_copy", "name": "Copy of Basic Addition MCQ"})

        store.save(new_template)
    else:
        print("❌ Template not found.")

    print("\n📄 All available templates:")
    for t in store.list():
        print(f"- {t.id}: {t.name}")
    # Try deleting the copied template
    store.delete("template_001_copy")
