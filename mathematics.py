import jarvis as je


#this file contains the mathematics functions whuch can be performed by our assistant
#currently it has some basic funtions u can add more functions similar to this functions

#extract numbers from string
def extract_numbers(query):
    a = str(query).split(' ')
    numbers = [int(x)  for x in a if x.isdecimal() ]
    return numbers

#for adding the numbers
def add(query):
    #Now suppose user says in the jarvis.py jarvis what is the addition of 5 and 6
    #extract_numbers will extract 5 and 6 from the query and returns the list
    sum = 0
    print("Add function Called")
    numbers = extract_numbers(query)
    for element in numbers:
        sum +=element
    else:
        print("jarvis:"+"it's "+str(sum) +' Sir')
        je.speak("Total Addition value is "+str(sum) +' Sir')
        

def mult(query):
    mul = 1
    print("mul function Called")
    numbers = extract_numbers(query)
    
    for element in numbers:
        mul *= int(element)
    else:
        print("jarvis:"+"it's "+str(mul) +' Sir')
        je.speak("it's "+str(mul) +' Sir')
        

def div(query):
    print("div function Called")
    result = 0
    numbers = extract_numbers(query)
    result = numbers[0]/numbers[1]
    print("jarvis:"+"it's "+str(result) +' Sir')
    je.speak("it's "+str(result) +' Sir')
    

def sub(query):
    print("subtraction function Called")
    result = 0
    numbers = extract_numbers(query)
    result = numbers[0]-numbers[1]
    print("jarvis:"+"it's "+str(result) +' Sir')
    je.speak("it's "+str(result) +' Sir')



    
