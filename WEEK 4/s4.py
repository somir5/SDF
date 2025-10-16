count = 0
def increment():
    global count
    count += 1
    print(f"count inside function:{count}")

increment() 
increment()

print(f"Count outside function:{count}")