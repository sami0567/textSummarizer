import ssl
ssl._create_default_https_context = ssl._create_unverified_context
#import nltk library which has tools and methods to work with human language data
import nltk 
#downloads stopwords and punkt
nltk.download("stopwords")
nltk.download('punkt', force=True)
nltk.download('punkt_tab')
#imports module to work with stopwords
from nltk.corpus import stopwords
#imports module to work with tokens
from nltk.tokenize import word_tokenize, sent_tokenize
#handles system-specific parameters - checks the script directly 
import sys

class TextSummarizer:
    def __init__(self):
        # Initialize instance variables
        self.stop_words = set(stopwords.words("english"))  # Set of stop words
        self.freqTable = {}  # Dictionary to store word frequencies
        self.sentenceValue = {}  # Dictionary to store sentence scores

    #new function to add task to list
    def summarize_text(self, text):

        #creates a set of all the stopwords in the english language - provided by the nltk modle
        stopWords = set(stopwords.words("english"))

        #tokenizes/seperates each significant word or character in the input text and turns it into a list
        words = word_tokenize(text)

        #initalizes an empty dictionary to store word frequencies
        freqTable = dict()
        #loops through each word in the list of all tokenized words
        for word in words:
            #convers the word to lowercase - to handle casesensitivity 
            word = word.lower()
            #checks if the word is a stopWord
            if word in stopWords and word.isalnum:
                #doesn't count the word/do anything
                continue
            #if the word is alreadu in the freqTable
            if word in freqTable:
                #increases the frequency count of the word
                freqTable[word] += 1
            else:
                #starts the frequency count in the dictionary
                freqTable[word] = 1

        #tokenizes the input text into sentences in a list
        sentences = sent_tokenize(text)
        #creates an empty dictionary to store sentence scores
        sentenceValue = dict()

        #loops through each sentence in the list of all tokenized sentences
        for sentence in sentences:
            #iterates through each word and its respective frequency in the freqTable
            for word, freq in freqTable.items():
                #if the word from the freqTable dictionary is in the selected tokenized sentence - sentence is lowercased to handle casesensitivity
                if word in sentence.lower():
                    #checks if the sentence is in the sentence value table
                    if sentence in sentenceValue:
                        #if its in the table then the sentence score value will increase by the word's frequency value
                        sentenceValue[sentence] += freq
                    else:
                        #if the sentence is not in the value table then it will be added and the score value will be set to the word frequency value
                        sentenceValue[sentence] = freq

        #creates a variable to store the sum of all sentence scores
        sumValues = 0
        #for each sentence in the sentenceValue table
        for sentence in sentenceValue:
            #adds the sentence value to the sum values
            sumValues += sentenceValue[sentence]
        #gets the average score of the sentences by dividing the total score by the number of sentences

        if len(sentenceValue) == 0:
            average = 0
        else:
            average = sumValues/ len(sentenceValue) if sentenceValue else 0

        #creates an empty string to sore the summary
        summary = ''

        summarized_sentences = sorted(sentenceValue, key=sentenceValue.get, reverse=True)[:3]
        for sentence in summarized_sentences:
            summary += " " + sentence

        return summary.strip()


        #the score of the sentence shows how many significant words (non-stopwords) it contains - the higher the score the more significant words it has thus the more significant it is
        #the score is calculated with the word's total frequency because the more frequent the word it is - the more significant it is so it weights the significance of each word in the sentene itself as well
        #the score is taken in context of the average becase it each sentence is 100 words long then a 50 words long sentence is not as significant vs if the average was 10 words long 
