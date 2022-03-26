# Imports
import string
import plotly.express as px
import pandas as pd

def lazer(df: pd.DataFrame, axis: string, axisx,axisy):
    for i in range(len(df.index)):
			  print(df.iloc(i))

data = [
	{'player': 1, 'x': 0, 'y': 0, 'z': 0},
	{'player': 1, 'x': 1, 'y': 0, 'z': 0}
]
df = pd.DataFrame(columns=['player','x','y','z'], data=data)

print(df)

fig = px.scatter_3d(df, color='player', x='x', y='y', z='z', hover_data=['player'])
fig.update_layout(scene_zaxis_type="log")
fig.show()
lazer(df,'x',1,1)
