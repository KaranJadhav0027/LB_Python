def CheckEven(No):
    if No%2==0:
         return True
    else:
         return False

def main():
    print("Enter First Number")
    Value1=int(input())

    bRet=CheckEven(Value1)
    
    if (bRet==True):
        print(f"{Value1} is Even Number")
    else:
        print(f"{Value1} is Odd Number")
    
if __name__=="__main__":
    main()