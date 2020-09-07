import pandas 

print("Welcome to Golfly")

print("Importing Data...")

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

# listOfStats = data.groupby(['statistic'])['variable'].unique() 
# listOfStats.to_json("./Data/statistics.json")

listOfWinnings = data.query("statistic == 'Official Money' and variable == 'MONEY'")
print("List of winnings retrieved")

# clean up values
listOfWinnings['value'] = listOfWinnings['value'].replace('[\$,]', '', regex=True)
listOfWinnings['value'] = pandas.to_numeric(listOfWinnings.value, errors='coerce')
print("Cleaned up values")

# sum all of each players winnings
highestEarningOutput = listOfWinnings.groupby(['player_name'])[['value']].sum()
# sort in descending order
highestEarningOutput = highestEarningOutput.sort_values(by=['value'], ascending=False)
highestEarningOutput.to_json("./Data/highestEarningOutput.json")
print("Highest Earners calculated")

highestAvgEarningOutput = listOfWinnings.groupby(['player_name'])[['value']].mean()
highestAvgEarningOutput = highestAvgEarningOutput.sort_values(by=['value'], ascending=False)
highestAvgEarningOutput.to_json("./Data/highestAvgEarningOutput.json")
print("Best Average Earners calculated")