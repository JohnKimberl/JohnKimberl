user= input("Enter Your Name:")
if user.isdigit():
  print(f"Hello {user}")
else: 
  print(f"Hello {user}"))
  
operator= input ("Enter a operator (+ - * /):")
num1 = float(input("Enter the first number: "))
num2= float(input("Enter the second number: "))

if operator == "+":
    result = num1 +num2
elif operator == "-":
    result = num1- num2
elif operator == "*":
    result = num1*num2
elif operator == "/":
    result = num1/num2
else:
    print(f"{operator} is not a valid operator")

print (f"\n Hello your operation gives the result of {result:.2f}. Thank you for using the program")
    
