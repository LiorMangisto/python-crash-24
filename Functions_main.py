person = "Lior"
print("Hello, " + person)
person = "World"
print("Hello, " + person)
print("Hello, " + "Python")

# DRY - Don't repeat yourself

def say_hello(say_to):
    print(f"Hello,{say_to}!")

say_hello("Lior")
say_hello(say_to="World!")
say_hello(say_to="Pyhton")
print("hello after function")


def calulate(num1, num2):
    print("Getting numbers...")
    result = num1 + num2
    print("Calculating result...")
    print(f"{result = }")

calulate(5, 10)
calulate(num1=200, num2=100)