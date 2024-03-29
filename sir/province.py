import PySimpleGUI as sg
from FAS import FAS
from DP import DP
from minimum_requirements import mr

sg.LOOK_AND_FEEL_TABLE['Theme'] = {'BACKGROUND': '#292929',
                                    'TEXT': '#009bff',
                                    'INPUT': '#ffffff',
                                    'TEXT_INPUT': '#000000',
                                    'SCROLL': '#ffffff',
                                    'BUTTON': ('#5cfd46', '#151515'),
                                    'PROGRESS': ('#01826B', '#D0D0D0'),
                                    'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                    }

sg.theme("Default1")
sg.set_options(font=("yu Gothic u1",10))

dilg_logo = [[sg.Image("logo_FINAL1.png")]]
sglg_logo = [[sg.Image("SGLG_LOGO.png")]]

header_frame = [[sg.Text("SGLG Regional Monitoring and Compliance Tracking System",font=("Courier New",20),justification="center")]]

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
                       ['Jane G. Moreno','Joselito S. Ramos','Julius R. Carrido','Mayonito Fernan E. Ramos','Mark Anthony C. Obani','Julieto O. Curayag','Merril B. Espenido','Marichelle O. Gultiano','Sharamae I. Dalogdog','Bella C. Decena','Ian Reigh M. Elimanco','Ferdy Benigno R. Avila','Noel L. Arreza','Ernie Y. Gultiano','Redgy V. Panilan','Ma. Rosario M. Ambray','Roel J. Camba','Arman M. Decena','Marlon C. Monterola']]

def cm():
    result = []
    for cm in adn_array:
        result.append(cm)
    return result
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

locality = [[sg.Text("Province: ",size=12),sg.Combo(['Agusan Del Norte','Agusan Del Sur','Surigao Del Norte','Surigao Del Sur','Province of Dinagat Islands'],key='PROVINCE',enable_events=True,size=23)],
            [sg.Text("City/Municipality: ",size=12),sg.Combo([],key="CM",size=23,enable_events=True)],
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
