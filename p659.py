def CountNonVowels(data):
    Count=0

    pattern="aeiouAEIOU"
    for ch in data:
        if (ch in pattern):
            Count+=1
            
    return len(data)-Count

def main():
    print("Enter a String")
    str=input()

    Ret=CountNonVowels(str)
    print(f"Frequency of Non Vowels in {str} is  {Ret}")
        
if __name__=="__main__":
    main()