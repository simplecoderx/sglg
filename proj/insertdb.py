import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('SGLG.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Insert data into the PROVINCE table
#cursor.execute("INSERT INTO PROVINCE (PName) VALUES ('Agusan Del Norte'), ('Agusan Del Sur'), ('Surigao Del Norte'), ('Surigao Del Sur'), ('Province of Dinagat Islands')")

# Insert data into the MUNICIPALITY table
#cursor.execute("INSERT INTO MUNICIPALITY (MName, pID) VALUES ('Buenavista', 1), ('Carmen', 1), ('Nasipit', 1), ('Butuan', 1)")

# Insert data into the FIELD OFFICERS table
#cursor.execute("INSERT INTO FIELD_OFFICERS (foName, mID, pID) VALUES ('Lynn', 2, 1)")
#cursor.execute("INSERT INTO FIELD_OFFICERS (foName, mID, pID) VALUES ('Jane', 1, 1)")
# Add more INSERT statements for other field officers

# Insert data into the INCOMECLASS table
#cursor.execute("INSERT INTO INCOMECLASS (icName, mID) VALUES ('5th Class', 2)")
#cursor.execute("INSERT INTO INCOMECLASS (icName, mID) VALUES ('CC', 2)")
# Add more INSERT statements for other income classes

# Insert data into the CATEGORIES table
#cursor.execute("INSERT INTO CATEGORIES (cName, mID) VALUES ('1. Financial Administration and Sustainability', 2)")
#cursor.execute("INSERT INTO CATEGORIES (cName, mID) VALUES ('Category2', 2)")
# Add more INSERT statements for other categories

# Insert data into the MINIMUMREQUIREMENTS table
#cursor.execute("INSERT INTO MINIMUMREQUIREMENTS (mrName, cID) VALUES ('Requirement1', 1)")
#cursor.execute("INSERT INTO MINIMUMREQUIREMENTS (mrName, cID) VALUES ('Requirement2', 2)")
# Add more INSERT statements for other minimum requirements

# Insert data into the FINANCIAL ADMINISTRATION AND SUSTAINABILITY table
#cursor.execute("INSERT INTO MINIMUMREQUIREMENTS (faID, auditOpinion, lguPosting, dataTYPO, aveLocalRevGrowth, ntaUtilization, performanceChallengeFund, upload, lguPCFradioBtn, fo_id, mun_id, c_id) VALUES ('Requirement1', 1)")
""" cursor.execute('''
    INSERT INTO FINANCIAL_AD_ANS (
        faID, 
        auditOpinion, 
        lguPosting, 
        dataTYPO, 
        aveLocalRevGrowth, 
        ntaUtilization, 
        performanceChallengeFund, 
        upload, 
        lguPCFradioBtn, 
        fo_id, 
        mun_id, 
        c_id
    ) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 
            (SELECT foID FROM FIELD_OFFICERS WHERE foName = ?),   -- fo_id
            (SELECT mID FROM MUNICIPALITY WHERE MName = ?),       -- mun_id
            (SELECT cID FROM CATEGORIES WHERE cName = ?))         -- c_id
''', (
    '1',                   # faID (String or Integer)
    'Unmodified',          # auditOpinion (Integer)
    'None',                # lguPosting (String)
    'Yes',                 # dataTYPO (String)
    '100%',                # aveLocalRevGrowth (String)
    '50%',                 # ntaUtilization (String)
    'No',                  # performanceChallengeFund (String)
    b'upload_data',        # upload (BLOB data)
    "There are received funds that are not fully liquidated and disbursed.",           # lguPCFradioBtn (String)
    'Lynn',                # foName (String)
    'Carmen',              # MName (String)
    "1. Financial Administration and Sustainability"                   # cName (String)
)) """


#Insert data to Users
cursor.execute("INSERT INTO USERS (UName, Password, provinceId, municipalityId) VALUES ('Carmen', '123', 1, 2)")


# Add more INSERT statements for other FINANCIAL ADMINISTRATION AND SUSTAINABILITY table


# Commit changes to the database
conn.commit()

# Close the cursor and the connection
cursor.close()
conn.close()
