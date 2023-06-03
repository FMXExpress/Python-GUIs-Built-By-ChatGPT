import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QListWidget, QTextEdit, QLineEdit
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("GPT-like Chat")

        self.layout = QVBoxLayout()

        self.listWidget = QListWidget()
        self.listWidget.setSelectionMode(QListWidget.NoSelection)

        self.textEdit = QTextEdit()
        self.textEdit.setReadOnly(True)

        self.lineEdit = QLineEdit()
        self.lineEdit.returnPressed.connect(self.update_chat)

        self.layout.addWidget(self.listWidget)
        self.layout.addWidget(self.textEdit)
        self.layout.addWidget(self.lineEdit)

        self.container = QWidget()
        self.container.setLayout(self.layout)

        self.setCentralWidget(self.container)

    def update_chat(self):
        text = self.lineEdit.text()
        self.listWidget.addItem("You: " + text)
        self.lineEdit.clear()

        # Here you would typically use the GPT-4 model to generate a response
        response = "AI: " + text[::-1] # Just an example of a "response", it reverses the input
        self.listWidget.addItem(response)

        self.listWidget.scrollToBottom()

app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())
