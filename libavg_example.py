from libavg import avg, app, player
from libavg.ui import TextArea, TextField

class ChatGPTDiv(app.MainDiv):
    def onInit(self):
        self.create_UI()

    def onExit(self):
        pass

    def onFrame(self):
        pass

    def create_UI(self):
        self.question_list = avg.DivNode(parent=self, size=(self.width/2, self.height), 
                                          pos=(0,0))
        self.answer_list = avg.DivNode(parent=self, size=(self.width/2, self.height), 
                                       pos=(self.width/2, 0))

        self.question_input = TextField(pos=(0, self.height - 30), size=(self.width, 30), 
                                        parent=self, text="Type your question here...")
        self.question_input.subscribe(self.question_input.TEXT_ENTERED, self.on_question_entered)

        self.question_list_view = TextArea(parent=self.question_list, 
                                           size=(self.width/2, self.height - 30))
        self.answer_list_view = TextArea(parent=self.answer_list, 
                                         size=(self.width/2, self.height - 30), 
                                         multiline=True)

    def on_question_entered(self, event):
        question = self.question_input.text
        self.question_input.text = ""
        self.question_list_view.appendText(question+"\n")

        response = self.get_chat_gpt_response(question)
        self.answer_list_view.appendText(response+"\n")

    def get_chat_gpt_response(self, question):
        # This function should be implemented with the actual ChatGPT API.
        pass

app.App().run(ChatGPTDiv())
