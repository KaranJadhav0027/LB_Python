def CountNonVowels(data):
    Count=0

    pattern="aeiouAEIOU"
    for ch in data:
        if (ch not in pattern):
            Count+=1
            
    return Count

def main():
    print("Enter a String")
    str=input()

    Ret=CountNonVowels(str)
    print(f"Frequency of Non Vowels in {str} is  {Ret}")
        
if __name__=="__main__":
    main()