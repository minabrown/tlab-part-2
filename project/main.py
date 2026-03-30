from cleaner import clean_heartrate_data  # bring in the cleaning function from cleaner.py
from stats import average, median, range  # bring in the stat functions from stats.py
import pandas as pd
import matplotlib.pyplot as plt


def run(file: str):
    """
    Process heart rate data from the a file by cleaning and
    calculating summary statistics. Print out final values.

    Args:
        filename (str): The path to the data file (e.g., 'data/phase0.txt').

    Returns:
        float, float, float: You will return the average, median, and range.
    """
    data = []

    # open file using file I/O and read it into the `data` list
    file_object = open(file)
    for line in file_object:
        data.append(line.strip())   # strip() removes extra spaces and newlines
    file_object.close()


    # Use `clean_heartrate_data` to clean the data and remove invalid entries
    cleaned_list, removed_values = clean_heartrate_data(data)

    # calculate the average, median, and range of this file using the functions you've wrote
    avg = average(cleaned_list)
    med = median(cleaned_list)
    ran = range(cleaned_list)


    # print out your data quality measures to the console
    print(f" File: {file}")                          # print out the file name being processed
    print(f" Total rows: {len(data)}, Valid rows: {len(cleaned_list)}, Skipped rows: {len(removed_values)}")  # print out the total number of rows, valid rows, and skipped rows
    
    
    
    
    '''# print out your descriptive statistics to the console
    #print(average.describe())           #print out the descriptive statistics of the average value
    #print(median.describe())            #print out the descriptive statistics of the median value
    #print(range.describe())             #print out the descriptive statistics of the range valu'''
    
    
    # -- To use .describe, you must first convert cleaned_list into a dataframe, using pandas -- #
    
    clean_df = pd.DataFrame(cleaned_list) #convert list into a dataframe to use .describe
    
  
   #print(clean_df.describe())      #print out the descriptive statistics of the cleaned data list
    print(avg)
    print(med)
    print(ran)
    
    
    #Data Exploration using Matplotlib
    plt.hist(clean_df)
    plt.xlabel("Heart Rate")
    plt.ylabel("Frequency")
    plt.show()
  
#remove /data from each phaseX.txt as it is contained in the same project folder
if __name__ == "__main__":
    run("phase0.txt") 
    run("phase1.txt")
    run("phase2.txt")
    run("phase3.txt")