with open ('story.txt','r') as f:
    story = f.read() #story is a string here

#find presence of < to >, ask the user for words to replace <words>
start = 0
#words = [] allows duplicates of animal etc, but for unique we can use sets
words = set()

#enumerate gives access to position as well as the element at that position
for i, char in enumerate(story):
    if char == "<":
        start = i
    if char == ">":
        word = story[start: i+1] #in story starting from start upto i+1 as upper bound is not included
        words.add(word) #in sets we have add instead of append in lists
        start = 0

'''for i in range (0, len(words)): #syntax is len(list) not list.length()
    replace = input("What do you want to print as " + words[i] + " ")    
    words[i] = replace'''   
answers = {}
for i in words:
    
    replace = input("What do you want to print as " + i + " ")  
    answers[i] = replace

'''for j in answers.items():
    for i, char in enumerate(story):
        if char == "<":
            start = i
        if char == ">":
            story[start : i+1] = j''' #assignment operator does not work for str

#saving words in dictionary with key

#for i, char in enumerate(story):
#    if char == "<":

for i in words:
    story = story.replace(i, answers[i]) #to replace words directly

print (story)

with open('story_updated.txt', 'a') as f1:
    f1.write(story)

