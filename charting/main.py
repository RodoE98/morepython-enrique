#!/bin/python3
from pygal import Bar

# Create a chart
#chart = Bar(title = 'Olympic medals')
#chart = Bar(title = "Population")
chart = Bar(title = "GDP")

# Add data to the chart
#with open('medals.csv') as f:
    #for line in f:
        #print(line)
        #pieces = line.split(',') # Breaks the string into a list
        #print(pieces) # Print each list
        #team = pieces[0]
        #medals = pieces[1]
        #chart.add(team, int(medals))  # Make medals a number
#with open('pop.csv') as f:
 #   for line in f:
  #      #print(line)
  #      pieces = line.split(',')
  #      #print(pieces)
   #     team = pieces[0]
  #      population = pieces[1]
   #     chart.add(team, int(population))  # Make population a number
with open('gdp.csv') as f:
    for line in f:
        #print(line)
        pieces = line.split(',')
        #print(pieces)
        team = pieces[0]
        gdp = pieces[1]
        chart.add(team, float(gdp))  # Make GDP a number

# Display the chart
chart.render()