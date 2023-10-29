# string are immutable hence donot provide facility of assignment or append
# strings can be concatenated using "+" operator
# space complexity - O(n)
# time complexity - O(n)

a = "this is which case"
b = ""

for i in range(len(a)):
    b += chr(ord(a[i])-32)

print("converted string: ", b)