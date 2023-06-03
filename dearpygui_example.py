import dearpygui.dearpygui as dpg

def send_callback(sender, app_data):
    # Simulate a chatbot response, just echoes the message for now
    msg = dpg.get_value("MessageInput")
    dpg.add_text(f'User: {msg}', parent='chat_log')
    dpg.add_text(f'GPT: {msg}', parent='chat_log')
    dpg.set_value("MessageInput", "")

dpg.create_context()
dpg.create_viewport(title='Chatbot GPT-4', width=800, height=600)

with dpg.window(label="Chatbot GPT-4"):
    with dpg.child_window(height=300, width=200, horizontal_scrollbar=True):
        dpg.add_listbox(items=["User 1", "User 2", "User 3"], label="User List")
    with dpg.child_window(height=300, width=500, horizontal_scrollbar=True, id='chat_log'):
        pass
    dpg.add_input_text(multiline=False, on_enter=True, callback=send_callback, hint="Enter message here...", id="MessageInput")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
