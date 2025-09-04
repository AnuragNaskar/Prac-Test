num = int(input("Enter a number: "))
flag = True
for i in range(2, num-1):
    if num % i == 0:
        flag = False
        break
if flag:
    print(f"{num} is a Prime number.")
else:
    print(f"{num} is not a Prime number.")
#DoubleChecked prime number.
#UnChecked prime number.
#Changed main to branch.