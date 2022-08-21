import random
#Letters list
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#numbers list
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#symbols list
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#Greet user
print("Welcome to the PyPassword Generator!")
#take input from user.
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#create a list to hold all the random chars
password_list = []
#loop through all the numbers at random add to list
for x in range(1,nr_numbers+1):
    password_list.append(random.choice(numbers))
#loop through all the letters at random add to the list
for x in range(1,nr_letters+1):
    password_list.append(random.choice(letters))
#loop through all the Symbols at random add to the list
for x in range(1,nr_symbols+1):
    password_list.append(random.choice(symbols))
# create password variable
password = ""
#shuffle the password list
random.shuffle(password_list)
#add loop through the shuffled list.
for char in password_list:
    #append to password variable
    password+=char
#print password.
print(password)
""" rand_pass = ""
for x in password_list:
    rand_pass += random.choice(password_list)
print(rand_pass) """