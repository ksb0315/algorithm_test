largest = 0
smallest = 0
flag = 0

while True:
    try:
        num = input("Enter a number: ")
        if num == "done": break
        num = int(num)
    except ValueError:
        print("Invalid input")
    else:
        if flag == 0:
            largest = num
            smallest = num
            flag = 1
            continue

        if num > largest:
            largest = int(num)
        if num < smallest:
            smallest = int(num)

print("Maximum", largest)
print("Minimum", smallest)