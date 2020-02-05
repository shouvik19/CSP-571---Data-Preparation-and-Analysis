# CSP/MATH 571
# Homework 1
# Note you must show all your code to receive credit. Some of these questions could be 
# solved without code, but the point here is to practice doing basic data manipulation in R
# and to start thinking about how to break down data analysis tasks into steps.


# 1 point
# Question 1: Create a variable named "myName" and assign to have a value of your
# preferred name. Create a varaible named "myEmail" and assign it to have a value
# of your email.
myName <- "Shouvik Sharma"
myEmail <- "ssharma25@hawk.iit.edu"

# 1 point
# Question 2: Create a vector of integers from 99 to 10000 (inclusive). Assign
# the variable myVector. Randomly reorder that vector. 
# Write your own functions to sum, calculate the min value, the max value and the median value.
# You do not need to implement your own sorting algorithms. 
# Return the sum, min, max, and median of this vector and assign it below.
# 
# Note: in practice, you should usually use the predefined functions that R provides to 
# compute summary statistics. However, we can use this as an opportunity to practice our R
# while having an easy way to check for mistakes by comparing our function output with the 
# default R function output. 

# creating a vector 
myVector <- 99:10000

# randomly distributing the vector using the sample function
myVector<-sample(myVector)

# Creating the sum function

mySumFunc <- 
function(x){  
  summ=0
  for (i in seq(from=1,to=length(x)))
{
    summ = x[i] + summ  
    p=p+1
  }
  summ
}

# sum of myVector is 50000149
mySumFunc(myVector)
# 50000149

# Creating the minimum function
myMinFunc <- function(x) {
  min_val<- x[1] 
  for (i in seq(from =2,to=length(x))) { 
    if(x[i] < min_val) 
      min_val <- x[i]  
  }
  min_val
}

# computing the minimum of the vector i.e: 99
myMinFunc(myVector)
# 99

# creating a function for computing the maximum value of the vector
myMaxFunc <- function(x) {
  max_val<- x[1] 
  for (i in seq(from =2,to=length(x))) { 
    if(x[i] > max_val) 
      max_val <- x[i]  
  }
  max_val
}

myMaxFunc(myVector)
#10000


myMedianFunc <-
  function(x) {
    
    x<-sort(x)
    n <- length(x);
    t <- (n+1)/2;
    median = (x[(floor(t))]+x[(ceiling(t))])/2; 
    median
  }

#5049.5


# 1 point
# Question 3: Write a function that accepts a number as an input returns
# TRUE if that number is divisible by 127 FALSE if that number is not divisible
# by 127.  For example, divis(127*5) should return TRUE and divis(80)
# should return FALSE. Hint: %% is the modulo operator in R.
divis <- 
  function(number){
    number<-as.integer(number)
    isTRUE(number%%127==0)
  }

divis(127*5)
# TRUE

# 1 point
# Question 4: Using the function you wrote for Question 3 and the vector you
# defined in Question 2, deterine how many integers between 100 and 10000 are
# divisible by 127. Assign it to the variable below.
countDivis <-
function(x){
count=0
for (i in x)
{
if (divis(i) == TRUE)
{
count=count+1
}
}
count
}
	
countDivis(myVector)
# 78


# 1 point
# Question 5: Using the vector of names below, write code to return the 9th
# last name in the vector.
names <- c("Kermit Chacko",
           "Eleonore Chien",
           "Genny Layne",
           "Willene Chausse",
           "Taylor Lyttle",
           "Tillie Vowell",
           "Carlyn Tisdale",
           "Antione Roddy",
           "Zula Lapp",
           "Delphia Strandberg",
           "Barry Brake",
           "Warren Hitchings",
           "Krista Alto",
           "Stephani Kempf",
           "Sebastian Esper",
           "Mariela Hibner",
           "Torrie Kyler")

ninth_name<-strsplit(names[9],split = " ")
ninth_name[[1]][[2]]
# Lapp


# 1 point
# Question 6: Using the vector "names" from Question 5, write code to
# determine how many last names start with L.

countLastNameStartsWithL <- function(x){
p=1
count=0
full_names<-0
last_name<-0
for (i in x)
{
   full_names[p]<-strsplit(i,split = " ")
   last_name[p]<-full_names[p][[1]][[2]]  
   if (isTRUE(substr(last_name[p],1,1)=="L")==TRUE)
   {
     count=count+1
   }
   p=p+1
}
count
}

countLastNameStartsWithL(names)
# 3

  
# 1 point 
# Question 7: Using the vector "names" from Question 5, write code to create a
# list that allows the user to input a first name and retrieve the last name.
# For example, nameMap["Krista"] should return "Alto".
nameMap<- function(first_n){
name_Map <- vector(mode="list", length=length(names))
p=1
last_name<-0
first_name<-0
full_name<-0
for (i in names)
{  
  full_name[p]<-strsplit(i,split = " ")
  first_name[p]<-full_name[[p]][[1]] 
  last_name[p]<-full_name[[p]][[2]] 
  name_Map[[p]]<-last_name[p]
  p=p+1
}
names(name_Map) <- c(first_name)
return(name_Map[first_n])
}

nameMap("Krista")
# Alto

# 2 points
# Question 8: Load in the "Adult" data set from the UCI Machine Learning
# Repository. http://archive.ics.uci.edu/ml/datasets/Adult	
# Load this into a dataframe. Rename the variables to be the proper names
# listed on the website. Name the income attribute (">50K", "<=50K") to be
# incomeLevel

library(plyr)

adult <- read.table('https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data', 
                    sep = ',', fill = F, strip.white = T)
colnames(adult) <- c('age', 'workclass', 'fnlwgt', 'education', 
                     'education_num', 'marital_status', 'occupation', 'relationship', 'race', 'sex', 
                     'capital_gain', 'capital_loss', 'hours_per_week', 'native_country', 'income')

library(tidyverse)
adult<-adult %>% rename(incomeLevel=income)


# 2 points
# Question 9: Create a new variable called workSector. Label all government
# employees as "government", all self-employeed employees as "selfEmployed",
# all Private employees as "Private" and everyone else as "Other".
# Enter the number of government employees in the text here, as well as showiing the code belo
adult$workSector<-ifelse(adult$workclass=="Federal-gov"|adult$workclass=="Local-gov"|adult$workclass=="State-gov","government",
                           ifelse(adult$workclass=="Self-emp-inc"|adult$workclass=="Self-emp-not-inc","selfEmployed",
                                  ifelse(adult$workclass=="Private","Private","Other")))

# 2 points
# Question 10: Create a histogram of the 'age'. Hint: You may need to convert
# age to be numeric first. Save this histogram and include it with your
# submission

hist(adult$age,col = "lightblue",border = "grey",main="Histogram Of Employee's AGE")



# 2 points
# Question 11: Determine the top 3 occupations with the highest average hours-per-week
# Hint: One way to do this is to use tapply
# List the occupations in the comments, as well as showing the code you used to determine that.
# Q11
    head(sort(rank(-tapply(adult$hours_per_week, adult$occupation,mean))),n=3)
#1 Farming-fishing
#2 Exec-managerial
#3 Transport-moving


# 2 points
# Question 12: Your friend works for the government and claims that in order to make more money, you have to work
# longer hours. Use this data set to determine if your friend is right. State your conclusion in the comments.
library(plyr)    
library(dplyr)

    
# filtering the government employees
gov_data<-filter(adult,adult$workSector=="government")

# taking descriptive statistics with mean of each group
tapply(gov_data$hours_per_week, gov_data$incomeLevel,mean)
barplot(tapply(gov_data$hours_per_week, gov_data$incomeLevel,mean))
# conclusion the average number of hours of the two groups do not differ much, (<=50k =38.80 hours and >50 k = 43.86)

# Taking a deep dive
cdplot(as.numeric(gov_data$hours_per_week),factor(gov_data$incomeLevel))

# Some of the people belonging in the range 20-40 who work lesser hours earn more than the people who work more number of hours 
# We can conclude that the hypothesis that the people with more hours earn more can be rejected.















# 3 points
# Question 13: Implement a function call charCombos from scratch 
# (only using base R; no using 3rd party libraries for this question!) 
# that counts how many times each parameter z of 
# letters occur sequentially in a string. 
# For example, charCombos('abcbcb', z=2)
# should return ab:1, bc:2, cb: 2
# charCombos('abcbcb', z=3) should return
# abc: 1, bcb: 2, cbc: 1
# Hint, use the substr function

 
charCombos <- 
function(string,z){
values<-vector()

# Taking the limit till total vector length - z value + 1, we add one as substr takes the starting digit value

    for (i in seq(from=1,to=nchar(string)-z+1))
  {


      temp<-substr(string,i,i+(z-1))

# Using if-else loop we add the extracted value to our vector
      
	  if (temp %in% names(values))
      {
		values[temp]=values[temp]+1
	  
	  }  
	  else
	  
	  {
	  values[temp]=1
	  }
	  
      }
  values
}

myTestString <- 'abcbcb'
charCombos(string = myTestString, z= 2)
charCombos(string = myTestString, z= 3)

# charCombos(string = myTestString, z= 2)
# ab bc cb 
# 1  2  2 
# charCombos(string = myTestString, z= 3)
# abc bcb cbc 
#  1   2   1 







# 3 points
# Question 14: In the traditional English language, students are taught
# "Always use a 'u' after a 'q'!". Using the function from 
# question 13 (won't get full credit otherwise) 
# and a link to a dictionary of english word provided below
# determine the percentage of times that  'q' is indeed 
# immediately followed by a 'u'.
# Specifically, words containing q that are immediately followed 
# by a u divided by total number of words containing q. 
# Hint: Ensure you don't count q followed by whitespace or other 
# non-alphanumeric characters. For example, don't count 
# something like "Shaq upended the game."
# Note for words with multiple q's or multiple q-u's, count them once.
# This can be rather naively done and achieve short run times. If you are
# issues with the length of this run-time, check your code. 

bigListOfWords <- readLines('https://raw.githubusercontent.com/dwyl/english-words/master/words.txt')
bigListOfWords <- as.vector(bigListOfWords)

# cleaning text to keep words with q/Q and which have second letter alphanumberic ( word or number)
cleaning <- grep('[Qq][a-zA-Z]', bigListOfWords)	
bigListOfWords <- bigListOfWords[cleaning]
count_qu=0
count_q=0
for (i in bigListOfWords)
{
  qu_extract<-charCombos(string = i, z= 2)  
  q_extract<-charCombos(string = i, z= 1)  
  
  # Computing words with qu
  for (word in names(qu_extract))
  {
    if (("qu" %in%  tolower(word))==TRUE)
    {
      count_qu=count_qu+1  # count with words containing "qu"
    }
  }
  
  # computing words with q 
  for (word in names(q_extract))
  {
    if (grepl('q',tolower(word)))
    {
      count_q=count_q+1  # count with words containing "q"
    }
  }
  
}

# Number of qu's - 7673
# Number of q's - 7856

# calculating the percentage 'qu'

per_qu <- (count_qu/count_q)*100
per_qu


# We have 97.67 percent words with 'qu' out of all the words containing q


# 3 points
# Question 15: Find the top 5 
# most commonly used letters after q that are NOT equal to u sorted in descending 
# order of frequency.

####################    ANSWER  ###############################


# creating a vector list of two lettered words
temp <- vector()
for (word in bigListOfWords){
  string <- word
  pctQU <-charCombos(string, z=2)
  temp <- append(temp,pctQU,after = length(temp))
}


# Referencing to the two lettered words list and extracting the words which start with 'q'
list_words <- vector()
for (word in names(temp)) {
  if (tolower(substr(word,1,1))== "q")  {

# For all the words with q, extracting the second word    
        second_alpha = tolower(strsplit(word, '')[[1]][2])
    
    if (second_alpha %in% names(list_words) && second_alpha != 'u') 
      {
      
        list_words[second_alpha] = list_words[second_alpha] + 1
    
      } 
    else 
      {
        list_words[second_alpha] = 1
      }
  
    }
}

# extracting the top 5 from the list
list_words <- sort(list_words, decreasing = TRUE)
top_5 <- list_words[1:5]
top_5

# Top 5
# 1. a - 39
# 2. i - 23 
# 3. s - 17
# 4. r - 14
# 5. t - 11



 


