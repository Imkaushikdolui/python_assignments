# 7) Write a Python class to reverse a string word by word. 
# Input string : 'hello .py' Expected Output : '.py hello' 


class WordReverser:
    def reverse_words(self, sentence):
        words = sentence.split()
        reversed_words = words[::-1]
        return ' '.join(reversed_words)

word = WordReverser()
print(word.reverse_words("hello .py"))