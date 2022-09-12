import pandas as pd

##df = pd.read_csv(r'C:\Users\shahm\Downloads\coffee.csv')

##print(df.to_string())

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

my_df = pd.DataFrame(mydataset)

print(my_df)

print(pd.__version__)
