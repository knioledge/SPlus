from tinydb import TinyDB, Query

# Initialize database
db = TinyDB("question_templates.json")


def add_template(template_id, category, subtopic, template_text, parameters):
    """Adds a new template to the store."""
    db.insert({
        "template_id": template_id,
        "category": category,
        "subtopic": subtopic,
        "template_text": template_text,
        "parameters": parameters
    })


def get_templates(category=None, subtopic=None):
    """Retrieve templates based on category/subtopic filters."""
    if category and subtopic:
        return db.search((Query().category == category) & (Query().subtopic == subtopic))
    elif category:
        return db.search(Query().category == category)
    else:
        return db.all()


def update_template(template_id, new_data):
    """Updates a template based on template_id."""
    db.update(new_data, Query().template_id == template_id)


def delete_template(template_id):
    """Deletes a template."""
    db.remove(Query().template_id == template_id)


# Example Usage:
if __name__ == "__main__":
    add_template(
        template_id="read_write_01",
        category="Number Sense and Place Value",
        subtopic="Read and Write Numbers",
        template_text="Write the number that has {{tens}} tens and {{units}} units.",
        parameters={"tens": {"type": "integer", "min": 1, "max": 9}, "units": {"type": "integer", "min": 0, "max": 9}}
    )

    print(get_templates("Number Sense and Place Value"))
