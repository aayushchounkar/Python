
# class Finance:
#     print("1.Investment")
#     print("2.Loan")
#     choice=int(input("Enter the choice"))
#     if choice==1:
#         def calculate_future_value(principal, interest_rate, time):
            
#             future_value = ((principal *interest_rate * time)/100) + principal
#             return future_value

#         # Example usage:
#         principal_amount = float(input("Enter the principal amount: "))
#         interest_rate = float(input("Enter the annual interest rate (as a decimal): "))
#         investment_time = int(input("Enter the number of years the money is invested: "))

#         result = calculate_future_value(principal_amount, interest_rate, investment_time)

#         print(f"The future value of the investment is: {result}")


#     elif choice == 2:
#         def check_credit_score(credit_score):
#             return credit_score >= 700

#         def check_loan_amount(loan_amount,income):
#             return loan_amount <= (income*0.3)

#         def loan_approval(credit_score, income, loan_amount):
#             if check_credit_score(credit_score) and check_loan_amount(loan_amount,income):
#                 return "Loan Approved"
#             else:
#                 return "Loan Denied"

#         credit_score = int(input("Enter your credit score: "))
#         income = float(input("Enter your annual income: "))
#         loan_amount = float(input("Enter the loan amount you are requesting: "))

#         approval_status, message = loan_approval(credit_score, income, loan_amount)

#         print(f"Loan Status: {message}")
