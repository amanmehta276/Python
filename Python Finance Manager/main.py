import pandas as pd
import csv
from datetime import datetime
from data_entry import get_date,get_amount,get_category,get_description

class CSV:
    CSV_FILE="Finance_data.csv"
    COLUMNS=["Date","Amount","Category","Description"]
    FORMAT="%d-%m-%Y"

    @classmethod #used to access csv_file causse this is a class variable
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE) #pd.read_csv reads data isnisde csv file
        except FileNotFoundError: #df=dataframe
            df=pd.DataFrame(columns=cls.COLUMNS) #created 4 columns for csv file
            df.to_csv(cls.CSV_FILE,index=False) #to_csv sends data to csv file

    @classmethod
    def add_entry(cls,Date,Amount,Category,Description):
        new_entry={
            "Date":Date,
            "Amount":Amount,
            "Category":Category,
            "Description":Description
        }
        with open(cls.CSV_FILE,"a",newline="") as csvfile:  #context manager as it always opens
            writer=csv.DictWriter(csvfile,fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Entry added Successfully")

    @classmethod
    def get_transactions(cls,start_date,end_date):
        df=pd.read_csv(cls.CSV_FILE)
        df["Date"]=pd.to_datetime(df["Date"],format=CSV.FORMAT)
        start_date=datetime.strptime(start_date,CSV.FORMAT)
        end_date=datetime.strptime(end_date,CSV.FORMAT)

        mask=(df["Date"]>=start_date) & (df["Date"]<=end_date)
        filtered_df=df.loc[mask]

        if filtered_df.empty:
            print("No transactions found in the given date range")
        else:
            print(f"Transactions from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}")
            print(filtered_df.to_string(index=False,formatters={"Date":lambda x:x.strftime(CSV.FORMAT)}))
            total_income = filtered_df[filtered_df["Category"] == "Income"]["Amount"].sum()
            total_expense = filtered_df[filtered_df["Category"] == "Expense"]["Amount"].sum()
            print("\nSummary: ")
            print(f"Total Income: ${total_income:.2f}")
            print(f"Total Expense: ${total_expense:.2f}")
            print(f"Net Savings: ${(total_income-total_expense):.2f}")

def add():
    CSV.initialize_csv()
    date=get_date("Enter the date of transaction: ",allow_defaults=True)
    amount=get_amount()
    category=get_category()
    description=get_description()
    CSV.add_entry(date,amount,category,description)
    
add()
# CSV.initialize_csv()  #oops stuffs
# CSV.add_entry("22-07-2026",125.65,"Income","Salary")
CSV.get_transactions("01-01-2026","22-07-2026")
