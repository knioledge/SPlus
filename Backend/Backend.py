from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import random
from jinja2 import Template
from template_store import get_templates, add_template

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    """Homepage displaying available categories and a form to generate questions."""
    all_templates = get_templates()
    categories = list(set(template["category"] for template in all_templates))
    return templates.TemplateResponse("index.html", {"request": request, "categories": categories})


@app.post("/generate/")
async def generate_question(request: Request, category: str = Form(...)):
    """Generate a random question from a selected category."""
    available_templates = get_templates(category=category)
    if not available_templates:
        return templates.TemplateResponse("index.html",
                                          {"request": request, "error": "No templates available for this category."})

    selected_template = random.choice(available_templates)
    param_values = {
        key: random.randint(param["min"], param["max"]) for key, param in selected_template["parameters"].items()
    }

    rendered_question = Template(selected_template["template_text"]).render(**param_values)
    return templates.TemplateResponse("index.html", {"request": request, "generated_question": rendered_question,
                                                     "categories": [category]})


@app.get("/admin", response_class=HTMLResponse)
async def admin_panel(request: Request):
    """Admin panel to add new templates."""
    return templates.TemplateResponse("admin.html", {"request": request})


@app.post("/admin/add")
async def add_new_template(
        category: str = Form(...), subtopic: str = Form(...), template_text: str = Form(...),
        tens_min: int = Form(...), tens_max: int = Form(...), units_min: int = Form(...), units_max: int = Form(...)
):
    """Endpoint for adding new templates."""
    parameters = {
        "tens": {"type": "integer", "min": tens_min, "max": tens_max},
        "units": {"type": "integer", "min": units_min, "max": units_max}
    }
    add_template(f"{category[:3]}_{subtopic[:3]}_{random.randint(1000, 9999)}", category, subtopic, template_text,
                 parameters)
    return {"message": "Template added successfully"}
