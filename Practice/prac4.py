def checkPalindrome(s):
    if s==s[::-1]:
        print(s,"is a palindrome")
    else:
        print(s,"is not a palindrome")

s = input("Enter a string: ")
checkPalindrome(s)