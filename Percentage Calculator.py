print("enter marks obtained in 4 subject : ")

english=int(input("Enter English Mark :"))
maths=int(input("Enter Maths Mark :"))
biology=int(input("Enter Biology Mark :"))
physics=int(input("Enter Physics Mark :"))

total=english + maths + biology + physics
print(f"total marks : {total}")

perc=(total/400)*100
print(f"percentage mark : {perc}%")
