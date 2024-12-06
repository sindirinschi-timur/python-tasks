from pycparser.ply.yacc import restart

username = "python"
password = "rules"
attempt = 0

while True:
    if attempt == 5:
        print("Access denied")
        break
    user = input("Enter the username: ")
    pas = input("Enter the password: ")
    attempt += 1
    if user != username or pas != password:
        print("Invalid username or password")
        continue
    elif user == username and pas == password:
        print("Welcome")
        break



