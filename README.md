## Project description
In this project we have trained our model on Titanic dataset using Random Forest Classifier and then deployed it on local machine using fastapi.

## Dataset 
You can download the datset from kaggle.This is the training datset(train.csv) from titanic competition.you can get the datset from the link
https://www.kaggle.com/competitions/titanic/data?select=train.csv or you can download it from the train.csv file in the repository.
In the datset the features names,fare,Pclass,Cabin,Age,etc. of the passengers are given and we need to train our model to predict whether the passenger will survive or not.

## Training details
First I did EDA on the dataset to get some insights.I dropped some features which were of no use and also created some features too based on the analysis.
Then I trained the model using RandomForestClassifier and got accuracy of 83.45% on training set and 79.36% on test set


## Deployment

I have deployed the model locally using fastapi as it is easy and fast.Also it creates the documentation of your api by itself. If you want to run this on your PC ,just go in this folder and then run the below command in your terminal

```cmd
  uvicorn main:app --reload
```

