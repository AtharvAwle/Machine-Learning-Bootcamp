try:
    a=b
    # 10/0
except Exception as ex:
    print(ex)
    
try:
    div = int(input("Give a number"))
except ValueError as ex1:
    print("this is not a valid number")
except ZeroDivisionError as ex2:
    print("We cannot divide by zero")
except Exception as ex3:
    print(ex3)
    