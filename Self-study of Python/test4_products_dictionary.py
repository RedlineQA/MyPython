# הגדרת המוצרים עם שמות ומחירים כמחרוזת
products = {
    "Gummy Bears": "5₪",
    "Chocolate Bar": "8₪",
    "Lollipop": "3₪",
    "Sour Strips": "6₪"
}

# קבלת שם המשתמש וברכת קבלת פנים
name = (input("Enter name: "))
print(f"Welcome {name}!\n") #הפקודה n\ בתחילת הפקודה יוצרת רווח של שורה מלמעלה. בסוף הפקודה יוצרת רווח של שורה מלמטה

# הצגת רשימת המוצרים עם מספרים סידוריים
print("What would you like to buy?")
for i, item in enumerate(products):
    print(f"{i+1}. {item}: {products[item]}")

# יצירת סל קניות ריק לשמירת הבחירות של המשתמש
basket = []

# לולאה שמאפשרת הוספת מוצרים לסל הקניות
while True:
    try:
        # בקשת מספר מוצר מהמשתמש
        product = int(input(f"\nEnter product number: "))

        # בדיקה אם מספר המוצר תקף (בתחום הרשימה)
        if product < 1 or product > len(products):
            print("Invalid product number. Please choose a number from the list.")
            continue

        # בקשת כמות עבור המוצר
        quantity = int(input(f"How many? "))

        # הוספת המוצר והכמות לסל הקניות
        basket.append((product, quantity))

        # לולאה פנימית לוודא שהמשתמש עונה "yes" או "no" בלבד
        while True:
            more = input("\nAnother product? (yes/no): ").strip().lower()
            if more == "no":
                exit_loop = True  # אם "no" - נשבור גם את הלולאה החיצונית
                break
            elif more == "yes":
                exit_loop = False  # אם "yes" - ממשיכים לסבב הבא
                break
            else:
                print("Please enter 'yes' or 'no'.")  # קלט לא תקין

        # יציאה מהלולאה החיצונית אם המשתמש סיים להזמין
        if exit_loop:
            break

    except:
        # טיפול בשגיאות (למשל אם הוזן טקסט במקום מספר)
        print("Invalid input. Please try again.")
        continue

# יצירת רשימה של שמות המוצרים לפי הסדר (מהמילון המקורי)
product_list = list(products.keys())

# שלב מיזוג: יצירת מילון חדש לאגירת כמות כוללת לכל מוצר שנבחר
merged_basket = {}
for product_index, quantity in basket:
    product_name = product_list[product_index - 1]  # קבלת שם המוצר לפי מספרו
    if product_name in merged_basket:
        merged_basket[product_name] += quantity  # אם כבר קיים, מוסיפים את הכמות
    else:
        merged_basket[product_name] = quantity  # אם לא קיים, יוצרים ערך חדש

# הדפסת הקבלה
print("\n--- Receipt ---")
total_price = 0  # משתנה לצבירת סך הכל

# מעבר על כל פריט ממוזג והצגת פירוט
for i, (product_name, quantity) in enumerate(merged_basket.items(), 1):
    price = int(products[product_name].replace("₪", ""))  # המרת מחיר למספר
    total = price * quantity  # חישוב מחיר כולל לפריט
    print(f"{i}. {product_name} x{quantity} → {total}₪")  # הדפסת השורה
    total_price += total  # צבירת הסכום הכולל

# הדפסת הסכום הכולל
print(f"\nTotal: {total_price}₪")