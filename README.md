# Expense Tracker CLI 💰

A simple and robust command-line application to manage your personal finances. This project allows you to track your expenses, set monthly budgets, and categorize your spending directly from your terminal.

This project is a solution to the [Expense Tracker project on roadmap.sh]https://github.com/WaritsaraCh/Expense-Tracker.git

## ✨ Features

* **Add Expenses**: Quickly add new expenses with a description, amount, and an optional category.
* **Update Expenses**: Modify existing expense details easily.
* **Delete Expenses**: Remove incorrect or old expenses using their ID.
* **List Expenses**: View a neatly formatted table of all your expenses. Filter by category if needed.
* **Expense Summary**: Get the total expenses overall, or filter the summary by a specific month and category.
* **Monthly Budgets**: Set a budget for each month. The app will warn you if you exceed your set budget!
* **Data Persistence**: Expenses and budgets are safely stored locally in JSON format (`expenses.json` and `budgets.json`).

## 🛠️ Prerequisites

* Python 3.x installed on your machine.
* No external libraries required! This project uses only Python's built-in modules (`argparse`, `json`, `datetime`, `os`).

## 🚀 Installation & Setup

1. Clone the repository to your local machine:
   ```bash
   git clone [https://github.com/](https://github.com/)<your-username>/expense-tracker.git
   ```
2. Navigate into the project directory:
    ```bash
    cd expense-tracker
    ```
3. Run the application:
   ```bash
    python app.py -h
   ```
## 📖 Usage Examples

Here are some common commands to get you started:

1. Add a new expense:
```bash
python app.py add --description "Lunch" --amount 20
# or with a category
python app.py add --description "Groceries" --amount 50 --category "Food"
```
2. List all expenses:
```bash
python app.py list
# filter by category
python app.py list --category "Food"
```
3. Update an expense (e.g., ID 1):
```bash
python app.py update --id 1 --description "Lunch with friends" --amount 25
```
4. Delete an expense:
```bash
python app.py delete --id 2
```
5. View summary of expenses:
```bash
# Total overall
python app.py summary 

# Total for August (Month 8)
python app.py summary --month 8 

```
6. Set a monthly budget (e.g., $1000 for August):
```bash
python app.py set_budget --month 8 --amount 1000

```

(If you add an expense that crosses this budget, the app will display a warning!)

📂 Project Structure

- `app.py`: The main entry point handling the Command Line Interface (CLI) user input.

- `expense_manager.py`: Contains the business logic and file handling operations (Separation of Concerns).

🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

Built with ❤️ using Python.