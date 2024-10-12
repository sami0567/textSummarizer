#imports UI elements for widget and broader graphical usage 
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QTextEdit, QLabel
from PyQt5.QtGui import QIcon
from summarizer import TextSummarizer

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

        # Initialize the summarizer instance
        self.summarizer = TextSummarizer()  # Add this line to initialize the summarizer
        
        #creates a text input field - allows for entering text to be summarized
        self.input_field = QTextEdit()
        #placeholder text so user knows what to do
        self.input_field.setPlaceholderText("Enter text to summarize")
        #creates a button called "Summarize" to start summarization process
        self.add_button = QPushButton("Summarize")
        #creates a widget to show the summarized text
        self.summary = QTextEdit()
        #summary box is read only so no edits are made
        self.summary.setReadOnly(True)

         # labels the input box
        input_label = QLabel("Input Text:")
         # Set the color to black
        input_label.setStyleSheet("color: black;") 
        #adds input label to layout
        self.layout.addWidget(input_label)
        #adds a widget for entering an input field to the layout
        self.layout.addWidget(self.input_field)
        #adds a button to the layout
        self.layout.addWidget(self.add_button)
         # labels the summary box
        summary_label = QLabel("Summary:")
         # Set the color to black for the summary label
        summary_label.setStyleSheet("color: black;")
        #adds summary label to layout
        self.layout.addWidget(summary_label)
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
            QTextEdit {
                border: 1px solid #6200EA; /* Purple border */
                border-radius: 5px; /* Rounded corners */
                padding: 2px; /* Padding inside the input field */
                font-size: 14px; /* Font size */
                color: #000; /* Text color for input field */
            }
            QPushButton {
                background-color: #006ADC; /* Blue background */
                color: white; /* White text */
                border: none; /* No border */
                border-radius: 5px; /* Rounded corners */
                padding: 10px; /* Padding inside the button */
                font-size: 16px; /* Font size */
                cursor: pointer; /* Pointer cursor on hover */
            }
            QPushButton:hover {
                background-color: #00254D; /* Darker blue on hover */
            }
            QTextEdit {
                background-color: white; /* White background for the summary box */
                border: 2px solid #CCCCCC; /* Light gray border */
                border-radius: 5px; /* Rounded corners */
                padding: 5px; /* Padding inside the summary box */
                font-size: 14px; /* Font size */
                color: #333; /* Text color for summary */
            }
            QLabel {
                font-weight: bold; /* Bold text for labels */
                font-size: 14px; /* Font size */
                margin-top: 10px; /* Space above labels */
            }
            QScrollBar:vertical {
                width: 6px;  /* Adjust the width of the vertical scrollbar */
                background: #f0f0f0;  /* Background color for the scrollbar area */        
            }
            QScrollBar::handle:vertical {
                background: #888;  /* Color of the scrollbar handle */
                min-height: 20px;  /* Minimum height of the scrollbar handle */
                background-clip: padding-box;
            }
            QScrollBar::handle:vertical:hover {
                background: #555;  /* Darker handle on hover */
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                background: none;  /* No background for the buttons */
            }
            QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
                background: none;  /* No background for the arrows */
            }
            QScrollBar::corner {
                background: none;  /* No background for the corner area */
            }
        """)
      
    def summarize_text(self):
        try:
            text = self.input_field.toPlainText()  # Get the input text
            if not text:  # Check if input is empty
                self.summary.setPlainText("Please enter some text to summarize.")
                return

            summary = self.summarizer.summarize_text(text)  # Call the summarizer's method
            self.summary.setPlainText(summary)  # Display the summary in the QTextEdit
        except Exception as e:
            self.summary.setText("An error occurred: " + str(e))  # Display error message in summary area
            print(f"Error: {e}")  # Print the error in the console for debugging
