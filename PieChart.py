# This is the python program to create well functioning Pie Chart in Python
# We need Matplotlib python library and Pyplot module from the matplotlib library
# let's start !!!

import matplotlib.pyplot as plt

# let's give labels to the pie chart blocks

labels = ['A','B','C'] # We created a list to store labels

sizes = [20,50,30] # These are the precentage portions of A,B,C blocks in pie chart

explode = (0 , 0 ,0.5) # This is used to separate the blocks from pie chart ,We use value inbetween 0 and 1 . We separated 3rd block here .
# because we used separation measurement on third block .

fig1 , ax = plt.subplots()
# pie() is used to finally give measurements to pie chart
# sizes and labes are the lists as we defines and assigned above
# autpct is used to show the percentile measurement upto desired fractions .
# shadow is used to provide shadow feature if it is True .
# startangle sets the first block of pie chart to a required angle , we are using 90 degree .

ax.pie(sizes , labels=labels , autopct= '%1.2f%%' , shadow = True , startangle= 90 , explode= explode )

# axis() is used to ensure the aspect ratio for complete pie chart 
ax.axis('equal')

# finally use show() of pyplot to display chart
plt.show()

# Let's see the output 
