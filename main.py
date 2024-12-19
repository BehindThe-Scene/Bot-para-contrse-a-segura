import random

longuitud = int(input("¿De cuanto sera la longitud de su contraseña?"))
password = ''
for i in range(longuitud):
    ce = random.choice(".,;:?!'()[]{}-0123456789abcdefghijqlmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    password = password + ce
print("contraseña genereda:")
print(password)
