import pandas as pd
wheather = {'day':["1/1/2020","4/5/1033","4/2/1565"],
           'temperature':[45,84,65],
           'windspeed':[4,4,5],
           'event':["rainy","sunny","snow"]}
df = pd.DataFrame(wheather)
print(df)