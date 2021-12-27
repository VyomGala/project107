import pandas as pd
import plotly.express as px


fig = pd.read_csv("project107.csv")
print(fig.groupby(["student_id","level"])["attempt"].mean())
mean= fig.groupby(["student_id","level"],as_index=False)["attempt"].mean()
graph = px.scatter(mean,x="student_id",y="level",color="attempt",size="attempt")
graph.show()