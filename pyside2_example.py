import sys
from PySide2.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
    QListWidget, QTextEdit, QLineEdit, QLabel)

class ChatApp(QWidget):

    def __init__(self, parent=None):
        super(ChatApp, self).__init__(parent)

        # Create layout
        self.main_layout = QHBoxLayout()
        self.chat_layout = QVBoxLayout()

        # Create widgets
        self.list_view = QListWidget()
        self.memo_field = QTextEdit()
        self.question_box = QLineEdit("Write a question here...")
        
        # Configure widgets
        self.memo_field.setReadOnly(True)

        # Add widgets to layout
        self.chat_layout.addWidget(self.memo_field)
        self.chat_layout.addWidget(self.question_box)
        
        self.main_layout.addWidget(self.list_view)
        self.main_layout.addLayout(self.chat_layout)

        # Set main layout
        self.setLayout(self.main_layout)

        # Connect signals
        self.question_box.returnPressed.connect(self.add_message)

    def add_message(self):
        message = self.question_box.text()
        self.memo_field.append("You: " + message)
        self.question_box.clear()

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = ChatApp()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec_())
