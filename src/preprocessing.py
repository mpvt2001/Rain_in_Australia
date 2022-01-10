def outliers(df, variable):
  IQR = df[variable].quantile(0.75) - df[variable].quantile(0.25)
  low = df[variable].quantile(0.25) - 3*IQR
  upp = df[variable].quantile(0.75) + 3*IQR
  return low, upp