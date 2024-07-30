#import nltk library which has tools and methods to work with human language data
import nltk 
#downloads stopwords and punkt
nltk.download("stopword")
nltk.download('punkt')
#imports module to work with stopwords
from nltk.corpus import stopwords
#imports module to work with tokens
from nltk.tokenize import word_tokenize, sent_tokenize
#handles system-specific parameters - checks the script directly 
import sys
#imports UI elements for widget and broader graphical usage 
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QTextEdit, QLabel

#creates a class that inherits QWidget properties 
class TextApp(QWidget):
    #initiliazing a ToDoApp object
    def __init__(self):
        #calls the constructor of the parent class - QWidget
        super().__init__()
        #Sets the title of the Window
        self.setWindowTitle("Text-Summarizer")
        #sets the position (100, 100) of the window and the width (400) and height (300)
        self.setGeometry(100, 100, 400, 300)
        
        #initializes an empty list for tasks
        self.tasks = []

        #creates a new layout to have the widgets arranged vertically
        self.layout = QVBoxLayout()

        #creates a text input field - allows for entering text to be summarized
        self.input_field = QLineEdit()
        #placeholder text so user knows what to do
        self.input_field.setPlaceholderText("Enter text to summarize")
        #creates a button called "Summarize" to start summarization process
        self.add_button = QPushButton("Summarize")
        #creates a widget to show the summarized text
        self.summary = QTextEdit()
        #summary box is read only so no edits are made
        self.summary.setReadOnly(True)

        #labels the input box
        self.layout.addWidget(QLabel("Input Text:"))
        #adds a widget for entering an input field to the layout
        self.layout.addWidget(self.input_field)
        #adds a button to the layout
        self.layout.addWidget(self.add_button)
        #labels the summary box
        self.layout.addWidget(QLabel("Summary:"))
        #adds a paragraph to the layout
        self.layout.addWidget(self.summary)
        
        #if the add button is clicked then the summary method will be completed
        self.add_button.clicked.connect(self.summarize_text)

        #sets the layout for the window
        self.setLayout(self.layout)

    #new function to add task to list
    def summarize_text(self):
        #task being handled is the text entered in the input field
        text = self.input_field.text()

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
            if word in stopWords:
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
            average = int(sumValues/ len(sentenceValue))

        #creates an empty string to sore the summary
        summary = ''
        #loops each sentence in the tokenized sentences list
        for sentence in sentences:
            #if sentence in sentence value table and the sentence score is greater than 1.2 times the average 
            if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2*average)):
                #adds the sentence to the summary
                summary += " " + sentence

        #sets the summary widget to the generated summary text
        self.summary.setText(summary)


        #the score of the sentence shows how many significant words (non-stopwords) it contains - the higher the score the more significant words it has thus the more significant it is
        #the score is calculated with the word's total frequency because the more frequent the word it is - the more significant it is so it weights the significance of each word in the sentene itself as well
        #the score is taken in context of the average becase it each sentence is 100 words long then a 50 words long sentence is not as significant vs if the average was 10 words long 

            
#script has to be directly executed not imported
if __name__ == "__main__":
    #allows for command-line arguments to be run on PyQt application
    app = QApplication(sys.argv)
    #crates an instance of the ToDoApp class
    window = TextApp()
    #displays window on the screen
    window.show()
    #allowing for the application to start executing
    sys.exit(app.exec())
    #returns the exit status 
    app.exec()