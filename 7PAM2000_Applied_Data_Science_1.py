
#importing the required libraries for the further analysis.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ### Function for reading the raw data and returning the Dataframe and its transpose


#function to read the raw data and returning the transpose and the woriking data for further analysis
def readData(x):
    newData=pd.read_csv(x,skiprows = 4) #reading the raw worldbank metadata.
    returnt=newData.transpose() #Transposing the dataset.
    return [newData,returnt]

#calling the function
tempData=readData("API_19_DS2_en_csv_v2_4700503.csv")


# ## Transpose Dataset

#Transpose Dataset
transposeData = tempData[1]
transposeData.head(2)


# ## Dataframe for further Analysis

#Dataset for the further analysis
main=tempData[0]
main.head(2)

#columns in dataset
main.columns

#Droping the unnecessery columns
main=main.drop(main[['Unnamed: 66']],axis=1)
main.rename(columns={'Country Name':'Country_Name','Country Code':'Country_Code','Indicator Name':'Indicator_Name','Indicator Code':'Indicator_Code'},inplace=True)
main.head(2)

#Checking the null values
main.isnull().sum()

#operation on the null values
main=main.replace(np.nan,0)
main.head()

#checking null values after operation
main.isnull().sum()

#Checking the datatypes of the columns
main.dtypes

#Data distribution descriptions
main.describe()

main.head(2)

#Fresh columns name in the dataset
main.columns

#checking the shape of the data and its columns
print("Shape of data :",main.shape,end="\n\n")
cols = main.columns.tolist()
print(cols)

#modifying the columns name for overcome the future errors
Indicator_Name=main.groupby(['Country_Name','Country_Code','Indicator_Name', 'Indicator_Code','1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']).size().reset_index()
Indicator_Name.head(2)

#after modification of the coulmns name
columns = Indicator_Name.columns.tolist()
print(columns)


# ## 1. Urban Population % Indicator

#Urban Population indexing on the dataset
Indicator_Name.set_index("Indicator_Name",inplace = True)
urban = Indicator_Name.loc["Urban population (% of total population)"]
urban.head(2)

urban = urban.drop(["Country_Code","Indicator_Code"],axis =1)
urban.head(2)

#taking the some countries for the further analysis
sample =urban[::37]
sample.head(2)

#plotting the graph for the data of the urban population of the given countires and the 10 year range
year1=['1960', '1970', '1980', '1990', '2000', '2010', '2020']
sample.plot(x= "Country_Name", y = year1,figsize = (15,6), color=["#b30000", "#7c1158", "#4421af", "#1a53ff", "#0d88e6", "#00b7c7", "#5ad45a", "#8be04e", "#ebdc78"],linewidth = '3')



temp=main.groupby(['Country_Name','Country_Code','Indicator_Name', 'Indicator_Code','1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020','2021']).size().reset_index()
temp.head(2)


# ## 2. CO2 emissions from liquid fuel consumption

#Defining the data by the co2 emission from liquid fuel form the dataset
temp.set_index("Indicator_Name",inplace = True)
u="CO2 emissions from liquid fuel consumption (kt)"
CO2 = temp.loc[u]
CO2 = CO2.drop(["Country_Code","Indicator_Code"],axis =1)
CO2.head(2)

CO2sample =CO2[::37]
CO2sample=CO2sample[["Country_Name",'1985', '1990', '1995', '2000', '2005', '2010', '2016']]
CO2sample=CO2sample.reset_index(drop=True)
CO2sample=CO2sample.set_index(['Country_Name'])
CO2sample

#Plotting the heatmap of the given dataset over the CO2 emitions
plt.figure(figsize = (16,5))
sns.heatmap(CO2sample,annot=True, fmt=".1f",linewidth=1,cmap="tab10")


# ## 3. Forest area measures

#Analysis the dataset over the forest area of the selected countries
frst="Forest area (% of land area)"
forest = temp.loc[frst]


forest = forest.drop(["Country_Code","Indicator_Code"],axis =1)
forest.head(2)


#Plotting the bar graph for the forest area changes by the year basis.
yax=['1985', '1990', '1995', '2000', '2005', '2010', '2016']
forestSample =forest[::37]
forestSample.plot(x= "Country_Name", y = yax,kind = "bar",figsize = (15,6),logy = True,color=["#ea5545", "#f46a9b", "#ef9b20", "#edbf33", "#ede15b", "#bdcf32", "#87bc45", "#27aeef", "#b33dc6"])


# # 4. Access to electricity (% of population)

#Taking the access of electricity example for anlysis over the climate change on the year
Electricity="Access to electricity (% of population)"
Electricity = temp.loc[Electricity]

Electricity = Electricity.drop(["Country_Code","Indicator_Code"],axis =1)
Electricity.head(2)

yaxEle=['1990', '1995', '2000', '2005', '2010', '2015', '2020']
ElectricitySample =Electricity[::37]

ElectricitySample.head(2)

#plotting the graph
ElectricitySample.plot(x= "Country_Name", y = yaxEle,kind = "bar",figsize = (15,6),logy = True,color=["#2e2b28", "#3b3734", "#474440", "#54504c", "#6b506b", "#ab3da9", "#de25da", "#eb44e8", "#ff80ff"])


# # 5. Renewable energy production

#For the further analysis we took the example of the renewable energy production that helps to reduces the risk of climate change
Renewable="Electricity production from renewable sources, excluding hydroelectric (% of total)"
Renewable = temp.loc[Renewable]

Renewable_energy = Renewable.drop(["Country_Code","Indicator_Code"],axis =1)
Renewable_energy.head(2)

sampleEnergy =Renewable_energy[::37]
sampleEnergy=sampleEnergy[["Country_Name",'1980','1985', '1990', '1995', '2000', '2005', '2010', '2016']]
sampleEnergy=sampleEnergy.reset_index(drop=True)
sampleEnergy1=sampleEnergy
sampleEnergy=sampleEnergy.set_index(['Country_Name'])
sampleEnergy


#Plotting the heatmap of the taken sample of the coutries for analysis
plt.figure(figsize = (16,5))
sns.heatmap(sampleEnergy,annot=True, fmt=".1f",linewidth=1,cmap="YlGnBu")


# ## Table Plot of FDI over GDP


#Foreign Direct Investment that help in the gdp over the change of the climate of the countries
fdiGDP="Foreign direct investment, net inflows (% of GDP)"
fdiGDP = temp.loc[fdiGDP]

GDP = fdiGDP.drop(["Country_Code","Indicator_Code"],axis =1)
GDP.head(2)

GDP =GDP[::37]
GDP=GDP[['Country_Name','1990', '1995', '2000', '2005', '2010', '2015','2020']]
GDP=GDP.reset_index(drop=True)
GDP

#Plotting the table graph that helps us to identify which is going beast FDI and GDP records.
figure, axis = plt.subplots(dpi=200)
figure.patch.set_visible(False)
axis.axis('off')
axis.axis('tight')
plt.title("Electricity production from renewable sources, excluding hydroelectric (% of total)")
table = axis.table(cellText=GDP.values, colLabels=GDP.columns, loc='center')
figure.tight_layout()
plt.show()


