import pandas 

print("Welcome to Golfly")

print("Importing Data...")

dtype = {
    "player_name" : str,
    "date": str,
    "tournament": str,
    "statistic": str,
    "variable": str,
    "value": str
    }

data = pandas.read_csv(
    "./Data/PGA_Data_Historical.csv", 
    sep=',',
    quotechar='"',
    dtype={
        "player_name" : str,
        "tournament": str,
        "statistic": str,
        "variable": str,
        "value": str
    },
    parse_dates=['date']) 

print("Data Imported")
print("# of records: " + str(data.size))

listOfStats = data.groupby(['statistic'])['variable'].unique() 
print(listOfStats)