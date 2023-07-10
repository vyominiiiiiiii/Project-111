import pandas as pd
import plotly.express as px
import statistics
import plotly.figure_factory as ff
import random
import csv
import plotly.graph_objects as go

df=pd.read_csv("medium_data.csv")
data=df["reading_time"].to_list()

def random_set_of_mean(counter):
    dataSet=[]
    for i in range(0,counter):
        randomIndex=random.randint(0,len(data)-1)
        x=data[randomIndex]
        dataSet.append(x)
    
    mean=statistics.mean(dataSet)
    return mean

meanList=[]
for i in range(0,100):
    setOfMeans=random_set_of_mean(30)
    meanList.append(setOfMeans)

stdv=statistics.stdev(meanList)
mean=statistics.mean(meanList)
print(stdv,mean)

first_stdv_start,first_stdv_end=mean-stdv,mean+stdv
second_stdv_start,second_stdv_end=mean-(2*stdv),mean+(2*stdv)
third_stdv_start,third_stdv_end=mean-(3*stdv),mean+(3*stdv)

df1=pd.read_csv("sample_1.csv")
data1=df1["reading_time"].to_list()

mean_sample1=statistics.mean(data1)
print("Sample 1 :",data1)

fig1=ff.create_distplot([meanList],["Student marks"],show_hist=False)
fig1.add_trace(go.Scatter(x=[mean,mean],y=[0,1.4],mode="lines",name="Mean"))

fig1.add_trace(go.Scatter(x=[first_stdv_start,first_stdv_start],y=[0,1.4],mode="lines",name="First standard deviation start"))
fig1.add_trace(go.Scatter(x=[first_stdv_end,first_stdv_end],y=[0,1.4],mode="lines",name="First standard deviation end"))

fig1.add_trace(go.Scatter(x=[second_stdv_start,second_stdv_start],y=[0,1.4],mode="lines",name="Second standard deviation start"))
fig1.add_trace(go.Scatter(x=[second_stdv_end,second_stdv_end],y=[0,1.4],mode="lines",name="Second standard deviation end"))

fig1.add_trace(go.Scatter(x=[third_stdv_start,third_stdv_start],y=[0,1.4],mode="lines",name="Third standard deviation start"))
fig1.add_trace(go.Scatter(x=[third_stdv_end,third_stdv_end],y=[0,1.4],mode="lines",name="Third standard deviation end"))

fig1.add_trace(go.Scatter(x=[mean_sample1,mean_sample1],y=[0,1.4],mode="lines",name="Mean of students who had Math labs"))

fig1.show()



df2=pd.read_csv("sample_2.csv")
data2=df2["reading_time"].to_list()

mean_sample2=statistics.mean(data2)
print("Sample 2 :",data2)

fig2=ff.create_distplot([meanList],["Student marks"],show_hist=False)
fig2.add_trace(go.Scatter(x=[mean,mean],y=[0,1.4],mode="lines",name="Mean"))

fig2.add_trace(go.Scatter(x=[first_stdv_start,first_stdv_start],y=[0,1.4],mode="lines",name="First standard deviation start"))
fig2.add_trace(go.Scatter(x=[first_stdv_end,first_stdv_end],y=[0,1.4],mode="lines",name="First standard deviation end"))

fig2.add_trace(go.Scatter(x=[second_stdv_start,second_stdv_start],y=[0,1.4],mode="lines",name="Second standard deviation start"))
fig2.add_trace(go.Scatter(x=[second_stdv_end,second_stdv_end],y=[0,1.4],mode="lines",name="Second standard deviation end"))

fig2.add_trace(go.Scatter(x=[third_stdv_start,third_stdv_start],y=[0,1.4],mode="lines",name="Third standard deviation start"))
fig2.add_trace(go.Scatter(x=[third_stdv_end,third_stdv_end],y=[0,1.4],mode="lines",name="Third standard deviation end"))

fig2.add_trace(go.Scatter(x=[mean_sample2,mean_sample2],y=[0,1.4],mode="lines",name="Mean of students who used the App"))

fig2.show()



df3=pd.read_csv("sample_3.csv")
data3=df3["reading_time"].to_list()

mean_sample3=statistics.mean(data3)
print("Sample 3 :",data3)

fig3=ff.create_distplot([meanList],["Student marks"],show_hist=False)
fig3.add_trace(go.Scatter(x=[mean,mean],y=[0,1.4],mode="lines",name="Mean"))

fig3.add_trace(go.Scatter(x=[first_stdv_start,first_stdv_start],y=[0,1.4],mode="lines",name="First standard deviation start"))
fig3.add_trace(go.Scatter(x=[first_stdv_end,first_stdv_end],y=[0,1.4],mode="lines",name="First standard deviation end"))

fig3.add_trace(go.Scatter(x=[second_stdv_start,second_stdv_start],y=[0,1.4],mode="lines",name="Second standard deviation start"))
fig3.add_trace(go.Scatter(x=[second_stdv_end,second_stdv_end],y=[0,1.4],mode="lines",name="Second standard deviation end"))

fig3.add_trace(go.Scatter(x=[third_stdv_start,third_stdv_start],y=[0,1.4],mode="lines",name="Third standard deviation start"))
fig3.add_trace(go.Scatter(x=[third_stdv_end,third_stdv_end],y=[0,1.4],mode="lines",name="Third standard deviation end"))

fig3.add_trace(go.Scatter(x=[mean_sample3,mean_sample3],y=[0,1.4],mode="lines",name="Mean of students who were enforced with math registers"))

fig3.show()


z_score1=(mean_sample1-mean)/stdv
print(z_score1)

z_score2=(mean_sample2-mean)/stdv
print(z_score2)

z_score3=(mean_sample3-mean)/stdv
print(z_score3)


