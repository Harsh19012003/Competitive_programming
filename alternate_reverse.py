s = "this is code for alternate reverse function"
ans = ""

words = s.split()
print(f"words are : {words}")  #t O(n)

def reversing_function(word):
    rword = ""
    
    for j in range(len(word)-1, -1, -1):
        rword += word[j]
    
    return rword


for i in range(len(words)): #O(n)
    if i % 2 == 0:
        ans += words[i]
        ans += " "
    else:
        # print(reversing_function(words[i]))
        ans += reversing_function(words[i])
        ans += " "

print(f"alternate reverse answer is {ans}")


# Time complexity - O(n)