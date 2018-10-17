#Maniga Constantin-Alexandru, Group 914 IE1

from math import sqrt

#MAIN OPERATIONS =================================================

def create_number(real, imaginary):
    return [real, imaginary]

def add_number(numbers, number):
    numbers.append(number)

def get_real(number):
    return number[0]

def get_imaginary(number):
    return number[1]

def set_real(number, value):
    number[0] = value

def set_imaginary(number, value):
    number[1] = value

#PROPERTIES ==============================================

#Property 1 - Numbers having increasing modulus

def calculate_modulus(number):
    #Calculate the modulus of a complex number ( sqrt(x^2 + y^2) )
    return int(sqrt(get_real(number)**2 + get_imaginary(number)**2))

def property1(numbers):
    #Function that returns the longest sequence of numbers having increasing modulus
    #Variable declarations
    largest = 0
    temp_largest = 0
    start_location = 0
    end_location = 0
    i = 0
    #Looping over the list of complex numbers with i starting from the first numner
    while i < len(numbers):
        #j will loop after i
        j = i+1
        #Looping with j from the number after i and checking if the modulus of the number j is less than the modulus of number i
        while (j < len((numbers)) and calculate_modulus(numbers[j-1]) < calculate_modulus(numbers[j])):
            j += 1
        #Determine de temporary largest  sequence
        temp_largest = j-i
        #If it is largest than our maximum determined sequence, then update the maximum
        if temp_largest > largest:
            largest = temp_largest
            #Determine the start index of our current maximum sequence
            start_location = i
            #Determine the end index of our current maximum sequence
            end_location = j-1
        #i will take the value of j to skip some unnecessary iterations
        i=j
    #We will return the indexes of our longest sequence as a list of [start_location, end_location] if the size of our sequence is at least 2 or greater
    return start_location, end_location if end_location - start_location > 0 else  0

def print_property1(numbers):
    #This function is only used to print the maximum sequence that satisfies the property of numbers having increasing modulus
    location = property1(numbers)
    if location == (0,0):
            print("There is no sequence that satisfies the property")
    else:
        for i in range(location[0], location[1]+1):
            if get_imaginary(numbers[i]) < 0:
                print("{0} - {1}i".format(get_real(numbers[i]), abs(get_imaginary(numbers[i]))))
            else:
                print("{0} + {1}i".format(get_real(numbers[i]), get_imaginary(numbers[i])))

#Property 2 - Consecutive number pairs have equal sum.
def sum_number(number):
    return get_real(number) + get_imaginary(number)

def property2(numbers):
    # Function that returns the longest sequence of consecutive numbers pairs having equal sum
    # Variable declarations
    largest = 0
    temp_largest = 0
    start_location = 0
    end_location = 0
    i = 0
    while(i<len(numbers)):
        j = i+3
        Flag = False
        while(j<len(numbers) and i<len(numbers) and sum_number(numbers[j-3]) + sum_number(numbers[j-2]) == sum_number(numbers[j-1]) + sum_number(numbers[j])):
            Flag = True
            j+=2
        if Flag == True:
            temp_largest = j-i+1
        if temp_largest > largest:
            largest = temp_largest
            start_location = i
            end_location = j-2
        i+=1
    return start_location, end_location


def print_property2(numbers):
    #This function is only used to print the maximum sequence that satisfies the property of numbers having increasing modulus
    location = property2(numbers)
    if location == (0,0):
            print("There is no sequence that satisfies the property")
    else:
        for i in range(location[0], location[1]+1):
            if get_imaginary(numbers[i]) < 0:
                print("{0} - {1}i".format(get_real(numbers[i]), abs(get_imaginary(numbers[i]))))
            else:
                print("{0} + {1}i".format(get_real(numbers[i]), get_imaginary(numbers[i])))

#UI =====================================================

def print_options():
    #Function used to print all the available options to the console
    print("1 - Read a list of complex numbers\n"
          "2 - Print the entire list of numbers\n"
          "3 - Print the largest sequence of numbers having increasing modulus\n"
          "4 - Print the largest sequence of consecutive number pairs having equal sum\n"
          "5 - Exit the application")

def add_numbers(numbers):
    while True:
        real = input("Real part of the number:  (or type 'stop' to end reading)")
        if real == "stop":
            break
        imaginary = input("Imaginary part of the number: (or type 'stop' to end reading")
        if imaginary == "stop":
            break
        number = create_number(int(real), int(imaginary))
        add_number(numbers,number)

def print_numbers(numbers):
    for n in numbers:
        if n[1] < 0:
            print("{0} - {1}i".format(get_real(n), abs(get_imaginary(n))))
        else:
            print("{0} + {1}i".format(get_real(n), get_imaginary(n)))

def run_menu():
    #Initialize the list of complex numbers for the purpose of testing
    numbers = [[1,3],[1,2], [1,2], [1,2], [1,2], [1,5], [1,3], [4,5],[5,7],[4,1]]
    #Creating a dictionary containing all the options available
    options = {1 : add_numbers,
               2 : print_numbers,
               3 : print_property1,
               4 : print_property2}
    #The option reading loop
    while True:
        print_options()
        opt = input("Option= ")
        if opt == "5":
            break
        try:
            opt = int(opt)
            options[opt](numbers)
        except KeyError:
            print("this option does not exist")
        except ValueError:
            print("this is not a valid option")

if __name__ == '__main__':
    run_menu()
