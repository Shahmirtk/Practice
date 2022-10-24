import pandas as pd
import matplotlib.pyplot as plt

#use pd.read_csv(r'<path>') if file not here
##df = pd.read_csv('coffee.csv')

##print(pd.options.display.max_rows)
##pd.options.display.max_rows = 9999

##print(df.to_string())

## key becomes column name, values become row values
##mydataset = {
##  'car': ["BMW", "Volvo", "Ford"],
##  'passing': [3, 7, 2]
##}
##
##my_df = pd.DataFrame(mydataset, index=["b", "v", "f"])
##
##print(my_df.loc[["b", "v"]])

##print(pd.__version__)

df = pd.read_json('data.js')

###print the entire dataframe
##print(df.to_string())
##
###print the first n rows
##print(df.head(10))
##
###print the last n rows
##print(df.tail(12))
##
###print the info of df, including count of Non-Null values
##print(df.info())

###creates a new df with rows with empty cells dropped
##new_df = df.dropna()
##
##print(new_df.to_string())
##
###replaces the original df (does not change file)
##df.dropna(inplace = True)

###only dropna for a subset of the df
##df.dropna(subset=['Calories'], inplace = True)

###you can also use median() or mode()[0]
##calories_mean = df["Calories"].mean()
##
##x = calories_mean
###replace the empty values with x
##df["Calories"].fillna(x, inplace = True)

###convert to DateTime object
##df['Date'] = pd.to_datetime(df['Date'])

###replace the cell at row with index 9 and column with name "Pulse" to 45
###this does not change the original file
##df.loc[9, 'Pulse'] = 45
##
##print(df.head(10))

###remove all duplicates
##df.drop_duplicates(inplace = True)

#table represents how well the relationship is between two columns
print(df.corr(), "<.")

#plot a graph
df.plot()

plt.show()

#plot a hist of 'Duration' column
df["Duration"].plot(kind = 'hist')

plt.show()

print(df.info())
