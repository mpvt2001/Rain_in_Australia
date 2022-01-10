In this folder you can find the different notebooks of code that have been created. Each one of them analyzes the data.

# 1.EDA&preprocessing.ipynb
Initial analysis of the data: variables, target, correlation...

Removing outliers, NaNs, scale methods...

# 2.Model_selection.ipynb
Different models are studied. The results are the following:
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

# 3.Crossvalidation
Models from ```Model_selection``` are studied using crossvalidation.

# 4.MetricAnalysis
Precision-recall and ROC curves are analyzed from the best models obtained.

# 5.HyperparameterSearch
The method used has been ```RadomizedSearchCV()```. Only some models have been studied as it has a very high cost of time.

|Model|Best parameters|
|----|-----|
|LogisticRegression| L2, C=10|
|RandomForestClassifier| n_estimators=100, min_samples_split=2, criterion='entropy'|
