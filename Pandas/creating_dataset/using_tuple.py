#using tuple
import pandas as pd
wheather =[('1/1/2020',45,5,'sunny'),
           ('7/4/2018',85,8,'rainy'),
           ('10/5/2002',35,4,'snow')]
df = pd.DataFrame(wheather,columns=['day','temp','windspeed','event'])
print(df) 