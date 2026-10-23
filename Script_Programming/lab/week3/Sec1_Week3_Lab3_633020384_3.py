# lab3_1.py

print("=== Part 1: ตารางสูตรคูณแม่เดียว (Single Number Table) ===")
try:
    
    target_num = int(input("กรอกตัวเลขที่ต้องการสร้างแม่สูตรคูณ: "))
    
    
    for i in range(1, 13):
        print(f"{target_num} x {i} = {target_num * i}")
        
except ValueError:
    print("กรุณากรอกเฉพาะตัวเลขจำนวนเต็มเท่านั้น")

print("\n" + "="*50 + "\n")

print("=== Part 2: ตารางสูตรคูณแบบเต็ม (Full Multiplication Grid) ===")

for i in range(1, 13):
    
    for j in range(1, 13):
        print(f"{i * j:4d}", end="")
    print()

# lab3_2.py

print("=== Part 1: โปรแกรมตัวนับถอยหลัง (Countdown Timer) ===")
try:
    count = int(input("กรอกตัวเลขเริ่มต้นสำหรับนับถอยหลัง: "))
    
    while count >= 0:
        print(count)
        count -= 1  
        
    print("Blast off! (จุดระเบิดยาน!)")
    
except ValueError:
    print("กรุณากรอกตัวเลขจำนวนเต็ม")

print("\n" + "="*50 + "\n")

print("=== Part 2: เกมทายตัวเลขอย่างง่าย (Simple Guessing Game) ===")
secret_number = 42
max_guesses = 5
guess_count = 0

print(f"ระบบได้สุ่มเลขลับไว้แล้ว คุณมีสิทธิ์ทายทั้งหมด {max_guesses} ครั้ง!")

while True:
    try:
        if guess_count >= max_guesses:
            print(f"เสียใจด้วย! คุณหมดโควตาการทายแล้ว (ทายครบ {max_guesses} ครั้ง) เลขลับคือ {secret_number}")
            break
            
        guess = int(input(f"ครั้งที่ {guess_count + 1} - ทายตัวเลขของคุณ: "))
        guess_count += 1
        
        if guess < secret_number:
            print("Too low! Try again. (น้อยเกินไป! ลองใหม่นะ)")
        elif guess > secret_number:
            print("Too high! Try again. (มากเกินไป! ลองใหม่นะ)")
        else:
            print("Congratulations! You guessed it! (ยินดีด้วย! คุณทายถูกแล้ว)")
            break 
            
    except ValueError:
        print("กรุณากรอกเฉพาะตัวเลขจำนวนเต็ม")
