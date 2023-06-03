import PySimpleGUI as sg

sg.theme('DarkAmber')  # Choose a theme

# Layout definition
layout = [
    [sg.Listbox(values=[], enable_events=True, size=(40,20), key='-CHAT-', select_mode=sg.LISTBOX_SELECT_MODE_SINGLE),
     sg.Multiline(size=(40,20), disabled=True, autoscroll=True, key='-DETAILS-')],
    [sg.Multiline(size=(80, 5), key='-INPUT-')],
    [sg.Button('Send', bind_return_key=True), sg.Button('Exit')]
]

window = sg.Window('ChatGPT-like Interface', layout)

chat_history = []

while True:  # The Event Loop
    event, values = window.read()
    print(event, values)

    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

    elif event == 'Send':
        new_message = values['-INPUT-']
        chat_history.append(new_message)
        window['-CHAT-'].update(chat_history)
        window['-INPUT-'].update('')  # Clear the input field

    elif event == '-CHAT-':  # If a chat message was clicked
        selected_message = values['-CHAT-'][0]  # Get the selected message
        window['-DETAILS-'].update(selected_message)  # Update the details box

window.close()
