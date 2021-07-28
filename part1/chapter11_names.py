from chapter11_func_module import get_formatted_name

while True:
    first = input("Give me your first name or 'q' to exit: ")
    if (first == 'q'):
        break
    
    second = input("Give me your second name or 'q' to exit: ")
    if (second == 'q'):
        break

    fullname = get_formatted_name(first, second)
    print(f"Fully formatted name: {fullname}")