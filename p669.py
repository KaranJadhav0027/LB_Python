# input 4
# 4 3 2 1

def Display(No):
    for i in range(No,0,-1):
        print(i,end="\t")
    
    print()

def main():
    print("Enter a Number")
    Value=int(input())

    Display(Value)  

if __name__=="__main__":
    main()