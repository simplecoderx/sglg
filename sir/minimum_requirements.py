import textwrap

import PySimpleGUI as sg

def mr():

    mr1_1 = [[sg.Text(textwrap.fill("Most recent COA AAR that is UNMODIFIED or QUALIFIED AND 30% of Recommendations FULLY complied with",60))]]
    mr1_2 = [[sg.Text(textwrap.fill("P/C/M must have FULL Compliance with FDP (CY 2022 2nd to 4th Qtr and CY 2023 1st Qtr) posting in FDP Portal and CP AND FY 2022 Q4 LIFT System Reports",60))]]

    mr1_1_frame = [[sg.Frame("1.1",mr1_1,expand_y=True,expand_x=True,title_color="#AF6F09")],
                   [sg.Frame("1.2",mr1_2,expand_x=True,title_color="#AF6F09")]]

    mr1_1_column = [[sg.Column(mr1_1_frame,vertical_scroll_only=True,expand_x=True,expand_y=True,scrollable=True)]]

    return mr1_1_column