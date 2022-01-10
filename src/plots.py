import matplotlib.pyplot as plt
def boxplot(variables, df):
  for v in variables:
    plt.figure()
    fig = df.boxplot(column=v)
    fig.set_ylabel(v)

def histogram(x, y, df):
  plt.figure()
  fig = df[x].hist()
  fig.set_xlabel(x)
  fig.set_ylabel(y)