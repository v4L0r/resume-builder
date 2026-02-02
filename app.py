from flask import Flask, render_template, request, send_file
from ai.resume_ai import generate_resume_content
from docx_generator.generator import create_docx

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    user_data = {
        "name": request.form["name"],
        "target_job": request.form["target_job"],
        "competitiveness": request.form["competitiveness"],
        "custom_prompt": request.form["custom_prompt"],
    }

    structured_resume = generate_resume_content(user_data)
    file_path = create_docx(structured_resume)

    return send_file(file_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)