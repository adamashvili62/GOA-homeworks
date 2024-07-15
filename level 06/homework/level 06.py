# Python: 
# Easy:
# 1. შექმენით ცვლადი სახელად name, სადაც მომხმარებელს input-ის მეშვეობით შემოატანინებთ სახელს,
#  შემდეგ კი მისალმების მესიჯი, მაგალითად 'hello ' + (სახელი). 

name = input("Enter your name: ")
print("hello" + " " + name)
# 2. შექმენით სამი ცვლადი, სამივეში შეინახეთ განსხვავებული ინფორმაციის ტიპები, შემდეგ კი დაპრინტეთ ისინი.

favorite_car = "Lamborgini"
age = 12
height = 1.51

print(favorite_car)
print(age)
print(height)


# 3. შექმენით ცვლადი სახელად user_name, სადაც მომხარებელს შემოატანინებთ სახელს, 
# შემდეგ შექმენით ცვლადი სახელად last_name, სადაც მომხმარებელს შემოატანინებთ გვარს,
#  ბოლოს დაუპრინტეთ მსგავსი მესიჯი: 'hello ' + (სახელი) + (გვარი).

user_name = input("Enter your name: ")
last_name = input("Enter your lastname: ")
print("hello" + " " + user_name + " " + last_name )


# 4. კომენტარში ახსენით რა არის input და output, შემდეგ ახსენით რა არის კარგი პრაქტიკები და რომელი კარგი პრაქტიკები ვიცით.

#input - შემოტანა, 
# output - გატანა / შედეგი


# Hard:
# 5. შექმენით ორი ცვლადი, სადაც მომხმარებელს შემოატანინებთ ორ რიცხვს, 
# შეასრულეთ ამ რიცხვებზე შეკრება, გამოკლება, გამრავლება, გაყოფა და დაპრინტეთ შედეგები,
# (მინიშნება: input() მთლიანათ გადააქციეთ ინტეჯერად, int() ფუნქციის მეშვეობით).

number = int(input("Enter number: "))
number2 = int(input("Enter second number: "))
print(number + number2)
print(number - number2)
print(number * number2)
print(number / number2)
