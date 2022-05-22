def isPalindrome(str):
    # Run loop from 0 to len/2
    for i in range(0, int(len(str) / 2)):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True


# main function
s = input("Enter lowercase English Alphabets only!!!: ")
if s.isdigit():
    print("Digits passed please enter Alpabets")
else:
    if len(s)>=1 and len(s)<=100:
        newString = s.lower()
        ans = isPalindrome(newString)
        if (ans):
            print("YES")
        else:
            print("NO")
    else:
        print("String length too long")
