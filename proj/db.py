import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('SGLG.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create PROVINCE table
""" cursor.execute('''CREATE TABLE IF NOT EXISTS PROVINCE
                  (pID INTEGER PRIMARY KEY, PName TEXT UNIQUE)''') """

# Create MUNICIPALITY table
""" cursor.execute('''CREATE TABLE IF NOT EXISTS MUNICIPALITY
                  (mID INTEGER PRIMARY KEY, MName TEXT UNIQUE, pID INTEGER,
                  FOREIGN KEY (pID) REFERENCES PROVINCE(pID))''') """

# Create FIELD OFFICERS table
""" cursor.execute('''CREATE TABLE IF NOT EXISTS FIELD_OFFICERS
                  (foID INTEGER PRIMARY KEY, foName TEXT, mID INTEGER, pID INTEGER,
                  FOREIGN KEY (mID) REFERENCES MUNICIPALITY(mID),
                  FOREIGN KEY (pID) REFERENCES PROVINCE(pID))''') """

# Create INCOMECLASS table
""" cursor.execute('''CREATE TABLE IF NOT EXISTS INCOMECLASS
                  (iID INTEGER PRIMARY KEY, icName TEXT UNIQUE, mID INTEGER,
                  FOREIGN KEY (mID) REFERENCES MUNICIPALITY(mID))''') """

# Create CATEGORIES table
""" cursor.execute('''CREATE TABLE IF NOT EXISTS CATEGORIES
                  (cID INTEGER PRIMARY KEY, cName TEXT, mID INTEGER,
                  FOREIGN KEY (mID) REFERENCES MUNICIPALITY(mID))''') """

# Create MINIMUMREQUIREMENTS table
""" cursor.execute('''CREATE TABLE IF NOT EXISTS MINIMUMREQUIREMENTS
                  (mrID INTEGER PRIMARY KEY, mrName TEXT, cID INTEGER,
                  FOREIGN KEY (cID) REFERENCES CATEGORIES(cID))''') """

# Create FINANCIAL ADMINISTRATION AND SUSTAINABILITY table
""" cursor.execute('''CREATE TABLE FINANCIAL_AD_ANS (
    faID INTEGER PRIMARY KEY,
    auditOpinion TEXT CHECK(length(auditOpinion) <= 100),
    lguPosting TEXT CHECK(length(lguPosting) <= 200),
    dataTYPO TEXT CHECK(length(lguPosting) <= 10),
    aveLocalRevGrowth TEXT CHECK(length(aveLocalRevGrowth) <= 30),
    ntaUtilization TEXT CHECK(length(ntaUtilization) <= 30),
    performanceChallengeFund TEXT CHECK(length(performanceChallengeFund) <= 30),
    upload BLOB,  
    lguPCFradioBtn TEXT CHECK(length(lguPCFradioBtn) <= 200),
    fo_id INTEGER,  
    mun_id INTEGER, 
    c_id INTEGER,
    FOREIGN KEY (fo_id) REFERENCES FieldOfficers(foID),
    FOREIGN KEY (mun_id) REFERENCES Municipality(mID),
    FOREIGN KEY (c_id) REFERENCES Categories(cID)
    )''')  """

#CREATE USERS TABLE
""" cursor.execute('''
    CREATE TABLE IF NOT EXISTS USERS (
        UId INTEGER PRIMARY KEY,    -- Unique identifier for each user
        UName TEXT NOT NULL,        -- Username, required and of type text
        Password TEXT NOT NULL,     -- Password, required and of type text
        provinceId INTEGER,                -- Foreign key to the parent table
        municipalityId INTEGER,                -- Foreign key to the mentor table
        FOREIGN KEY (provinceId) REFERENCES PROVINCE(pID),  -- Foreign key constraint referencing PARENT_TABLE and PId
        FOREIGN KEY (municipalityId) REFERENCES MUNICIPALITY(mID)   -- Foreign key constraint referencing MENTOR_TABLE and MId
    )
''') """


# RENAME MUNICIPALITY table column mID
""" cursor.execute('''ALTER TABLE INCOMECLASS
RENAME COLUMN mID TO munID;
''') """

# Adding new MUNICIPALITY table column
cursor.execute('''ALTER TABLE INCOMECLASS
RENAME COLUMN mID TO munID;
''')

                  
# Commit changes to the database
conn.commit()

# Close the cursor and the connection
cursor.close()
conn.close()
