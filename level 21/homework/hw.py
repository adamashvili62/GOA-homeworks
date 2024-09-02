# level 21

# 1. სიაში შეინახეთ 5 რიცხვი, შემდეგ კი დარპინტეთ პირველი და მეოთხე ელემენტების ნამრავლი.


# 1
#          0  1  2   3  4
# numbers = [2, 5, 7, 10, 3]  # 5 რიცხვის შემცველი სია
# result = numbers[0] * numbers[3]  # პირველი და მეოთხე ელემენტების ნამრავლი
# print(result)

# # 2. სიაში შეინახეთ 7 სტრინგი, შემდეგ დაპრინტეთ შუა სტრინგი.

# strings = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi"]  # 7 სტრინგის შემცველი სია
# middle_string = strings[len(strings) // 2]  # შუა სტრინგის მოძებნა
# print(middle_string)

# # 3. ცვლადში შეინახეთ სტრინგი, შემდეგ კი დაპრინტეთ ამ სტრინგის მხოლოდ მეორე ასო.

# my_string = "python"
# second_letter = my_string[1]
# print(second_letter) 

# 4. შექმენით ვენდინგ მანქანის თამაში პითონის მეშვეობით, როგორც გაკვეთილზე გავაკეთე, უნდა გქონდეთ პროდუქტები, მომხმარებელს უნდა შეეძლოს არჩევა რიცხვის მიხედვით, შემდეგ კი უნდა დაუპრინტოს ის პროდუქტი, რომელიც ამოირჩია, პროდუქტები შეინახეთ სიაში.

 # პროდუქტების სია
products = ["Water", "Soda", "Juice", "Chips", "Candy"]

# მომხმარებლისთვის პროდუქტების სიის ჩვენება

print("welcome to Vending Machinr! Here are our Products")
for i, product in enumerate(products):
    print(f"{i + 1}, {product}")

# მომხმარებლის არჩევანის მიღება

choice = int(input("Please enter the number of the product you want:  "))

# მომხმარებლისთვის არჩეული პროდუქტის ჩვენება
if 1 <= choice <= len(products):
    print(f"you selected: {products[choice - 1]}")
else:
    print("invalid selection. please try again")
