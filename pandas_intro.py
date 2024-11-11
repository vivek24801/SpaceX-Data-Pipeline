import pandas as pd
data={'rocket':['Falcon 1','Falcon 9','Falcon Heavy'],
      'launches':[5,100,3],}
df=pd.DataFrame(data)

print(df['rocket'])

fivelaunches_df=df[df['launches'] >= 5]
print(fivelaunches_df['rocket'])

df['success_rate']=[0.5,0.98,1.0]

