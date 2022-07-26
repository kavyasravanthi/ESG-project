"""
This program uses database from the World Bank ESG platform. The database includes six ESG metrics for six global regions. 
Based on the user inputs, the program returns a graphical respresentation of the data over time. 

References are given below the program. 
@Kavya and Navishka [add your names]
"""
import numpy as np
import matplotlib.pyplot as plt

def csvToDictOfLists(filename):
  #this function, similar to HW5, takes in a csv file and returns a dictionary of lists
   f = open(filename, 'r')

   dictionary = {}
   years = np.array([])
   i = 0
   
   for line in f:
     curr_line = line.split(',')
     curr_line[-1] = curr_line[-1].strip()

     if i == 0:
      years = np.array(curr_line)
     elif i != 0:
      dictionary[i] = curr_line

     i = i + 1

   f.close()

   return dictionary, years

def filterByColumn(dictionary, s, index): 

  result = []

  for key in dictionary.keys():
    if s.lower() in dictionary[key][index].lower():
        result.append(key)

  return result

def extractValues(dictionary, years, indices, indexFlag=False): 
  # function takes in four arguments 
  # indexFlag is a flag to denote whether indices is a single index or a list of indices. 
  # indexFlag is true when values are extracted only for a single region for a single metric. 
  # indexFlag is false when values are extracted only for a multiple regions for a single metric. 
  result = []
  valueVectorLength = []
  yearsToUse = []

  if indexFlag:  
    result = np.zeros((1, 1))
    valueVectorLength = len(dictionary[indices]) 
  else:  
    result = np.zeros((len(indices), 1))
    valueVectorLength = len(dictionary[indices[0]])

  for j in range(2, valueVectorLength): #need to consider from third column in the csv
    skipFlag = False
    #skipFlag is a flag which is true until data is available for all indicies, as data may not be available for all years in the csv file. 

    temp = np.zeros((1, 1))

    if not indexFlag:
      temp = np.zeros((len(indices), 1))

    if not indexFlag:
      for i in range(len(indices)): #checks if any of the data for that year is available 
        if dictionary[indices[i]][j] == '..':
          skipFlag = True
          break

        temp[i, 0] = dictionary[indices[i]][j]

      if skipFlag == True: #we want it to skip the '..' data and use only numerical data in the file
        continue
    else:
      if dictionary[indices][j] == '..':
        continue
      
      temp[0, 0] = dictionary[indices][j]
    
    # 'yearsToUse' is a list that holds years that data is available for all regions. Ex: one country doesn't have data in between and data starts at different yesrs for each metric
    yearsToUse.append(int(years[j]))
    result = np.append(result, temp, axis = 1)

  result = np.delete(result, 0, axis = 1)
  
  return result, np.array(yearsToUse)

def plotGraph(dictionary, result, years, indices):

  x = years
  for i in range(len(indices)):
    y = result[i,:]
    plt.plot(x, y, label=dictionary[indices[i]][0])
    plt.legend(bbox_to_anchor=(1.04,1), loc="upper left")

  plt.title(dictionary[indices[0]][1])
  plt.xlabel('Years')
  plt.ylabel(dictionary[indices[0]][1])
 
  plt.show()
  plt.close()


def main():
  print("Welcome to our Environmental, Social and Governance(ESG) Comparison Tool")
  print("This is a comparison tool for the ESG Metrics.")

  print("\nThe 6 ESG metrics are as follows: ")
  print("1. Access to clean fuels and technologies for cooking (% of population)")
  print("2. Access to electricity (% of population)")
  print("3. CO2 emissions (metric tons per capita)")
  print("4. Fossil fuel energy consumption (% of total)")
  print("5. Individuals using the Internet (% of population)")
  print("6. Ratio of female to male labor force participation rate (%)")

  print("\nAvailable regions are listed below: ")
  print("European Union")
  print("Latin America & Carribean")
  print("Middle East & North Africa")
  print("North America")
  print("South Asia")
  print("Sub-Saharan Africa")

  continue_flag = 'y'

  while continue_flag == 'y':

    data = input('\nPlease enter a number from 1-6 or the name of a region: ')
    dictionary, years = csvToDictOfLists('projectdata.csv')
    
    filteredIndices = []
    # String input is a flag to indicate whether the input is a string or a number. 
    stringInput = False

    if data == '1':
      filteredIndices = filterByColumn(dictionary, 'clean fuels', 1)
    elif data == '2':
      filteredIndices = filterByColumn(dictionary, 'electricity', 1)
    elif data == '3':
      filteredIndices = filterByColumn(dictionary, 'emissions', 1)
    elif data == '4':
      filteredIndices = filterByColumn(dictionary, 'fossil fuel', 1)
    elif data == '5':
      filteredIndices = filterByColumn(dictionary, 'internet', 1)
    elif data == '6':
      filteredIndices = filterByColumn(dictionary, 'labor force', 1)
    else:

      filteredIndices = filterByColumn(dictionary, data, 0)
      stringInput = True #here we know it is a string

      columns_chosen = input("\nEnter a number between 1-6 according to the metric list above: ")
      
      columns_chosen = columns_chosen.split(' ')
      # column_indices is a list of filtered indices from the columns_chosen list
      column_indices = [filteredIndices[int(x) - 1] for x in columns_chosen]
      originalYears = years

      for i in range(len(column_indices)):
        # extracting values for a specific region for each metric and plotting it
        index = column_indices[i]
        result, years = extractValues(dictionary, originalYears, index, True)
        plotGraph(dictionary, result, years, [index])

    if not stringInput:
      # extracting values for all regions for a specific metric and plotting it
      result, years = extractValues(dictionary, years, filteredIndices)
      plotGraph(dictionary, result, years, filteredIndices)

    continue_flag = input("\nWould you like to continue? (Y/N): ").lower()
 
###
# Do not delete the following lines of code. Add the body of your code to the main() function.
###
if __name__ == "__main__":
    main()

"""""
References: 

Flags :  https://www.geeksforgeeks.org/use-of-flag-in-programming/ 

Matplotlib : https://stackoverflow.com/questions/4700614/how-to-put-the-legend-outside-the-plot-in-matplotlib  

Worldbank ESG database : https://datacatalog.worldbank.org/search/dataset/0037651

"""