from docxtpl import DocxTemplate

def create_docx(resume_data):
    doc = DocxTemplate("templates/resume_template.docx")
    doc.render(resume_data)

    output_path = "resume_output.docx"
    doc.save(output_path)
    return output_path