numb1 = int(input("Enter the number: "))
numb2 = int(input("Enter the number: "))
op = input("Enter the operator: ")

if op == '+':
    print(numb1+numb2)
elif op == '-':
    print(numb1-numb2)
elif op == '*':
    print(numb1*numb2)
elif op == '/':
    print(abs(numb1/numb2))
else:
    print("Invalid Operator")