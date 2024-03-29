    actual_data_1 = [
        [sg.Radio("Unmodified","RADIO1",key="Unmodified",size=29)],
        [sg.Radio("Qualified","RADIO1",key="Qualified",size=29)],
        [sg.Radio("Adverse", "RADIO1", key="ADVERSE",size=29)],
        [sg.Radio("Disclaimer/No Opinion", "RADIO1", key="DNO",size=29)],
        [sg.Radio("No Annual Audit Report", "RADIO1", key="NAAR",size=29)]
    ]
    window = sg.Window("Radio Button Example", actual_data_1)

    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        print("Window closed.")
    else:
        print("Value of the radio button:", values["Unmodified"])