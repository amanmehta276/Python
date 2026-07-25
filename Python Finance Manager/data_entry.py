from datetime import datetime

date_format="%d-%m-%Y"
CATEGORIES={"I":"Income","E":"Expense"}

def get_date(prompt,allow_defaults=False):
    date_str=input(prompt)
    if allow_defaults and not date_str:
        return datetime.today().strtime(date_format)

    try:
        valid_date=datetime.strptime(date_str,date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid format .please enter in dd-mm-yyyy format")
        return get_date(prompt,allow_defaults)

    
def get_amount():
    try:
        amount=float(input("Enter the amount: "))
        if amount <=0:
            raise ValueError("Amount must be non negative")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()

def get_category():
    category=input("enter the category ('I' for Income or 'E' for Expense) : ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]
    print("Invalid Category,Please Enter 'I' for Income or 'E' for Expense")
def get_description():
    return input("Enter a description (Optional)")