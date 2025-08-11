# input Hello


def Display(No):
    for i in range(-No,No+1):
        print(i,end="\t")
      
    print()

def main():
    print("Enter a Number")
    Value=int(input())

    Display(Value)  

if __name__=="__main__":
    main()