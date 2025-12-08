# Expense Tracker Project

expensesList = []   #list of expense in the from of dictionary 
print("WELCOME TO THE EXPENSE TRACKER")

while True:
    print("\n=======MENU=======")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expense")
    print("4. Exit")

    choice = int(input("Please Enter Your Choice : "))


# 1. ADD EXPENSE

    if choice == 1 :
        date = input("Enter the date of transaction :-")
        category = input("Enter the category :- (Food/Travel/Shopping etc...)")
        discription = input("Add details :-")
        amount = float(input("Enter the amount :-"))

        expense= {
            "date": date,
            "category": category,
            "discription": discription,
            "amount": amount

        }

        expensesList.append(expense)
        print("\nEXPENSES ADDED SUCCESFULLY")


# 2. VIEW ALL EXPENSES

    elif choice == 2:
        if len(expensesList) == 0 :
            print("NO EXPENSE ADDED.")
        else:
            print("\n====== Here, All Your Expenses ======")
            count = 1
            for transaction in expensesList:
                print(f"\n{count} ==> {transaction["date"]} {transaction["category"]} {transaction["discription"]} {transaction["amount"]}")
                count = count+1

# 3. VIEW TOTAL EXPENSE

    elif choice == 3:
        total =0

        for transaction in expensesList:
         total= total + transaction["amount"]


        print("\n Your Total Expense :- ",total,  "/-")   


# 4. EXIT

    elif choice == 4:
        print("THANKYOU FOR USING OUR EXPENSE TRACKER.")
        break

    else:
     print("INVALID CHOISE.\nPLEASE TRY AGAIN")
    

