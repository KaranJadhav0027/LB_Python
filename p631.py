
def DisplayFactors(No):
    print(f"Factors of {No} are :")
    # for i in range(1,(No+2)//2):
    for i in range(1,(No//2)+1):
        if(No%i==0):
            print(i)

def main():
    print("Enter Numnber :")
    Value=int(input())

    DisplayFactors(Value)

if __name__=="__main__":
    main()