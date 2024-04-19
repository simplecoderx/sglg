import sqlite3
import sys, os
#main_py_path = r'C:/python_playground/project/proj/main.py'
#conn = main_py_path.conn
#from ...proj.main import munName as munName

#from main import munName

storage = []

""" conn2 = sqlite3.connect('SGLG.db')
cursor = conn2.cursor() """

class financialReq():
    def __init__(self, conn) -> None:
        self.conn = conn
        self.cursor = self.conn.cursor()
        self.mainHeadings = ("1.1 Most recent audit opinion is unmodified or qualified plus 30% of recommendations fully complied with",
                        "1.2 The LGU fully complied with posting in (please tick all applicable items)",
                        "1.3 Average local revenue growth of LGU from CYs 2020 to 2022 (please supply information)",
                        "1.4 Utilization percentage of the 20% component of the National Tax Allotment for local development projects (please supply information)",
                        "1.5 Full utilization of all Performance Challenge Funds released in CY 2019 and earlier, if applicable"
                        )
        self.subHeadings = ["Most Recent Audit Opinion (CY2021 or CY2022)",
                            "Percentage of fully-complied recommendations (please supply information)",
                            "If data in the provided NGA database contains typographical errors, LGU submitted a portion of the Annual Audit Report "
                                "that will support the correct data (i.e. Executive Summary and Status of implementation of prior year's audit recommendations)",
                            ]
        self.sectionTwoText = ("Full Disclosure Policy Portal for CY 2022 2nd to 4th Quarters, and CY 2023 1st Quarter posting period documents", 
                           "Three (3) conspicuous places for CY 2022 2nd to 4th quarters, and CY 2023 1st Quarter posting period documents (based on accomplished Form 2E: DILG Field Office)", 
                           "Timely submission of  FY 2022-Q4 LIFT System Reports (SRE and QRRPA)",
                           "None of the above")
        self.sectionFiveSubHeadings = ("All the received funds are fully liquidated and disbursed, with no unobligated balances.", 
                                       "All the received funds are fully liquidated and disbursed, with all unobligated balances reverted back to the National Treasury.",
                                       "There are received funds that are not fully liquidated and disbursed.",
                                       "There are unobligated balances that are yet to be reverted back to the National Treasury.",
                                       "The LGU is included in the list of LGUs with pending PCF-funded projects from DILG-BLGD."
                                       )
        #self.cm = munName
        
    def displayHeadings(self, val):
        print(val)
        return self.mainHeadings[val]
        #print(main3Headings[val])
        #return self.mainHeadings[0]
    def displaySubHeadings(self, val):
        print(val)
        return self.subHeadings[val]

    def displaySectionTwoChoices(self, val):
        return self.sectionTwoText[val]
    
    def displaySectionFiveSubHeadings(self, val):
        return self.sectionFiveSubHeadings[val]
    
    def controllerFinancialReq(self): #def controllerFinancialReq(self, province, cm):
        """ munWithFinancialReq = ("Nasipit", "Butuan City", "Carmen")
        for i in munWithFinancialReq:
            if cm in munWithFinancialReq:
                print(province, cm, "this is from unEmptyLocality of controllerFinancialRe fass")
                return True
            else:
                return False """
        print("its working")
        """ query = "SELECT COUNT(*) FROM CATEGORIES WHERE mID IN (SELECT mID FROM MUNICIPALITY WHERE MName = ?)"
        self.cursor.execute(query, (cm,))
        count = self.cursor.fetchone()[0]
        return count > 0 """
            
    def handle_unmodified(e, val, cm):
        """ print(e, val["Unmodified"], cm)
        unmodified_value = val.get("Unmodified")  # Get the value from the Unmodified radio button
        print(e, unmodified_value, cm)
        # Add your logic here for handling the Unmodified event
        query = "INSERT INTO FINANCIAL_AD_ANS (auditOpinion) VALUES (?)"
        cursor.execute(query, (unmodified_value,))
        print("Successfully inserted into the table.")
        conn.commit() """
        print("this is handle unmodified")
        print(e, val["Unmodified"], cm)
        storage = val
        print(storage, "this is storage")

    def handle_qualified(e, val):
        print(e, val["Qualified"])
        # Add your logic here for handling the Unmodified event

    def handle_dno(e, val):
        print(e, val["DNO"])


    def handle_adverse(e, val):
        print(e, val["ADVERSE"]) 


    def handle_naar(e, val):
        print(e, val["NAAR"])   


    def handle_upload(e, val):
        print(e, val["UPLOAD"]) 


    def handle_typo(e, val):
        print(e, val["TYPO"])  


    def handle_ok1(e, val):
        print(e, val["OK1"])  


    def handle_ok2(e, val):
        print(e, val["OK2"])   


    def handle_notok1(e, val):
        print(e, val["NOTOK1"]) 


    def handle_notok2(e, val):
        print(e, val["NOTOK2"])


    def handle_notok3(e, val):
        print(e, val["NOTOK3"]) 

    def handle_coaRecommendation(e, val):
        print(e, val) 
        coa_recommendation = val
        return coa_recommendation
    
    def get_answers(self, auditopinion, percentageOfFullyCompliedReco, oneDropdown, lguFullyComplied, averageLRG, utilization, beneficiaryOfPCF, yesPCF):
    #def get_answers(self):
        print(self.cm, "this is get answers")

"""     def unEmptyLocality(province, cm):
        print(province, cm, "this is from unEmptyLocality of fass") """

""" a = financialReq()
a.displayHeadings(0) """
