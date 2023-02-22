# prefixes = 'JKLMNOPQ'
# suffix = 'ack'
# for letter in prefixes:
#     # if letter == "Q" or letter == "O":
#     # if letter in ['Q', 'O']:
#     if letter in 'QO':
#         print(letter + 'u' + suffix)
#     else:
#         print(letter + suffix)

team = 'New England Patriots'
# last = team[len(team)-1]
# print(last)

# new_team = team[:12]+'Seahawks'
# print(new_team)

# def find(word, letter):
#     index = 0
#     while index < len(word):
#         if word[index] == letter:
#             return index
#         index = index + 1
#     return -1

# print(find(team, 'E'))

# word = 'New England Patriots'
# count = 0
# for letter in word:
#     if letter == 'a':
#         count = count + 1
# print(count)

team = 'New England Patriots'
index = team.find('a')
print(index)

print(team.find('En'))
print(team.find('a', 10)) 
'a' in team
'Boston' in team
name = 'bob'
print(name.find('b', 1, 2))
"""In the arguments name.find('b', 1, 2), the third argument 2 specifies the end index of the search. 
This means that the search will end at the position immediately before index 2.
Since Python strings are zero-indexed, the string 'bob' has indices 0, 1, and 2. 
Therefore, when the find() method is called with the start index 1 and the end index 2, 
it only searches the single character at index 1 (which is 'o'), but not the character at index 2 (which is 'b')."""