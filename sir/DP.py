import PySimpleGUI as sg

def DP():
    main_1 = [
        [sg.Text("2.1 The LGU has an established and functional Local Disaster Risk Reduction and Management Council (LDRRMC)")]
    ]
    main_1_frame = [[sg.Frame("",main_1,expand_x=True)]]
    sub_1 = [
        [sg.Text("1.a The LDRRMC meets standards set under R.A. No. 10121 and includes(please tick all applicable items)",size=(40,2),justification="left")]
    ]
    actual_data_1 = [
        [sg.Checkbox("At least four (4) accredited CSO members",key="4")],
        [sg.Checkbox("At least one (1) private sector representative",key="1")],
        [sg.Checkbox("None of the above",key="NONE")]
    ]

    main_1_column = [
        [sg.Column(main_1_frame)],
        [sg.Frame("",[[sg.Column(sub_1),sg.Column(actual_data_1)]],expand_x=True)]
        ]
    main_column = [[sg.Column(main_1_column,scrollable=True,vertical_scroll_only=True,expand_y=True)]]
    return main_column