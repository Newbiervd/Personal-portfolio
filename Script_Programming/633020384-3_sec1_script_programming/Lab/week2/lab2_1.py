#แก้ไขโค้ดนี้ให้ถูกต้อง

try:

    number = int(input("Enter an integer: "))
    

    if number > 0:
        sign = "positive"
    elif number < 0:
        sign = "negative"
    else:
        sign = "zero"
        
    
    if number % 2 == 0:
        parity = "even"
    else:
        parity = "odd"
        

    print(f"The number is {sign} and {parity}.")

except ValueError:
    print("Please enter a valid integer.")