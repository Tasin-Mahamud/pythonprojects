import  random

list_of_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
list_of_number = ['0','1','2','3','4','5','6','7','8','9']
list_of_symbols = ["!","$","&","*","(",")"]


letters = int(input("how many letters? \t"))
numbers = int(input("how many numbers? \t"))
symbols = int(input("how many symbols? \t"))


password = []
for alphabet in range(0,letters):
   r =  random.choice(list_of_letters)
   password += r


for numbers in range(0,numbers):
   r =  random.choice(list_of_number)
   password += r

for numbers in range(0,symbols):
   r =  random.choice(list_of_symbols)
   password += r


random.shuffle(password)



newpass = ''
for pswd in password:
   newpass += pswd

print(f" Your password is : {newpass}")



