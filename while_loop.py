my_lucky_number = 7
guess = int(input("Guess my lucky number! I think it is: "))
while my_lucky_number != guess:
     guess = int(input("Oops! Not it. Try again: "))
print("Congrats! You guessed it.")