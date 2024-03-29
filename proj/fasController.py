class financialReq():
    def __init__(self) -> None:
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
    
    def controllerFinancialReq(province, cm):
        munWithFinancialReq = ("Nasipit", "Butuan City", "Carmen")
        for i in munWithFinancialReq:
            if cm in munWithFinancialReq:
                print(province, cm, "this is from unEmptyLocality of controllerFinancialRe fass")
                return True
            else:
                return False
            
    def handle_unmodified(e, values):
        print(e, values["Unmodified"])
        # Add your logic here for handling the Unmodified event

    def handle_qualified(e, values):
        print(e, values["Qualified"])
        # Add your logic here for handling the Unmodified event

    def handle_dno(e, values):
        print(e, values["Qualified"])
    def handle_adverse(e, values):
        print(e, values["Qualified"])        
    def handle_naar(e, values):
        print(e, values["Qualified"])        
    def handle_upload(e, values):
        print(e, values["Qualified"])        
    def handle_typo(e, values):
        print(e, values["Qualified"])        
    def handle_ok1(e, values):
        print(e, values["Qualified"])        
    def handle_ok2(e, values):
        print(e, values["Qualified"])        
    def handle_notok1(e, values):
        print(e, values["Qualified"])        
    def handle_notok2(e, values):
        print(e, values["Qualified"])        
    def handle_notok3(e, values):



"""     def unEmptyLocality(province, cm):
        print(province, cm, "this is from unEmptyLocality of fass") """

""" a = financialReq()
a.displayHeadings(0) """
