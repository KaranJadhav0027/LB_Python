def CountVowels(data):
    Count=0

    pattern="aeiouAEIOU"
    for ch in data:
        if (ch in pattern):
            Count+=1
            
    return Count

def main():
    print("Enter a String")
    str=input()

    Ret=CountVowels(str)
    print(f"Frequency of Vowels in {str} is  {Ret}")
        
if __name__=="__main__":
    main()