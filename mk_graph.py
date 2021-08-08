from plotnine import *
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('result.csv', encoding = 'utf8')

df = df.rename(columns = {"회복탄력성":"resilience"})
df = df[df['성별']=='F']

X = df['resilience']
Y = df['FAA']


fig = plt.Figure()

(
ggplot(df, aes(x=X,  y=Y)) 
+ labs(title = "Female")
+ geom_point(color = '#ff0066', size = 3)
+ stat_smooth(method='lm', se=False, color = '#990000', linetype = '--')
+ geom_text(x=200, y=0.06, label="r =.285")
)


(
ggplot(df, aes(x=X,  y=Y)) 
+ labs(title = "Correlation of FAA & resilience")
+ geom_point(color = 'black', size = 3)
+ stat_smooth(method='lm', se=False, color = 'gray', linetype = '--')
+ geom_text(x=230, y=0.09, label="r =.436*")
)


