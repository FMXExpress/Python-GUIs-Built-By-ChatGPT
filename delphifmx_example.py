from delphifmx import *
from os.path import exists

class GptChatForm(Form):

    def __init__(self, owner):
        self.SetProps(Caption = "GPT Chat Interface", OnShow = self.__form_show, OnClose = self.__form_close)

        self.chatList = ListBox(self)
        self.chatList.SetProps(Parent = self, Position = Position(PointF(20, 20)), Width = 250)

        self.chatMemo = Memo(self)
        self.chatMemo.SetProps(Parent = self, Position = Position(PointF(280, 20)), Width = 250, Height = 250)

        self.questionBox = Edit(self)
        self.questionBox.SetProps(Parent = self, Position = Position(PointF(20,280)), Width = 350)

        self.submitButton = Button(self)
        self.submitButton.SetProps(Parent = self, Text = "Submit", Position = Position(PointF(380, 280)), Width = 80, OnClick = self.__button_click)

    def __button_click(self, sender):
        self.chatList.items.add(self.questionBox.text)
        self.chatMemo.text = self.chatMemo.text + '\n' + 'You: ' + self.questionBox.text
        self.chatMemo.text = self.chatMemo.text + '\n' + 'GPT: ' + self.questionBox.text
        self.questionBox.text = ""

    def __form_show(self, sender):
        self.SetProps(Width = 560, Height = 320)

    def __form_close(self, sender, action):
        action = "caFree"

def main():
    Application.Initialize()
    Application.Title = "GPT Chat Interface"
    Application.MainForm = GptChatForm(Application)
    Application.MainForm.Show()
    Application.Run()
    Application.MainForm.Destroy()

if __name__ == '__main__':
    main()
