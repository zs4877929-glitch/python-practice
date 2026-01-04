n = int(input("Enter a number: "))
if n < 0:
    print("Not a Palindrome number!")
else:
    original = n
    reverse = 0

    while n > 0:
        reverse = reverse * 10 + (n % 10)
        n //= 10

    if original == reverse:
        print("Palindrome number!")
    else:
        print("Not a Palindrome number!")
