import ascii
def add(n1,n2):
    return n1+n2

#To add 3 more functions:subtract,divide,multiply.

def subtract(s1,s2):
    ''' used for canceling out each other'''   
    return s1-s2


def multiply(m1,m2):
    ''' used for increasing out each other'''   
    return m1*m2


def divide(d1,d2):
    ''' used for cutting out each other'''   
    return d1/d2
# TODO:To add these 4 fn in dict and add them as values,keys="-","+","/","*".
operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}


def calculator():
    print(ascii.logo)
    num1=float(input("enter the number1:"))
    calculation=True
    while calculation:
        for symbols in operations:
            print(symbols)
        mathematical_operator=input("choose the right symbol:")
        num2=float(input("enter the number2:"))
        answer=operations[mathematical_operator](num1,num2)
        print(f"{num1} {mathematical_operator} {num2} = {answer}")    
        choice=input(" 'y' for yes,'n' for no for continuing:")

        if choice=='y':
            answer=num1
            
        else:
            print("\n"*20)
            calculation=False
            calculator()

calculator()            

