def CountFrequency(data):
    
    Count=0
    for ch in data:
        if (ch=='a'):
            Count+=1
    return Count

def main():
    print("Enter a String")
    str=input()

    Ret=CountFrequency(str)
    print(f"Frequency of A in {str} is  {Ret}")
        
if __name__=="__main__":
    main()