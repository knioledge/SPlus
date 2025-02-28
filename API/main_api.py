from fastapi import FastAPI
from pydantic import BaseModel
import random
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow cross-origin requests from your streamlit app (if running on different ports)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production for security.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Example data: a simple question template (in a real app, this would come from your template store)
question_templates = [
    {
        "template_id": "read_write_01",
        "category": "Number Sense and Place Value",
        "template_text": "Write the number that has {tens} tens and {units} units.",
        "parameters": {"tens": {"min": 1, "max": 9}, "units": {"min": 0, "max": 9}},
    }
]

# Define a Pydantic model for the generated question
class GeneratedQuestion(BaseModel):
    template_id: str
    text: str

@app.get("/generate_question", response_model=GeneratedQuestion)
def generate_question(category: str = "Number Sense and Place Value"):
    # Filter templates by category (for now, we only have one)
    filtered = [t for t in question_templates if t["category"] == category]
    if not filtered:
        return {"template_id": "", "text": "No template available."}

    template = random.choice(filtered)
    # Generate parameters randomly
    tens = random.randint(template["parameters"]["tens"]["min"], template["parameters"]["tens"]["max"])
    units = random.randint(template["parameters"]["units"]["min"], template["parameters"]["units"]["max"])
    # Render the question text using basic Python string formatting
    question_text = template["template_text"].format(tens=tens, units=units)
    return {"template_id": template["template_id"], "text": question_text}
