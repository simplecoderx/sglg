class emptyCategories:
    def __init__(self) -> None:
        self.categories = ("1. Financial Administration and Sustainability", "2. Disaster Preparedness", "3. Social Protection and Sensitivity",
                           "4. Health Compliance and Responsiveness", "5. Sustainable Education", "6. Business-Friendliness and Competitiveness",
                            "7. Safety, Peace and Order","8. Environmental Management", "9. Tourism, Heritage Dev't, Culture and Arts", "10. Youth Development" )
        
    def displayHeaders(self):
        print(self.categories[0])

a = emptyCategories()
a.displayHeaders()