code="875418"
#set keyword this is gonna be the secret code
ans=""
#player value if store in that ans variable
guesscount=1;
#guesscount variable can count ,how many guesses used by the player for give or not nect chance
guesslimit=3;
#guesslimit is cut the guessing chance for player if he used all the guesslimit value
outofguess=False;
#outofguess variable hold false value then only it allow to get into the loops
while(outofguess!=True):
    if(guesscount<=guesslimit):
        #if guesscount is lesser than guesslimit it allow to give guess one more time
        ans=input("enter your number" )
        guesscount=guesscount+1;
        #after entered the guess the guesscount variable can increment its value by add 1 with it
        if(ans==code):
            #if the entered guess is correct is say win 
            print("Your guess is correct")
            #if guess is right ther is no need for another guess so the break statement will help the brak theloop
            break;      
    else:
        #if the player reach his all guesslimt and still not guess corrctly hten the out of guess
        #varibale will change it value for false to true because ther is no more guesses
        outofguess=True;
#lostly of if else state for annonce result does that player is win or not based upon above variables
    
if(outofguess==True):
    print("Out of guess you lose")
else:
    print("You Win")
