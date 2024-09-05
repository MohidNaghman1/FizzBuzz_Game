import random 
list1 = [0]
def check_Fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "fizzbuzz"
    elif number % 3 ==0:
        return "fizz"
    elif number% 5==0:
        return "buzz"
    else:
        return ''
    
def User_input(random_number):
    randomNum1 = sum(list1)
    # randomNum = random_number
    if not list1:
        print("List is Empty")
        print(list1)
    elif len(list1) == 1:
        list1.append(random_number)
        randomNum = sum(list1)

    elif len(list1) == 2:
        list1[0] = list1[0] + list1[1]
        list1.pop()
        list1.append(random_number)

    
    randomNum = sum(list1)
    print(f"Random Number {random_number}")

    print(f"This is your Question Eq which you will answer {randomNum}")


     
    User_input = input("Enter your choise Fizz, Buzz, FizzBuzz or Empty: ").lower()
    res = check_Fizz_buzz(randomNum)
    if res == User_input:
        print("Correct!")
        print(list1)
        return True
    else:
        print("Wrong! Try Again")
        
        return False
    
while True:

    random_number = random.randint(1,101)

    if User_input(random_number):
        play_again = input("Do you Want to play again? ").strip().lower()
        if play_again != "yes":
            print("Thank you for palying! ")
            print(list1)
            break





