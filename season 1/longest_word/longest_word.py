#global variables and imports
words =[]

#get the user sentence
def get_sentence():
    sentence = input("please enter your desire sentence: ")
    words.extend(sentence.split())
    return words

#find the longest word(s)
def find_longest_word(words):
    longest_words=[]
    longest_length = len(max(words, key=len))
    for word in words:
        if len(word) == longest_length:
            longest_words.append(word)
    return print("the longest word(s) in your sentence is: ", *longest_words)

#run the app
get_sentence()
find_longest_word(words)