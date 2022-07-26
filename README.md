[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=7762001&assignment_repo_type=AssignmentRepo)
# Final Project

# 1. Project Introduction, Purpose and Goal

With this project, we aim to compare six Environmental, Social and Governance (ESG) metrics for six global regions. These regions include both dveeloped and developing nations. This allows us to visalize the differences between each ESG metric for all regions. 

The regions are:
European Union
Latin America & Carribean
Middle East & North Africa
North America
South Asia
Sub-Saharan Africa

The 6 ESG metrics are as follows: 
Social:
1. Access to clean fuels and technologies for cooking (% of population)
2. Access to electricity (% of population)
Environmental:
3. CO2 emissions (metric tons per capita)
4. Fossil fuel energy consumption (% of total)
Governance:
5. Individuals using the Internet (% of population)
6. Ratio of female to male labor force participation rate (%)

The program asks the user for some inputs and prints a time-series graph to show the change in the metric over time for the individual metric or for all regions. The results are shown in the sections below. 

# 2. Installation of modules

The program uses two modules, numpy and matplotlib. They are installed using the syntax given below. 
import numpy as np
import matplotlib.pyplot as plt

'NumPy': NumPy offers comprehensive mathematical functions, random number generators, linear algebra routines, Fourier transforms, and more. (https://numpy.org/)
'MatPlotLib': Matplotlib is a comprehensive library for to create visualizations in Python.(https://matplotlib.org/)

# 3. Running of program 

The program uses four functions to extract, modify, represent and visualize the data. The four functions are given below. 
 * `csvToDictOfLists(filename)`: This function converts the csv file into a dictionary of lists. As we needed the keys to be unique, the code accomodates this by using the line number as the key. 'curr_line' = a list containing the comma-separated values from the csv file.
* `filterByColumn(dictionary, s, index)`: The function takes in three arguments, the specified dictionary, a string and an associated column index. It returns a list of keys after the dictionary is filtered with the the input string 's'.
* `extractValues(dictionary, years, indices, indexFlag=False)`: The function takes in four arguments. indexFlag is a flag to denote whether indices is a single index or a list of indices. 
* `plotGraph(dictionary, result, years, indices)`: This function takes in four arguments and returns a line graph with the legend on the right side, outside the plot. 

Execution of the program:
The program asks the user for either a number (for the ESG metrics) or a region that they want to explore. It then asks prompts based on the input. 

Case 1. If the user inputs a number, it returns a graph of the specific ESG metric for all the regions. 
Case 2. If the user inputs a region, it prompts for single or multiple numbers correlating to the specific ESG metrics. It returns the requested graph(s). 

After the graphs are shown, the user is further asked if they want to proceed with other regions or metrics. 

# 4. Screenshots of program running
<img width="743" alt="program running 1" src="https://user-images.githubusercontent.com/101598255/166811709-4c699a65-71a1-4f00-aa93-f5a67a33e98f.png">

<img width="664" alt="program running 2" src="https://user-images.githubusercontent.com/101598255/166811727-3038c583-7983-4ef8-9806-53fcdce0775d.png">


# 5. Results of program

###### CO2 emissions for all six regions:

![figure 1](https://user-images.githubusercontent.com/101598255/166811816-f3c033d1-c79e-41dc-af03-be96068976db.png)

###### CO2 emissions for South Asia:

![figure 2](https://user-images.githubusercontent.com/101598255/166811829-a533ffc2-b9d8-45b2-aeea-59c871089561.png)

###### CO2 emissions for Latin America & Caribbean:

![figure 3](https://user-images.githubusercontent.com/101598255/166811837-73c3a742-8c4c-4ae5-b42c-1f4559ed5525.png)

###### Fossil Fuel Energy consumption for all regions:

![figure 4](https://user-images.githubusercontent.com/101598255/166811850-cf119046-2067-4868-bf49-b2c203201849.png)

###### Fossil Fuel Energy for North America:

![figure 5](https://user-images.githubusercontent.com/101598255/166811861-c4a9da59-a29f-4527-b249-e800ba153b39.png)

###### Ratio of female to male labor force participation rate (%) for all regions:

![figure 6](https://user-images.githubusercontent.com/101598255/166812425-2e489a28-b22a-4a16-b6b9-47949644da6b.png)


# 6. Distribution of work

`Extract data and clean data`: Kavya

`csvToDictOfLists`: Kavya

`filterByColumn`: Navishka

`extractValues`: Kavya and Navishka

`plotGraph`: Navishka

`main`: Kavya and Navishka

`ReadMe`: Kavya and Navishka

