def func():
    print("FUNC() IN ONE.PY")

def func1():
    print("THIS IS A FUNCTION")

def func2():
    print("This is a function!")
print("TOP LEVEL IN ONE.PY")

# if __name__ == "__main__":
#     print("ONE.PY is being run directly!")
# else:
#     print("ONE.PY has been imported!")

# For code organization
if __name__ == "__main__":
    func1()
    func2()