def check_credit_score(credit_score):
    return credit_score >= 700

def check_loan_amount(loan_amount,income):
    return loan_amount <= (income*0.3)

def loan_approval(credit_score, income, loan_amount):
    if check_credit_score(credit_score) and check_loan_amount(loan_amount,income):
        return True, "Loan Approved"
    else:
        return False, "Loan Denied"

credit_score = int(input("Enter your credit score: "))
income = float(input("Enter your annual income: "))
loan_amount = float(input("Enter the loan amount you are requesting: "))

approval_status, message = loan_approval(credit_score, income, loan_amount)

print(f"Loan Status: {message}")
