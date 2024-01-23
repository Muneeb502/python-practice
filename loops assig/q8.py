#  <<<--. Write a program that prompts the user to input a number and prints its multiplication table->>
print("multiplication table")
num = int(input("ENTER ANY NUMBER :"))
for i in range(1,11):
    print(f"{num} * {i} = {i*num}")