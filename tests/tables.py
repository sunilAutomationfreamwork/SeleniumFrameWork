def tables(number):
    for i in range(1,11):
        table=number*i

        print(f"Table of {number}is {number} * {i} = {table} ")
user_number=int(input("enter a number"))
print(range(10))

tables(user_number)
