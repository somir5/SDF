correct_password = 'python123'
attempts = 3
while attempts > 0:
    password = input("Enter password: ")
    if password == correct_password:
        print("Access granted!")
        break
    else:
        attempts -= 1
        print(f"Incorrect!{attempts}attempts left")
if attempts == 0:
    print("access denied.Too many failed attempts.")         