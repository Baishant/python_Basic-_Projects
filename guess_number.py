# DESIGNIMG A NUMBER GUESSING GAME
import random
import math
def main():
   # METHOD TO INPUT NUMBER RANGE FROM USERTS **************
 print("NOTE : upper bound must be greater then lower bound ! ")
 lower_bound = int( input("\nEnter lower range :"))
 upper_bound = int( input("\nEnter upper range :"))

    # GENERATING RANDOM NUMBER BETWEEN THAT RANGE ***********
 random_number = random.randint(lower_bound,upper_bound)

    #MAXIMUM ROUNDS UNDER WHICH THE NUMBER CAN BE GUESSED UNTIL CORRECT GUESS
 if upper_bound > lower_bound:
    print("\nYou have ",
    round(math.log(upper_bound-lower_bound+1,2)),
    "rounds remaining")


    # CREATING LOOPS TO KNOW THE ROUND WHERE THE USER HAS CORRECTLY GUESSED THE RANDOM NUMBER
    # INITIALIZING THE NUMBER OF ROUNDS TO GUESS
 count = 0

 while count < round(math.log(upper_bound-lower_bound+1,2)):
  count +=1
    
    # INPUT FOR INPUT OF GUESSED NUMBER
  user_guess = int(input("\n Guess a random number:"))
  if user_guess == random_number :
        print("\nCongratulations! you guessed it within", count , "rounds")
        break                                
  elif user_guess < random_number :
        print("\nTry again! By entering slightly higher number ")
  elif user_guess > random_number :
        print("\nTry again! By entering slightly lower number ")
        yes_no = input()
    
  else:
       
        print("\nYOu have no rounds left",
          "\nBetter luck next time !")
 print("\nDo you want to play again ? ",
      "\nEnter 1 for yes and 0 for no respectively." )
 yes_no = bool(input())
 if yes_no == "yes":
    main()
 else:
    exit()
 
   

      



 
 


      