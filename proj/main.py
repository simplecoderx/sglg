import PySimpleGUI as sg
import sqlite3
import sys
from fasFrontend import FAS
from fasController import financialReq
from DP import DP
from minimum_requirements import mr

#ACTIONS SECTION
class SGLG:
    def __init__(self) -> None:
        self.data = {'Agusan Del Norte': ['Buenavista','Cabadbaran City','Carmen','Jabonga','Kitcharao','Las Nieves','Magallanes','Nasipit','RTR','Santiago','Tubay','Butuan City', 'One'],
                    'Agusan Del Sur': ['Bayugan City','Bunawan','Esperanza','La Paz','Loreto','Properidad','Rosario','San Francisco','San Luis','Sibagat','Sta. Josefa','Talacogon','Trento','Veruela'],
                    'Surigao Del Norte': ['Alegria','Bacuag','Burgos','Claver','Dapa','Del Carmen','General Luna','Gigaquit','Mainit','Malimono','Pilar','Placer','San Benito','San Francisco','San Isidro','Sison','Socorro','Sta. Monica','Tagana-an','Tubod','Surigao City'],
                    'Surigao Del Sur': ['Barobo','Bayabas','Bislig City','Cagwait','Cantilan','Carmen','Carrascal','Cortes','Hinatuan','Lanuza','Llanga','Lingig','Madrid','Marihatag','San Agustin','San Miguel','Tagbina','Tago','Tandag City'],
                    'Province of Dinagat Islands': ['Basilisa','Cagdianao','Dinagat','Libjo','Loreto','San Jose','Tubajon']}
        self.incomeClass = {'HUC':[''],'CC':[],'1st Class':['Bayugan City'],'2nd Class':['Buenavista'],'3rd Class':[],'4th Class':[],'5th Class':['Carmen'],'6th Class':[]}
        self.fieldOfficers = {'Agusan Del Norte': {'Carmen': 'Lynn', 'Buenavista': 'Jane', 'Jabonga': 'Jay'},
                        'Agusan Del Sur': {'d': 'Lynn', 'e': 'Jane', 'f': 'Jay'},
                        'Surigao Del Sur': {'g': 'Lynn', 'h': 'Jane', 'i': 'Jay'},
                        'Surigao Del Norte': {'j': 'Lynn', 'k': 'Jane', 'l': 'Jay'},
                        'Province of Dinagat Islands': {'m': 'Lynn', 'n': 'Jane', 'o': 'Jay'}}
        self.conn = sqlite3.connect('SGLG.db')
        self.cursor = self.conn.cursor()
        
    def clear(self, e):
        window['PROVINCE'].update('')
        window['CM'].update('')
        window['FIELD_OFFICER'].update('')
        window['INCOME_CLASS'].update('')
        window["FAS_FRAME"].update(visible=False)
        window["DP_FRAME"].update(visible=False)

    #def get_municipalities(self, province):
        #print(self.income_class)
        #if province in self.data:
            #return self.data[province]
        #else:
            #return None
        
    def get_municipalities(self, province):
        query = "SELECT MName FROM MUNICIPALITY INNER JOIN PROVINCE ON MUNICIPALITY.pID = PROVINCE.pID WHERE PName = ?"
        self.cursor.execute(query, (province,))
        municipalities = self.cursor.fetchall()
        return [m[0] for m in municipalities]
        
    #def get_cm(self, mun):
    #    print("municipality function")
    #    cm = ''
    #    for i in self.incomeClass:
    #        if mun in self.incomeClass[i]:
    #            cm = i
    #            print(mun, "is", cm)
    #    return cm
                
    #def get_fo(self, mun, province):
    #    print(mun, "this is for get_fo function")
    #    print(province, "this is for get_fo function")
    #    field_officer = self.fieldOfficers.get(province, {}).get(mun)
    #    if field_officer:
    #        print(field_officer)
    #        return field_officer
    #    else:
    #        print("No Field Officer")


    def get_cm(self, mun):
        query = "SELECT icName FROM INCOMECLASS WHERE mID IN (SELECT mID FROM MUNICIPALITY WHERE MName = ?)"
        self.cursor.execute(query, (mun,))
        cm = self.cursor.fetchone()
        if cm:
            return cm[0]
        else:
            return "Error. No income class."

    def get_fo(self, mun, province):
        query = "SELECT foName FROM FIELD_OFFICERS WHERE mID IN (SELECT mID FROM MUNICIPALITY WHERE MName = ?) AND pID IN (SELECT pID FROM PROVINCE WHERE PName = ?)"
        self.cursor.execute(query, (mun, province))
        fo = self.cursor.fetchone()
        if fo:
            return fo[0]
        else:
            return "Error. No field officer."
        
    def emptyLocality(self):
        if values['PROVINCE'] == "":
            sg.PopupError('Please Select Province!')
        elif values['CM'] == "":
            sg.PopupError("Please Select City/Municipality!")
        elif values['INCOME_CLASS'] == "":
            sg.PopupError('Empty Income Class. Please select Province first!')
        elif values['FIELD_OFFICER'] == "":
            sg.PopupError('Empty Field Officer. Please select Province first!')
        else:
            frInstance = financialReq(self.conn)
            cat1_1 = frInstance.controllerFinancialReq(province, cm)
            if cat1_1 == True:
                window["FAS_FRAME"].update(visible=True)
                window["DP_FRAME"].update(visible=False)
            else:
                print(cat1_1, "this is else after controllerFinancialReq was called in emptyLocality\n")

    def unEmptyLocality(province, cm):
        print(province, cm, "this is from unEmptyLocality")

    def close_connection(self):
        self.conn.close()
        


#FRONTEND SECTION
sg.LOOK_AND_FEEL_TABLE['Theme'] = {'BACKGROUND': '#292929',
                                    'TEXT': '#009bff',
                                    'INPUT': '#ffffff',
                                    'TEXT_INPUT': '#000000',
                                    'SCROLL': '#ffffff',
                                    'BUTTON': ('#5cfd46', '#151515'),
                                    'PROGRESS': ('#01826B', '#D0D0D0'),
                                    'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,}
sg.theme("Default1")
sg.set_options(font=("yu Gothic u1",10))


#INSTANCES
sglg_instance = SGLG()

# Access the conn attribute
conn = sglg_instance.conn

#VARIABLES FOR IMAGES SECTION
dilg_logo = [[sg.Image("logo_FINAL1.png")]]
sglg_logo = [[sg.Image("SGLG_LOGO.png")]]

#APPLICATION TITLE
header_frame = [[sg.Text("SGLG Regional Monitoring and Compliance Tracking System",font=("Courier New",20),justification="center")]]

#CONSTANTS
provinces = ('Agusan Del Norte','Agusan Del Sur','Surigao Del Norte','Surigao Del Sur','Province of Dinagat Islands')

#LOCALITY FRAME
locality = [[sg.Text("Province: ",size=12),sg.Combo(provinces,key='PROVINCE',enable_events=True,size=23)],
            [sg.Text("City/Municipality: ",size=12),sg.Combo([],key='CM',size=23,enable_events=True)],
            [sg.Text("Income Class: ",size=12),sg.InputText(key='INCOME_CLASS',size=24,disabled=True)],
            [sg.Text("Field Officer: ",size=12),sg.InputText(key='FIELD_OFFICER',size=24,disabled=True)]]

#CATEGORIES
category = [
    [sg.Button("1. Financial Administration and Sustainability",size=35,key="1")],
    [sg.Button("2. Disaster Preparedness",size=35,key="2")],
    [sg.Button("3. Social Protection and Sensitivity",size=35)],
    [sg.Button("4. Health Compliance and Responsiveness",size=35)],
    [sg.Button("5. Sustainable Education",size=35)],
    [sg.Button("6. Business-Friendliness and Competitiveness", size=35)],
    [sg.Button("7. Safety, Peace and Order", size=35)],
    [sg.Button("8. Environmental Management", size=35)],
    [sg.Button("9. Tourism, Heritage Dev't, Culture and Arts", size=35)],
    [sg.Button("10. Youth Development", size=35)]

]

#SHOW MINIMUM REQ BUTTON STYLE
minimum_requirements = [[sg.Button("Show Minimum Requirements",size=35)]]

#ACTIONS
button = [
        [sg.Button("SAVE",expand_x=True,button_color=("#90FFEE","gray"),font=("Courier New",10))],
        [sg.Button("CLEAR", expand_x=True,button_color=("#FFFF3C","gray"),font=("Courier New",10))],
        [sg.Button("EXIT", expand_x=True,button_color=("Red","gray"),font=("Courier New",10))],]

#COLUMN DIVISIONS
category_Column = [[sg.Column(category,expand_x=True)]]
locality_Column = [[sg.Column(locality,expand_x=True)]]
minimum_requirements_column = [[sg.Column(minimum_requirements,expand_x=True)]]
button_column = [[sg.Column(button,expand_x=True)]]

left_column = [
    [sg.Frame("",locality_Column,expand_x=True)],
    [sg.Frame("Category",category_Column,expand_y=True,title_color="green",font=("Courier New Bold",10))],
    [sg.Frame("Technical Notes",minimum_requirements_column,expand_x=True,title_color="green",font=("Courier New Bold",10))],
    [sg.Frame("Option",button_column,expand_x=True,title_color="green",font=("Courier New Bold",10))]]

layout = [
    [sg.Frame("",[[sg.Column(dilg_logo),sg.Column(sglg_logo),sg.Column(header_frame)]],expand_x=True,element_justification="c")],
    [sg.Column(left_column,expand_x=True),
    sg.Frame("Financial Administration and Sustainability",FAS(conn),expand_y=True,key="FAS_FRAME",visible=False,font=("Courier New",13),title_color="#00075B"),
     sg.Frame("Disaster Preparedness",DP(),key="DP_FRAME",visible=False,expand_y=True,font=("Courier New",13)),
     sg.Frame("Minimum Requirements",mr(),visible=False,key="MR",expand_y=True,title_color="Green",font=("Courier New",13))]
]

window = sg.Window("Main Window",layout,resizable=True).Finalize()
window.Maximize()
window['CB_1'].Widget.configure(justify="left")
window['CB_2'].Widget.configure(justify="left")
window['OK1'].Widget.configure(justify="left")
window['OK2'].Widget.configure(justify="left")
window['NOTOK1'].Widget.configure(justify="left")
window['NOTOK2'].Widget.configure(justify="left")
window['NOTOK3'].Widget.configure(justify="left")

# window["1"].bind("<Enter>", "+MOUSE OVER+")
# window["1"].bind("<Leave>", "+MOUSE AWAY+")


""" EVENT HANDLING SECTION """
while True:
    event, values = window.read()
    if event ==sg.WIN_CLOSED or event == "EXIT":
        break
    if event == "CLEAR":
        a = SGLG.clear("",event)
    if event == "1":
        cm = values["CM"]
        sglgInstance = SGLG()
        cat1 = sglgInstance.emptyLocality()
    if event == "2":
        cat1 = SGLG.emptyLocality()

#1.1 Sub Section Dropdown Menu
    if values["TYPO"] == "Yes":
        window["MOV"].update(visible=True)
    else:
        window["MOV"].update(visible=False)

#Minimum Req
    if event == "Show Minimum Requirements":
        window["MR"].update(visible=True)

#Province
    if event == "PROVINCE":
        municipalities = SGLG()
        province = values['PROVINCE']
        result_mun = municipalities.get_municipalities(province)
        if result_mun:
            window["CM"].update(values=result_mun)
        else:
            sg.popup("Province not Found.")

        #municipalities = SGLG()
        #province = values['PROVINCE']
        #result_mun = municipalities.get_municipalities(province)
        #if result_mun:
        #    print(result_mun)
        #    window["CM"].update(values=result_mun)
        #else:
        #    print("Province not Found.")

#City/Municipality
    if event == "CM":
        municipalities = SGLG()
        cm = values['CM']
        income = values['INCOME_CLASS']
        print(cm)
        result_cm = municipalities.get_cm(cm)
        result_fo = municipalities.get_fo(cm, province)
        print(result_cm)
        if result_cm:
            print(result_cm)
            window["INCOME_CLASS"].update(result_cm)
        else:
            print("Error. No income class.")
        if result_fo:
            print(result_fo)
            window["FIELD_OFFICER"].update(result_fo)
        else:
            print("Error. No field officer.")

# FAS 1.1 SECTION
    if event == "Unmodified":
        fo = values['FIELD_OFFICER']
        print(cm, fo, "kuan ni")
        #fr_instance = financialReq()
        cat1_1 = financialReq.handle_unmodified(event, values, cm, fo)
    elif event == "Qualified":
        cat1_1 = financialReq.handle_qualified(event, values)
    elif event == "ADVERSE":
        cat1_1 = financialReq.handle_adverse(event, values)
    elif event == "DNO":
        cat1_1 = financialReq.handle_dno(event, values)
    elif event == "NAAR":
        cat1_1 = financialReq.handle_naar(event, values)
    elif event == "Upload":
        cat1_1 = financialReq.handle_upload(event, values)
    elif event == "TYPO":
        cat1_1 = financialReq.handle_typo(event, values)
    elif event == "OK1":
        cat1_1 = financialReq.handle_ok1(event, values)
    elif event == "OK2":
        cat1_1 = financialReq.handle_ok2(event, values)
    elif event == "NOTOK1":
        cat1_1 = financialReq.handle_notok1(event, values)
    elif event == "NOTOK2":
        cat1_1 = financialReq.handle_notok2(event, values)
    elif event == "NOTOK3":
        cat1_1 = financialReq.handle_notok3(event, values)
    else:
        print("fas section main not working")

#FAS 1.1 INPUT TEXT SECTION
    if event == "COA_RECOMMENDATION":
        coa_recommendation = window["COA_RECOMMENDATION"].get()
        res = financialReq.handle_coaRecommendation(event, coa_recommendation)
        print(res, coa_recommendation, event,  "this is from main event function coa recommendation\n")
        print("this is main from coa recomendation\n")
    else:
        print("COA RECOMMENDATION EVENT IS NOT WORKING")
        