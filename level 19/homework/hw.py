#  level 11

# 1

city1 = "tbilisi"
city2 = "batumi"
city3 = "kutaisi"
print(city1)
print(city2)
print(city3)

# 2

first_name = "hello"
last_name = "world"
full_name = first_name + " " + last_name
print(full_name)

# 3

num1 = 10
num2 = 5
print("Sum:", num1 + num2) #ჯამი
print("Difference:", num1 - num2) #სხვაობა
print("ნამრავლი:", num1 * num2)  #
print("განაყოფი:", num1 / num2)

# 4

a = 15
b = a
print("a: ", a)
print("b: ", b)

# ამ კოდში b ღირებულება მიიღებს a ღირებულებას, ამიტომ ორივე ცვლადი (a და b) იქნება 15.

# 5

favorite_color = input("enter you favorite color: ")
print("Your favorite color is " + favorite_color + ".")


# 7


float_number = 7.89
int_number = int(float_number)
print("Original float:", float_number)
print("Converted to integer:", int_number)

# 8

number = 123
print(type(number))

# 9


num1 = 15
num2 = 20


print(f"{num1} < {num2}:", num1 < num2)    # True
print(f"{num1} > {num2}:", num1 > num2)    # False
print(f"{num1} <= {num2}:", num1 <= num2)  # True
print(f"{num1} >= {num2}:", num1 >= num2)  # False
print(f"{num1} == {num2}:", num1 == num2)  # False
print(f"{num1} != {num2}:", num1 != num2)  # True


# 10

str1 = "Python"
str2 = "is"
str3 = "awesome!"
sentence = str1 + " " + str2 + " " + str3 
print(sentence)

# 11

num1 = 10
num2 = 20
print(num1 < num2)  # True
print(num1 > num2)  # False
print(num1 <= num2)  # True
print(num1 >= num2)  # False
print(num1 == num2)  # False
print(num1 != num2)  # True



# 12

age1 = 25
age2 = 30
print(age1 > age2)  # False
print(age1 >= age2)  # False

# 13

a = 5
b = 10
c = 15
print(a < b)  # True
print(a < c)  # True
print(b < c)  # True

# 14

str1 = "Hello"
str2 = "World"
print(str1 == str2)  # False
print(str1 != str2)  # True



# new

# ახალი: 

# 1. დაწერეთ if-else განცხადება, რომელიც დაბეჭდავს "დილა მშვიდობისა!" თუ მიმდინარე საათი 12-მდეა და "დილა მშვიდობისა!" თუ ეს არის 12 ან უფრო გვიან. 

# 1

current_hour = 15

if current_hour < 12: 
    print("Good morning!")    
else:
    print("Good Afternoon!")   




# 2. შექმენით if-else განცხადება, რათა შეამოწმოთ თუ ტემპერატურა 30 გრადუსს აღემატება. თუ ასეა, დაბეჭდეთ "გარეთ ცხელა!"; წინააღმდეგ შემთხვევაში, დაბეჭდეთ „არ არის ძალიან ცხელი“. 

# 2

temperature = 35

if temperature > 30:
    print("its hot outside! ")    
else:
    print("its not too hot outside.")    

# 3. შექმენით if-else განცხადება, რათა დაადგინოთ არის თუ არა ადამიანი მოზარდი. თუ ასაკი 19 წელზე ნაკლებია დაბეჭდეთ „შენ მოზარდი ხარ!“; წინააღმდეგ შემთხვევაში დაბეჭდეთ „შენ არ ხარ მოზარდი“.

# 3

age = 17

if age < 19:
    print('you are teenager! ')
else:
    print("you are not a teenager")