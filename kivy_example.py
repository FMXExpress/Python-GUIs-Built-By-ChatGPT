import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

kivy.require('2.1.0')

class ChatBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(ChatBoxLayout, self).__init__(**kwargs)
        self.orientation = "vertical"

        self.history_layout = BoxLayout(orientation='vertical', size_hint_y=None)
        self.history_layout.bind(minimum_height=self.history_layout.setter('height'))

        self.history = ScrollView(size_hint=(1, 0.9))
        self.history.add_widget(self.history_layout)
        self.add_widget(self.history)

        self.new_message = TextInput(size_hint=(1, 0.1), multiline=False)
        self.new_message.bind(on_text_validate=self.on_enter)
        self.add_widget(self.new_message)

    def on_enter(self, instance):
        label = Label(text=instance.text, size_hint_y=None, height=40)
        self.history_layout.add_widget(label)
        instance.text = ''


class ChatApp(App):
    def build(self):
        return ChatBoxLayout()


if __name__ == "__main__":
    ChatApp().run()
