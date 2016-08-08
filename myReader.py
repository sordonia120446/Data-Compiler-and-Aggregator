"""
Reads in a csv file.  Also has the option to filter out by time some 
of the transient data.  Finally, it groups by run and outputs the 
mean value of the attribute of interest per run.  

Requires venv to run pandas.  

@author Sam O.  

Created on 4/1/2016.  
"""

import pandas as pd
import csv, os 

def average_by_run(my_df,attribute):
	"""
	Takes in a dataframe and a string attribute of one of the columns 
	in the dataset.  Outputs the mean of that attribute per run.  
	"""
	my_data = my_df.groupby('Run').mean()
	return my_data[attribute]

def open_csvfile(csvfile):
	"""
	Reads in the csv file in subdirectory "raw_data" as a dataframe object.
	"""
	# csvfile = raw_input("What is the csv file?...")
	# csvfile = "raw_data/" + csvfile
	my_df = pd.read_csv(csvfile,encoding='latin1')
	return my_df

def remove_transient(my_df,time_delay=0):
	"""
	Removes the first few seconds of the dataset (default is zero seconds
	removed).  
	"""
	steady_state_data = my_df[my_df['Time'] > time_delay]
	return steady_state_data

def iterate_over_files(path):
	file_list = []
	main_dir = os.getcwd()
	new_dir = main_dir + "/raw_data"
	os.chdir(new_dir)
	for file in os.listdir(path):
		if file.endswith(".csv"):
			my_df = open_csvfile(file)
			file_list.append(my_df)
	os.chdir(main_dir)
	return file_list

"""
Driver:  

Specify how much transient [sec] need to be filtered out.  
Name the attribute(s).  For >1 attribute, make an array.  
Outputs aggregate data into output.csv.  
"""
time_delay = 4
attribute = "Source Power"

path = os.getcwd() + "/raw_data"
my_files = iterate_over_files(path)
print(my_files)

my_df = open_csvfile()
modified_df = remove_transient(my_df,time_delay)
stuff = average_by_run(modified_df,attribute)
stuff.to_csv("output.csv")




