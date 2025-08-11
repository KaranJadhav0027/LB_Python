
def CheckPerfect(No):
    sum=0 
    for i in range(1,(No//2)+1):
        if(No%i==0):
            sum+=i
    if(sum==No):
        return True
    else:
        return False

def main():
    print("Enter Numnber :")
    Value=int(input())

    Ret=CheckPerfect(Value)

    if(Ret==True):
        print(f"{Value} is perfect Number")
    else:
        print(f"{Value} is Not perfect Number")

if __name__=="__main__":
    main()