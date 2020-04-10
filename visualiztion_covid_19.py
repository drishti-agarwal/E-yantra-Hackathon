
import numpy as np

import matplotlib.pyplot as plt

import datetime 
import pandas as pd
import seaborn as sns

covid_data = pd.read_csv("C:\\Users\\BADMAN\\Downloads\\novel-corona-virus-2019-dataset\\covid_5_4.csv", encoding='cp1252')

# print(covid_data.head())


# print(covid_data.isnull())

# print(covid_data.isnull().sum())

df1 = covid_data.drop(['State code','Patient Number','Contracted from which Patient (Suspected)','Notes','Type of transmission','Source_1','Source_2','Source_3','Contracted from which Patient (Suspected)','Detected City','Backup Notes','Age Bracket','Gender','State Patient Number','Nationality'],axis=1)

# print(df1.columns)


#print(df1)

#df1 = df1.dropna()

#df1 = covid_data

df1 = df1.dropna()

#print(df1.isnull().sum())

#df1 = df1.sort_values(by=['Date Announced'],ascending=False)

# df1['Date Announced'] =pd.to_datetime(df1['Date Announced'])

# print(df1.sort_values('Date Announced',ascending=False))

#print(df1)

# gr = df1.groupby(['Detected District','Date Announced']).count()

#print(gr['Status Change Date'])
 
# for y in df1['Detected District'].sort_values(ascending=True).unique():
# 	print(y)

# for x in gr:
# 	print(x)

print(len(df1['Detected District'].sort_values(ascending=True).unique()))

graph_data_death = []
graph_data_date = []
district_arr = []

date_arr = []

death_arr = []

# print(df1.groupby(['Detected District','Date Announced']).count())

for name, group in df1.groupby(['Detected District','Date Announced']):
	#print("gigi")
	if name[0] not in district_arr:
		# print(name[0])
		district_arr.append(name[0])
		graph_data_date.append(date_arr)
		graph_data_death.append(death_arr)
		date_arr = []
		death_arr = []

	#print(district_arr)

	date_arr.append(name[1])
	death_arr.append(group.count(axis = 0)[0])
	#print(death_arr)


graph_data_date.append(date_arr)

graph_data_death.append(death_arr)

graph_data_death.pop(0)
graph_data_date.pop(0)

print(district_arr)
print(graph_data_death)
print(graph_data_date)


# date = '03/03/2020'


# date_object = datetime.strptime(date, '%m/%d/%y')


# print(date_object)

for tub in range(len(district_arr)):


	x_date = []
	x = graph_data_date[tub]
	timestamps =x
	y = graph_data_death[tub]
	# print(y)
	# print(x)

	for txt in x:
		temp = txt.split("/")
		#print(temp)
		# print(datetime.datetime(int(temp[2]),int(temp[1]),int(temp[0])).strftime("%d-%b-%y"))
		x_date.append(datetime.datetime(int(temp[2]),int(temp[1]),int(temp[0])).strftime("%d-%b-%y"))

	#x_date.sort()

	#x = ['03-Apr-20', '03-Sep-20', '04-Apr-20', '04-Feb-20', '04-Jan-20', '04-Mar-20', '04-May-20']

	x_date.sort(key=lambda date: datetime.datetime.strptime(date, "%d-%b-%y"))

	#print(x_date)
	x = x_date
	colors = (0,0,0)
	#area = np.pi*3

	# Plot

	# my_data = pd.DataFrame({'x':x, 'y':y})

	# sns.lineplot(x="dates", y="deaths",hue="event", style="event", markers=True,data=my_data)

	plt.ion()
	
	fig= plt.figure(figsize=(20,10))

	axes= fig.add_axes([0.1,0.1,0.8,0.8])

	plt.title(district_arr[tub])
	plt.xticks(rotation=45)
	plt.xlabel('Dates')
	plt.ylabel('Deaths')

	#plt.plot(x, y, c=colors, alpha=0.5)



	plt.scatter(x,y)
	axes.plot(x,y)
	plt.savefig('C:\\Users\\BADMAN\\Desktop\\image_5\\'+district_arr[tub]+'.png')

	plt.close()
	print(tub)




#plt.show()


# for name, group in df1.groupby(['Detected District','Date Announced']):
	
#     print(name) 
#     print(group.count(axis = 0)[0])
#     print() 


# y = np.array(gr['Status Change Date'])

# x = df1['Detected District'].sort_values(ascending=True).unique()

# print(len(gr['Status Change Date']))

# print(len(df1['Detected District'].sort_values(ascending=True).unique()))



# for a in gr['Status Change Date']:
# 	print(a)

#print(len(gr['Detected District']))

#print(gr['Detected District'])

# print(gr['Current Status'])

# y = gr['Current Status']

# x = df1['Detected District','Date Announced']

#print(df1['Date Announced'].unique())

#print(gr.first())

# y = df1['Detected State']

# x = df1['Date Announced']

# print(type(df1['Detected State']))
