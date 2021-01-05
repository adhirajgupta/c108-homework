import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import random

df = pd.read_csv("student.csv")
data = df.Avg
group_labels = str(df.Mobile)


fig = ff.create_distplot([data],[group_labels])
fig.show()

