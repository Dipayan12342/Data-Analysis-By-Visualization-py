import pandas as pd 
import csv
import plotly.express as px 

df = pd.read_csv("data.csv")
dipayan = df.groupby(["student_id", "level"], as_index = False)["attempt"].mean()
fig = px.scatter(dipayan, x="student_id", y="level", size="attempt", color="attempt")
fig.show()
