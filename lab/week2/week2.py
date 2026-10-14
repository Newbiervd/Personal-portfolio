# lab2_1.py

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

# lab2_2.py

try:
  
    age = int(input("กรุณากรอกอายุของคุณ: "))
    
    
    if age < 13:
        genre_recommend = "ภาพยนตร์แอนิเมชันหรือภาพยนตร์สำหรับครอบครัว (Animation / Family)"
    elif age <= 17:
        genre_recommend = "ภาพยนตร์วัยรุ่นหรือแฟนตาซี (Teen / Fantasy)"
    else:
        genre_recommend = "ภาพยนตร์ทั่วไป ดราม่า หรือไซไฟ (Drama / Sci-Fi)"
        
    print(f"ประเภทภาพยนตร์ที่เหมาะสมกับคุณคือ: {genre_recommend}")
    
   
    like_action = input("คุณชอบภาพยนตร์แอคชันหรือไม่? (yes/no): ").strip().lower()
    
    
    if age >= 18 and like_action == "yes":
        print("ข้อความแนะนำพิเศษ: คุณอาจจะชอบภาพยนตร์แอคชันเรท R ที่มีความตื่นเต้นและเนื้อหาที่เข้มข้นขึ้น!")

except ValueError:
    print("กรุณากรอกอายุเป็นตัวเลขจำนวนเต็มเท่านั้น")
