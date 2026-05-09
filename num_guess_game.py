import random
n = random.randint(1, 100)
print("             Welcome to the Number Guessing Game!            \n")
print("Who guesses, computer or user? (c for computer, u for user) ")
op = input("enter: ").lower()
#user guesses the number
if op == "u":
   s= int(input("Guess a number between 1 and 100: "))
   j = 1
   while s != n:
      if s < n:
        print("Too low! Try again.") 
      else:
        print("Too high! Try again.")
      s = int(input("Guess a number between 1 and 100: "))
      j += 1
   print(f"***Congratulations! You guessed the number {n} in {j} attempts.***")
#computer guesses the number
elif op == "c":
    start = 1
    end  = 100
    k =0
    while start <= end:
        guess_num = (start + end) // 2
        k += 1
        print(f"Computer's guess: {guess_num}")
        ans = input("The correct number is higher, lower, or equal to the number you guessed? (h for higher, l for lower, y for yes): ").lower()
        if ans == "l":
           end = guess_num - 1
        elif ans == "h":
           start = guess_num + 1
        elif ans == "y":
           print(f"***The computer guessed the number {guess_num} in {k} attempts.***")
           break
        else:
              print("Invalid input. Please enter 'y', 'h', or 'l'.")
else:
    print("Invalid input. Please enter 'c' for computer or 'u' for user.")
