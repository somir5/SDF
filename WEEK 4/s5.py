total_sum = 0
def add_to_sum(num):
    global  total_sum
    total_sum += num
def display_sum():
    print(f"Total sum:{total_sum}") 

add_to_sum(5)  
add_to_sum(10)
add_to_sum(20)
display_sum() 