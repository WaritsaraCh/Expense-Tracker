import argparse
from datetime import datetime
from expense_manager import ExpenseManager

def main():
    
    manager = ExpenseManager()
    
    parser = argparse.ArgumentParser(description='A simple command-Line application')
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
 
    # Add command parser
    add_parser = subparsers.add_parser('add', help='Adds expenses with a description and amount')
    add_parser.add_argument('--description', type=str, required=True, help='Description of the expense')
    add_parser.add_argument('--amount', type=float, required=True, help='Amount of the expense')
    add_parser.add_argument('--category', type=str, help='Category of the expense (optional)')
    
    # Update command parser
    update_parser = subparsers.add_parser('update', help='Updates an exising expense with a new description and amount') 
    update_parser.add_argument('--id', type=int, required=True, help='ID of the expense to update')
    update_parser.add_argument('--description', type=str, required=True, help='New description of the expense')
    update_parser.add_argument('--amount', type=float, required=True, help='New amount of the expense')
    update_parser.add_argument('--category', type=str, help='Category of the expense (optional)')
    
    # Delete command parser
    delete_parser = subparsers.add_parser('delete', help='Deletes an existing expense by ID')
    delete_parser.add_argument('--id', type=int, required=True, help='ID of the expense to delete')
    
    # List command parser
    list_parser = subparsers.add_parser('list', help='Lists all expenses')
    list_parser.add_argument('--category', type=str, help='Category to filter expenses (optional)')
    
    # Summary command parser
    summary_parser = subparsers.add_parser('summary', help='Provides a summary of expenses')
    summary_parser.add_argument('--month', type=int, help='Month for the summary (1-12)')
    summary_parser.add_argument('--category', type=str, help='Category for the summary (optional)')
    
    # Set Budget command parser
    budget_parser = subparsers.add_parser('set_budget', help='Sets a budget for each month')
    budget_parser.add_argument('--month', type=int, required=True, help='Month for the budget (1-12)')
    budget_parser.add_argument('--amount', type=float, required=True, help='Budget amount for the month')
    
    # Export command parser
    export_parser = subparsers.add_parser('export', help='Exports expenses to CSV ')
    
    args = parser.parse_args()
    
    if args.command == "add":
        if args.amount < 0:
            print('Amount must be a positive number')
            return
        expense_id = manager.add_expense(args.description, args.amount, args.category)
        print(f"Expense added successfully (ID: {expense_id})")
        
        current_month = datetime.now().month
        budget_amount, remaining_budget = manager.check_budget(current_month)
        if remaining_budget is not None and remaining_budget < 0:
            print(f"⚠️ Warning: You have exceeded your budget by ${abs(remaining_budget):.2f}!")
            
    elif args.command == "update":
        success, expense_id = manager.update_expense(args.id, args.description, args.amount, args.category)
        if success:
            print("Expense updated successfully")
        else:
            print(f"Expense with ID {expense_id} not found")
        
    elif args.command == "delete":
        success = manager.delete_expense(args.id)
        if success:
            print("Expense deleted successfully")
        else:
            print(f"Expense with ID {args.id} not found")
            
    elif args.command == "list":
        expenses = manager.list_expenses(args.category)
        print(f"ID\tDate\t\tDescription\tAmount\t\tCategory")
        if expenses:
            for expense in expenses:
                print(f"{expense['id']}\t{expense['date']}\t{expense['description']}\t\t${expense['amount']:.2f}\t\t{expense['category'] or 'N/A'}")
                
    elif args.command == "summary":
        total = manager.summary(args.month, args.category)
        if args.month:
            month_name = datetime(2026, args.month, 1).strftime('%B')
            print(f"Total expenses for {month_name}: ${total:.2f}")
        else:
            print(f"Total expenses: ${total:.2f}")
            
    elif args.command == "set_budget":
        if args.amount < 0:
            print('Budget amount must be a positive number')
            return
        
        manager.set_budget(args.month, args.amount)
        print(f"Budget for {args.month} set to ${args.amount:.2f}")
            
    elif args.command == 'export':
        manager.export_to_csv()
        print("Expenses exported to expenses.csv successfully")
        
    else:
        parser.print_help()

if __name__ == "__main__":
    main()