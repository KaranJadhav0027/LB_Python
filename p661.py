def CountSmall(data):
    Count=0

    for ch in data:
        if(ch>='a' and ch<='z'):
            Count+=1
            
    return Count

def main():
    print("Enter a String")
    str=input()

    Ret=CountSmall(str)
    print(f"Frequency of Small chatacter in {str} is  {Ret}")
        
if __name__=="__main__":
    main()