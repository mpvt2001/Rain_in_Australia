In this folder you can find the datasets that have been created along the study of the original data. 

```df_nonans_target```: original dataset without the instances that had NaNs in the target variable

```df_date```: df_nonans_target and the column date modified by creating 3 new columns (Day, Month, Year)

```data_encoded```: data prepared for studying the models. It includes X_train, X_test, y_train, y_test

```data_encoded_minmax```: like data_encoded but with the data scaled using MinMaxScaler()

```data_encoded_std```: like data_encoded but with the data scaled using StandardScaler()
