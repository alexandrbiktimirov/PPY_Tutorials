print("\n-- Task 1 --")
def task1():
    print("Hello PJATK")

task1()

print("\n-- Task 2 --")
def task2():
    integer_var = 10
    float_var = 10.5
    string_var = "Hello"
    boolean_var = True
    print(integer_var, float_var, string_var, boolean_var)

task2()

print("\n-- Task 3 --")
def task3():
    a = "a"
    b = 3
    c = 5.5
    try:
        a + b
    except:
        print("String + int is not allowed")

    try:
        a + c
    except:
        print("String + float is not allowed")

    print("b + c:", b + c)

task3()

print("\n-- Task 4 --")
def task4():
    x, y, z = 1, 2.5, "text"
    print(x, y, z)

task4()

print("\n-- Task 5 --")
def task5(word):
    print(word * 20)

task5("Hello")

print("\n-- Task 6 --")
def task6():
    text = """Line 1
Line 2
Line 3"""
    print(text)

task6()

print("\n-- Task 7 --")
def task7():
    name = "Mike"
    age = 35
    print(f"My name is {name} and I’m {age} years old.")

task7()

print("\n-- Task 8 --")
def task8():
    name = "Mike"
    age = 35
    print("F-method:")
    print(f"My name is {name} and I’m {age} years old.")
    print("Format method:")
    print("My name is {} and I’m {} years old.".format(name, age))

task8()

print("\n-- Task 9 --")
def task9():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("Sum:", num1 + num2)

task9()

print("\n-- Task 10 --")
def task10():
    text = input("Enter a text: ")
    print(text.lower())
    print(text.upper())
    print(text.replace("a", "b"))

task10()

print("\n-- Task 11 --")
def task11():
    bool1, bool2 = True, False
    print("AND:", bool1 and bool2)
    print("OR:", bool1 or bool2)
    print("NOT bool1:", not bool1)

task11()

print("\n-- Task 12 --")
def task12():
    myList = ["apple", 42, "banana", 3.14]
    print(myList)

task12()

print("\n-- Task 13 --")
def task13():
    myTuple = ("apple", 42, "banana", 3.14)
    print(myTuple)

task13()

print("\n-- Task 14 --")
def task14():
    myList = ["apple", 42, "banana", 3.14, "cherry", 99]
    print("All elements except last:", myList[:-1])
    print("Every second element:", myList[::2])
    print("Every second element up to the middle:", myList[:len(myList)//2:2])
    x = "banana"
    print("Is x in the list:", x in myList)
    print("Tuple vs List: Lists are mutable, Tuples are immutable")
    myList.append("new_value")
    myList.insert(1, "inserted_value")
    myList.pop()
    myList.pop(2)
    new_list = ["extra", "values"]
    myList.extend(new_list)
    print("Updated list:", myList)
    print("Count of 'X':", myList.count("X"))

task14()

print("\n-- Task 15 --")
def task15():
    myList = [
        ["apple", "banana"],
        ["cherry", "watermelon"],
    ]
    print(myList)

task15()

print("\n-- Task 16 --")
def task16():
    myList = [
        ["apple", "banana"],
        ["cherry", "watermelon"],
    ]
    print(myList)
    del myList
    try:
        print(myList)
    except:
        print("List was deleted")

task16()

print("\n-- Task 17 --")
def task17():
    myDictionary = {"Something_1" : 1,
                    "Something_2" : 2.54,
                    "Something_3" : True,
                    "Something_4" : [1,2,3]
                    }
    print(myDictionary)
    del(myDictionary["Something_1"])
    print(myDictionary)
    myDictionary["Something_5"] = 'c'
    print(myDictionary)

task17()