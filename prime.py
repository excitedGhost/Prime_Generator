
##########     Finds factors of a number       ##########################################
def factor_checker(factor,num):#checks for the factors of a number
    if (num/factor)%1 == 0:
        isFactor = True
    elif (num/factor)%1 != 0:
        isFactor = False
    else:
        return "An error has occurred"
    return isFactor


################   Finds if number is prime   ###########################################

def prime_checker_print(number): #Factor Finding
    factors = []
    for i in range(1,number+1): #added 1 to number to include number in range
        if factor_checker(i,number):
            factors.append(number)
    if len(factors) == 2:
        return str(number)
    else:
        return
################   Check for Prime Numbers   ############################################
def prime_checker(number): #Checks if a number is prime or not
    factors = []
    for i in range(1,number+1): #added 1 to number to include number in range
        if factor_checker(i,number):
            factors.append(number)
    if len(factors) == 2:
        return str(number) + " is Prime"
    elif len(factors) != 2:
        return str(number) + " is not Prime"
    else:
        return "An error has occurred"
################   Range of Primes   ####################################################
def prime_range(start, end):
    for x in range(start,end):
        result = prime_checker_print(x)
        if result:
            print(result)
################   Menu   ###############################################################
def menu_welcome():
    print('''Input a corresponding number.
    1. Check if Number is Prime
    2. Print Prime Numbers in a range
    Enter `quit`, `close` or `exit` to quit this program
    
    written by Zetsubou''')
    menu_value = input("Enter a Value: ")
    return menu_value

#########################################################################################
def main():
    while True:
        menu_value = menu_welcome()
        if menu_value == "1":
            print(prime_checker(int(input("Input a number: "))))
            print("\n")
        elif menu_value == "2":
            prime_range(int(input("Enter a starting number: ")),int(input("Enter an end number: ")))
            print("\n")
        elif menu_value in ("quit", "close", "exit"):
            print("Thank you for using this program")
            exit()
        else:
            print("Enter valid input!")


#########################################################################################
if __name__ == "__main__":
    main()
    


