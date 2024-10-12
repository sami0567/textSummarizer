import sys
from PyQt5.QtWidgets import QApplication
from gui import TextSummarizerGUI
from summarizer import TextSummarizer

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = TextSummarizerGUI()
    gui.show()
    sys.exit(app.exec_())
