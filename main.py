#a program to choose any number at random from 1 to 100
import random # importing the random library
rand = random.randint(1,100) #setting the range
print(rand) #printing the chosen value

floating_number = random.random() #chooing a random floating or decimal nmber in the range 0 to 1
print(floating_number) #printing the value

#increasing the range of floating_number, I multiplied by my new range
print(floating_number * 10)