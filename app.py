from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Function to query database
def query_db(query, params=()):
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()
    cursor.execute(query, params)
    result = cursor.fetchall()
    conn.close()
    return result

@app.route("/", methods=["GET"])
def home():
    return "Chat Assistant is running!"

@app.route("/query", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("query", "").lower()

    if "employees in" in user_input:
        department = user_input.split("employees in ")[1].strip()
        result = query_db("SELECT Name FROM Employees WHERE Department=?", (department,))
        return jsonify({"employees": [row[0] for row in result] or "No employees found."})

    elif "manager of" in user_input:
        department = user_input.split("manager of ")[1].strip()
        result = query_db("SELECT Manager FROM Departments WHERE Name=?", (department,))
        return jsonify({"manager": result[0][0] if result else "Department not found."})

    elif "hired after" in user_input:
        date = user_input.split("hired after ")[1].strip()
        result = query_db("SELECT Name FROM Employees WHERE Hire_Date > ?", (date,))
        return jsonify({"employees": [row[0] for row in result] or "No employees found."})

    elif "total salary expense for" in user_input:
        department = user_input.split("total salary expense for ")[1].strip()
        result = query_db("SELECT SUM(Salary) FROM Employees WHERE Department=?", (department,))
        return jsonify({"total_salary_expense": result[0][0] if result[0][0] else "Department not found."})

    else:
        return jsonify({"error": "Unsupported query."})

if __name__ == "__main__":
    app.run(debug=True)
