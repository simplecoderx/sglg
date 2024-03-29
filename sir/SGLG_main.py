import PySimpleGUI as sg
import sys
from FAS import FAS
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
    def clear(self, e):
        window['PROVINCE'].update('')
        window['CM'].update('')
        window['FIELD_OFFICER'].update('')
        window['INCOME_CLASS'].update('')

    def get_municipalities(self, province):
        #print(self.income_class)
        if province in self.data:
            return self.data[province]
        else:
            return None
        
    def get_cm(self, mun):
        print("municipality function")
        cm = ''
        for i in self.incomeClass:
            if mun in self.incomeClass[i]:
                cm = i
                print(mun, "is", cm)
        return cm
                
    
    def get_fo(self, mun, province):
        print(mun, "this is for get_fo function")
        print(province, "this is for get_fo function")
        field_officer = self.fieldOfficers.get(province, {}).get(mun)
        if field_officer:
            print(field_officer)
            return field_officer
        else:
            print("No Field Officer")
        
 
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


#VARIABLES FOR IMAGES SECTION
dilg_logo = [[sg.Image("logo_FINAL1.png")]]
sglg_logo = [[sg.Image("SGLG_LOGO.png")]]

#APPLICATION TITLE
header_frame = [[sg.Text("SGLG Regional Monitoring and Compliance Tracking System",font=("Courier New",20),justification="center")]]

#CONSTANTS
provinces = ('Agusan Del Norte','Agusan Del Sur','Surigao Del Norte','Surigao Del Sur','Province of Dinagat Islands')

""" adn = ('Buenavista','Cabadbaran City','Carmen','Jabonga','Kitcharao','Las Nieves','Magallanes','Nasipit','RTR','Santiago','Tubay','Butuan City')
adn_array = [['Buenavista','Cabadbaran City','Carmen','Jabonga','Kitcharao','Las Nieves','Magallanes','Nasipit','RTR','Santiago','Tubay','Butuan City'],
             ['Bayugan City','Bunawan','Esperanza','La Paz','Loreto','Properidad','Rosario','San Francisco','San Luis','Sibagat','Sta. Josefa','Talacogon','Trento','Veruela'],
             ['Basilisa','Cagdianao','Dinagat','Libjo','Loreto','San Jose','Tubajon'],
             ['Alegria','Bacuag','Burgos','Claver','Dapa','Del Carmen','General Luna','Gigaquit','Mainit','Malimono','Pilar','Placer','San Benito','San Francisco','San Isidro','Sison','Socorro','Sta. Monica','Tagana-an','Tubod','Surigao City'],
             ['Barobo','Bayabas','Bislig City','Cagwait','Cantilan','Carmen','Carrascal','Cortes','Hinatuan','Lanuza','Llanga','Lingig','Madrid','Marihatag','San Agustin','San Miguel','Tagbina','Tago','Tandag City']]
income_class_array = ['HUC','CC','1st Class','2nd Class','3rd Class','4th Class','5th Class','6th Class']
field_officer_array = [['Yul O. Guerta','Annabella O. Cadigal','Laarni Beauty C. Sepe','Jaimelyn S. Cobrado','Leslie Ann M. Bantasan','Myrna B. Libao','Maricel G. Torreon','Karolous Joseph A. Fuertes','Vincent Angelo M. Balansag','Jeffrey A. Ramo','Melchora L. Grana','Lolita S. Go'],
                       ['Alice B. Robles','Feliviv C. Cuanan','Atty. Daniel P. Longaquit','Sherwin C. Obien','Mary Nol P. Aban','Luth Edmund M. Apresto','Rena L. Naguita','Archie Rose V. Raza','Charles V. Lim Jr.','Maricel G. Dumanglas','Arturo O. Bombeo Jr.','Renelou F. Jaranilla','Jorem J. Luzon','Joemar S. Salmoro'],
                       ['Don Manuelo O. Patrimonio','Gretchen D. Jazon','Jecquel G. Cultura','Bryan F. Edulzura','Hazel Anne B. Plaza','Donna Dial D. Madelo','Desiree B. Bakit'],
                       ['Marilou E. Alovera','Welivie C. Diola','Jubilyn S. Blase','Jenita T. Ladres','Marjorie A. Dalagan','Ednon John E. Aparicio','Jacky A. Mellorin','Crisologo L. Virtudazo','Liza L. Montaner','Rosalina A. Sering','Nova D. Hilig','Roberto A. Reyna Jr.','Estela Marie M. Vallespin','Mary Jane C. Centino','Genalin C. Pegarro','Ian Jun A. Gesta','Wenefredo R. Lasala Jr.','Krisha Antonnette V. Cultura','Catherine A. Gealogo','Jimelyn H. Ballicud','Roberto E. Patayon'],
                       ['Jane G. Moreno','Joselito S. Ramos','Julius R. Carrido','Mayonito Fernan E. Ramos','Mark Anthony C. Obani','Julieto O. Curayag','Merril B. Espenido','Marichelle O. Gultiano','Sharamae I. Dalogdog','Bella C. Decena','Ian Reigh M. Elimanco','Ferdy Benigno R. Avila','Noel L. Arreza','Ernie Y. Gultiano','Redgy V. Panilan','Ma. Rosario M. Ambray','Roel J. Camba','Arman M. Decena','Marlon C. Monterola']] """
#APPENDING MUNICIPALITY, INCOME CLASS, FIELD OFFICER
""" def cm():
    result = []
    for cm in adn_array:
        result.append(cm)
    return result """
def ic():
    result = []
    for ic in income_class_array:
        result.append(ic)
    return result
def fo():
    result = []
    for fo in field_officer_array:
        result.append(fo)
    return result

locality = [[sg.Text("Province: ",size=12),sg.Combo(provinces,key='PROVINCE',enable_events=True,size=23)],
            [sg.Text("City/Municipality: ",size=12),sg.Combo([],key='CM',size=23,enable_events=True)],
            [sg.Text("Income Class: ",size=12),sg.InputText(key='INCOME_CLASS',size=24,disabled=True)],
            [sg.Text("Field Officer: ",size=12),sg.InputText(key='FIELD_OFFICER',size=24,disabled=True)]]

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
minimum_requirements = [[sg.Button("Show Minimum Requirements",size=35)]]
button = [
    [sg.Button("SAVE",expand_x=True,button_color=("#90FFEE","gray"),font=("Courier New",10))],
    [sg.Button("CLEAR", expand_x=True,button_color=("#FFFF3C","gray"),font=("Courier New",10))],
    [sg.Button("EXIT", expand_x=True,button_color=("Red","gray"),font=("Courier New",10))],

]

category_Column = [[sg.Column(category,expand_x=True)]]
locality_Column = [[sg.Column(locality,expand_x=True)]]
minimum_requirements_column = [[sg.Column(minimum_requirements,expand_x=True)]]
button_column = [[sg.Column(button,expand_x=True)]]

left_column = [
    [sg.Frame("",locality_Column,expand_x=True)],
    [sg.Frame("Category",category_Column,expand_y=True,title_color="green",font=("Courier New Bold",10))],
    [sg.Frame("Technical Notes",minimum_requirements_column,expand_x=True,title_color="green",font=("Courier New Bold",10))],
    [sg.Frame("Option",button_column,expand_x=True,title_color="green",font=("Courier New Bold",10))]
]

layout = [
    [sg.Frame("",[[sg.Column(dilg_logo),sg.Column(sglg_logo),sg.Column(header_frame)]],expand_x=True,element_justification="c")],
    [sg.Column(left_column,expand_x=True),
    sg.Frame("Financial Administration and Sustainability",FAS(),expand_y=True,key="FAS_FRAME",visible=False,font=("Courier New",13),title_color="#00075B"),
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

while True:
    event, values = window.read()
    if event ==sg.WIN_CLOSED or event == "EXIT":
        break
    if event == "CLEAR":
        """ a = SGLG("", "", "", "", event) """
        a = SGLG.clear("",event)
    if event == "1":
        if values['PROVINCE'] == "":
            sg.PopupError('Please Select Province!')
        elif values['CM'] == "":
            sg.PopupError("Please Select City/Municipality!")
        else:
            window["FAS_FRAME"].update(visible=True)
            window["DP_FRAME"].update(visible=False)
    if event == "2":
        window["FAS_FRAME"].update(visible=False)
        window["DP_FRAME"].update(visible=True)
    if values["TYPO"] == "Yes":
        window["MOV"].update(visible=True)
    else:
        window["MOV"].update(visible=False)

    if event == "Show Minimum Requirements":
        window["MR"].update(visible=True)

    if event == "PROVINCE":
        municipalities = SGLG()
        province = values['PROVINCE']
        result_mun = municipalities.get_municipalities(province)
        if result_mun:
            print(result_mun)
            window["CM"].update(values=result_mun)
        else:
            print("Province not Found.")

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


    if event == "FIELD_OFFICER":
        fieldOfficer = values["FIELD_OFFICER"]
        print(fieldOfficer)
        
        #result_fo = municipalities.get_fo(cm)
        #print(result_cm)
        #if result_cm:
        #    print(result_cm)
        #    window["INCOME_CLASS"].update(result_cm)
        #else:
        #    print("Municipality not Found.")

            
        """ if values["PROVINCE"] == "Agusan Del Norte":
            window["CM"].update(values=cm()[0])
            window['FIELD_OFFICER'].update("")
            window['INCOME_CLASS'].update("")
        elif values['PROVINCE'] == "Agusan Del Sur":
            window['CM'].update(values=cm()[1])
            window['FIELD_OFFICER'].update("")
            window['INCOME_CLASS'].update("")
        elif values['PROVINCE'] == "Province of Dinagat Islands":
            window['CM'].update(values=cm()[2])
            window['FIELD_OFFICER'].update("")
            window['INCOME_CLASS'].update("")
        elif values['PROVINCE'] == "Surigao Del Norte":
            window['CM'].update(values=cm()[3])
            window['FIELD_OFFICER'].update("")
            window['INCOME_CLASS'].update("")
        elif values['PROVINCE'] == "Surigao Del Sur":
            window['CM'].update(values=cm()[4])
            window['FIELD_OFFICER'].update("")
            window['INCOME_CLASS'].update("") """

"""     if event == "CM":
        if values["CM"] == "Buenavista":
            window["INCOME_CLASS"].update(ic()[2])
            window['FIELD_OFFICER'].update(fo()[0][0])
        elif values['CM'] == 'Cabadbaran City':
            window['FIELD_OFFICER'].update(fo()[0][1])
            window["INCOME_CLASS"].update(ic()[7])
        elif values['CM'] == 'Carmen':
            window['FIELD_OFFICER'].update(fo()[0][2])
            window["INCOME_CLASS"].update(ic()[5])
        elif values['CM'] == 'Jabonga':
            window['FIELD_OFFICER'].update(fo()[0][3])
            window["INCOME_CLASS"].update(ic()[4])
        elif values['CM'] == 'Kitcharao':
            window['FIELD_OFFICER'].update(fo()[0][4])
            window["INCOME_CLASS"].update(ic()[5])
        elif values['CM'] == 'Las Nieves':
            window['FIELD_OFFICER'].update(fo()[0][5])
            window["INCOME_CLASS"].update(ic()[3])
        elif values['CM'] == 'Magallanes':
            window['FIELD_OFFICER'].update(fo()[0][6])
            window["INCOME_CLASS"].update(ic()[5])
        elif values['CM'] == 'Nasipit':
            window['FIELD_OFFICER'].update(fo()[0][7])
            window["INCOME_CLASS"].update(ic()[4])
        elif values['CM'] == 'RTR':
            window['FIELD_OFFICER'].update(fo()[0][8])
            window["INCOME_CLASS"].update(ic()[6])
        elif values['CM'] == 'Santiago':
            window['FIELD_OFFICER'].update(fo()[0][9])
            window["INCOME_CLASS"].update(ic()[5])
        elif values['CM'] == 'Tubay':
            window['FIELD_OFFICER'].update(fo()[0][10])
            window["INCOME_CLASS"].update(ic()[5])
        elif values['CM'] == 'Butuan City':
            window['FIELD_OFFICER'].update(fo()[0][11])
            window["INCOME_CLASS"].update(ic()[0])
    if event == "CM":
        if values["CM"] == "Bayugan City":
            window['FIELD_OFFICER'].update(fo()[1][0])
            window['INCOME_CLASS'].update(ic()[6])
        if values["CM"] == "Bunawan":
            window['FIELD_OFFICER'].update(fo()[1][1])
            window['INCOME_CLASS'].update(ic()[2])
        if values["CM"] == "Esperanza":
            window['FIELD_OFFICER'].update(fo()[1][2])
            window['INCOME_CLASS'].update(ic()[2])
        if values["CM"] == "La Paz":
            window['FIELD_OFFICER'].update(fo()[1][3])
            window['INCOME_CLASS'].update(ic()[2])
        if values["CM"] == "Loreto":
            window['FIELD_OFFICER'].update(fo()[1][4])
            window['INCOME_CLASS'].update(ic()[2])
        if values["CM"] == "Prosperidad":
            window['FIELD_OFFICER'].update(fo()[1][5])
            window['INCOME_CLASS'].update(ic()[2])
        if values["CM"] == "Rosario":
            window['FIELD_OFFICER'].update(fo()[1][6])
            window['INCOME_CLASS'].update(ic()[3])
        if values["CM"] == "San Francisco":
            window['FIELD_OFFICER'].update(fo()[1][7])
            window['INCOME_CLASS'].update(ic()[2])
        if values["CM"] == "San Luis":
            window['FIELD_OFFICER'].update(fo()[1][8])
            window['INCOME_CLASS'].update(ic()[2])
        if values["CM"] == "Sibagat":
            window['FIELD_OFFICER'].update(fo()[1][9])
            window['INCOME_CLASS'].update(ic()[2])
        if values["CM"] == "Sta. Josefa":
            window['FIELD_OFFICER'].update(fo()[1][10])
            window['INCOME_CLASS'].update(ic()[4])
        if values["CM"] == "Talacogon":
            window['FIELD_OFFICER'].update(fo()[1][11])
            window['INCOME_CLASS'].update(ic()[3])
        if values["CM"] == "Tento":
            window['FIELD_OFFICER'].update(fo()[1][12])
            window['INCOME_CLASS'].update(ic()[2])
        if values["CM"] == "Veruela":
            window['FIELD_OFFICER'].update(fo()[1][13])
            window['INCOME_CLASS'].update(ic()[3])
        elif values['CM'] == "Basilisa":
            window['FIELD_OFFICER'].update(fo()[2][0])
            window['INCOME_CLASS'].update(ic()[5])
        elif values['CM'] == "Cagdianao":
            window['FIELD_OFFICER'].update(fo()[2][1])
            window['INCOME_CLASS'].update(ic()[4])
        elif values['CM'] == "Dinagat":
            window['FIELD_OFFICER'].update(fo()[2][2])
            window['INCOME_CLASS'].update(ic()[6])
        elif values['CM'] == "Libjo":
            window['FIELD_OFFICER'].update(fo()[2][3])
            window['INCOME_CLASS'].update(ic()[6])
        elif values['CM'] == "Loreto":
            window['FIELD_OFFICER'].update(fo()[2][4])
            window['INCOME_CLASS'].update(ic()[5])
        elif values['CM'] == "San Jose":
            window['FIELD_OFFICER'].update(fo()[2][5])
            window['INCOME_CLASS'].update(ic()[5])
        elif values['CM'] == "Tubajon":
            window['FIELD_OFFICER'].update(fo()[2][6])
            window['INCOME_CLASS'].update(ic()[6])
        elif values['CM'] == "Alegria":
            window['FIELD_OFFICER'].update(fo()[3][0])
            window['INCOME_CLASS'].update(ic()[6])
        elif values['CM'] == "Bacuag":
            window['FIELD_OFFICER'].update(fo()[3][1])
            window['INCOME_CLASS'].update(ic()[6])
        elif values['CM'] == "Burgos":
            window['FIELD_OFFICER'].update(fo()[3][2])
            window['INCOME_CLASS'].update(ic()[7])
        elif values['CM'] == "Claver":
            window['FIELD_OFFICER'].update(fo()[3][3])
            window['INCOME_CLASS'].update(ic()[3])
        elif values['CM'] == "Dapa":
            window['FIELD_OFFICER'].update(fo()[3][4])
            window['INCOME_CLASS'].update(ic()[5])
        elif values['CM'] == "Del Carmen":
            window['FIELD_OFFICER'].update(fo()[3][5])
            window['INCOME_CLASS'].update(ic()[6])
        elif values['CM'] == "General Luna":
            window['FIELD_OFFICER'].update(fo()[3][6])
            window['INCOME_CLASS'].update(ic()[6])
        elif values['CM'] == "Gigaquit":
            window['FIELD_OFFICER'].update(fo()[3][7])
            window['INCOME_CLASS'].update(ic()[5])
        elif values['CM'] == "Mainit":
            window['FIELD_OFFICER'].update(fo()[3][8])
            window['INCOME_CLASS'].update(ic()[5])
        elif values['CM'] == "Malimono":
            window['FIELD_OFFICER'].update(fo()[3][9])
            window['INCOME_CLASS'].update(ic()[6])
        elif values['CM'] == "Pilar":
            window['FIELD_OFFICER'].update(fo()[3][10])
            window['INCOME_CLASS'].update(ic()[6])
        elif values['CM'] == "Placer":
            window['FIELD_OFFICER'].update(fo()[3][11])
            window['INCOME_CLASS'].update(ic()[5])
        elif values['CM'] == "San Benito":
            window['FIELD_OFFICER'].update(fo()[3][12])
            window['INCOME_CLASS'].update(ic()[7])
        elif values['CM'] == "San Francisco":
            window['FIELD_OFFICER'].update(fo()[3][13])
            window['INCOME_CLASS'].update(ic()[6])
        elif values['CM'] == "San Isidro":
            window['FIELD_OFFICER'].update(fo()[3][14])
            window['INCOME_CLASS'].update(ic()[6])
        elif values['CM'] == "Sison":
            window['FIELD_OFFICER'].update(fo()[3][15])
            window['INCOME_CLASS'].update(ic()[6])
        elif values['CM'] == "Socorro":
            window['FIELD_OFFICER'].update(fo()[3][16])
            window['INCOME_CLASS'].update(ic()[5])
        elif values['CM'] == "Sta. Monica":
            window['FIELD_OFFICER'].update(fo()[3][17])
            window['INCOME_CLASS'].update(ic()[6])
        elif values['CM'] == "Tagana-an":
            window['FIELD_OFFICER'].update(fo()[3][18])
            window['INCOME_CLASS'].update(ic()[6])
        elif values['CM'] == "Tubod":
            window['FIELD_OFFICER'].update(fo()[3][19])
            window['INCOME_CLASS'].update(ic()[6])
        elif values['CM'] == "Surigao City":
            window['FIELD_OFFICER'].update(fo()[3][20])
            window['INCOME_CLASS'].update(ic()[4])
        elif values['CM'] == "Barobo":
            window['FIELD_OFFICER'].update(fo()[4][0])
            window['INCOME_CLASS'].update(ic()[4])
        elif values['CM'] == "Bayabas":
            window['FIELD_OFFICER'].update(fo()[4][1])
            window['INCOME_CLASS'].update(ic()[6])
        elif values['CM'] == "Bislig City":
            window['FIELD_OFFICER'].update(fo()[4][2])
            window['INCOME_CLASS'].update(ic()[4])
        elif values['CM'] == "Cagwait":
            window['FIELD_OFFICER'].update(fo()[4][3])
            window['INCOME_CLASS'].update(ic()[5])
        elif values['CM'] == "Cantilan":
            window['FIELD_OFFICER'].update(fo()[4][4])
            window['INCOME_CLASS'].update(ic()[3])
        elif values['CM'] == "Carmen":
            window['FIELD_OFFICER'].update(fo()[4][5])
            window['INCOME_CLASS'].update(ic()[6])
        elif values['CM'] == "Carrascal":
            window['FIELD_OFFICER'].update(fo()[4][6])
            window['INCOME_CLASS'].update(ic()[5])
        elif values['CM'] == "Cortes":
            window['FIELD_OFFICER'].update(fo()[4][7])
            window['INCOME_CLASS'].update(ic()[5])
        elif values['CM'] == "Hinatuan":
            window['FIELD_OFFICER'].update(fo()[4][8])
            window['INCOME_CLASS'].update(ic()[3])
        elif values['CM'] == "Lanuza":
            window['FIELD_OFFICER'].update(fo()[4][9])
            window['INCOME_CLASS'].update(ic()[5])
        elif values['CM'] == "Llanga":
            window['FIELD_OFFICER'].update(fo()[4][10])
            window['INCOME_CLASS'].update(ic()[5])
        elif values['CM'] == "Lingig":
            window['FIELD_OFFICER'].update(fo()[4][11])
            window['INCOME_CLASS'].update(ic()[3])
        elif values['CM'] == "Madrid":
            window['FIELD_OFFICER'].update(fo()[4][12])
            window['INCOME_CLASS'].update(ic()[5])
        elif values['CM'] == "Marihatag":
            window['FIELD_OFFICER'].update(fo()[4][13])
            window['INCOME_CLASS'].update(ic()[4])
        elif values['CM'] == "San Agustin":
            window['FIELD_OFFICER'].update(fo()[4][14])
            window['INCOME_CLASS'].update(ic()[5])
        elif values['CM'] == "San Miguel":
            window['FIELD_OFFICER'].update(fo()[4][15])
            window['INCOME_CLASS'].update(ic()[2])
        elif values['CM'] == "Tagbina":
            window['FIELD_OFFICER'].update(fo()[4][16])
            window['INCOME_CLASS'].update(ic()[3])
        elif values['CM'] == "Tago":
            window['FIELD_OFFICER'].update(fo()[4][17])
            window['INCOME_CLASS'].update(ic()[3])
        elif values['CM'] == "Tandag City":
            window['FIELD_OFFICER'].update(fo()[4][18])
            window['INCOME_CLASS'].update(ic()[7]) """