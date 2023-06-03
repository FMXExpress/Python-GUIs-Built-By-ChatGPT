from delphivcl import *

class ChatForm(Form):
    def __init__(self, owner):
        self.__create_comps()
        self.__config_comps()

    def __create_comps(self):
        self.lb_history = ListBox(self)
        self.mm_conversation = Memo(self)
        self.edt_input = Edit(self)
        self.btn_send = Button(self)

    def __config_comps(self):
        self.caption = "Chat with ChatGPT"
        self.SetProps(ClientHeight = 600, ClientWidth = 800, Position = "poScreenCenter")
        
        # Configure ListBox for conversation history
        self.lb_history.SetProps(Parent = self, Left = 20, Top = 20, Width = 200, Height = 500)

        # Configure Memo for current conversation
        self.mm_conversation.SetProps(Parent = self, Left = 240, Top = 20, Width = 540, Height = 500)

        # Configure Edit for new message input
        self.edt_input.SetProps(Parent = self, Left = 20, Top = 540, Width = 660, Height = 40)

        # Configure Button to send message
        self.btn_send.SetProps(Parent = self, Left = 700, Top = 540, Width = 80, Height = 40, Caption = 'Send', OnClick = self.__btn_send_click)

    def __btn_send_click(self, sender):
        # Add the new message to the ListBox and Memo
        self.lb_history.Items.Add(self.edt_input.Text)
        self.mm_conversation.Lines.Add(f'You: {self.edt_input.Text}')
        # Call GPT for a response and add it to the Memo
        response = self.get_gpt_response(self.edt_input.Text)
        self.mm_conversation.Lines.Add(f'ChatGPT: {response}')
        # Clear the Edit text
        self.edt_input.Clear()

    def get_gpt_response(self, message):
        # TODO: Add actual call to GPT here. For now, just return a placeholder
        return "GPT response to: " + message

def main():
    Application.Initialize()
    Application.Title = "Chat with ChatGPT"
    MainForm = ChatForm(Application)
    MainForm.Show()
    FreeConsole()
    Application.Run()
    MainForm.Destroy()

if __name__ == '__main__':
    main()

