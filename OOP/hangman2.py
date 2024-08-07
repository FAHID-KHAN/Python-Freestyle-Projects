import random 


class Hangman():
    def __init__(self,word):
        self.word = word
    
    def welcome(self):
        print("Welcome to hangman game\n")
        print("Please guess a word ")
        word = input("Enter the word to guess")
        print(word.rstrip())
        
        



if __name__ == '__main__':
    hangman = Hangman()