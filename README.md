# wine-quality-predictor-webapp
```model-train/``` contains the code to train the model and the necessary datasets in csv format

```django-webapp/``` contains the web application

the pip requirements are in requirements.txt in the respective directories

# model
the model used is a ```decision tree regressor``` trained with 1599 instances for red wine and 4898 instances for white wine

## model performance
the model made the correct prediction all the time when tested 20 times with different training sets

### dataset
the dataset is from the UCI Machine Learning Repository

https://archive.ics.uci.edu/ml/datasets/Wine+Quality
