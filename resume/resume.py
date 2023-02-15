from pathlib import Path
import streamlit as st
from PIL import Image
import pandas as pd 


video_file = open('portfolio.mp4', 'rb')
video_bytes = video_file.read()

video_file = open('wego.mp4', 'rb')
video_byte = video_file.read()

with open("Aakash.pdf","rb") as pdf_file:
  PDFbyte=pdf_file.read()

with open("Calculator_AakashNambiar.ipynb","rb") as py_file:
  PY_file1=py_file.read()

with open("Rock-Paper-Scissors_Aakash Nambiar.ipynb","rb") as py_file2:
  PY_file2=py_file2.read()

with open("Xand0-AakashNambiar.ipynb","rb") as py_file3:
  PY_file3=py_file3.read()

data=pd.read_csv("winequality-red.csv")

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

def txt(a, b):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(f'`{b}`')

def txt1(a, b, c, d):
  col1, col2, col3, col4= st.columns([0.5,1,2,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)
  with col4:
    st.markdown(d)
  

rad=st.sidebar.radio("Navigation",["Summary","Educational Background","Skills","Data Science"])

if rad=="Summary":
  st.write("""
  # Aakash Madhu Nambiar
  ##### *Resume* 
  """)

  image = Image.open('photo.jpg')
  st.image(image, width=150)
    
  st.markdown('<div style="text-align: center;"> Summary', unsafe_allow_html=True  )
  st.info('''
 As a passionate Machine Learning and AI enthusiast with a strong foundation in statistical and predictive analysis, I am eager to bring my skills and continual desire for learning to a junior data scientist role in your organization. I am confident in my ability to work in diverse data situations and contribute to the company's growth while advancing my own knowledge and expertise as a data scientist. I believe that I have the drive and dedication to make a meaningful impact in this field and I am excited to take the next step in my career with your company.
 ''')


  # WORK EXPERIENCE
  st.markdown('''
### Work Experiences
''')
  st.markdown('''
#### Junior Structural Engineer
''')
  st.markdown("""
' **Jetwing Technologies**, Bangalore',
'2016-2018'
""")
 
  st.markdown("""
  Responsibilities: \n
  - Design and conceptualization of drone and quadcopter projects
  - Structural analysis of drone and quadcopter projects to ensure stability and reliability
  - Implementation of design solutions that meet requirements for weight, strength, and performance
  - Collaboration with cross-functional teams to ensure successful integration of mechanical, electrical, and software components
  - Conducting simulation and testing of prototypes to validate performance and resolve any issues
""")

  st.markdown('''
  #### Senior Software Engineer
  ''')
  st.markdown("""
  **Capgemini Brigade Metrolopolis**, Bangalore,
  '2018-2020' \n
  Responsibilities:\n
  ***The responsibilities involved in documenting aircraft manuals for the Bombardier Global 7500:***
  """)
  st.markdown("""
  - Documented aircraft manuals for the Bombardier Global 7500, including design specifications, drawings, and schematics to ensure compliance with original design during manufacturing and maintenance processes.
  - Assisted in documenting the structural components and individual components of the aircraft, including specifications and critical information for safe and efficient operation.
  - Prepared and compiled technical manuals for various systems and components of the aircraft, serving as a reference for maintenance personnel and pilots.
  - Continuously updated aircraft manuals to reflect changes in design, structure, and components, ensuring accuracy and relevance.
""")

  st.markdown("""___""")

  # EDUCATION

  st.markdown("""
  ### Education
  """)

  st.markdown("""
  #### EDURE: Data Science 
  """)
  st.markdown("""
  Trivandrum,
  August-2022-December 2022 \n
  - Intermediate course from Python Basics to Machine Learning. Program covered topics from Python Basics to Machine Learning, including data analysis, data visualization, Natural language processing and deployment of prediction models.
  - Acquired hands-on experience in data analysis, data visualization, and machine learning through completion of several projects as part of the program, setting a solid foundation in machine learning knowledge.
  """)

  st.markdown("""
  #### Bachelors in Engineering : Aeronautical Engineering
  ***MVJ College of Engineering Bangalore , 2011-2015*** \n
  Visveswaraya Univeristy \n
  *Aggregate Percentage* - `74%` \n
  *Rank* - `First Class with Distinction`
  """)

  st.markdown("""
  #### Christ Nagar Senior Secondary School
  ***CBSE , 12th Computer Science-Mathematics*** \n
  *Aggregate Percentage* - `82%`
  """)
  st.markdown("""
  #### Christ Nagar Senior Secondary School
  ***CBSE , 10th*** \n
  *Aggregate Percentage* - `87%`
  """)

  st.markdown("""
  :blue[This section of the resume only explains educational background pertaining to Data Science Job appliaction. Use the sidebar option to navigate to detailed educational background]
  """)

  st.markdown("""___""")

  st.markdown('''
  ### Skills
  ''')
  txt('Programming' ,'Python')
  txt('Data Analysis' ,'Pandas, Numpy')
  txt('Data Visualization' ,'Matplotlib,Seaborn')
  txt('Model Deployment' ,'Streamlit,Tknter')

  st.markdown("""___""")

  st.markdown("""
  ### Hobbies
  """)

  st.markdown("""
  Dedicated to personal growth and self-improvement through engaging in leisure activities such as reading, practicing martial arts, yoga, cartoon drawing, and poster making.
  """)
  st.markdown("""___""")

  st.markdown("""
  ### Languages
  """)

  st.markdown("""
  - English - Speak, Read and Write
  - Malayalam - Speak, Read and Write
  - Hindi - Speak, Read and Write
  - Tamil - Speak
  """)



if rad=="Educational Background":
  st.title("""
   Education Background
  """)
  st.markdown("""
  *This portion of my educational background encompasses all the courses I have taken, regardless of their relationship to Data Science and Machine Learning. This provides a complete view of my educational background and highlights the breadth of subjects I have studied. Additionally, it can demonstrate my capacity for learning new subjects and emphasize any transferable skills I have acquired.*
  """)

  st.markdown("""
  #### EDURE: Data Science 
  """)
  st.markdown("""
  Trivandrum,
  August-2022-December 2022 \n
  - Intermediate course from Python Basics to Machine Learning. Program covered topics from Python Basics to Machine Learning, including data analysis, data visualization, Natural language processing and deployment of prediction models.
  - Acquired hands-on experience in data analysis, data visualization, and machine learning through completion of several projects as part of the program, setting a solid foundation in machine learning knowledge.
  """)

  st.markdown("""
  #### Bachelors in Engineering : Aeronautical Engineering
  ***MVJ College of Engineering Bangalore , 2011-2015*** \n
  Visveswaraya Univeristy \n
  *Aggregate Percentage* - `74%` \n
  *Rank* - `First Class with Distinction`
  """)

  st.markdown("""
  #### Christ Nagar Senior Secondary School
  ***CBSE , 12th Computer Science-Mathematics*** \n
  *Aggregate Percentage* - `82%`
  """)
  st.markdown("""
  #### Christ Nagar Senior Secondary School
  ***CBSE , 10th*** \n
  *Aggregate Percentage* - `87%`
  """)

  st.markdown("""
  #### Bridge UX/UI
  ***2020, Bangalore***\n
  """)

  st.markdown("""
  - Acquired hands-on experience in the software development lifecycle, including web and mobile application development, heuristic evaluation, and the interview process.
  - Demonstrated proficiency through successful completion of a web or mobile application project
  """)

  st.markdown("""
  #### Extreme Media
  """)

  st.markdown("""
  ***JAIN_X University, 2021 Trivandrum***
  """)

  st.markdown("""
  - Completed a course in Graphic Design from JAIN_X University, Trivandrum in 2021. 
  - Educated in the use of tools such as Adobe Illustrator, Photoshop, After Effects, and CorelDraw.
  - Acquired skills in creating various graphic design elements including posters, templates, logos, illustrations, and motion graphics.
  - Achieved an A+ grade, demonstrating a high level of proficiency in graphic design.
  """)

  st.markdown("""
  ### Trinity NDT Engineers
  """)
  st.markdown("""
  ###### Technical service in Bengaluru, Karnataka, *2017*
  """)

  st.markdown("""
  - Completed an American Society for Non-Destructive Testing (ASNT) Level II Certification from Trinity Institute of NDT Technology, Bengaluru, Karnataka in 2017. 
  - Achieved an aggregate grade of 90 percentile in the certification, demonstrating a thorough understanding of Non-Destructive Testing (NDT) methods.
  - Acquired comprehensive knowledge in NDT methods, including techniques for testing without causing damage to the tested material.
  """)

if rad=="Skills":
  st.markdown('''
  ### Data Science Tools
  ''')
  txt('Programming' ,'Python')
  txt('Data Analysis' ,'Pandas, Numpy')
  txt('Data Visualization' ,'Matplotlib,Seaborn')
  txt('Model Deployment' ,'Streamlit,Tknter')
  txt('Natural Language Porcessing' ,'NLTK')
  st.markdown('''
  ### Aerospace Tools
  ''')
  txt('Design' ,'CATIA V5,Solid Edge,CAM')
  txt('Aircraft Structures' ,'GD&T, NASTRAN-PATRAN,ANSYS')
  txt('Technical Authoring' ,'Arbortext Editor,SAP')

  st.markdown('''
  ### Graphic Design and Animation
  ''')
  txt('Animation' ,'MAYA 3D')
  txt('Graphic designing' ,'Adobe Illustrator,Adobe photoshop,CorelDraw')
  txt('UX/UI' ,'Adobe XD')

  st.markdown("""
  ### Languages
  """)

  st.markdown("""
  - English - Speak, Read and Write
  - Malayalam - Speak, Read and Write
  - Hindi - Speak, Read and Write
  - Tamil - Speak
  """)

  st.markdown("""
  ### Sample Work
  """)
  st.markdown("""
  ***Below click for sample work on graphic design, UX/UI designs, posters, letter heads and sketches***
  """)
  st.download_button(
    label= "Download Graphic design work sample",
    data=PDFbyte,
    file_name="Aakash.pdf",
    mime='application/octet-stream'
  )

  st.markdown("""
  ***Here is compilation of few 3D animation clips created by me using Maya 3D software***
  """)

  st.video(video_bytes)
  st.video(video_byte)


if rad=="Data Science":

  st.title("Data Science and Machine Learning")
  st.markdown("""
Below are the projects I completed while learning Data Science and Machine Learning. Before delving into Data Science, it was crucial to have a solid understanding of basic Python programming. As a milestone in my learning journey. These projects helped me to gain hands-on experience in solving real-world problems using data and algorithms. The following are the Data Science and Machine Learning projects I worked on, each providing me with a unique challenge and opportunity to expand my skillset in these fields.

  """)

  st.markdown("""
  ## Data Science/Machine Learning Projects 
  """)

  txt1(":red[S.No]",':red[Projects]',':red[Summary]',':red[web-link]')
  txt1('1','Loan status prediction','Loan prediction analysis is the process of determining the likelihood that a loan applicant will repay a loan based on various factors.Various prediction models used and best accuracy model chosen for deployment.',"https://github.com/Amadhuna/LOAN")
  txt1('2','Credit card data analysis','A Customer Credit Card Information Dataset which can be used for Identifying Loyal Customers, Customer Segmentation, Targeted Marketing and other such use cases in the Marketing Industry. The K means model was used for creating the prediction model.',"https://github.com/Amadhuna/Credit-Card-Customer-Data")
  txt1('3','Employee Attrition analysis','Employee attrition classification is the process of categorizing employees based on the likelihood that they will leave their job, also known as employee turnover. Various prediction models used and best accuracy model chosen for deployment',"https://github.com/Amadhuna/Employee-Attrition")
  txt1('4','Customer behavior analysis','Customer behavior classification is the process of grouping customers based on their behavior, attitudes, and purchase patterns. This information can be used by companies to better understand their target market, identify profitable customer segments, and design more effective marketing strategies. Various prediction models used and best accuracy model was selected',"https://github.com/Amadhuna/Customer-Behaviour-Classification")
  txt1('5','Glass classification','A glass classification prediction model is a machine learning model that is used to predict the class or type of glass based on its physical and chemical properties. The goal of this type of model is to identify the class of glass accurately by analyzing the properties such as refractive index, sodium and magnesium oxide content, and density.',"https://github.com/Amadhuna/Glass")
  txt1('6','Income evaluation','Income evaluation prediction is the process of determining an individual likely income based on various factors. This can be used to predict the financial stability of individuals and make decisions about loan applications, insurance policies, and other financial products. Gaussian Naive Bayes model used.',"https://github.com/Amadhuna/Income-Evaluation")
  txt1('7','Bank Marketing','Bank marketing term deposit prediction is the process of determining the likelihood that a customer will subscribe to a term deposit product offered by a bank. Decision Tree Classifier was used for prediction.',"https://github.com/Amadhuna/Bank-Project")
  txt1('8','Graduation admission prediction','Graduate admission prediction is the process of determining the likelihood that a student will be admitted to a graduate program based on various factors. Various prediction models used and best accuracy model chosen for deployment',"https://github.com/Amadhuna/Graduate-Admission-Prediciton")
  txt1('9','Spam classifier','A spam classifier is a machine learning model that is designed to identify and categorize email messages as either spam (unsolicited and often fraudulent messages) or not spam (legitimate messages). The classifier can be trained on a large dataset of labeled email messages, and then make predictions on new, unseen messages. NLP model used',"https://github.com/Amadhuna/Spam_Classifier")
  txt1('11','Fake news classifier','A fake news classifier is a machine learning model that is designed to identify and categorize news articles or headlines as either real or fake. The classifier can be trained on a large dataset of news articles and their labels, and then make predictions on new, unseen articles.',"https://github.com/Amadhuna/Fake-News-Classiifer")
  txt1('12','Tweet sentiment analysis','Tweet sentiment analysis for flights refers to the process of determining the sentiment or emotion expressed in tweets related to flights. This can involve using natural language processing (NLP) and machine learning techniques to analyze the text of tweets and classify them as positive, negative, or neutral based on the sentiment expressed.',"https://github.com/Amadhuna/Tweet-Sentiment-Analysis")
  txt1('13','Airline passenger satisfaction','The aim of airline passenger satisfaction prediction is to provide airlines with valuable information that can help them improve their services and increase passenger satisfaction. Random Forest Model used.',"https://github.com/Amadhuna/Airline-Passenger-Satisfaction-Prediction")
  txt1('14','Drinking-Water-Potability','Drinking water potability refers to the quality of water that is safe for human consumption. Potability of drinking water is an important concern for public health, as contaminated water can cause a range of health problems, including diseases and illnesses. SVM model used.',"https://github.com/Amadhuna/Drinking-Water-Potability")
  txt1('15','Diabetes prediction','Diabetes prediction is the process of determining the likelihood that an individual will develop diabetes in the future based on various risk factors. SVM model used here',"https://github.com/Amadhuna/Diabetes-Prediction")
  txt1('16','Mobile price classification','Mobile price classification is the process of categorizing mobile phones into different price ranges based on various factors such as features, specifications, and brand. The goal is to classify mobile phones into different price ranges, such as budget, mid-range, and premium, based on their features and specifications.Random Forest model used here',"https://github.com/Amadhuna/Mobile-Price-Classification")
  txt1('17','Used car price prediction','The aim of used car price prediction is to provide a realistic estimate of the value of a pre-owned vehicle, which can be useful for buyers, sellers, and traders in the automotive industry. Multiple linear regression model is used here',"https://github.com/Amadhuna/User-car-Price-prediction")
  txt1('18','Gold Price Prediction','The Dataset contain gold prices (in USD) from 2001 to 2019. Our goal is to predict where the gold prices will be in the coming years. This is simple linear regression project',"https://github.com/Amadhuna/Gold-Price-Prediction")
  txt1('19','Payment fraud detection','Payment fraud occurs when someone steals another person payment information and uses it to make unauthorized transactions or purchases. The actual cardholder or owner of the payment information then notices their account being used for transactions or purchases they did not authorize, and raises a dispute. KNN model used for prediction',"https://github.com/Amadhuna/Payment-Fraud-Detection")
  txt1('20','Heart-Failure-Prediction','People with cardiovascular disease or who are at high cardiovascular risk (due to the presence of one or more risk factors such as hypertension, diabetes, hyperlipidaemia or already established disease) need early detection and management wherein a machine learning model can be of great help. KNN model used for prediciton',"https://github.com/Amadhuna/Heart-Failure-Prediction")
  txt1('21','Mall-Customers-Clustering','You are owing a supermarket mall and through membership cards , you have some basic data about your customers like Customer ID, age, gender, annual income and spending score. Spending Score is something you assign to the customer based on your defined parameters like customer behavior and purchasing data. K means model was used to create prediction',"https://github.com/Amadhuna/Mall-Customers-Clustering")
 
  st.markdown("""
  ### Python Projects
  """)
  st.markdown("""
   ###### 1.  Calculator
  """)
  st.markdown("""
  Created a simple basic calculator that could perform basic arithmetic functions like addition, subtraction, multiplication. \n
  Tools used - :red[Jupyter Notebook, Tkinter]
  """)

  st.image("Calculator.png")
  st.download_button(
    label= "Download Calculator files",
    data=PY_file1,
    file_name="Calculator_AakashNambiar.ipynb",
    mime='application/octet-stream'

  )

  st.markdown("""
   ###### 2.  Tic Tac Toe
  """)
  st.markdown("""
  Created tic-tac-toe game in Python. Used the Tkinter tool kit from the Python standard library to create the game’s GUI. \n
  Tools used - :red[Jupyter Notebook, Tkinter]
  """)

  st.image("TICTACTOE.png")
  st.download_button(
    label= "Download Game files",
    data=PY_file3,
    file_name="Xand0-AakashNambiar.ipynb",
    mime='application/octet-stream'

  )

  st.markdown("""
   ###### 3.  Rock Paper Scissors
  """)
  st.markdown("""
  Created Rock Paper Scissors game in Python. This game is one player game, the other player being the computer \n
  Tools used - :red[Jupyter Notebook]
  """)

  st.download_button(
    label= "Download Game files",
    data=PY_file2,
    file_name="Rock-Paper-Scissors_Aakash Nambiar.ipynb",
    mime='application/octet-stream'
  )
 