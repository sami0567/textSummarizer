#imports UI elements for widget and broader graphical usage 
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QTextEdit, QLabel
from PyQt5.QtGui import QIcon

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

        self.setStyleSheet("""
            QWidget {
                background-color: #F0F0F0; /* Light gray background for the window */
            }
            QLineEdit {
                border: 2px solid #6200EA; /* Purple border */
                border-radius: 5px; /* Rounded corners */
                padding: 10px; /* Padding inside the input field */
                font-size: 14px; /* Font size */
            }
            QPushButton {
                background-color: #6200EA; /* Purple background */
                color: white; /* White text */
                border: none; /* No border */
                border-radius: 5px; /* Rounded corners */
                padding: 10px; /* Padding inside the button */
                font-size: 16px; /* Font size */
                cursor: pointer; /* Pointer cursor on hover */
            }
            QPushButton:hover {
                background-color: #3700B3; /* Darker purple on hover */
            }
            QTextEdit {
                background-color: white; /* White background for the summary box */
                border: 2px solid #CCCCCC; /* Light gray border */
                border-radius: 5px; /* Rounded corners */
                padding: 5px; /* Padding inside the summary box */
                font-size: 14px; /* Font size */
            }
            QLabel {
                font-weight: bold; /* Bold text for labels */
                font-size: 14px; /* Font size */
                margin-top: 10px; /* Space above labels */
            }
        """)
      
