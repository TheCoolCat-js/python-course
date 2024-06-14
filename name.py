# name = input("Name: ")
# print(f"Hello, {name}")

# Login

# name = input("Name: ")
# password = input("Password: ")

# if name == "admin" and password == "password":
#     print("Login successful")
# else:
#     print("Invalid credentials")

# Admin login

name = input("Name: ")
repeatName = input("Repeat name: ")
password = input("Password: ")
repeatPassword = input("Repeat Password: ")

if name == name and password == repeatPassword:
    print("Login successful")
else:
    print("Invalid credentials")