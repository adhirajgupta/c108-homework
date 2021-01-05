import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import random

df = pd.read_csv("student.csv")

fig = ff.create_distplot([df.Avg.tolist()],["Avg"],)
fig.show()

