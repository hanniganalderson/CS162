import matplotlib.pyplot as plot
# set up your lists
numlist = [13, 2, 1, 19]
namelist = ['strawberry', 'blueberry', 'green apple', 'banana']
colorlist = ['red', 'blue', 'green', 'yellow' ]
explodelist = [0.1, 0.1, 0.2, 0.2]
# make the pie chart
plot.pie(numlist, labels=namelist, autopct='%.1f%%', colors=colorlist,
    	explode = explodelist, startangle = 900)
plot.axis('equal')
plot.savefig('piechart.png')
