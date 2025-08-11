def CheckDivisible(No):
    if ((No%5==0) and (No%3==0)):
         return True
    else:
         return False

def main():
    print("Enter First Number")
    Value1=int(input())

    bRet=CheckDivisible(Value1)
    
    if (bRet==True):
        print(f"{Value1} is divisible by 3 and 5")
    else:
        print(f"{Value1} is Not divisible by 3 &(or) 5")
    
if __name__=="__main__":
    main()