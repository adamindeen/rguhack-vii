# Imports
import string
import plotly.express as px
import pandas as pd
import numpy as np

# The board
# a = np.zeros((3, 3, 3))
# m = np.array([[[ 0.,  0.,  0.,  0.],
#         [ 0.,  0.,  0.,  0.],
#         [ 0.,  0.,  0.,  0.]],

#        [[ 0.,  0.,  0.,  0.],
#         [ 0.,  0.,  0.,  0.],
#         [ 0.,  0.,  0.,  0.]]])

def lazer(df: pd.DataFrame, axis: string, axisx,axisy):
    for i in range(len(df.index)):
        
        print(df[i])


df = pd.DataFrame(columns=['player','x','y','z'])
df.add(1,0,0,0)
df.add(1,1,0,0)
print(df)

# fig = px.scatter_3d(df, color='player', x='x', y='y', z='z', hover_data=['player'])
# fig.update_layout(scene_zaxis_type="log")
# fig.show()
lazer(df,'x',1,1)
