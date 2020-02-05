# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print("Question 1 (a)")
import os
os.chdir('C:/Users/shouv/Documents/CS 584')


print(" Importing libraries in python \n")

import pandas as pd
import scipy.stats as sp
import numpy as np
import matplotlib.pyplot as plt
import math
from numpy import linalg as LA
from sklearn.neighbors import KNeighborsClassifier
import seaborn


print("Reading the dataset")
Normal_data=pd.read_csv('NormalSample.csv')
print(Normal_data.head())

print ("Computing IQR")
# computing the iqr for the bin width
iqr=sp.stats.iqr(Normal_data['x']) 
print(sp.stats.iqr(Normal_data['x']))

print("Computing N")
print(Normal_data['x'].count())
N=Normal_data['x'].count()

# Bin length is
print("Bin length is given by",(2 * iqr*pow(N,-1/3)))

print("Question 1 (b)")

# computing the minimum value
min_val=np.min(Normal_data['x'])
print(min_val)

#computing the max value
max_val=np.max(Normal_data['x'])
print(max_val)

print("Question 1 (c)")

a=math.floor(min_val)
b=math.ceil(max_val)    

print("a :",a)
print("b :",b)
   
# Computing midpoints
# recursively computing the other midpoints 
def density_estimator(mid_point,h):
    count=0
    sort_x=sorted(Normal_data['x'])
    for i in sort_x:        
        u=(i-float(mid_point))/h        
        if u > -0.5 and u <= 0.5:
            count=count+1
    return count/(N*h)    

def midpoint(h):
# computing number of midpoints 
    number_of_midpoints=(b-a)/h

# Computing the first midpoint
    mid_point_1 = a+(h/2)
    mid_points.append(mid_point_1)
    
    for i in range(int(number_of_midpoints)-1):
        mid_points.append(mid_points[i]+h)  
        
    for mid in mid_points:
      density.append(density_estimator(mid,h))    
    
    return mid_points


print("Question 1 (d)")
# Computing midpoints
h=0.25
a=26
b=36
density=[]
mid_points=[]
mid_point_0_25=midpoint(h)

print(pd.DataFrame({'p(mi)':density,'mi':mid_point_0_25}))

# Histogram
number_of_midpoints = math.floor((b-a)/h)
plt.hist(Normal_data['x'],bins=number_of_midpoints)
plt.grid(axis="y")
plt.title("Histogram of X for h = 0.25")
plt.xlabel("Values of X")
plt.ylabel("Number of Observations")
plt.show()

plt.step(mid_point_0_25,density)
plt.grid(axis="y")
plt.title("Density Estimation of X for h = 0.25")
plt.xlabel("Mid Points")
plt.show()

print("Question 1 (e)")
# Computing midpoints
h=0.5
a=26
b=36
density=[]
mid_points=[]

mid_point_0_5=midpoint(h)
print(pd.DataFrame({'p(mi)':density,'mi':mid_point_0_5}))

# Histogram
number_of_midpoints = math.floor((b-a)/h)
plt.hist(Normal_data['x'],bins=number_of_midpoints)
plt.grid(axis="y")
plt.title("Histogram of X for h = 0.5")
plt.xlabel("Values of X")
plt.ylabel("Number of Observations")
plt.show()


plt.step(mid_point_0_5,density)
plt.grid(axis="y")
plt.title("Density Estimation of X for h = 0.5")
plt.xlabel("Mid Points")
plt.show()

print("Question 1 (f)")
# Computing midpoints
h=1
a=26
b=36
density=[]
mid_points=[]
mid_point_1=midpoint(h)

print(pd.DataFrame({'p(mi)':density,'mi':mid_point_1}))

# Histogram
number_of_midpoints = math.floor((b-a)/h)
plt.hist(Normal_data['x'],bins=number_of_midpoints)
plt.grid(axis="y")
plt.title("Histogram of X for h = 1")
plt.xlabel("Values of X")
plt.ylabel("Number of Observations")
plt.show()
    
plt.step(mid_point_1,density)
plt.grid(axis="y")
plt.title("Density Estimation of X for h = 1")
plt.xlabel("Mid Points")
plt.show()


print("Question 1 (g)")
# Computing midpoints
h=2
a=26
b=36
density=[]
mid_points=[]
mid_point_2=midpoint(h)
print(pd.DataFrame({'p(mi)':density,'mi':mid_point_2}))

# Histogram
number_of_midpoints = math.floor((b-a)/h)
plt.hist(Normal_data['x'],bins=number_of_midpoints)
plt.grid(axis="y")
plt.title("Histogram of X for h = 2")
plt.xlabel("Values of X")
plt.ylabel("Number of Observations")
plt.show()

plt.step(mid_point_2,density)
plt.grid(axis="y")
plt.title("Density Estimation of X for h = 2")
plt.xlabel("Mid Points")
plt.show()

print(" Question 2 (a)")
print("Five number summary")

def five_number_summary(x):
    Quartile_1=np.percentile(x,25)
    print("The 1st Quartile is ",Quartile_1)
    
    Quartile_2=np.percentile(x,50)
    print("The 2nd Quartile is ",Quartile_2)
    
    Quartile_3=np.percentile(x,75)
    print("The 3rd Quartile is ",Quartile_3)
    
    
    print("The minimum value", min(x))
    print("The maximum value", max(x))
    
    iqr=Quartile_3-Quartile_1
    print("the left whisker is given by:",Quartile_1-(1.5*iqr))
    print("the right whisker is given by:",Quartile_3+(1.5*iqr))

five_number_summary(Normal_data['x'])

print(" Question 2 (b)")

for i in (set(Normal_data['group'])):
   x=Normal_data[(Normal_data.group==i)]
   print("five number summary for the group ",i)
   five_number_summary(x['x'])
   print("\n")

print(" Question 2 (c)")
B=plt.boxplot(Normal_data['x'])
plt.ylabel("Number of Observations")
plt.xlabel("x")
plt.show()

print(" Question 2 (d)")

group_1=pd.DataFrame(Normal_data[(Normal_data.group==1)]['x'])
group_0= pd.DataFrame(Normal_data[(Normal_data.group==0)]['x'])
x= pd.DataFrame(Normal_data['x'])

sq=pd.concat([group_0,group_1,x],axis=1,keys=["Group 0","Group 1","x"])
seaborn.boxplot(data=sq,order=["Group 0","Group 1","x"],palette="RdBu")

# for group 0

Quartile_1=np.percentile(group_0,25)
    
Quartile_3=np.percentile(group_0,75)
    
iqr=Quartile_3-Quartile_1
left_whisker = Quartile_1-(1.5*iqr)
right_whisker = Quartile_3+(1.5*iqr)
outlier_0=[]
for i in list(group_0.x):
    if i > right_whisker or i < left_whisker:
        outlier_0.append(i)
print(outlier_0)

# for group 1
Quartile_1=np.percentile(group_1,25)
    
Quartile_3=np.percentile(group_1,75)
    
iqr=Quartile_3-Quartile_1
left_whisker = Quartile_1-(1.5*iqr)
right_whisker = Quartile_3+(1.5*iqr)
outlier_1=[]
for i in list(group_1.x):
    if i > right_whisker or i < left_whisker:
        outlier_1.append(i)        
print(outlier_1)

# for x

Quartile_1=np.percentile(x,25)
    
Quartile_3=np.percentile(x,75)
    
iqr=Quartile_3-Quartile_1
left_whisker = Quartile_1-(1.5*iqr)
right_whisker = Quartile_3+(1.5*iqr)
outlier_x=[]
for i in list(x.x):
    if i > right_whisker or i < left_whisker:
        outlier_x.append(i)        
print(outlier_x)        
        
##################               QUESTION 3             ##############################        
print("Question 3(a)")
Fraud_Data = pd.read_csv('Fraud.csv',delimiter=',')
percent_fraud = round((len(Fraud_Data[(Fraud_Data.FRAUD==1)])/len(Fraud_Data)) *100,4)
print("Display Fraud Percentage")
print(percent_fraud)


print("Question 3(b)")
Fraud_Data.describe()

Fraud_Data.boxplot(column='TOTAL_SPEND',by='FRAUD',patch_artist=True,vert=False)
plt.yticks([1, 2], ['Non-Fraudulent', 'Fradulent'])
plt.suptitle("")
plt.title("TOTAL_SPEND BOXPLOT grouped by FRAUD")
plt.xlabel("TOTAL_SPEND")
plt.ylabel("Fraud")
plt.show()

Fraud_Data.boxplot(column='DOCTOR_VISITS',by='FRAUD',patch_artist=True,vert=False)
plt.yticks([1, 2], ['Non-Fraudulent', 'Fradulent'])
plt.suptitle("")
plt.title("DOCTOR_VISITS BOXPLOT grouped by FRAUD")
plt.xlabel("DOCTOR_VISITS")
plt.ylabel("Fraud")
plt.show()

Fraud_Data.boxplot(column='NUM_CLAIMS',by='FRAUD',patch_artist=True,vert=False)
plt.yticks([1, 2], ['Non-Fraudulent', 'Fradulent'])
plt.suptitle("")
plt.title("NUM_CLAIMS BOXPLOT grouped by FRAUD")
plt.xlabel("NUM_CLAIMS")
plt.ylabel("Fraud")
plt.show()

Fraud_Data.boxplot(column='MEMBER_DURATION',by='FRAUD',patch_artist=True,vert=False)
plt.yticks([1, 2], ['Non-Fraudulent', 'Fradulent'])
plt.suptitle("")
plt.title("MEMBER_DURATION BOXPLOT grouped by FRAUD")
plt.xlabel("MEMBER_DURATION")
plt.ylabel("Fraud")
plt.show()


Fraud_Data.boxplot(column='OPTOM_PRESC',by='FRAUD',patch_artist=True,vert=False)
plt.yticks([1, 2], ['Non-Fraudulent', 'Fradulent'])
plt.suptitle("")
plt.title("OPTOM_PRESC BOXPLOT grouped by FRAUD")
plt.xlabel("OPTOM_PRESC")
plt.ylabel("Fraud")
plt.show()

Fraud_Data.boxplot(column='NUM_MEMBERS',by='FRAUD',patch_artist=True,vert=False)
plt.yticks([1, 2], ['Non-Fraudulent', 'Fradulent'])
plt.suptitle("")
plt.title("NUM_MEMBERS BOXPLOT grouped by FRAUD")
plt.xlabel("NUM_MEMBERS")
plt.ylabel("Fraud")
plt.show()


print("Question 3(c)")
interval_variables=Fraud_Data[['TOTAL_SPEND','DOCTOR_VISITS','NUM_CLAIMS','MEMBER_DURATION','OPTOM_PRESC','NUM_MEMBERS']]
x=np.matrix(interval_variables)
xtx=x.transpose()*x

evals, evecs = LA.eigh(xtx)
print("Eigenvalues of x = \n", evals)
print("Eigenvectors of x = \n",evecs)

# Hence eigen value are > 1, therefore dimensions are 1.

# We compute transformation matrix
transf_mat = evecs * LA.inv(np.sqrt(np.diagflat(evals)))
print("Transformation Matrix = \n", transf_mat)

print("\n We transform our original matrix ")
transf_interval_variables = x * transf_mat
print("The Transformed interval variables matrix = \n", transf_interval_variables )

print("We check the columns of the transformed x, if it is near identity")
I=transf_interval_variables .transpose() * transf_interval_variables 
print("Identity matrix = \n",I)


print("Question 3(d)")

# Specify target: 0 = Asia, 1 = Europe, 2 = USA
target = Fraud_Data['FRAUD']

neigh = KNeighborsClassifier(n_neighbors=5 , algorithm = 'brute', metric = 'euclidean')
nbrs = neigh.fit(transf_interval_variables, target)

# See the classification probabilities
class_prob = nbrs.predict_proba(transf_interval_variables)
print(class_prob)

# Using score for accuracy
Score_accuracy= nbrs.score(transf_interval_variables, target)
Score_accuracy

print("Question 3(e)")
test=np.matrix([7500,15,3,127,2,2])
test_t_test=test.transpose()*test
transf_test=test*transf_mat

# predicted prob. of the test
test_prob = nbrs.predict_proba(transf_test)
print(test_prob)

Neighbors_val = nbrs.kneighbors(transf_test, return_distance = False)
print("My Neighbors = \n", myNeighbors_t)

for i in Neighbors_val :
    print(Fraud_Data.loc[i])

