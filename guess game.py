code="875418"
ans=""
guesscount=1;
guesslimit=3;
outofguess=False;
while(outofguess!=True):
    if(guesscount<=guesslimit):
        ans=input("enter your number" )
        guesscount=guesscount+1;
        if(ans==code):
            print("Your guess is correct")
            break;      
    else:
        outofguess=True;
    
if(outofguess==True):
    print("Out of guess you lose")
else:
    print("You Win")
