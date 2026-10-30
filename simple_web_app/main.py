from flask import Flask, render_template, request
import platform
import sys
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    sys_info = {
        "python_version": sys.version.split()[0],
        "os_platform": platform.platform(),
        "server_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "runtime": "Google App Engine (Python 3.12)"
    }
    return render_template("index.html", sys_info=sys_info)

@app.route("/grade-calculator", methods=["POST"])
def grade_calculator():
    sys_info = {
        "python_version": sys.version.split()[0],
        "os_platform": platform.platform(),
        "server_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "runtime": "Google App Engine (Python 3.12)"
    }
    
    student_name = request.form.get("student_name", "").strip()
    roll_number = request.form.get("roll_number", "").strip()
    
    try:
        m1 = float(request.form.get("subject1", 0))
        m2 = float(request.form.get("subject2", 0))
        m3 = float(request.form.get("subject3", 0))
        m4 = float(request.form.get("subject4", 0))
        
        total = m1 + m2 + m3 + m4
        percentage = round((total / 400.0) * 100, 2)
        
        if percentage >= 90:
            grade = "A+ (Outstanding)"
            status = "Passed with Distinction"
        elif percentage >= 75:
            grade = "A (First Class with Distinction)"
            status = "Passed"
        elif percentage >= 60:
            grade = "B (First Class)"
            status = "Passed"
        elif percentage >= 50:
            grade = "C (Second Class)"
            status = "Passed"
        elif percentage >= 40:
            grade = "D (Pass Class)"
            status = "Passed"
        else:
            grade = "F (Fail)"
            status = "Needs Improvement"
            
        result = {
            "name": student_name,
            "roll": roll_number,
            "m1": m1, "m2": m2, "m3": m3, "m4": m4,
            "total": total,
            "percentage": percentage,
            "grade": grade,
            "status": status,
            "passed": percentage >= 40
        }
    except ValueError:
        result = {"error": "Invalid numbers entered for marks. Please enter numeric values."}
        
    return render_template("index.html", sys_info=sys_info, grade_result=result)

@app.route("/text-analyzer", methods=["POST"])
def text_analyzer():
    sys_info = {
        "python_version": sys.version.split()[0],
        "os_platform": platform.platform(),
        "server_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "runtime": "Google App Engine (Python 3.12)"
    }
    
    user_text = request.form.get("user_text", "")
    words = user_text.split()
    
    text_result = {
        "original": user_text,
        "char_count": len(user_text),
        "char_count_no_spaces": len(user_text.replace(" ", "")),
        "word_count": len(words),
        "reversed": user_text[::-1],
        "uppercase": user_text.upper(),
        "lowercase": user_text.lower(),
        "vowel_count": sum(1 for c in user_text.lower() if c in "aeiou")
    }
    
    return render_template("index.html", sys_info=sys_info, text_result=text_result)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
