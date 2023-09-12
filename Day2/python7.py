#7)Write a function filter_long_words() that takes a list of words and an integer
#len and returns the list of words that are longer than len
def function_filtered_word(mylists,length):
    #empty list
    filter_word=[]
    for word in mylists:
        if len(word)>length:
            filter_word.append(word)
    return filter_word
#example usage
word_lists=["aman","arman","university","sunbeam","Engineering"]
length=5
filtered_word= function_filtered_word(word_lists, length)
print(f"the words {length} having greather than:{filtered_word}")