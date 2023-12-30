import random 
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-+=!@#$%^&*"
length = int(input("Enter the length of the password: "))
def password_generator(num):
    password = ''
    for i in range(num):
        password += random.choice(characters)
    return password
print(password_generator(length))   