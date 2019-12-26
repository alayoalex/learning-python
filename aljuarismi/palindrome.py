def palindrome_1(n):
    palindrome = True

    for i in range(len(n)):
        if (n[i] != n[len(n) - 1 - i]):
            palindrome = False
    return palindrome

def palindrome_2(n):
    n_inverted = ''
    palindrome = True

    for i in range(len(n)):
        n_inverted += n[len(n)-1-i]

    if n != n_inverted:
        palindrome = False
    return palindrome


n = input("Entre la cadena que quiere comprobar: ")
print(palindrome_1(n))
print(palindrome_2(n))