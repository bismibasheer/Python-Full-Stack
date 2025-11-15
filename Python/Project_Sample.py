# ================= Personal Finance Tracker =================
import pickle
import re


users = []     
expenses = []    
budgets = []   


def print_banner():
    print("*" * 30)
    print("  PERSONAL FINANCE TRACKER  ")
    print("*" * 30)


class User:
    def __init__(self, user_id, username, password):
        self.id = user_id
        self.username = username
        self._password = password  # Encapsulation

class Expense:
    def __init__(self, user_id, category, amount):
        self.user_id = user_id
        self.category = category.title()
        self.amount = amount

    @staticmethod
    def is_valid_amount(amount):
        return isinstance(amount, (int, float)) and amount >= 0

def register():
    username = input("Enter username: ")
    password = input("Enter password: ")

    for u in users:
        if u.username == username:
            print(" Username already exists!")
            return None

    user_id = len(users) + 1
    users.append(User(user_id, username, password))
    print(f" Registration successful! Your User ID is {user_id}")
    return user_id

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    for u in users:
        if u.username == username and u._password == password:
            print(f" Login successful! Welcome {username}")
            return u.id
    print(" Invalid username or password.")
    return None

def add_expense(user_id):
    category = input("Enter category: ")
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print(" Invalid amount.")
        return

    if not Expense.is_valid_amount(amount):
        print(" Amount must be >= 0")
        return

    exp = Expense(user_id, category, amount)
    expenses.append({"user_id": exp.user_id, "category": exp.category, "amount": exp.amount})
    print(f" Expense added: {exp.category} - ${exp.amount}")

def set_budget(user_id):
    category = input("Enter category: ")
    try:
        amount = float(input("Enter budget amount: "))
    except ValueError:
        print(" Invalid amount.")
        return
    budgets.append({"user_id": user_id, "category": category.title(), "amount": amount})
    print(f" Budget set: {category.title()} - ${amount}")

def view_reports(user_id):
    categories = list({e["category"] for e in expenses if e["user_id"] == user_id})

    if not categories:
        print(" No expenses recorded yet.")
        return

    total_per_category = {c: sum(e["amount"] for e in expenses if e["category"] == c and e["user_id"] == user_id) for c in categories}

    print("\n Expense Report:")
    for cat, total in total_per_category.items():
        print(f"- {cat}: ${total}")

    over_budget = [b for b in budgets if b["user_id"] == user_id and
                   sum(e["amount"] for e in expenses if e["category"] == b["category"] and e["user_id"] == user_id) > b["amount"]]
    if over_budget:
        print("\n Over-budget categories:")
        for b in over_budget:
            print(f"- {b['category']} (Budget: ${b['amount']})")
    else:
        print("\n All categories are within budget.")


def main():
    while True:
        print_banner()
        print("1. Register\n2. Login\n3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            user_id = login()
            if user_id:
                while True:
                    print("\n---- User Menu ----")
                    print("1. Add Expense\n2. Set Budget\n3. View Reports\n4. Logout")
                    sub_choice = input("Enter choice: ")

                    if sub_choice == "1":
                        add_expense(user_id)
                    elif sub_choice == "2":
                        set_budget(user_id)
                    elif sub_choice == "3":
                        view_reports(user_id)
                    elif sub_choice == "4":
                        print("Logged out.")
                        break
                    else:
                        print(" Invalid choice.")
        elif choice == "3":

            with open("users.pkl", "wb") as f:
                pickle.dump(users, f)
            with open("expenses.pkl", "wb") as f:
                pickle.dump(expenses, f)
            with open("budgets.pkl", "wb") as f:
                pickle.dump(budgets, f)
            print("Exiting... Data saved.")
            break
        else:
            print(" Invalid choice.")

if __name__ == "__main__":
    main()
