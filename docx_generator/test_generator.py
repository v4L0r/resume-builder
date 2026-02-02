from generator import create_docx

fake_resume = {
    "name": "Jane Doe",
    "summary": "AI-assisted backend engineer",
    "skills": ["Python", "Flask", "Poe API"],
    "education" : "DBS, MIT",
    "title": "Super Backend Dev",
    "experience": "Started coding when sperm made contact with egg"
}

path = create_docx(fake_resume)
print("Generated:", path)