municipalities = {'Agusan del Norte': ['Buenavista','Cabadbaran City','Carmen','Jabonga','Kitcharao','Las Nieves','Magallanes','Nasipit','RTR','Santiago','Tubay','Butuan City', 'One'],
                  'Agusan del Sur': ['Bayugan City','Bunawan','Esperanza','La Paz','Loreto','Properidad','Rosario','San Francisco','San Luis','Sibagat','Sta. Josefa','Talacogon','Trento','Veruela'],
                  'Surigao del Norte': ['Alegria','Bacuag','Burgos','Claver','Dapa','Del Carmen','General Luna','Gigaquit','Mainit','Malimono','Pilar','Placer','San Benito','San Francisco','San Isidro','Sison','Socorro','Sta. Monica','Tagana-an','Tubod','Surigao City'],
                  'Surigao del Sur': ['Barobo','Bayabas','Bislig City','Cagwait','Cantilan','Carmen','Carrascal','Cortes','Hinatuan','Lanuza','Llanga','Lingig','Madrid','Marihatag','San Agustin','San Miguel','Tagbina','Tago','Tandag City'],
                  'Province of Dinagat Island': ['Basilisa','Cagdianao','Dinagat','Libjo','Loreto','San Jose','Tubajon']}
provinces = {'Agusan Del Norte','Agusan Del Sur','Surigao Del Norte','Surigao Del Sur','Province of Dinagat Islands'}
""" for i in provinces:
    print(i) """

""" province = 'Agusan del Norte'
age = {'Peter': 5, 'John':7}
for i, j in municipalities.items():
    if i == province:
        print((j)) """

""" def cProvince(province, event):
    for i, j in municipalities.items():
        if i == province:
            print(i, province, "this is from demo2 cProvince")
            print((j)) """


    #def __init__(self, province, cityMunicipality, incomeClass, fieldOfficer, e ):
     #   self.province = province
      #  self.cityMunicipality = cityMunicipality
       # self.incomeClass = incomeClass
        #self.fieldOfficer = fieldOfficer


fieldOfficers = {'Agusan del Norte': {'a': 'Lynn', 'b': 'Jane', 'c': 'Jay'},
                'Agusan Del Sur': {'d': 'Lynn', 'e': 'Jane', 'f': 'Jay'},
                'Surigao Del Sur': {'g': 'Lynn', 'h': 'Jane', 'i': 'Jay'},
                'Surigao Del Norte': {'j': 'Lynn', 'k': 'Jane', 'l': 'Jay'},
                'Province of Dinagat Islands': {'m': 'Lynn', 'n': 'Jane', 'o': 'Jay'}}
""" 
for i, j, in fieldOfficers.items():
    #print(i,j)
    for k in fieldOfficers:
        print(k) """

""" print(fieldOfficers['Agusan del Norte']['a']) """
municipality = 'a'
province = 'Agusan del Norte'

field_officer = fieldOfficers.get(province, {}).get(municipality)

if field_officer:
    print(field_officer)
else:
    print("No Field Officer")
    