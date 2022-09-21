# -*- coding: utf-8 -*-
"""
@author: mirac
"""

import pandas as pd
import numpy as np
Data = pd.read_csv("StudentsPerformance.csv")


Data.head(n = 10)

Data.describe()


# missing data
Data.isnull().sum()


# Visualization of Data #######################################################
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 12))
plt.suptitle("Student Distribution",fontsize=35)

# Gender distribution
plt.subplot(2,2,1)
gender = Data["gender"].value_counts()
genderPie = plt.pie(gender , labels = gender.index,autopct='%1.1f%%',shadow=True, startangle=90, textprops={'fontsize': 12})
plt.title("Gender",fontsize=20)


# Parent education level
plt.subplot(2,2,2)
parent = Data["parental level of education"].value_counts()
parentPie = plt.pie(parent , labels = parent.index,autopct='%1.1f%%',shadow=True, startangle=90, textprops={'fontsize': 12})
plt.title("Parent Education Level",fontsize=20)


#Lunch
plt.subplot(2,2,3)
lunch = Data["lunch"].value_counts()
lunchPie = plt.pie(lunch , labels = lunch.index,autopct='%1.1f%%',shadow=True, startangle=90, textprops={'fontsize': 12})
plt.title("Lunch",fontsize=20)


# Those who go to the preparatory course and those who do not
plt.subplot(2,2,4)
course = Data["test preparation course"].value_counts()
coursePie = plt.pie(course , labels = course.index,autopct='%1.1f%%',shadow=True, startangle=90, textprops={'fontsize': 12})
plt.title("Test Preparation Course",fontsize=20)

plt.show()



##############################################################################
PLE = Data.groupby("parental level of education").mean()

x = np.arange(PLE.index.size)

fig, axs = plt.subplots(figsize=(13,9.5))

axs.bar(x + 0.0, PLE.iloc[:,0].values,0.20, label ="Math Score")
axs.bar(x + 0.2, PLE.iloc[:,1].values,0.20, label ="Reading Score")
axs.bar(x + 0.4, PLE.iloc[:,2].values,0.20, label ="Writing Score")

plt.xticks(rotation = 45)

axs.set_ylabel('Score',fontsize = 20)
axs.set_title('Student Exam Score Average by Parent Education Level',fontsize = 22)
axs.set_xticks(x)
axs.set_xticklabels(PLE.index,fontsize = 15)
axs.legend(fontsize = 12)

plt.show()




##############################################################################
LNCH = Data.groupby("lunch").mean()

x = np.arange(LNCH.index.size) 
fig, axs = plt.subplots(figsize=(10,10))

axs.bar(x + 0.0, LNCH.iloc[:,0].values,0.15, label ="Math Score")
axs.bar(x + 0.15, LNCH.iloc[:,1].values,0.15, label ="Reading Score")
axs.bar(x + 0.30, LNCH.iloc[:,2].values,0.15, label ="Writing Score")


axs.set_ylabel('Score',fontsize = 20)
axs.set_title('Student Exam Score by Lunch',fontsize = 22)
axs.set_xticks(x)
axs.set_xticklabels(LNCH.index,fontsize = 18)
axs.legend(fontsize = 10)

plt.show()



##############################################################################
CRS = Data.groupby("test preparation course").mean()

x = np.arange(course.index.size) 
fig, axs = plt.subplots(figsize=(10, 10))
axs.bar(x + 0.0, CRS.iloc[:,0].values,0.15, label ="Math Score")
axs.bar(x + 0.15, CRS.iloc[:,1].values,0.15, label ="Reading Score")
axs.bar(x + 0.30, CRS.iloc[:,2].values,0.15, label ="Writing Score")


axs.set_ylabel('Score',fontsize = 20)
axs.set_title('Average Score by Exam Preparation Course',fontsize = 22)
axs.set_xticks(x)
axs.set_xticklabels(["Yes","No"],fontsize = 18)
axs.legend(fontsize = 10)

plt.show()






##############################################################################
ETH = Data.groupby("race/ethnicity").mean()

x = np.arange(ETH.index.size)

fig, axs = plt.subplots(figsize=(12,8.5))

axs.bar(x + 0.0, ETH.iloc[:,0].values,0.20, label ="Math Score")
axs.bar(x + 0.2, ETH.iloc[:,1].values,0.20, label ="Reading Score")
axs.bar(x + 0.4, ETH.iloc[:,2].values,0.20, label ="Writing Score")

plt.xticks(rotation = 45)

axs.set_ylabel('Score',fontsize = 20)
axs.set_title("Student Exam Score Average by Ethnicity",fontsize = 22)
axs.set_xticks(x)
axs.set_xticklabels(ETH.index,fontsize = 15)
axs.legend(fontsize = 10)

plt.show()






##############################################################################
GND = Data.groupby("gender").mean()

x = np.arange(GND.index.size) 
fig, axs = plt.subplots(figsize=(10,10))
a = x
axs.bar(a + 0.0, GND.iloc[:,0].values,0.15, label ="Matematik başarısı")
axs.bar(a + 0.15, GND.iloc[:,1].values,0.15, label ="Okuma başarısı")
axs.bar(a + 0.30, GND.iloc[:,2].values,0.15, label ="Yazma başarısı")

plt.xticks(rotation = 45)

axs.set_ylabel('Score',fontsize = 20)
axs.set_title("Student Exam Success by Gender",fontsize = 22)
axs.set_xticks(x)
axs.set_xticklabels(["Female","Male"],fontsize = 18)
axs.legend(fontsize = 10)

plt.show()



##############################################################################
##############################################################################


# Math
plt.figure(figsize=(18, 18))
plt.suptitle("Score Distribution in the Mathematics Exam", fontsize=35)

#race/ethnicity
plt.subplot(3,3,1)
EBV1 = Data[Data["math score"] <= 40]["parental level of education"].value_counts()
EBV1_pie = plt.pie(EBV1 , labels = EBV1.index,autopct='%1.1f%%',shadow=True, startangle=90, textprops={'fontsize': 12})
plt.title("Parental level of education\nScore < 40",fontsize=15)


plt.subplot(3,3,4)
EBV2 = Data[Data["math score"] >= 70]["parental level of education"].value_counts()
EBV2_pie = plt.pie(EBV2 , labels = EBV2.index,autopct='%1.1f%%',shadow=True, startangle=90, textprops={'fontsize': 12})
plt.title("Score > 70",fontsize=15)


plt.subplot(3,3,7)
EBV3 = Data[Data["math score"] >= 95]["parental level of education"].value_counts()
EBV3_pie = plt.pie(EBV3 , labels = EBV3.index,autopct='%1.1f%%',shadow=True, startangle=90, textprops={'fontsize': 12})
plt.title("Score > 95",fontsize=15)


# lunch
plt.subplot(3,3,2)
EBV1 = Data[Data["math score"] <= 40]["lunch"].value_counts()
EBV1_pie = plt.pie(EBV1 , labels = EBV1.index,autopct='%1.1f%%',shadow=True, startangle=90, textprops={'fontsize': 12})
plt.title("Lunch\nScore < 40",fontsize=15)

plt.subplot(3,3,5)
EBV2 = Data[Data["math score"] >= 70]["lunch"].value_counts()
EBV2_pie = plt.pie(EBV2 , labels = EBV2.index,autopct='%1.1f%%',shadow=True, startangle=90, textprops={'fontsize': 12})
plt.title("Score > 70",fontsize=15)

plt.subplot(3,3,8)
EBV3 = Data[Data["math score"] >= 95]["lunch"].value_counts()
EBV3_pie = plt.pie(EBV3 , labels = EBV3.index,autopct='%1.1f%%',shadow=True, startangle=90, textprops={'fontsize': 12})
plt.title("Score > 95",fontsize=15)


# test preparation course
plt.subplot(3,3,3)
EBV1 = Data[Data["math score"] <= 40]["test preparation course"].value_counts()
EBV1_pie = plt.pie(EBV1 , labels = EBV1.index,autopct='%1.1f%%',shadow=True, startangle=90, textprops={'fontsize': 12})
plt.title("Test preparation course\nScore < 40",fontsize=15)

plt.subplot(3,3,6)
EBV2 = Data[Data["math score"] >= 70]["test preparation course"].value_counts()
EBV2_pie = plt.pie(EBV2 , labels = EBV2.index,autopct='%1.1f%%',shadow=True, startangle=90, textprops={'fontsize': 12})
plt.title("Score > 70",fontsize=15)

plt.subplot(3,3,9)
EBV3 = Data[Data["math score"] >= 95]["test preparation course"].value_counts()
EBV3_pie = plt.pie(EBV3 , labels = EBV3.index,autopct='%1.1f%%',shadow=True, startangle=90, textprops={'fontsize': 12})
plt.title("Score > 95",fontsize=15)

plt.show()




##############################################################################
##############################################################################



# reading
plt.figure(figsize=(18, 18))
plt.suptitle("Score Distribution in the Reading  Exam", fontsize=35)

#race/ethnicity
plt.subplot(3,3,1)
EBV1 = Data[Data["reading score"] <= 40]["parental level of education"].value_counts()
EBV1_pie = plt.pie(EBV1 , labels = EBV1.index,autopct='%1.1f%%',shadow=True, startangle=90, textprops={'fontsize': 12})
plt.title("Parental level of education\nScore < 40",fontsize=15)


plt.subplot(3,3,4)
EBV2 = Data[Data["reading score"] >= 70]["parental level of education"].value_counts()
EBV2_pie = plt.pie(EBV2 , labels = EBV2.index,autopct='%1.1f%%',shadow=True, startangle=90, textprops={'fontsize': 12})
plt.title("Score > 70",fontsize=15)


plt.subplot(3,3,7)
EBV3 = Data[Data["reading score"] >= 95]["parental level of education"].value_counts()
EBV3_pie = plt.pie(EBV3 , labels = EBV3.index,autopct='%1.1f%%',shadow=True, startangle=90, textprops={'fontsize': 12})
plt.title("Score > 95",fontsize=15)


# lunch
plt.subplot(3,3,2)
EBV1 = Data[Data["reading score"] <= 40]["lunch"].value_counts()
EBV1_pie = plt.pie(EBV1 , labels = EBV1.index,autopct='%1.1f%%',shadow=True, startangle=90, textprops={'fontsize': 12})
plt.title("Lunch\nScore < 40",fontsize=15)

plt.subplot(3,3,5)
EBV2 = Data[Data["reading score"] >= 70]["lunch"].value_counts()
EBV2_pie = plt.pie(EBV2 , labels = EBV2.index,autopct='%1.1f%%',shadow=True, startangle=90, textprops={'fontsize': 12})
plt.title("Score > 70",fontsize=15)

plt.subplot(3,3,8)
EBV3 = Data[Data["reading score"] >= 95]["lunch"].value_counts()
EBV3_pie = plt.pie(EBV3 , labels = EBV3.index,autopct='%1.1f%%',shadow=True, startangle=90, textprops={'fontsize': 12})
plt.title("Score > 95",fontsize=15)


# test preparation course
plt.subplot(3,3,3)
EBV1 = Data[Data["reading score"] <= 40]["test preparation course"].value_counts()
EBV1_pie = plt.pie(EBV1 , labels = EBV1.index,autopct='%1.1f%%',shadow=True, startangle=90, textprops={'fontsize': 12})
plt.title("Test preparation course\nScore < 40",fontsize=15)

plt.subplot(3,3,6)
EBV2 = Data[Data["reading score"] >= 70]["test preparation course"].value_counts()
EBV2_pie = plt.pie(EBV2 , labels = EBV2.index,autopct='%1.1f%%',shadow=True, startangle=90, textprops={'fontsize': 12})
plt.title("Score > 70",fontsize=15)

plt.subplot(3,3,9)
EBV3 = Data[Data["reading score"] >= 95]["test preparation course"].value_counts()
EBV3_pie = plt.pie(EBV3 , labels = EBV3.index,autopct='%1.1f%%',shadow=True, startangle=90, textprops={'fontsize': 12})
plt.title("Score > 95",fontsize=15)

plt.show()



##############################################################################
##############################################################################




# Writing 
plt.figure(figsize=(18, 18))
plt.suptitle("Score Distribution in the Writing Exam", fontsize=35)

#race/ethnicity
plt.subplot(3,3,1)
EBV1 = Data[Data["writing score"] <= 40]["parental level of education"].value_counts()
EBV1_pie = plt.pie(EBV1 , labels = EBV1.index,autopct='%1.1f%%',shadow=True, startangle=90, textprops={'fontsize': 12})
plt.title("Parental level of education\nScore < 40",fontsize=15)


plt.subplot(3,3,4)
EBV2 = Data[Data["writing score"] >= 70]["parental level of education"].value_counts()
EBV2_pie = plt.pie(EBV2 , labels = EBV2.index,autopct='%1.1f%%',shadow=True, startangle=90, textprops={'fontsize': 12})
plt.title("Score > 70",fontsize=15)


plt.subplot(3,3,7)
EBV3 = Data[Data["writing score"] >= 95]["parental level of education"].value_counts()
EBV3_pie = plt.pie(EBV3 , labels = EBV3.index,autopct='%1.1f%%',shadow=True, startangle=90, textprops={'fontsize': 12})
plt.title("Score > 95",fontsize=15)


# lunch
plt.subplot(3,3,2)
EBV1 = Data[Data["writing score"] <= 40]["lunch"].value_counts()
EBV1_pie = plt.pie(EBV1 , labels = EBV1.index,autopct='%1.1f%%',shadow=True, startangle=90, textprops={'fontsize': 12})
plt.title("Lunch\nScore < 40",fontsize=15)

plt.subplot(3,3,5)
EBV2 = Data[Data["writing score"] >= 70]["lunch"].value_counts()
EBV2_pie = plt.pie(EBV2 , labels = EBV2.index,autopct='%1.1f%%',shadow=True, startangle=90, textprops={'fontsize': 12})
plt.title("Score > 70",fontsize=15)

plt.subplot(3,3,8)
EBV3 = Data[Data["writing score"] >= 95]["lunch"].value_counts()
EBV3_pie = plt.pie(EBV3 , labels = EBV3.index,autopct='%1.1f%%',shadow=True, startangle=90, textprops={'fontsize': 12})
plt.title("Score > 95",fontsize=15)


# test preparation course
plt.subplot(3,3,3)
EBV1 = Data[Data["writing score"] <= 40]["test preparation course"].value_counts()
EBV1_pie = plt.pie(EBV1 , labels = EBV1.index,autopct='%1.1f%%',shadow=True, startangle=90, textprops={'fontsize': 12})
plt.title("Test preparation course\nScore < 40",fontsize=15)

plt.subplot(3,3,6)
EBV2 = Data[Data["writing score"] >= 70]["test preparation course"].value_counts()
EBV2_pie = plt.pie(EBV2 , labels = EBV2.index,autopct='%1.1f%%',shadow=True, startangle=90, textprops={'fontsize': 12})
plt.title("Score > 70",fontsize=15)

plt.subplot(3,3,9)
EBV3 = Data[Data["writing score"] >= 95]["test preparation course"].value_counts()
EBV3_pie = plt.pie(EBV3 , labels = EBV3.index,autopct='%1.1f%%',shadow=True, startangle=90, textprops={'fontsize': 12})
plt.title("Score > 95",fontsize=15)

plt.show()




##############################################################################
import seaborn as sns

plt.figure(dpi=100)
plt.title('Correlation Matrix')
sns.heatmap(Data.corr(),annot=True,lw=1,linecolor='white',cmap='viridis')
plt.xticks(rotation=60)
plt.yticks(rotation = 60)
plt.show()



scaMat = pd.plotting.scatter_matrix(Data, alpha = 0.5, figsize=(10, 10), marker = "o")




















