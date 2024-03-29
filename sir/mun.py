class Municipalities:
    def __init__(self) -> None:
        self.municipalities = {'Agusan del Norte': ['Buenavista','Cabadbaran City','Carmen','Jabonga','Kitcharao','Las Nieves','Magallanes','Nasipit','RTR','Santiago','Tubay','Butuan City', 'One'],
                  'Agusan del Sur': ['Bayugan City','Bunawan','Esperanza','La Paz','Loreto','Properidad','Rosario','San Francisco','San Luis','Sibagat','Sta. Josefa','Talacogon','Trento','Veruela'],
                  'Surigao del Norte': ['Alegria','Bacuag','Burgos','Claver','Dapa','Del Carmen','General Luna','Gigaquit','Mainit','Malimono','Pilar','Placer','San Benito','San Francisco','San Isidro','Sison','Socorro','Sta. Monica','Tagana-an','Tubod','Surigao City'],
                  'Surigao del Sur': ['Barobo','Bayabas','Bislig City','Cagwait','Cantilan','Carmen','Carrascal','Cortes','Hinatuan','Lanuza','Llanga','Lingig','Madrid','Marihatag','San Agustin','San Miguel','Tagbina','Tago','Tandag City'],
                  'Province of Dinagat Island': ['Basilisa','Cagdianao','Dinagat','Libjo','Loreto','San Jose','Tubajon']}

    def get_municipalities(self, province):
        if province in self.municipalities:
            return self.municipalities[province]
        else:
            return None
        
def main():
    municipalities = Municipalities()
    province = 'Agusan del Norte'
    result = municipalities.get_municipalities(province)
    if result:
        print(result)
    else:
        print("Province not Found.")

if __name__ == "__main__":
    main()