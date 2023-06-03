import tkinter as tk
from tkinter import ttk, scrolledtext

class ChatApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("ChatGPT Interface")

        self.chat_history = scrolledtext.ScrolledText(self.root, width=30, height=20)
        self.chat_history.grid(column=1, row=0, rowspan=4)

        self.user_list = tk.Listbox(self.root, height=20)
        self.user_list.grid(column=0, row=0, rowspan=4)
        self.user_list.insert(1, "User1")
        self.user_list.insert(2, "User2")

        self.input_frame = ttk.Frame(self.root, padding=10)
        self.input_frame.grid(column=0, row=4, columnspan=2)

        self.question_var = tk.StringVar()
        self.input_field = ttk.Entry(self.input_frame, textvariable=self.question_var, width=50)
        self.input_field.pack(side=tk.LEFT)

        self.send_button = ttk.Button(self.input_frame, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.RIGHT)

    def send_message(self):
        message = self.question_var.get()
        if message:  # if the message is not empty
            self.chat_history.insert(tk.END, f'You: {message}\n')  # display the message
            self.question_var.set('')  # clear the input field

root = tk.Tk()
app = ChatApplication(root)
root.mainloop()
