import random
number = random.randint(1, 100)
print (number)
count=0
guess=0
while number!=guess:
    guess = int(input("Guess a number between 1 and 100: "))
    if (guess < number/2):
        print("Your guess is too low!")
    elif (guess < number):
        print("That's low!")
    elif (guess > number*2):
        print("Your guess is too high!")
    else:
        print("Your guess is high!")
    count+=1  
else:
    print ("Hurray! you got it right and your score is:",(100-count))
