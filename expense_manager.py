from datetime import datetime
import json
import os
import csv

class ExpenseManager:
    FILE_NAME = "expenses.json"
    BUDGET_FILE_NAME = "budget.json"
    
    def __init__(self):
        self.expenses = self.load_expenses()
        self.budgets = self.load_budgets()
    
    def load_expenses(self):
        if not os.path.exists(self.FILE_NAME):
            return []
        with open(self.FILE_NAME, 'r', encoding='utf-8') as file:
            return json.load(file)
        
    def load_budgets(self):
        if not os.path.exists(self.BUDGET_FILE_NAME):
            return []
        with open(self.BUDGET_FILE_NAME, 'r', encoding='utf-8') as file:
            return json.load(file)
        
    def save_expenses(self):
        with open(self.FILE_NAME, 'w', encoding='utf-8') as file:
            json.dump(self.expenses, file, indent=4)
    
    def save_budgets(self):
        with open(self.BUDGET_FILE_NAME, 'w', encoding='utf-8') as file:
            json.dump(self.budgets, file, indent=4)
            
    def add_expense(self, description, amount, category=None):
        new_id = 1 if not self.expenses else max(exp["id"] for exp in self.expenses) + 1
        date_str = datetime.now().strftime("%Y-%m-%d")
        
        expense = {
            'id' : new_id,
            'date' : date_str,
            'description': description,
            'amount': amount,
            'category': category
        }
        
        self.expenses.append(expense)
        self.save_expenses()
        return new_id
    
    def update_expense(self, expense_id, description, amount, category=None):
        for expense in self.expenses:
            if expense['id'] == expense_id:
                expense['description'] = description
                expense['amount'] = amount
                expense['category'] = category

                self.save_expenses()
                return True, expense_id
        return False, expense_id
    
    def delete_expense(self, expense_id):
        initial_length = len(self.expenses)
        self.expenses = [expense for expense in self.expenses if expense['id'] != expense_id]
        if len(self.expenses) < initial_length:
            self.save_expenses()
            return True
        return False
    
    def list_expenses(self, category=None):
        if category:
            return [expense for expense in self.expenses if expense['category'] == category]
        return self.expenses
    
    def summary(self, month=None, category=None):
        total = 0
        for expense in self.expenses:
            if category and expense['category'] != category:
                continue
            if month:
                expense_month = datetime.strptime(expense['date'], '%Y-%m-%d').month
                if expense_month == month:
                    total += expense['amount']
            else:
                total += expense['amount']
                
        return total
    
    def set_budget(self, month, amount):
        for budget in self.budgets:
            if budget['month'] == month:
                budget['amount'] = amount
                self.save_budgets()
                return
        self.budgets.append({'month': month, 'amount': amount})
        self.save_budgets()
        
    def get_budget(self, month):
        for budget in self.budgets:
            if budget['month'] == month:
                return budget['amount']
        return None
    
    def check_budget(self, month):
        budget_amount = self.get_budget(month)
        if budget_amount is None:
            return None, None
        
        total_expenses = self.summary(month)
        remaining_budget = budget_amount - total_expenses
        return budget_amount, remaining_budget
    
    def export_to_csv(self):
        with open('expenses.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'date', 'description', 'amount', 'category']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for expense in self.expenses:
                writer.writerow(expense)
            