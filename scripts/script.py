import matplotlib.pyplot as plt
import pandas as pd  # A data structure optimized for storing data in rows and columns
import seaborn as sns

def get_data():
	wiki_url = "https://en.wikipedia.org/wiki/Road_safety_in_Europe"
	dfs = pd.read_html(wiki_url) # all the tables present in the wiki page
	required_table = dfs[2]  # the table containing European Union Road Safety Facts and Figures

	required_table = dfs[2][[ 'Country', 'Area (thousands of km2)[24]', 'Population in 2018[25]', 'GDP per capita in 2018[26]', 
			 'Population density (inhabitants per km2) in 2017[27]', 'Vehicle ownership (per thousand inhabitants) in 2016[28]', 'Total Road Deaths in 2018[30]', 
			 'Road deaths per Million Inhabitants in 2018[30]']]
			 
			 
	required_table['Year'] = '2018'
	required_table.sort_values(by = ["Road deaths per Million Inhabitants in 2018[30]"],inplace=True)

	required_table.to_csv("data.csv")

	return required_table
	
	
get_data()