import random

def descision(game,you):
    if game==you:
        return None
    elif game=="stone":
        if you=="paper":
            return True
        else:
            return False

    elif game=="paper":
        if you=="stone":
            return False
        else:
            return True

    elif game=="scissor":
        if you=="stone":
            return True
        else:
            return False




#Driver code
c,m=0,0
points=int(input("Enter points: "))

for i in range(points):
 computer=random.randint(1,3)
 #print(computer)

 y=int(input("stone(1),paper(2),scissor(3)\nEnter your choice:"))


 #___ For Computer__________
 if computer==1:
    game="stone"
 elif computer==2:
    game="paper"
 else:
    game="scissor"



 if y==1:
    you="stone"
 elif y==2:
    you="paper"
 else:
    you="scissor"


 print("Computer Choice :",game)
 print("Your Choice :",you)

 win=descision(game,you)

 if win==None:
    print("Game Draw")
 elif win:
    c=c+1
    print("c=",c,"m=",m)
 else:
    m=m+1
    print("c=",c,"m=",m)



