# League of legends prediction using Spark 

This is a big data pipeline and machine learning model to predict League of Legends matches. 
It is deployed to a webapp.

Data Collection/data_collection_VM: Data collecting script

Data Collection/league_api.py: connects to Riot Games API to collect data

Feature Creation/create_features_lite.ipynb: feature processing and engineering for feature matrix with no mastery data

Feature Creation/create_full_features.ipynb: feature processing and engineering for full range of features

Machine Learning Model/Final_Scikit_ML.ipynb: fits a Logistic Regression model using Scikit-learn and gets predictions, performance metrics for the model

Machine Learning Model/Final_SparkML_model.ipynb: fits a Logistic Regression model using SparkML and gets predictions, performance metrics for the model.

Deploy Website/webapp: contains the files for the webapp made using flask. 

routes.py: interface between user input, the model and the LoL API

Deploy Website/Deploy Machine Learning Model.ipynb: Create docker container for model