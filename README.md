# Kaggle APC UAB 2021-2022
### Name: Maria Pallejà
### Dataset: Rain in Australia

## Objective
The objective of this analysis is to predict the target variable: `RainTomorrow`. It's a categorical variable that includes Yes and No values, meaning it rains tomorrow or not respectively.

## Exploratory Data Analysis
- 145460 instances
- 23 variables

· There are categorical and numerical variables
- Categorical: `Date`, `Location`, `WindGustDir`, `WindDir9am`, `WindDir3pm`, `RainToday`, `RainTomorrow`
- Numerical: `MinTemp`, `MaxTemp`, `Rainfall`, `Evaporation`, `Sunshine`, `WindGustSpeed`, `WindSpeed9am`, `WindSpeed3pm`, `Humidity9am`, `Humidity3pm`, `Pressure9am`, `Pressure3pm`, `Cloud9am`, `Cloud3pm`, `Temp9am`, `Temp3pm`.

· Target variable
- Categorical, 2 unique values: (Yes, No)
- Imbalanced: 77.58% Nom 22.42% Yes

· The variables with more outliers are `Rainfall`, `Evaporation` and the different `winds`. Their distribution has been studied but as it was very skewed, the interquantile range has been used in order to remove outliers in preprocessing.

· Correlation

The pair variables more correlated are (`MaxTemp`, `Temp3pm`), (`Pressure9am`, `Pressure3pm`)...
There is also correlation between numerical and categorical variables sucha as `Temperature` and `Location`, `Evaporation` and `Location`...

## Preprocessing
· The NaN values in the target variable have been removed. The quantity wasn't too representative and it was better to study data we are sure we can analyze correctly.

· The NaNs in the numerical variables have been replaced by the median as the mean wasn't a good idea due to the outliers found in the exploratory data analysis.

· The NaNs in the categorical variables have been replaced by the mode

· The function ```get_dummies()``` has been used in order to remover categorical variables. Because of it, the number of variables has increased.

· The data has been scaled using two different ways: ```MinMaxScaler()``` and ```StandardScaler()```

· Outliers have been removed

## Model Selection
|Models|Original|MinMax|Standard|
|-----|-----|-----|-----|
|LogisticRegression|0.840677|0.845916|0.845916|
|SGDClassifier|0.822849|0.844650|0.845248|
|KNeighborsClassifier|0.832308|0.801329|0.801329|
|DecisionTreeClassifier|0.784767| 0.775801| 0.775906|
|GaussianNB|0.641338|0.637329|0.637329|
|LinearDiscriminantAnalysis|0.846338|0.845599|0.845599|
|RandomForestClassifier|0.855480|0.854249	| 0.854601|
|XGBoostClassifier|0.847744|0.847147|0.847147|

|Ensemble Methods | Original |MinMax|Standard|
|-------|------|------|------|
|RandomForestClassifier|0.841098|0.839516|0.841098|
|BaggingClassifier|0.833819|0.820528|0.823412|
|GradientBoostingClassifier|0.845072|0.844228|0.844228|

· Confusion matrix have been studied

## Crossvalidation
By looking at model slecteion and after doing cross validation with the same models, we can conclude there's not a significant difference between the different scale methods of the data in this dataset. The model that has returned better results are ```RandomForestClassifier()``` and ```XGBoostClassifier()```.

## MetricAnalysis
In this section the precision-recall and ROC curve have been studied. 
As our dataset isn't balanced, it is better to look at the precision-recall curve which shows that the negative class is almost classified without making any errors. On the other side, the positive class makes mistakes as we have less instances to learn from.

## Hyperparameter Search
The method used has been ```RadomizedSearchCV()```. Only some models have been studied as it has a very high cost of time.

|Model|Best parameters|
|----|-----|
|LogisticRegression| L2, C=10|
|RandomForestClassifier| n_estimators=100, min_samples_split=2, criterion='entropy'|


## Future ideas
The previous analysis of the data allows us to predict our target variable RainTomorrow and a lot has been learned from it. Nevertheless, there are som aspect that could have been studied in order to obtain better results and learn more from the data provided.
First of all, with more time, more models can be studied. Moreover, in the hyperparameter search it is possible tu use other ways to find them such as GridSearchCV and also increase the variety and quantity of parameters given in order to find the best match.
Finally, another aspect that can be studied are temporal series, these can help understand in more detail if raining has usually the smae distribution throuugh the years or not.
