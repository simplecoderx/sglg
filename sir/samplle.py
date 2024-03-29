""" import PySimpleGUI as sg

layout = [[sg.Button('Hello')]]

window = sg.Window('Demo', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'Hello':
        print('Hello, World!')

window.close()

# Output:
# 'Hello, World!'
 """


adn_array = [['Buenavista','Cabadbaran City','Carmen','Jabonga','Kitcharao','Las Nieves','Magallanes','Nasipit','RTR','Santiago','Tubay','Butuan City'],
             ['Bayugan City','Bunawan','Esperanza','La Paz','Loreto','Properidad','Rosario','San Francisco','San Luis','Sibagat','Sta. Josefa','Talacogon','Trento','Veruela'],
             ['Basilisa','Cagdianao','Dinagat','Libjo','Loreto','San Jose','Tubajon'],
             ['Alegria','Bacuag','Burgos','Claver','Dapa','Del Carmen','General Luna','Gigaquit','Mainit','Malimono','Pilar','Placer','San Benito','San Francisco','San Isidro','Sison','Socorro','Sta. Monica','Tagana-an','Tubod','Surigao City'],
             ['Barobo','Bayabas','Bislig City','Cagwait','Cantilan','Carmen','Carrascal','Cortes','Hinatuan','Lanuza','Llanga','Lingig','Madrid','Marihatag','San Agustin','San Miguel','Tagbina','Tago','Tandag City']]


field_officer_array = [['Yul O. Guerta','Annabella O. Cadigal','Laarni Beauty C. Sepe','Jaimelyn S. Cobrado','Leslie Ann M. Bantasan','Myrna B. Libao','Maricel G. Torreon','Karolous Joseph A. Fuertes','Vincent Angelo M. Balansag','Jeffrey A. Ramo','Melchora L. Grana','Lolita S. Go'],
                       ['Alice B. Robles','Feliviv C. Cuanan','Atty. Daniel P. Longaquit','Sherwin C. Obien','Mary Nol P. Aban','Luth Edmund M. Apresto','Rena L. Naguita','Archie Rose V. Raza','Charles V. Lim Jr.','Maricel G. Dumanglas','Arturo O. Bombeo Jr.','Renelou F. Jaranilla','Jorem J. Luzon','Joemar S. Salmoro'],
                       ['Don Manuelo O. Patrimonio','Gretchen D. Jazon','Jecquel G. Cultura','Bryan F. Edulzura','Hazel Anne B. Plaza','Donna Dial D. Madelo','Desiree B. Bakit'],
                       ['Marilou E. Alovera','Welivie C. Diola','Jubilyn S. Blase','Jenita T. Ladres','Marjorie A. Dalagan','Ednon John E. Aparicio','Jacky A. Mellorin','Crisologo L. Virtudazo','Liza L. Montaner','Rosalina A. Sering','Nova D. Hilig','Roberto A. Reyna Jr.','Estela Marie M. Vallespin','Mary Jane C. Centino','Genalin C. Pegarro','Ian Jun A. Gesta','Wenefredo R. Lasala Jr.','Krisha Antonnette V. Cultura','Catherine A. Gealogo','Jimelyn H. Ballicud','Roberto E. Patayon'],
                       ['Jane G. Moreno','Joselito S. Ramos','Julius R. Carrido','Mayonito Fernan E. Ramos','Mark Anthony C. Obani','Julieto O. Curayag','Merril B. Espenido','Marichelle O. Gultiano','Sharamae I. Dalogdog','Bella C. Decena','Ian Reigh M. Elimanco','Ferdy Benigno R. Avila','Noel L. Arreza','Ernie Y. Gultiano','Redgy V. Panilan','Ma. Rosario M. Ambray','Roel J. Camba','Arman M. Decena','Marlon C. Monterola']]

""" main_2 = [[sg.Text("1.2 The LGU fully complied with posting in (please tick all applicable items)",text_color="#AF6F09")],
                [sg.Checkbox(New_text,key="CB_1")],
              [sg.Checkbox(new_text_2,key="CB_2")],
              [sg.Checkbox("Timely submission of  FY 2022-Q4 LIFT System Reports (SRE and QRRPA)")],
              [sg.Checkbox("None of the above")]] """

""" for i in adn_array:
    print (i, "\n") """


""" name = ['lyn', 'len', 'lin']
print(name[0])
name[0] = 'lynn gwapa'
print(name[0])
print(name) """

""" color = ('red', 'green', 'blue')
print(color[0])
color[0] = 'dilaw'
print(color[0])
print(color) """