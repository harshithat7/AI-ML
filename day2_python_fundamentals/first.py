bill=float(input("Enter the total bill amount: "))
people=int(input("Enter the number of people: "))
share=bill/people
print(f"Total bill amount: {bill: .2f}")
print(f"Each person pays: {share: .2f}")