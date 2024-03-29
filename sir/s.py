import textwrap
import PySimpleGUI as sg

class FASForm:
    def __init__(self):
        self.layout = self.create_layout()
        self.window = sg.Window('FAS Form', self.layout)

    def create_layout(self):
        main_1 = [
            [sg.Text("1.1 Most recent audit opinion is unmodified or qualified plus 30% of recommendations fully complied with", expand_x=True, text_color="#AF6F09")]
        ]
        sub_1 = [[sg.Text("Most Recent Audit Opinion (CY2021 or CY2022)", size=(40, 1))]]
        actual_data_1 = [
            [sg.Radio("Unmodified", "RADIO1", key="Unmodified", size=29)],
            [sg.Radio("Qualified", "RADIO1", key="Qualified", size=29)],
            [sg.Radio("Adverse", "RADIO1", key="ADVERSE", size=29)],
            [sg.Radio("Disclaimer/No Opinion", "RADIO1", key="DNO", size=29)],
            [sg.Radio("No Annual Audit Report", "RADIO1", key="NAAR", size=29)]
        ]
        sub_2 = [[sg.Text("Percentage of fully-complied recommendations (please supply information)", size=(40, 2)),
                  sg.InputText(key="COA_RECOMMENDATION", size=30, justification="c")]]
        sub_3 = [[sg.Text("If data in the provided NGA database contains typographical errors, LGU submitted a portion of the Annual Audit Report "
                          "that will support the correct data (i.e. Executive Summary and Status of implementation of prior year's audit recommendations)", size=(40, 5)),
                  sg.Combo(["Yes", "No"], key="TYPO", size=10, enable_events=True)]]
        mov = [[sg.Text("if YES, upload submitted document/s", size=(40, 1)),
                sg.InputText("", key="UPLOAD", enable_events=True, size=28), sg.Button("Upload")]]
        main_1_query = [
            [sg.Column(main_1, expand_x=True)],
            [sg.Frame("", [[sg.Column(sub_1), sg.Column(actual_data_1)]], expand_x=True)],
            [sg.Frame("", [[sg.Column(sub_2)]], expand_x=True)],
            [sg.Frame("", [[sg.Column(sub_3)]], expand_x=True)],
            [sg.pin(sg.Frame("", [[sg.Column(mov, expand_x=True)]], expand_x=True, key="MOV", visible=False), expand_x=True)],
        ]

        text = "Full Disclosure Policy Portal for CY 2022 2nd to 4th Quarters, and CY 2023 1st Quarter posting period documents"
        text_2 = "Three (3) conspicuous places for CY 2022 2nd to 4th quarters, and CY 2023 1st Quarter posting period documents (based on accomplished Form 2E: DILG Field Office)"
        New_text = textwrap.fill(text, 105)
        new_text_2 = textwrap.fill(text_2, 95)
        main_2 = [[sg.Text("1.2 The LGU fully complied with posting in (please tick all applicable items)", text_color="#AF6F09")],
                    [sg.Checkbox(New_text, key="CB_1")],
                  [sg.Checkbox(new_text_2, key="CB_2")],
                  [sg.Checkbox("Timely submission of  FY 2022-Q4 LIFT System Reports (SRE and QRRPA)")],
                  [sg.Checkbox("None of the above")]]

        main_3 = [[sg.Text("1.3 Average local revenue growth of LGU from CYs 2020 to 2022 (please supply information)", size=(40, 2), text_color="#AF6F09"),
                   sg.InputText(key="REVENUE_GROWTH", size=30)]]

        main_4 = [[sg.Text("1.4 Utilization percentage of the 20% component of the National Tax Allotment for local development projects (please supply information)", size=(40, 3), text_color="#AF6F09"),
                   sg.InputText(key="NTA_UTILIZATION", size=30)]]

        main_5 = [[sg.Text("1.5 Full utilization of all Performance Challenge Funds released in CY 2019 and earlier, if applicable", text_color="#AF6F09")]]
        sub_5_1 = [[sg.Text("The LGU is a beneficiary of the Performance Challenge Fund in CY 2019 and/or prior year/s"),
                    sg.Combo(["Yes", "No"], key="PCF", size=10)]]
        sub_5_2 = [[sg.Text("if YES, Please tick one", size=20)]]

        text_5_1 = "All the received funds are fully liquidated and disbursed, with no unobligated balances"
        text_5_2 = "All the received funds are fully liquidated and disbursed, with all unobligated balances reverted back to the National Treasury"
        text_5_3 = "There are received funds that are not fully liquidated and disbursed"
        text_5_4 = "There are unobligated balances that are yet to be reverted back to the National Treasury"
        text_5_5 = "The LGU is included in the list of LGUs with pending PCF-funded projects from DILG-BLGD"
        new_text_5_1 = textwrap.fill(text_5_1, 70)
        new_text_5_2 = textwrap.fill(text_5_2, 70)
        new_text_5_3 = textwrap.fill(text_5_3, 70)
        new_text_5_4 = textwrap.fill(text_5_4, 70)
        new_text_5_5 = textwrap.fill(text_5_5, 70)
        sub_5_3 = [[sg.Radio(new_text_5_1, "RADIO2", key="OK1")],
        [sg.Radio(new_text_5_2, "RADIO2", key="OK2")],
        [sg.Radio(new_text_5_3, "RADIO2", key="NOTOK1")],
        [sg.Radio(new_text_5_4, "RADIO2", key="NOTOK2")],
        [sg.Radio(new_text_5_5, "RADIO2", key="NOTOK3")]]
        sub_5_1_frame = [[sg.Column(sub_5_1, expand_x=True)]]
        sub_5_2_frame = [[sg.Column(sub_5_2, expand_x=True), sg.Column(sub_5_3, expand_x=True)]]
        main_5_query = [[sg.Column(main_5, expand_x=True)],
        [sg.Frame("", sub_5_1_frame, expand_x=True)],
        [sg.Frame("", sub_5_2_frame, expand_x=True)]]

        main_1_column = [
        [sg.Frame("", main_1_query, expand_x=True)],
        [sg.Frame("", [[sg.Column(main_2, expand_x=True)]], expand_x=True)],
        [sg.Frame("", [[sg.Column(main_3, expand_x=True)]], expand_x=True)],
        [sg.Frame("", [[sg.Column(main_4, expand_x=True)]], expand_x=True)],
        [sg.Frame("", main_5_query, expand_x=True)]
        ]
        main_column = [[sg.Column(main_1_column, scrollable=True, vertical_scroll_only=True, expand_y=True)]]

        return main_column

    def run(self):
        while True:
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED:
                break
        self.window.close()
        if name == 'main':
            form = FASForm()
            form.run()

