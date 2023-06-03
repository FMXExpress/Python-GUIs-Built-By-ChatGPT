import wx
import wx.xrc

class ChatInterface(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title="Chat Interface", pos=wx.DefaultPosition,
                          size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.HORIZONTAL)

        self.chat_list_ctrl = wx.ListCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                          wx.LC_REPORT)
        bSizer1.Add(self.chat_list_ctrl, 1, wx.ALL | wx.EXPAND, 5)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.chat_text_ctrl = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                          wx.DefaultSize, wx.TE_MULTILINE | wx.TE_READONLY)
        bSizer2.Add(self.chat_text_ctrl, 1, wx.ALL | wx.EXPAND, 5)

        self.question_text_ctrl = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                              wx.DefaultSize, wx.TE_PROCESS_ENTER)
        bSizer2.Add(self.question_text_ctrl, 0, wx.ALL | wx.EXPAND, 5)

        bSizer1.Add(bSizer2, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Event Handlers
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.question_text_ctrl.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)

    def __del__(self):
        pass

    # Event handler functions
    def OnClose(self, event):
        dlg = wx.MessageDialog(self,
                               "Do you really want to close this application?",
                               "Confirm Exit", wx.OK | wx.CANCEL | wx.ICON_QUESTION)
        result = dlg.ShowModal()
        dlg.Destroy()
        if result == wx.ID_OK:
            self.Destroy()

    def OnEnter(self, event):
        # This is where you can use the GPT model to process the entered text
        # For now we just add it to the chat list and the text control
        question = self.question_text_ctrl.GetValue()
        self.chat_list_ctrl.InsertItem(self.chat_list_ctrl.GetItemCount(), question)
        self.chat_text_ctrl.AppendText(question + '\n')
        self.question_text_ctrl.Clear()


app = wx.App(False)
frame = ChatInterface(None)
frame.Show(True)
app.MainLoop()
