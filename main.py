import json;



def load_expenses(file_path):
    
    try:
        with open(file_path , 'r') as file:
            expenses = json.load(file)
    except:
        expenses = []
    
    return expenses

def save_expenses(expenses , file_path):
    try:
        with open(file_path , 'w') as file:
            json.dump(expenses , file , indent = 4)
            
    except FileNotFoundError:
        print("The path is not found")

def add_expenses(expenses ,amount, description, category, date):
    
    expense = {
        "amount": amount,
        "description": description,
        "category": category,
        "date": date
    }
    expenses.append(expense)
    print("Expensed added successfully!!")
    
def view_expenses(expenses):
    
    for expense in expenses:
        print(f"{expense["amount"]} | {expense["description"]} | {expense["category"]} | {expense["date"]}")


def delete_expense(expenses , user_delete_index):
    
    try:
        expenses.pop(user_delete_index - 1)
    except IndexError:
        print("No available number index") 

def total_expenses(expenses):
    total = 0
    
    for amount_expense in expenses:
        expense_amount = amount_expense['amount']
        total += expense_amount
    
    print(f"Total Expenses: {total}")
    


def main():
    
    file_path = 'expenses.json'
    expenses = load_expenses(file_path)
    while True:
        
        print("Welcome to Expenses Tracking System.")
        print("1. Add The Expenses")
        print("2. View The Expenses")
        print("3. Delete The Expenses")
        print("4. Display Total Expenses")
        print("5. Exit the Application")
        
        user_choice = input("Choose the above category (1 - 5): ")
        
        if user_choice == '1':
            amount = int(input("Write the amount used: "))
            decription = input("Enter description: ")
            category = input("Enter category (food , transport): ")
            date = input("Enter the date (YYY - MM - DD): ")
            add_expenses(expenses , amount , decription , category , date)
            save_expenses(expenses , file_path)
        
        elif user_choice == '2':
            view_expenses(expenses)
        
        elif user_choice == '3':
            user_delete_index = int(input("What expense do you want to delete: "))
            delete_expense(expenses , user_delete_index)
            save_expenses(expenses , file_path)
            
        elif user_choice == '4':
            total_expenses(expenses)
            
        else:
            print("You have successfully exit the application.")
            break
        
        

if __name__ == "__main__":
    main()
