from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

class ChatInterface(QWidget):
    def __init__(self):
        super().__init__()

        # ListView for users on the left
        self.user_list = QListWidget()
        self.user_list.setMinimumWidth(200)

        # Populate the user list with example users
        self.user_list.addItem("User1")
        self.user_list.addItem("User2")
        self.user_list.addItem("User3")

        # Scrolling memo field on the right
        self.text_area = QPlainTextEdit()
        self.text_area.setReadOnly(True)

        # Question box on the bottom
        self.message = QLineEdit()

        # Main layout
        main_layout = QHBoxLayout()

        # Adding widgets to the layout
        main_layout.addWidget(self.user_list)
        main_layout.addWidget(self.text_area)

        # Bottom layout for question box
        bottom_layout = QVBoxLayout()
        bottom_layout.addLayout(main_layout)
        bottom_layout.addWidget(self.message)

        # Set main layout
        self.setLayout(bottom_layout)

        # Connect signals
        self.message.returnPressed.connect(self.send_message)

    def send_message(self):
        current_user = self.user_list.currentItem().text() if self.user_list.currentItem() else "Unknown user"
        self.text_area.appendPlainText(current_user + ": " + self.message.text())
        self.message.clear()


if __name__ == "__main__":
    app = QApplication([])
    chat_interface = ChatInterface()
    chat_interface.show()
    app.exec()
