# EXP3 - Python Data Analysis <br/> *Christian Justin M. Fernando | 2ECE-B | ECE2112*
Hello! This repository contains Python codes I made for my ECE2112 course, particularly for Experiment #3. <br/><br/> 
# For experiment #3 the **instructions** are:

**1.** Write a Python script/code in the Jupyter Notebook to solve the problems.<br/>
**2.** submit your Jupyter notebook in the dedicated submission bin.<br/>
**3.** For this programming assignment,  download the following file and save it to your default user folder: http://bit.ly/Cars_file<br/>

#### Important note: The problem outputs can be seen inside my `.ipynb` files. You can also use my `.py` executable files which leads you directly to a specific problem. 

# Problem 1 <br/>

Using knowledge obtained from the experiment and demonstrations: 

##### a. Load the corresponding .csv file into a data frame named cars using pandas 

```python
import pandas as pd

#Load cars.csv file into a data frame named cars using pandas.
cars = pd.read_csv('cars.csv')
cars
```

##### b. Display the first five and last five rows of the resulting cars. 

```python
#Display the first five rows of the resulting cars.
cars.head()

#Display the last five rows of the resulting cars.
cars.tail()
```
<br/>

**Data and Results Discussion:** In this problem, importing Pandas as pd is crucial. This is declared to be able to access the core library for Python Data Analysis; used for working with data sets.

For **part a**, make sure that you have downloaded the necessary `.csv` file to load the data set. If not, kindly refer to instruction #3. To begin, I loaded a dataset from a CSV file into a pandas data frame named cars. This step is crucial for any data analysis process, as it transforms the raw data stored in a file into a structured format that I can easily manipulate and analyze using Python. 

For **part b**, I wanted to get a quick overview of the data. I used the `.head()` function to display the first five rows, which allowed me to verify the dataset's structure, including the column names and data types. To ensure the completeness of the dataset, I also employed the `.tail()` function to view the last five rows. This helped me confirm that there were no unexpected entries at the end. 

<br/>

# Problem 2

Using the data frame `cars` in problem 1, extract the following information using subsetting, slicing and 
indexing operations.
<br/>

##### a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7…) of cars. 
```python
#Display the first five rows of the `cars` data frame, selecting every second row starting from index 1.
cars[1::2].head()
```

##### b. Display the row that contains the ‘Model’ of ‘Mazda RX4’. 
```python
#Retrieve the 'Model' column for the first row (index 0) of the `cars` data frame.
cars.loc[[0], ['Model']]
```

##### c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have? 
```python
#Calling the 'Model' and 'cyl' columns for the row at index 23 of the `cars` data frame.
cars.loc[[23], ['Model', 'cyl']]
```

##### d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have. 
```python
#Retrieve the 'Model', 'cyl', and 'gear' columns for the rows at indices 1, 28, and 18 of the `cars` data frame.
cars.loc[[1, 28, 18], ['Model', 'cyl', 'gear']]
```

**Data and Results Discussion:** Before testing this problem, you have to make sure that you have created a data frame `cars` by loading the `cars.csv` file using pandas. If not, go ahead and check part a of problem 1 to ensure that you can execute this given problem.

For **part a**, the task was to display the first five rows of the `cars` data frame while selecting every second row starting from index 1. I achieved this by using the slicing technique `cars[1::2]`, where the 1 indicates that I wanted to start from the second row and ::2 means I wanted to select every second row thereafter. This approach allowed me to create a subset of the DataFrame that skips every alternate row. After obtaining this subset, I used the `.head()` function to display the first five rows, providing a quick snapshot of the selected data.

For **part b**, I focused on the 'Model' column for the first row (index 0) of the `cars` data frame to retrieve specific information from the dataset. I used the loc method, which allows for label-based indexing. By specifying `[[0], ['Model']]`, I indicated that I wanted to access the first row and the 'Model' column. This approach enabled me to extract the relevant data point directly without displaying the entire row or data frame. 

For **part c**, I accessed the 'Model' and 'cyl' columns for the row at index 23 of the `cars` data frame to retrieve specific information from the dataset. Using the `loc` method, I specified `[[23], ['Model', 'cyl']]`, which allowed me to select both the desired columns for that particular row. This approach made extracting relevant details about the car model and its number of cylinders in a single operation easy.

For **part d**, To gather specific details from the dataset, I retrieved the 'Model', 'cyl', and 'gear' columns for the rows at indices 1, 28, and 18 of the cars data frame. I used the `loc` method and specified `[[1, 28, 18], ['Model', 'cyl', 'gear']]`. This allowed me to select multiple rows and columns in one command. By doing this, I efficiently extracted relevant information about these specific cars, enabling me to compare their models, number of cylinders, and gear configurations without the need to examine the entire data frame. This approach streamlined my data exploration and analysis process.

# About the author

The author is currently a second-year student pursuing a Bachelor's degree in Electronics Engineering. They have a strong passion for technology and are dedicated to applying their knowledge to real-world projects. In addition to their academic pursuits, the author continually seeks to expand their skill set. They are excited about the opportunities in the electronics field and aim to contribute to innovative solutions in the industry.

##### The problems above focus on Python Data Analysis. Feel free to let the author know if there is anything they can do to improve the code. Thank you!









