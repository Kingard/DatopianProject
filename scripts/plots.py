from script import *
import matplotlib.pyplot as plt
import seaborn as sns

table = get_data()

## Line Graph showing the vehicle ownership 

plt.figure(figsize=(15,12))
plt.plot(table['Road deaths per Million Inhabitants in 2018[30]'],table['Vehicle ownership (per thousand inhabitants) in 2016[28]'],label='vehicle ownership to deaths curve')
plt.plot()
plt.ylabel('vehicle ownership in thousands')
plt.xlabel('road deaths in millions')
plt.title("A graph showing how vehicle ownership influences vs road deaths")
plt.legend()
plt.show()


## stacked bar plot for vehicle ownership against area

plt.figure(figsize=(15,12))
plt.bar(table['Country'],table['Area (thousands of km2)[24]'],color='g')
plt.bar(table['Country'],table['Vehicle ownership (per thousand inhabitants) in 2016[28]'],bottom= table['Area (thousands of km2)[24]'] ,color='y')
plt.xticks(rotation = 45)
plt.title('Stacked plot for Area vs Vehicle ownership')
plt.legend(['Area(km.sq)','vehicle ownership(per thousand habitats',])
plt.show()



## Density table Plot for European Union Road Safettable Facts and Figures

plt.figure(figsize=(16,10), dpi= 80)
sns.kdeplot(table['Total Road Deaths in 2018[30]'],shade=True, color="deeppink", label="total deaths", alpha=.7)
sns.kdeplot(table['Population density (inhabitants per km2) in 2017[27]'],shade=True, color="dodgerblue", label="population density", alpha=.7)
sns.kdeplot(table['Vehicle ownership (per thousand inhabitants) in 2016[28]'],shade=True, color="orange", label="Vehicle ownership", alpha=.7)
sns.kdeplot(table['Area (thousands of km2)[24]'],shade=True, color="g", label="Area", alpha=.7)
plt.title('density Plot for European Union Road Safettable Facts and Figures', fontsize=10)
plt.legend()
plt.show()



## Density curve with histogram

plt.figure(figsize=(13,10), dpi= 80)
sns.distplot(table['Area (thousands of km2)[24]']*4, color="dodgerblue", label="Area", hist_kws={'alpha':.7}, kde_kws={'linewidth':3})
sns.distplot(table['Total Road Deaths in 2018[30]'], color="orange", label="Total road deaths", hist_kws={'alpha':.7}, kde_kws={'linewidth':3})
sns.distplot(table['Population density (inhabitants per km2) in 2017[27]']*6, color="g", label="population density", hist_kws={'alpha':.7}, kde_kws={'linewidth':3})
#plt.tablelim(0, 0.35)
plt.title('density curve (with histogram) for European Union Road Safettable Facts and Figures', fontsize=10)
plt.legend()
plt.show()