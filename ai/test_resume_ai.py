from resume_ai import generate_resume_content

fake_user_data = {
    "name": "John Doe",
    "summary": "Junior backend developer",
    "experience": "Built Flask APIs",
    "education": "BSc Computer Science",
    "skills": "Python, Flask, Git"
}

result = generate_resume_content(fake_user_data)

print(result)
print(type(result))