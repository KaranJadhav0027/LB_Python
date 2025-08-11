def Addition(No1,No2):
    Sum=0
    Sum=No1+No2
    return Sum

def main():
    print("Enter First Number")
    Value1=int(input())

    print("Enter Second Number")
    Value2=int(input())

    Ans=0
    Ans=Addition(Value1,Value2)
    
    print(f"Addition is {Value1} & {Value2} is :{Ans}")

if __name__=="__main__":
    main()