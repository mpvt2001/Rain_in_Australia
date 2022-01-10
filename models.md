If you are interested in knowing more about the models studied, go to notebook `2.Model_selection.ipynb`.
You will be able to find the following methods studied with their scores respectively.

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

In `3.Crossvalidation.ipynb` the same models have been studied but using crossvalidation.
