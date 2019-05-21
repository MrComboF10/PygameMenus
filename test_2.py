class Test:
    def __init__(self):
        pass

    def __str__(self):
        return "hello"


test = Test()

# print(str(test) == "hello")

print(type(test).__name__)