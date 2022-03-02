#no. of guesses - 9
#print no. of guesses left
#game over

                           #Exercise 3
i=10
hidden=15 # Hidden number
print("You have 9 attempts to guess a number")

while(i>1):
    print("\n")
    i=i-1
    print("Guesses Left:", i)
    n=int(input("Guess the hidden number from 1 to 30: "))
    if (n<=10):
        print("Your guess is very smaller than the hidden number.")
    elif(n>=20):
        print("Your guess is very greater than the hidden number.")
    elif(10<n<15):
        print("Your guess is smaller but too close.")
    elif(15<n<20):
        print("Your guess is greater but too close.")
    elif(n==15):
        print("Congrats! You guessed the right number.")
        break

if(n!=15):
    print("GAME OVER! No guesses left.")