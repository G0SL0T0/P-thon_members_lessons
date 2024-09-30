def remove_vowels(s):
    vowels = 'aeiouAEIOU'
    new_s = ''
    for char in s:
        if char not in vowels:
            new_s += char
    return new_s

s= input("Enter a string: ")
print(remove_vowels(s))