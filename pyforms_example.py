import pyforms
from pyforms import BaseWidget
from pyforms.controls import ControlButton
from pyforms.controls import ControlList
from pyforms.controls import ControlTextArea
from pyforms.controls import ControlText

class ChatInterface(BaseWidget):

    def __init__(self):
        super(ChatInterface,self).__init__('ChatGPT Interface')

        #Definition of the forms fields
        self._chatlist      = ControlList('Chat List')
        self._chatdetails   = ControlTextArea('Chat Details')
        self._newmessage    = ControlText('Your Message')
        self._sendbutton    = ControlButton('Send Message')

        #Define the actions
        self._chatlist.item_selection_changed_event = self.__on_select
        self._sendbutton.value = self.__send_message

        #Setting the form layout
        self._formset = [
            ('_chatlist', '_chatdetails'), 
            '_newmessage',
            '_sendbutton'
        ]

    def __on_select(self):
        """List selection event"""
        try:
            selected_row_index = self._chatlist.selected_row_index
            selected_item = self._chatlist.value[selected_row_index]
            self._chatdetails.value = str(selected_item)
        except:
            self._chatdetails.value = ''

    def __send_message(self):
        """Button send message event"""
        new_message = self._newmessage.value
        self._chatlist += [new_message]
        self._newmessage.value = ''

#Execute the application
if __name__ == "__main__":   
    pyforms.start_app(ChatInterface)
