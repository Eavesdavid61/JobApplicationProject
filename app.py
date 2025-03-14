from flask import Flask, request, render_template, redirect, url_for, flash
from flask_pymongo import PyMongo
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "supersecretkey"

# MongoDB Configuration
app.config["MONGO_URI"] = "mongodb://localhost:27017/mydatabase"
mongo = PyMongo(app)

# File Upload Configuration
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        file = request.files["file"]

        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(file_path)

            # Save to MongoDB
            mongo.db.users.insert_one({"name": name, "email": email, "file_path": file_path})
            flash("File uploaded successfully!", "success")
        
        return redirect(url_for("index"))

    return render_template("index.html")

if (__name__) == "__main__":
    app.run(debug=True)