name = input()
password = input()
while True:
    new_password = input()
    if new_password == password:
        break
print(f"Welcome {name}!")