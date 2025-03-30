amount = int(input("enter total amount : "))

note100 = amount // 100
note50 = (amount % 100) // 50
note10 = ((amount % 100) % 50) // 10

print(f"notes of 100 yen {note100}")
print(f"notes of 50 yen {note50}")
print(f"notes of 10 yen {note10}")
 