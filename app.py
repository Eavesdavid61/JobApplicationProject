from flask import Flask, request, render_template, redirect, url_for, flash
from flask_pymongo import PyMongo
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "supersecretkey"
app.config['SERVER_NAME'] = 'jaimieagencyapp.onrender.com'
# MongoDB Configuration
app.config["MONGO_URI"] = "mongodb+srv://eavesdavid61:internaL123@cluster0.7w9qz.mongodb.net/Mydatabase?retryWrites=true&w=majority&appName=Cluster0"
mongo = PyMongo(app)

# File Upload Configuration
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {"pdf", "doc", "docx"}

def allowed_file(filename):
    """Check if file has an allowed extension."""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        position = request.form.get("position")

        # Salary Mapping
        salary_map = {
            "Marketing Specialist": "$400,000 including compensations, rewards, and other entities.",
            "Social Media Management": "$300,000 including compensations, rewards, and other entities.",
            "Driver": "$150,000 including compensations and rewards."
        }
        salary = salary_map.get(position, "Salary not specified")

        # File Upload Handling
        if "file" not in request.files:
            flash("No file uploaded.", "error")
            return redirect(url_for("index"))

        file = request.files["file"]

        if file.filename == "":
            flash("No file selected.", "error")
            return redirect(url_for("index"))

        if not allowed_file(file.filename):
            flash("Invalid file type. Only PDF, DOC, and DOCX are allowed.", "error")
            return redirect(url_for("index"))

        # Save file securely
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(file_path)

        # Save application data to MongoDB
        mongo.db.applications.insert_one({
            "name": name,
            "email": email,
            "phone": phone,
            "position": position,
            "salary": salary,
            "file_path": file_path
        })

        flash("Application submitted successfully!", "success")
        return redirect(url_for("index"))

    return render_template("index.html")

if (__name__) == "(__main__)":
    app.run(debug=True)

