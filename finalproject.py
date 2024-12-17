import os

name = input("What's your name: ")  
print(f"Hello, {name}")
ans = input("Do you want to start the Program? YES/NO: ")
os.system('cls')

def back():
    print("-------------------------------------------------------------------------------------------------")
    print(f"Hi! {name}, WELCOME to PRINTING IN PYTHON")
    print("The print() function prints the specified message to the screen, or other standard output device.")
    print("")    
    print("\t\t\t----MENU IN PRINTING PYTHON----\t\t\t")
    print("\t\t\t1. SIMPLE PRINTING")
    print("\t\t\t2. PRINTING WITH STRINGS AND CONCENTRATION")
    print("\t\t\t0. BACK TO MAIN MENU")
    
#1
def simple_printing():
    print("OUTPUT:")
    print("")
    print("\tITCS")
    print("\tPE")
    print("\tNSTP")
    print("")
    print("INPUT:")
    print("")
    print('\tprint("ITCS")')
    print('\tprint("PE")')    
    print('\tprint("NSTP")')
    print("0. Back")
    
def cont_printing():
    print("Merge variable a with variable b into variable c:")
    print("OUTPUT:")
    print("")
    print("\tHelloWorld")
    print("")
    print("INPUT:")
    print("")
    print('\ta = "Hello"')
    print('\tb = "World"')
    print("\tc = a + b")
    print("\n0. Back")

#2
def var():
    print("Variables are containers for storing data values.")
    print("Python has no command for declaring a variable.\nA variable is created the moment you first assign a value to it.")
    print("")
    print("\t---------------------------------------------------")
    print("\t\t\tMENU IN VARIABLES PYTHON")
    print("")
    print("\t1. PLUS AND CONCENTRATION OF PRINTING WITH VARIABLES")
    print("\t2. EXPLANATION")
    print("\t0. BACK TO MAIN")

def var1():
    v1 = eval(input("Enter a number: "))
    v2 = eval(input("Enter another number: "))
    print(v1," + ", v2," = ", v1+v2)

def var2():
    print("INPUT:")
    print("")
    print('v1 = eval(input("Enter a number: "))')
    print('v2 = eval(input("Enter another number: "))')
    print('print(v1," + ", v2," = ", v1+v2)')

#3
def con():
    print(f"Hi! {name} Welcome to Conditional Statement in Python")
    print("")
    print("\t\t----------------------------------------------------------")
    print("\t\t\tMENU IN CONDITIONAL STATEMENT IN PYTHON")
    print("")
    print("1. CONDITIONAL STATEMENT DEFINITION")
    print("2. CONDITIONAL STATEMENT SAMPLE PROGRAM")
    print("3. CONDITIONAL STATEMENT INPUT")
    print("0. BACK TO MAIN MENU")

def con1():
    print("-------------------------------------------------------------------------------------------------------------------------------------")
    print('Conditional statements are those statements where a hypothesis is followed by a conclusion.\nIt is also known as an " If-then" statement.If the hypothesis is true and the conclusion is false,\nthen the conditional statement is false.Likewise, if the hypothesis is false the whole statement is false.')
    print("-------------------------------------------------------------------------------------------------------------------------------------")

def con2():
    name = input("Enter your name: ")

    prelim = float(input("Enter your prelim grade: "))
    midterm = float(input("Enter your midterm grade: ")) 
    semifinal = float(input("Enter your Semi-Final grade: ")) 
    final = float(input("Enter your Final grade: "))
    quiz = float(input("Enter your Quiz grade: ")) 
    project = float(input("Enter your Project Grade: "))

    prelim = prelim * 0.15
    midterm = midterm * 0.15
    semifinal = semifinal * 0.15
    final = final * 0.15
    quiz = quiz * 0.25
    project = project * 0.15

    grade = prelim + midterm + semifinal + final + quiz + project

    print(grade)

    if grade >= 100:
        print("Error")
    elif grade >= 98:
        print("Congratulations You're with Highest Honors")
    elif grade >= 95:
        print("Congratulations You're with High Honors")
    elif grade >= 90:
        print("Congratulations You're with Honors")
    elif grade >= 75:
        print("Congratulations You're Passed")
    else:
        print("You're Failed")

def con3():
    print("INPUT:")
    print("")
    print('name = input("Enter your name: ")')
    print("")
    print('prelim = float(input("Enter your prelim grade: "))')
    print('midterm = float(input("Enter your midterm grade: "))')
    print('semifinal = float(input("Enter your Semi-Final grade: "))')
    print('final = float(input("Enter your Final grade: "))')
    print('quiz = float(input("Enter your Quiz grade: "))')
    print('project = float(input("Enter your Project Grade: "))')
    print("")
    print('prelim = prelim * 0.15')
    print('midterm = midterm * 0.15')
    print('semifinal = semifinal * 0.15')
    print('final = final * 0.15')
    print('quiz = quiz * 0.25')
    print('project = project * 0.15')
    print("")
    print('grade = prelim + midterm + semifinal + final + quiz + project')
    print("")
    print('print(grade)')
    print("")
    print('if grade >= 100:\n\tprint("Error")')
    print("elif grade >= 98:\n\tprint('Congratulations You're with Highest Honors')")
    print("elif grade >= 95:\n\tprint('Congratulations You're with High Honors')")
    print("elif grade >= 90:\n\tprint('Congratulations You're with Honors')")
    print("elif grade >= 75:\n\tprint('Congratulations You're Passed')")
    print("else:\n\tprint('You're Failed')")

#4
def loop():
    print(f"Hi! {name} Welcome to Looping Statement in Python")
    print("")
    print("\t\t----------------------------------------------------------")
    print("\t\t\tMENU IN LOOPING STATEMENT IN PYTHON")
    print("")
    print("1. LOOPING STATEMENTS")
    print("2. FOR LOOP PROGRAM SAMPLE")
    print("3. FOR LOOP PROGRAM INPUT")
    print("0. BACK TO MAIN MENU")

def loop1():
    print("")
    print("-------------------------------------------------------------------------------------------------------------------------------------")
    print("Loops, also known as iterative statements, are used when we need to execute a block of code repetitively.\nLoops in programming are control flow structures that enable the repeated execution of a set of instructions or code block\nas long as a specified condition is met. Loops are fundamental to the concept of iteration in programming, enhancing code efficiency, readability\nand promoting the reuse of code logic.")
    print("-------------------------------------------------------------------------------------------------------------------------------------")

def loop2():
    upto = eval(input("Enter a number: "))
    number = eval(input("Enter another number: "))
    for i in range(1, upto + 1):
        print(f"{number} x {i} = {number * i}")

def loop3():
    print("INPUT:")
    print("")
    print('upto = eval(input("Enter a number: "))')
    print('number = eval(input("Enter another number: "))')
    print('for i in range(1, upto + 1):')
    print('   print(f"{number} x {i} = {number * i}")')

#5
def fun():
    print(f"Hi! {name} Welcome to Functions in Python")
    print("")
    print("A function is a block of code which only runs when it is called.\nYou can pass data, known as parameters, into a function.\nA function can return data as a result.")
    print("\t\t----------------------------------------------------------")
    print("\t\t\tMENU IN FUNCTIONS IN PYTHON")
    print("")
    print("1. CALLING FUNCTION")
    print("2. RETURNS FUNCTION")
    print("0. BACK TO MAIN MENU")

def fun1():
    def my_function():
        print("Hello from a function")
    print("OUTPUT:")
    my_function()
    print("")
    print("INPUT:")
    print('def my_function():\nprint("Hello from a function")\nmy_function()')

def fun2():
    # Function to add two numbers and return the result
    num1 = eval(input("Enter a number: "))
    num2 = eval(input("Enter another number: "))

    def add_numbers(num1, num2):
        return num1 + num2  # Return the sum of a and b

    # Example usage
    result = add_numbers(num1, num2)
    print("") 
    print("OUTPUT:")
    print(f"The sum of {num1} and {num2} is: {result}")
    print("")
    print("INPUT:")
    print('num1 = eval(ninput("Enter a number: "))\num2 = eval(input("Enter another number: "))')
    print('def add_numbers(num1, num2):\nreturn num1 + num2')
    print("")
    print('result = add_numbers(num1, num2)')

#6
def array():
    print(f"Hi! {name} Welcome to ARRAYS in Python")
    print("")
    print("\t\t----------------------------------------------------------")
    print("\t\t\tMENU IN ARRAYS IN PYTHON")
    print("")
    print("1. ARRAYS DEFINITION")
    print("2. ARRAY PROGRAM EXAMPLE")
    print("0. BACK TO MAIN MENU")

def array1():
    print("-------------------------------------------------------------------------------------------------------------------------------------")
    print("In Python, array is a collection of items stored at contiguous memory locations.\nThe idea is to store multiple items of the same type together.\nUnlike Python lists (can store elements of mixed types), arrays must have all elements of same type.\nHaving only homogeneous elements makes it memory-efficient.")
    print("-------------------------------------------------------------------------------------------------------------------------------------")

def array2():
    even_number = []
    odd_number = 0

    tuloy = True
    while tuloy == True:
        number = input("Enter a number (type 'zero' to stop): ")

        if number == "zero":
            break

        elif int(number) % 2 == 0:
            even_number.append(number)
        
        else:
            odd_number += int(number)

        
    print(f"Sum of odd numbers: {odd_number}")
    print(f"even numbers: {even_number}")

#7
def dict():
    print(f"Hi! {name} Welcome to Dictionary in Python")
    print("")
    print("\t\t----------------------------------------------------------")
    print("\t\t\tMENU IN DICTIONARY IN PYTHON")
    print("")
    print("1. DICTIONARY DEFINITION")
    print("2. DICTIONARY EXAMPLE")
    print("0. BACK TO MAIN MENU")

def dict1():
    print("-------------------------------------------------------------------------------------------------------------------------------------")
    print("Python dictionaries are a powerful built-in data type that allows you to store key-value pairs for efficient data retrieval and manipulation.\nLearning about them is essential for developers who want to process data efficiently. ")
    print("-------------------------------------------------------------------------------------------------------------------------------------")

def dict2():
    print("INPUT:")
    print('thisdict = {')
    print(' "brand": "Ford",')
    print(' "model": "Mustang",')
    print(' "year": 1964}')
    print('print(thisdict["brand"])')
    print("")
    print("OUTPUT:")
    print("")
    print("Ford")

    



tuloy = True
if ans.lower() == "yes":
    while tuloy == True:
        print("--------MAIN MENU-------")
        print("1. PRINTING IN PYTHON")
        print("2. VARIABLES IN PYTHON")
        print("3. CONDITIONAL STATEMENTS")
        print("4. LOOPING STATEMENTS")
        print("5. FUNCTIONS")
        print("6. ARRAYS")
        print("7. DICTIONARY")
        print("8. EXIT")
        print("------------------------")
        choice = input("Enter a number of your chosen topic: ")
        os.system('cls')
        
        
        if choice == "1":
            while tuloy == True:
                back()
                print_choice = input("What type of printing?: ")
                os.system('cls')
            
                if print_choice == 0:
                    break
                elif print_choice == "1":
                    os.system('cls')
                    simple_printing()
                    bback = input("Enter: ")
                    os.system('cls')
                
                elif print_choice == "2":
                    os.system('cls')
                    cont_printing()
                    bback = input("Enter: ")
                    os.system('cls')
                else:
                    print("choose again")
                    os.system('cls')
                    break
            else: 
                break
        
        elif choice == "2":
            os.system('cls')
            while tuloy == True:  
                var()
                print_choice2 = input("Select number of your choice: ")
                os.system('cls')
                
                if print_choice2 == "1":
                    var1()
                    print("")
                    print("0. Back")
                    bback = input("Enter: ")
                    os.system('cls')
                
                elif print_choice2 == "2":
                    var2()
                    print("")
                    print("0. Back")
                    bback = input("Enter: ")
                    os.system('cls')
                
                elif print_choice2 == "0":
                    break
        
        elif choice == "3":
            os.system('cls')
            while tuloy == True:
                con()
                print_choice3 = input("Select number of your choice: ")
                os.system('cls')

                if print_choice3 == "1":
                    con1()
                    print("")
                    print("0. Back")
                    bback = input("Enter: ")
                    os.system('cls')
                
                elif print_choice3 == "2":
                    con2()
                    print("")
                    print("0. Back")
                    bback = input("Enter: ")
                    os.system('cls')
                
                elif print_choice3 == "3":
                    con3()
                    print("0. Back")
                    bback = input("Enter: ")
                    os.system('cls')
                
                else:
                    break
                
        elif choice == "4":
            os.system('cls')
            while tuloy == True:
                loop()
                print_choice4 = input("Select number of your choice: ")
                if print_choice4 == "1":
                    os.system('cls')
                    loop1()
                    print("")
                    print("0. Back")
                    bback = input("Enter: ")
                    os.system('cls')
                
                elif print_choice4 == "2":
                    os.system('cls')
                    loop2()
                    print("")
                    print("0. Back")
                    bback = input("Enter: ")
                    os.system('cls')
                
                elif print_choice4 == "3":
                    os.system('cls')
                    loop3()
                    print("")
                    print("0. Back")
                    bback = input("Enter: ")
                    os.system('cls')
                
                else:
                    os.system('cls')
                    break
        elif choice == "5":  
            os.system("cls")
            while tuloy == True:
                fun()
                print_choice5 = input("Select number of your choice: ")
            
                if print_choice5 == "1":
                    os.system('cls')
                    fun1()
                    print("")
                    print("0. Back")
                    bback = input("Enter: ")
                    os.system('cls')
                
                elif print_choice5 == "2":
                    os.system('cls')
                    fun2()
                    print("")
                    print("0. Back")
                    bback = input("Enter: ")
                    os.system('cls')
                
                else:
                    os.system('cls')
                    break

        elif choice == "6":
            os.system('cls')    
            while tuloy == True:
                array()
                print_choice6 = input("Select number of your choice: ")
                if print_choice6 == "1":
                    os.system('cls')
                    array1()
                    print("")
                    print("0. Back")
                    bback = input("Enter: ")
                    os.system('cls')

                elif print_choice6 == "2":
                    os.system('cls')
                    array2()
                    print("")
                    print("0. Back")
                    bback = input("Enter: ")
                    os.system('cls')
                
                else: 
                    os.system('cls')
                    break

        elif choice == "7":
            os.system('cls')    
            while tuloy == True: 
                dict()
                print_choice7 = input("Select number of your choice: ")
                
                if print_choice7 == "1":
                    os.system('cls')
                    dict1()
                    print("")
                    print("0. Back")
                    bback = input("Enter: ")
                    os.system('cls')

                elif print_choice7 == "2":
                    os.system('cls')
                    dict2()
                    print("")
                    print("0. Back")
                    bback = input("Enter: ")
                    os.system('cls')
                
                else:
                    break
            
        elif choice == "8":
            break

        else:
            print("Bye")
    else:
        print("Thanks")
else:
    print("ByeBye")