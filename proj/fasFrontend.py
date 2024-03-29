import textwrap

import PySimpleGUI as sg
import sys
from fasController import financialReq

def FAS(conn):

    cat1_1 = financialReq(conn)

#1.1 SECTION    
    main_1 = [
        [sg.Text(cat1_1.displayHeadings(0), expand_x=True,text_color="#AF6F09")]
    ]
    sub_1 = [[sg.Text(cat1_1.displaySubHeadings(0),size=(40,1))]]
    actual_data_1 = [
        [sg.Radio("Unmodified","RADIO1",key="Unmodified",size=29, enable_events=True)],
        [sg.Radio("Qualified","RADIO1",key="Qualified",size=29, enable_events=True)],
        [sg.Radio("Adverse", "RADIO1", key="ADVERSE",size=29, enable_events=True)],
        [sg.Radio("Disclaimer/No Opinion", "RADIO1", key="DNO",size=29, enable_events=True)],
        [sg.Radio("No Annual Audit Report", "RADIO1", key="NAAR",size=29, enable_events=True)]
    ]
    coa_recommendation = []
    sub_2 = [[sg.Text(cat1_1.displaySubHeadings(1), size=(40,2)), 
          sg.InputText(key="COA_RECOMMENDATION", size=30, enable_events=True, justification="c")]]
    sub_3 = [[sg.Text(cat1_1.displaySubHeadings(2),size=(40,5)),
              sg.Combo(["Yes","No"],key="TYPO",size=10,enable_events=True)]]
    mov = [[sg.Text("if YES, upload submitted document/s",size=(40,1)),
            sg.InputText("",key="UPLOAD",enable_events=True,size=28),sg.Button("Upload")]]
    main_1_query = [
        [sg.Column(main_1,expand_x=True)], #1.1 column header title
        [sg.Frame("", [[sg.Column(sub_1), sg.Column(actual_data_1)]], expand_x=True)], #radio button choices
        [sg.Frame("", [[sg.Column(sub_2)]], expand_x=True)], #sub 2 section 1.1
        [sg.Frame("", [[sg.Column(sub_3)]],expand_x=True)], #sub 3 section 1.1
        [sg.pin(sg.Frame("", [[sg.Column(mov,expand_x=True)]], expand_x=True,key="MOV",visible=False),expand_x=True)],
    ]

#1.2 SECTION
    text1 = textwrap.fill(cat1_1.displaySectionTwoChoices(0),105)
    text2 = textwrap.fill(cat1_1.displaySectionTwoChoices(1),95)
    main_2 = [[sg.Text(cat1_1.displayHeadings(1),text_color="#AF6F09")],
                [sg.Checkbox(text1,key="CB_1")],
              [sg.Checkbox(text2,key="CB_2")],
              [sg.Checkbox(cat1_1.displaySectionTwoChoices(2))],
              [sg.Checkbox(cat1_1.displaySectionTwoChoices(3))]]

#1.3 SECTION
    main_3 = [[sg.Text(cat1_1.displayHeadings(2),size=(40,2),text_color="#AF6F09"),
               sg.InputText(key="REVENUE_GROWTH",size=30)]]

#1.4 SECTION
    main_4 = [[sg.Text(cat1_1.displayHeadings(3),size=(40,3),text_color="#AF6F09"),
               sg.InputText(key="NTA_UTILIZATION",size=30)]]

#1.5 SECTION
    main_5 = [[sg.Text(cat1_1.displayHeadings(4),text_color="#AF6F09")]]
    sub_5_1 = [[sg.Text("The LGU is a beneficiary of the Performance Challenge Fund in CY 2019 and/or prior year/s"),
                sg.Combo(["Yes","No"],key="PCF",size=10)]]
    sub_5_2 = [[sg.Text("if YES, Please tick one",size=20)]]

#1.5 SECTION: Bullets Choices
    text50 = textwrap.fill(cat1_1.displaySectionFiveSubHeadings(0),70)
    text51 = textwrap.fill(cat1_1.displaySectionFiveSubHeadings(1),70)
    text52 = textwrap.fill(cat1_1.displaySectionFiveSubHeadings(2),70)
    text53 = textwrap.fill(cat1_1.displaySectionFiveSubHeadings(3),70)
    text54 = textwrap.fill(cat1_1.displaySectionFiveSubHeadings(4),70)
    sub_5_3 = [[sg.Radio(text50,"RADIO2",key="OK1")],
                [sg.Radio(text51,"RADIO2",key="OK2")],
                [sg.Radio(text52,"RADIO2", key="NOTOK1")],
                [sg.Radio(text53,"RADIO2", key="NOTOK2")],
                [sg.Radio(text54,"RADIO2", key="NOTOK3")]]
    sub_5_1_frame = [[sg.Column(sub_5_1,expand_x=True)]]
    sub_5_2_frame = [[sg.Column(sub_5_2,expand_x=True),sg.Column(sub_5_3,expand_x=True)]]
    main_5_query = [[sg.Column(main_5,expand_x=True)],
                    [sg.Frame("",sub_5_1_frame,expand_x=True)],
                    [sg.Frame("",sub_5_2_frame,expand_x=True)]]

    main_1_column = [
        [sg.Frame("",main_1_query,expand_x=True)],
        [sg.Frame("",[[sg.Column(main_2,expand_x=True)]],expand_x=True)],
        [sg.Frame("",[[sg.Column(main_3,expand_x=True)]],expand_x=True)],
        [sg.Frame("",[[sg.Column(main_4,expand_x=True)]],expand_x=True)],
        [sg.Frame("",main_5_query,expand_x=True)]
        ]
    main_column = [[sg.Column(main_1_column,scrollable=True,vertical_scroll_only=True,expand_y=True)]]

    return main_column