'''
Exercises
Print every character of a string using indexing.
Print every second character using slicing.
Reverse a string without using [::-1] (use a loop).
Count uppercase and lowercase letters separately.
Check whether two strings are anagrams.
Remove all spaces from a sentence.
Count the frequency of each word in a sentence.
Convert a sentence to title case.
Replace all vowels with *.
Find the longest word in a sentence
'''

# 1. Print every character of a string using indexing.
text = "Ram"
# print(text[0],end=" ")
# print(text[1],end=" ")
# print(text[2])

# 2. Print every second character using slicing.
text1 = "Apple"
# print(text1[::2])

# 3. Reverse a string without using  [::-1] (use Loop)
temp = "Madam"

chars = list(temp)

s = 0
e = len(chars) - 1

while s < e:
    chars[s], chars[e] = chars[e], chars[s]
    s += 1
    e -= 1

rev = "".join(chars)
# print(rev)

# 4.Count uppercase and lowercase letters separately.
up = 0
lo = 0
for i in "ramAyan":
    if i == i.upper():
        up +=1
    else:
        lo += 1

# print(up,lo)

# 5. Check whether two strings are anagrams.
def is_anagram(s1,s2):

    if len(s1) != len(s2):
        return False

    visited = [False] * len(s2)

    for i in range(len(s1)):

        found = False
        for j in range(len(s2)):

            if s1[i] == s2[j] and not visited[j]:
                visited[j] = True
                found = True
                break

        if not found:
            return False

    return True

# print(is_anagram("madam","damam1"))

def is_anagram_v1(s1,s2):
    if len(s1) != len(s2):
        return False

    freq = {}

    for i in s1:
        freq[i] = freq.get(i,0) + 1

    for j in s2:
        if j not in freq:
            return False

        freq[j] -= 1

        if freq[j] == 0:
            del freq[j]

    return len(freq) == 0


# print(is_anagram_v1("listen", "silent"))

# 6.Remove all spaces from a sentence.
sentence = "Hi Ram, How Are You?"

for i in sentence:
    if i == " ":
        sentence = sentence.replace(" ","")
# print(sentence)

# 7. Replace all vowels with *.
text = "Rohit"
for i in text:
    if i in ['a','e','i','o','u']:
        text = text.replace(i,"*")
# print(text)

# 8. Find the longest word in a sentence
sentence = "Hi Ram, How Are Your?"
result = ""
words = sentence.split()
for i in words:
    if len(i) > len(result) - 1 :
        result = i

print(result)