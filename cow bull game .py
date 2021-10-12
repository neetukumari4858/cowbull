import random
name=input("enter your name:-")
def cow_bull(l2,guess):
    print(l2)
    l3=[]
    l4=[]
    i=0
    while i<=guess:
        number=int(input("enter the number"))
        index=int(input("enter the index"))
        if number in l2:
            if l2.index(number)==index:
                l3.insert(index,number)
                print( "**bull**",l3)
            else:
                l4.insert(index,number)
                print("these are corect no you can reuse it")
                print("**cow**",l4)
        else:
            print("your no is not in list guess the no again:-")
        i=i+1
        if l2==l3:
            break
    if l2==l3:
        print("congretulation",name,"you are the winner")
    else:
        print("opps you are the looser")
l1=[0,1,2,3,4,5,6,7,8,9]
l2=random.sample(l1,5)
cow_bull(l2,10)    

