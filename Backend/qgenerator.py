import random

# A list of question templates. In a full implementation, these might be loaded from a database or JSON file.
question_templates = [
    {
        "template_id": "read_write_01",
        "category": "Number Sense and Place Value",
        "template_text": "Write the number that has {tens} tens and {units} units.",
        "parameters": {
            "tens": {"min": 1, "max": 9},
            "units": {"min": 0, "max": 9}
        }
    },
    # You can add more templates here following the same structure.
]


def generate_question(category="Number Sense and Place Value"):
    """
    Generate a math question based on the selected category.

    Parameters:
        category (str): The category of the question template to use.

    Returns:
        dict: A dictionary containing the template_id and the generated question text.
    """
    # Filter templates by the requested category.
    filtered_templates = [t for t in question_templates if t["category"] == category]
    if not filtered_templates:
        return {"template_id": "", "text": "No template available for the selected category."}

    # Randomly select one template from the filtered list.
    template = random.choice(filtered_templates)

    # Generate random values for each parameter defined in the template.
    # Here we assume all parameters are integers with 'min' and 'max' constraints.
    params = {}
    for param_name, constraint in template["parameters"].items():
        params[param_name] = random.randint(constraint["min"], constraint["max"])

    # Format the question text using Python's string formatting.
    question_text = template["template_text"].format(**params)

    return {"template_id": template["template_id"], "text": question_text}


# For testing purposes, run this block to see output when running this module directly.
if __name__ == "__main__":
    question = generate_question()
    print("Template ID:", question["template_id"])
    print("Generated Question:", question["text"])
