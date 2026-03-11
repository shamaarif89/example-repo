import math

print("Investment - to calculate the amount of interest you'll earn on your investment.")
print("Bond - to calculate the amount you'll have to pay on a home loan.")

user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").strip().lower()

if user_choice == "investment":
    P = float(input("Enter the amount of money you are depositing: "))
    r = float(input("Enter the interest rate: ")) /100 
    t = float(input("Enter the number of years you plan on investing: "))
    interest = input("Do you want simple or compound interest? ").strip().lower()

    if interest == "simple":
        A = P * (1 + r * t)
        print("The total amount after simple interest is:", round(A, 2))

    elif interest == "compound":
        A = P * math.pow((1 + r), t)
        print("The total amount after compound interest is:", round(A, 2))

    else:
        print("Invalid interest type selected.")

elif user_choice == "bond":
    P = float(input("Enter the present value of the house: "))
    r = float(input("Enter the annual interest rate : ")) /100
    n = int(input("Enter the number of months to repay the bond: "))

    i = r / 12
    repayment = (i * P) / (1 - (1 + i) ** (-n))
    print("The monthly repayment amount is:", round(repayment, 2))

else:
    print("Invalid selection. Please enter 'investment' or 'bond'.")