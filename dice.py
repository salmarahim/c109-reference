import random
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go

dice_result=[]
for i in range(0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice_result.append(dice1+dice2)

mean=statistics.mean(dice_result)
median=statistics.median(dice_result)
mode=statistics.mode(dice_result)
standard_dev=statistics.stdev(dice_result)


first_stdev_start,first_stdev_end=mean-standard_dev,mean+standard_dev
second_stdev_start,second_stdev_end=mean-(2*standard_dev),mean+(2*standard_dev)
third_stdev_start,third_stdev_end=mean-(3*standard_dev),mean+(3*standard_dev)

fig=ff.create_distplot([dice_result],["Result"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[first_stdev_start,first_stdev_start],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_stdev_end,first_stdev_end],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_stdev_start,second_stdev_start],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_stdev_end,second_stdev_end],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 2"))



list_of_data_within_first_stdev=[result for result in dice_result if result>first_stdev_start and result<first_stdev_end]
list_of_data_within_second_stdev=[result for result in dice_result if result>second_stdev_start and result<second_stdev_end]
list_of_data_within_third_stdev=[result for result in dice_result if result>third_stdev_start and result<third_stdev_end]

print("The mean is {}".format(mean))
print("The median is {}".format(median))
print("The mode is {}".format(mode))
print("The standard deviation is {}".format(standard_dev))


print("{} % is within the first standard deviation".format(len(list_of_data_within_first_stdev)*100/len(dice_result)))
print("{} % is within the second standard deviation".format(len(list_of_data_within_second_stdev)*100/len(dice_result)))
print("{} % is within the third standard deviation".format(len(list_of_data_within_third_stdev)*100/len(dice_result)))