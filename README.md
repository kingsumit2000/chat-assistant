# chat-assistant
# Chat Assistant

This is a Flask-based chatbot that answers SQL queries from an SQLite database.

## 🚀 Hosted Link
[Chat Assistant on Render](https://chat-assistant.onrender.com)

## 🛠 Running Locally
1. Clone the repository:
git clone https://github.com/kingsumit2000/chat-assistant  cd chat-assistant

2. Install dependencies:
pip install -r requirements.txt
3. Initialize the database:
python init_db.py
4. Run the Flask app:
python app.py


## 📝 Supported Queries
- **"Show me all employees in Sales"** → Returns list of employees in Sales.
- **"Who is the manager of Engineering?"** → Returns manager name.
- **"List all employees hired after 2021-01-01"** → Returns filtered employees.
- **"What is the total salary expense for Marketing?"** → Returns total salary.

## 🔥 Future Improvements
- Support complex queries.
- Improve NLP processing for flexible queries.
- Add a frontend UI.


