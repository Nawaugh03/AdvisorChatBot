import mysql.connector
"""
Making it a class for later :)
class Cirriculum_Manager:
    def __init__ (self,host=None,user=None,password=None,dbname=None,curriculums=[()]):
        self.dbname=dbname
        self.host=host
        self.password=password
        self.curriculums=curriculums
"""
mydb = mysql.connector.connect(
                    host='localhost', # Change these strings to 
                    user='root',      #
                    password='1234',  # 
                    database='test'   # existing db name
                    )
mycursor = mydb.cursor()

inputvalue="""INSERT INTO list(course, number, title, credits) VALUES
                      ('ENGL','203','Fundamentals of Contemporary Speech','3'),
                      ('FREN','101','Fundamentals of French I','3'),
                      ('FREN','102','Fundamentals of French II','3'),
                      ('SPAN','101','Fundamentals of Spanish I','3'),
                      ('SPAN','102','Fundamentals of Spanish II','3'),
                      ('CHIN','101','Fundamentals of Chinese I','3'),
                      ('CHIN','102','Fundamentals of Chinese II','3'),
                      ('ARAB','101','Fundamentals of Arabic I','3'),
                      ('ARAB','102','Fundamentals of Arabic II','3'),
                      ('JAPN','101','Fundamentals of Japanese I','3'),
                      ('JAPN','102','Fundamentals of Japanese II','3'),
                      ('ECON','201','Principles of Economics(Macro)','3'),
                      ('ECON','201H','Principles of Economics(Macro) Honors','3'),
                      ('ECON','202','Principles of Economics(Micro)','3'),
                      ('ECON','202H','Principles of Economics(Micro) Honors','3'),
                      ('GEOG','101','The World Geography I','3'),
                      ('GEOG','102','The World Geography II','3'),
                      ('HIST','101','History of World Civilization I','3'),
                      ('HIST','102','History of World Civilization II','3'),
                      ('HIST','111H','History of World Civilization I Honors','3'),
                      ('HIST','112H','History of World Civilization II Honors','3'),
                      ('POLI','200','Introduction of American Government','3'),
                      ('POLI','200H','Introduction of American Government Honors','3'),
                      ('POLI','342','Urban Politics','3'),
                      ('SOCI','101','Introduction to Sociology','3'),
                      ('SOCI','111H','Introduction to Sociology Honors','3'),
                      ('CRJS','101','Introduction to Criminal Justice','3'),
                      ('HUEC','203','Human Development: A Lifespan Perspective','3'),
                      ('HUEC','220','Perspectives on Aging','3'),
                      ('HUEC','361','Contemporary Family Issues','3'),
                      ('PSYC','101','Introduction to Psychology','3'),
                      ('SOCI','201','Social Problems','3'),
                      ('SOWK','200','Social Work','3'),
                      ('SOCI','200H','Social Problems Honors','3'),
                      ('BIOL','111','Principles of Biology I','3'),
                      ('BIOL','113','Principles of Biology I Laboratory','1'),
                      ('BIOL','112','Principles of Biology II','3'),
                      ('BIOL','114','Principles of Biology II Laboratory','1'),
                      ('CHEM','111','Principles of Chemistry I','3'),
                      ('CHEM','113','Principles of Chemistry I Laboratory','1'),
                      ('CHEM','112','Principles of Chemistry II','3'),
                      ('CHEM','114','Principles of Chemistry II Laboratory','1'),
                      ('MATH','112','Calculus I','4'),
                      ('ENGL','101','Basic Composition I','3'),
                      ('ENGL','101H','Basic Composition I(Honors)','3'),
                      ('ENGL','102','Basic Composition II','3'),
                      ('ENGL','102H','Basic Composition II','3'),
                      ('ENGL','305/W','Twchnical Writing','3'),
                      ('ENGL','310/W','Advanced Composition','3'),
                      ('CSDP','100','Computer Science Orientation','1'),
                      ('EXSC','111','Personalized Health Fitness','3'),
                      ('CSDP','221','Introduction to Computer Programming','3'),
                       ('CSDP','222','Advabced Programming','3'),
                       ('CSDP','250','Data Structures','3'),
                       ('CSDP','301','Computer Organization & Assembly Language Programming','3'),
                       ('CSDP','305','Software Engineering I','3'),
                       ('CSDP','332','Internet Programming','3'),
                       ('CSDP','351','Computer Architecture','3'),
                       ('CSDP','390','Social, Ethical and Legal Isssues in Computer Science','3'),
                       ('CSDP','398','Computer Language Topics A: Java','3'),
                       ('CSDP','399','Computer Langauge Topics B: UNIX','3'),
                       ('CSDP','401','Operating Systems','3'),
                       ('CSDP','402','Computer Networks','3'),
                       ('CSDP','403','Computer Language Theory','3'),
                       ('CSDP','404','Database Management Systems','3'),
                       ('CSDP','450','Algorithms and Data Structures','3'),
                       ('CSDP','490','Senior Design Project','3'),
                       ('CSDP','341','Numerical Analysis I','3'),
                       ('CSDP','395','Internship','3'),
                       ('CSDP','405','Software Engineering II','3'),
                       ('CSDP','431','Data Warehosuing and Data Mining','3'),
                       ('CSDP','442','Numerical Analysis II','3'),
                       ('CSDP','498','Selected Topics in Computer Science A','3'),
                       ('CSDP','499','Selected Topics in Computer Science B','3'),
                       ('MATH','350','Linear Programming','3'),
                       ('MATH','211','Calculus II','4'),
                       ('MATH','232','Introduction to Linear Algebra','3'),
                       ('MATH','309','Introduction to Probability','3'),
                       ('MATH','323','Introduction to Discrete Structures','3'),
                       ('MATH','360','Statistics for Scientist','3'),
                       ('ACCT','201','Introductory Financial Accounting','3'),
                       ('ACCT','202','Introductory Corporate & Managerial Accounting/Hybrid','3'),
                       ('MKTG','308','Principles of Marketing','3'),
                       ('FINA','340','Financial Management','3'),
                       ('BUAD','302','Management and Organizational Behavior','3'),
                       ('MKTG','312','Sales Management','3'),
                       ('MKTG','314','Retail Management','3'),
                       ('MKTG','315','E-Commerce','3'),
                       ('MKTG','401','Advertising Management','3'),
                       ('MKTG','404','Consumer Behavior and Theory','3'),
                       ('MKTG','410','Marketing Strategy and Policy','3'),
                       ('FINA','341','Investment and Security Analysis','3'),
                       ('FINA','440','Advanced Fiancial Management','3'),
                       ('FINA','441','Insurance and Business Risks','3'),
                       ('BUAD','242','The Lagal Enviornment for Business','3'),
                       ('BUAD','303','Advanced Organizational Behavior','3'),
                       ('BUAD','420','International Business','3');"""

#print(insert_Curriculum)
mycursor.execute(inputvalue)
mydb.commit()
#myresult=mycursor.fetchall()
#print(myresult)

#print(type('hi'))
