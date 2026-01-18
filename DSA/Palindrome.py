s = "madam"
s = "hello"
rev = ""

for char in s:
    rev = char + rev

if s == rev:
    print(f"{rev} is Palindrome")
else:
    print(f"{rev} is not Palindrome") 