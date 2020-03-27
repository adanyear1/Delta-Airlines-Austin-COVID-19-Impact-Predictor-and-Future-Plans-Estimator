import mysql.connector 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics 
from statistics import mode

try:
    #open database
    db = mysql.connector.connect(
        host = "",
        user = "",
        password = "",
    )

    #prepare a cursor object 
    sql = "SELECT * FROM aircraftinformation.route_information"
    cursor = db.cursor()
    #execute sql command
    cursor.execute(sql)
    #Fetch all the rows in a list of lists
    results = cursor.fetchall()
    routedt = [list(i) for i in results]

    sql1 = "SELECT * FROM aircraftinformation.aircraft_data"
    cursor = db.cursor()
    cursor.execute(sql1)
    result = cursor.fetchall()
    aircraftdt = [list(j) for j in result]
    
except:
    print("Error: unable to fetch data")

finally:
    if (db.is_connected()):
        db.close()
        cursor.close()
        print("This project uses a mysql database to gather data, which is used to perform an analysis using the power of Python.")

#Setting the list for each route Destination[]
Atlanta = routedt[0]
Boston = routedt[1]
Detroit = routedt[2]
Los_Angeles = routedt[3]
New_York_City = routedt[4]
Minneapolis = routedt[5]
Salt_Lake_City = routedt[6]
Seattle = routedt[7]

#Setting the list for each aircraft
a321 = aircraftdt[0]
a319 = aircraftdt[1]
b738 = aircraftdt[2]
a320 = aircraftdt[3]

#sorting the route lists
destination = [Atlanta[2],Boston[2],Detroit[2],Los_Angeles[2],New_York_City[2],Minneapolis[2],Salt_Lake_City[2],Seattle[2]]
primary_aircraft = [Atlanta[3],Boston[3],Detroit[3],Los_Angeles[3],New_York_City[3],Minneapolis[3],Salt_Lake_City[3],Seattle[3]]
secondary_aircraft = [Atlanta[4],Boston[4],Detroit[4],Los_Angeles[4],New_York_City[4],Minneapolis[4],Salt_Lake_City[4],Seattle[4]]
daily_flights = [Atlanta[5],Boston[5],Detroit[5],Los_Angeles[5],New_York_City[5],Minneapolis[5],Salt_Lake_City[5],Seattle[5]]
avg_ticket_cost = [Atlanta[6],Boston[6],Detroit[6],Los_Angeles[6],New_York_City[6],Minneapolis[6],Salt_Lake_City[6],Seattle[6]]
avg_passengers = [Atlanta[7],Boston[7],Detroit[7],Los_Angeles[7],New_York_City[7],Minneapolis[7],Salt_Lake_City[7],Seattle[7]]
flight_cost = [Atlanta[8],Boston[8],Detroit[8],Los_Angeles[8],New_York_City[8],Minneapolis[8],Salt_Lake_City[8],Seattle[8]]
money_earned = [Atlanta[9],Boston[9],Detroit[9],Los_Angeles[9],New_York_City[9],Minneapolis[9],Salt_Lake_City[9],Seattle[9]]
predicted_growth = [Atlanta[10],Boston[10],Detroit[10],Los_Angeles[10],New_York_City[10],Minneapolis[10],Salt_Lake_City[10],Seattle[10]]
flight_time = [Atlanta[11],Boston[11],Detroit[11],Los_Angeles[11],New_York_City[11],Minneapolis[11],Salt_Lake_City[11],Seattle[11]]
profit = [Atlanta[12],Boston[12],Detroit[12],Los_Angeles[12],New_York_City[12],Minneapolis[12],Salt_Lake_City[12],Seattle[12]]

#sorting the aircraft list
model = [a321[1],a319[1],b738[1],a320[1]]
seating = [a321[2],a319[2],b738[2],a320[2]]
cost = [a321[3],a319[3],b738[3],a320[3]]
avg_aircraft_age = [a321[5],a319[5],b738[5],a320[5]]
hourly_cost = [a321[6],a319[6],b738[6],a320[6]]
aircraft_seats_filled = [a321[7],a319[7],b738[7],a320[7]]

#Flight data for DAL in AUS
destinations = 8
gates = 5
total_daily_flights = sum(daily_flights)
avg_gates = total_daily_flights/5
firstdeparture = 6
lastdeparture = 19.41667
firstarrival = 9.75
lastarrival = 24.25
operatingtime = (lastarrival-firstdeparture)

#ATL Route Data
atl_daily_cost = Atlanta[8]*Atlanta[5]
atl_daily_passengers = Atlanta[5]*Atlanta[7]
atl_daily_flight_time = Atlanta[5]*Atlanta[11]
atl_daily_earnings = Atlanta[5]*Atlanta[9]
atl_daily_profit = Atlanta[5]*Atlanta[12]
#ROI of Atlanta flight
atl_flight_cost = Atlanta[8]
atl_flight_profit = Atlanta[12]
def atlROI(atl_flight_cost, atl_flight_profit):
    atlROI = (atl_flight_profit/atl_flight_cost)*100
    return atlROI

#Bos Route Data
bos_daily_cost = Boston[8]*Boston[5]
bos_daily_passengers = Boston[5]*Boston[7]
bos_daily_flight_time = Boston[5]*Boston[11]
bos_daily_earnings = Boston[5]*Boston[9]
bos_daily_profit = Boston[5]*Boston[12]

#ROI of Boston flight
bos_flight_cost = Boston[8]
bos_flight_profit = Boston[12]
def bosROI(bos_flight_cost, bos_flight_profit):
    bosROI = (bos_flight_profit/bos_flight_cost)*100
    return bosROI

#DTW Route Data
dtw_daily_cost = Detroit[8]*Detroit[5]
dtw_daily_passengers = Detroit[5]*Detroit[7]
dtw_daily_flight_time = Detroit[5]*Detroit[11]
dtw_daily_earnings = Detroit[5]*Detroit[9] 
dtw_daily_profit = Detroit[5]*Detroit[12]

#ROI of Detroit flight
dtw_flight_cost = Detroit[8]
dtw_flight_profit = Detroit[12]
def dtwROI(dtw_flight_cost, dtw_flight_profit):
    dtwROI = (dtw_flight_profit/dtw_flight_cost)*100
    return dtwROI

#LAX Route Data
lax_daily_cost = Los_Angeles[8]*Los_Angeles[5]
lax_daily_passengers = Los_Angeles[5]*Los_Angeles[7]
lax_daily_flight_time = Los_Angeles[5]*Los_Angeles[11]
lax_daily_earnings = Los_Angeles[5]*Los_Angeles[9] 
lax_daily_profit = Los_Angeles[5]*Los_Angeles[12]

#ROI of Los Angeles flight
lax_flight_cost = Los_Angeles[8]
lax_flight_profit = Los_Angeles[12]
def laxROI(lax_flight_cost, lax_flight_profit):
    laxROI = (lax_flight_profit/lax_flight_cost)*100
    return laxROI

#jfk Route Data
jfk_daily_cost = New_York_City[8]*New_York_City[5]
jfk_daily_passengers = New_York_City[5]*New_York_City[7]
jfk_daily_flight_time = New_York_City[5]*New_York_City[11]
jfk_daily_earnings = New_York_City[5]*New_York_City[9]
jfk_daily_profit = New_York_City[5]*New_York_City[12]

#ROI of Los Angeles flight
jfk_flight_cost = New_York_City[8]
jfk_flight_profit = New_York_City[12]
def jfkROI(jfk_flight_cost, jfk_flight_profit):
    jfkROI = (jfk_flight_profit/jfk_flight_cost)*100
    return jfkROI

#MSP Route Data
msp_daily_cost = Minneapolis[8]*Minneapolis[5]
msp_daily_passengers = Minneapolis[5]*Minneapolis[7]
msp_daily_flight_time = Minneapolis[5]*Minneapolis[11]
msp_daily_earnings = Minneapolis[5]*Minneapolis[9]
msp_daily_profit = Minneapolis[5]*Minneapolis[12]

#ROI of Minneapolis flight
msp_flight_cost = Minneapolis[8]
msp_flight_profit = Minneapolis[12]
def mspROI(msp_flight_cost, msp_flight_profit):
    mspROI = (msp_flight_profit/msp_flight_cost)*100
    return mspROI

#SLC Route Data
slc_daily_cost = Salt_Lake_City[8]*Salt_Lake_City[5]
slc_daily_passengers = Salt_Lake_City[5]*Salt_Lake_City[7]
slc_daily_flight_time = Salt_Lake_City[5]*Salt_Lake_City[11]
slc_daily_earnings = Salt_Lake_City[5]*Salt_Lake_City[9]
slc_daily_profit = Salt_Lake_City[5]*Salt_Lake_City[12]

#ROI of Salt Lake City flight
slc_flight_cost = Salt_Lake_City[8]
slc_flight_profit = Salt_Lake_City[12]
def slcROI(slc_flight_cost, slc_flight_profit):
    slcROI = (slc_flight_profit/slc_flight_cost)*100
    return slcROI

#SEA Route Data
sea_daily_cost = Seattle[8]*Seattle[5]
sea_daily_passengers = Seattle[5]*Seattle[7]
sea_daily_flight_time = Seattle[5]*Seattle[11]
sea_daily_earnings = Seattle[5]*Seattle[9] 
sea_daily_profit = Seattle[5]*Seattle[12]

#ROI of Seattle flight
sea_flight_cost = Seattle[8]
sea_flight_profit = Seattle[12]
def seaROI(sea_flight_cost, sea_flight_profit):
    seaROI = (sea_flight_profit/sea_flight_cost)*100
    return seaROI

#STATISTICS SECTION
#Airplane Statistics
#Age of airplane fleet
aircraftage_mean = statistics.mean(avg_aircraft_age)
oldestairplane = max(avg_aircraft_age)

#Airplane seating
maxseating = max(seating) 
minseating = min(seating)
maxavgseating = max(aircraft_seats_filled)
minavgseating = min(aircraft_seats_filled)

#Cost analysis 
#Cost of flight
costlst = [atl_daily_cost,bos_daily_cost,dtw_daily_cost,lax_daily_cost,jfk_daily_cost,msp_daily_cost,slc_daily_cost,sea_daily_cost]
maxcost = max(flight_cost)
mincost = min(flight_cost)
daily_flight_cost = sum(costlst)#total
monthly_flight_cost = daily_flight_cost*30#total
yearly_flight_costs = daily_flight_cost*356#total

#Flight Profits & Earnings
earningslst = [atl_daily_earnings,bos_daily_earnings,dtw_daily_earnings,lax_daily_earnings,jfk_daily_earnings,msp_daily_earnings,slc_daily_earnings,sea_daily_earnings]
profitlst = [atl_daily_profit,bos_daily_profit,dtw_daily_profit,lax_daily_profit,jfk_daily_profit,msp_daily_profit,slc_daily_profit,sea_daily_profit]
maxprofit = max(profit)
minprofit = min(profit)
maxflightearnings = max(money_earned)
minflightearnings = min(money_earned)

#Future Trends (2020 - 2022)
time = 2.00

#Atlanta Predictions
atl_passenger_growth = Atlanta[7]*(1+(Atlanta[10]*0.01))**time
atl_passenger_gains = atl_passenger_growth - Atlanta[7]
atl_revenue_growth = Atlanta[9]*(1+(Atlanta[10]*0.01))**time
atl_revenue_gains = atl_revenue_growth - Atlanta[9]
atl_profit_growth = Atlanta[12]*(1+(Atlanta[10]*0.01))**time
atl_profit_gains = atl_profit_growth - Atlanta[12]

#Boston Predictions
bos_passenger_growth = Boston[7]*(1+(Boston[10]*0.01))**time
bos_passenger_gains = bos_passenger_growth - Boston[7]
bos_revenue_growth = Boston[9]*(1+(Boston[10]*0.01))**time
bos_revenue_gains = bos_revenue_growth - Boston[9]
bos_profit_growth = Boston[12]*(1+(Boston[10]*0.01))**time
bos_profit_gains = bos_profit_growth - Boston[12]

#Detroit Predictions
dtw_passenger_growth = Detroit[7]*(1+(Detroit[10]*0.01))**time
dtw_passenger_gains = dtw_passenger_growth - Detroit[7]
dtw_revenue_growth = Detroit[9]*(1+(Detroit[10]*0.01))**time
dtw_revenue_gains = dtw_revenue_growth - Detroit[9]
dtw_profit_growth = Detroit[12]*(1+(Detroit[10]*0.01))**time
dtw_profit_gains = dtw_profit_growth - Detroit[12]

#Los Angeles Predictions
lax_passenger_growth = Los_Angeles[7]*(1+(Los_Angeles[10]*0.01))**time
lax_passenger_gains = lax_passenger_growth - Los_Angeles[7]
lax_revenue_growth = Los_Angeles[9]*(1+(Los_Angeles[10]*0.01))**time
lax_revenue_gains = lax_revenue_growth - Los_Angeles[9]
lax_profit_growth = Los_Angeles[12]*(1+(Los_Angeles[10]*0.01))**time
lax_profit_gains = lax_profit_growth - Los_Angeles[12]

#New York City Predictions
jfk_passenger_growth = New_York_City[7]*(1+(New_York_City[10]*0.01))**time
jfk_passenger_gains = jfk_passenger_growth - New_York_City[7]
jfk_revenue_growth = New_York_City[9]*(1+(New_York_City[10]*0.01))**time
jfk_revenue_gains = jfk_revenue_growth - New_York_City[9]
jfk_profit_growth = New_York_City[12]*(1+(New_York_City[10]*0.01))**time
jfk_profit_gains = jfk_profit_growth - New_York_City[12]

#Minneapolis Predictions
msp_passenger_growth = Minneapolis[7]*(1+(Minneapolis[10]*0.01))**time
msp_passenger_gains = msp_passenger_growth - Minneapolis[7]
msp_revenue_growth = Minneapolis[9]*(1+(Minneapolis[10]*0.01))**time
msp_revenue_gains = msp_revenue_growth - Minneapolis[9]
msp_profit_growth = Minneapolis[12]*(1+(Minneapolis[10]*0.01))**time
msp_profit_gains = msp_profit_growth - Minneapolis[12]

#Salt Lake City Predictions
slc_passenger_growth = Salt_Lake_City[7]*(1+(Salt_Lake_City[10]*0.01))**time
slc_passenger_gains = slc_passenger_growth - Salt_Lake_City[7]
slc_revenue_growth = Salt_Lake_City[9]*(1+(Salt_Lake_City[10]*0.01))**time
slc_revenue_gains = slc_revenue_growth - Salt_Lake_City[9]
slc_profit_growth = Salt_Lake_City[12]*(1+(Salt_Lake_City[10]*0.01))**time
slc_profit_gains = slc_profit_growth - Salt_Lake_City[12]

#Seattle Predictions
sea_passenger_growth = Seattle[7]*(1+(Seattle[10]*0.01))**time
sea_passenger_gains = sea_passenger_growth - Seattle[7]
sea_revenue_growth = Seattle[9]*(1+(Seattle[10]*0.01))**time
sea_revenue_gains = sea_revenue_growth - Seattle[9]
sea_profit_growth = Seattle[12]*(1+(Seattle[10]*0.01))**time
sea_profit_gains = sea_profit_growth - Seattle[12]

#coronavirus impact
#Atlanta COVID-19 Impact
atl_empty = -1*(Atlanta[9])
atl_empty_day = -1*(atl_daily_cost)
atl_empty_month = atl_empty_day*30

#Boston COVID-19 Impact
bos_empty = -1*(Boston[9])
bos_empty_day = -1*(bos_daily_cost)
bos_empty_month = bos_empty_day*30

#Detroit COVID-19 Impact
dtw_empty = -1*(Detroit[9])
dtw_empty_day = -1*(dtw_daily_cost)
dtw_empty_month = dtw_empty_day*30

#Los Angeles COVID-19 Impact
lax_empty = -1*(Los_Angeles[9])
lax_empty_day = -1*(lax_daily_cost)
lax_empty_month = lax_empty_day*30

#New York City COVID-19 Impact
jfk_empty = -1*(New_York_City[9])
jfk_empty_day = -1*(jfk_daily_cost)
jfk_empty_month = jfk_empty_day*30

#Minneapolis COVID-19 Impact
msp_empty = -1*(Minneapolis[9])
msp_empty_day = -1*(msp_daily_cost)
msp_empty_month = msp_empty_day*30

#Salt Lake City COVID-19 Impact
slc_empty = -1*(Salt_Lake_City[9])
slc_empty_day = -1*(slc_daily_cost)
slc_empty_month = slc_empty_day*30

#Seattle COVID-19 Impact
sea_empty = -1*(Seattle[9])
sea_empty_day = -1*(sea_daily_cost)
sea_empty_month = sea_empty_day*30

#calculate the monthly cost for each route using num func

dailylst = [atl_daily_earnings,bos_daily_earnings,dtw_daily_earnings,lax_daily_earnings,jfk_daily_earnings,msp_daily_earnings,slc_daily_earnings,sea_daily_earnings]
def num_func(x):
    return x*30.0
monthly_earnings = map(num_func, dailylst)
resulted_monthly_earnings = set(monthly_earnings)

#use map() to calculate numbers
print('Daily Earnings:',dailylst)
print(resulted_monthly_earnings)
total_monthly_earnings = sum(resulted_monthly_earnings)
print(total_monthly_earnings)

#calculate monthly losses for each route
monthlyloss = [atl_empty_month, bos_empty_month, dtw_empty_month, lax_empty_month, jfk_empty_month, msp_empty_month, slc_empty_month, sea_empty_month]
total_monthly_losses = sum(monthlyloss)
print('Monthly Losses',monthlyloss)

#Data for graphs (y = mx)
month1_gains3 = total_monthly_earnings*1.0
month2_gains3 = total_monthly_earnings*2.0
month3_gains3 = total_monthly_losses
month4_gains3 = total_monthly_losses*2.0
month5_gains3 = total_monthly_losses*3.0
month6_gains3 = total_monthly_earnings*3.0
month7_gains3 = total_monthly_earnings*4.0
month8_gains3 = total_monthly_earnings*5.0
month9_gains3 = total_monthly_earnings*6.0
month10_gains3 = total_monthly_earnings*7.0
month11_gains3 = total_monthly_earnings*8.0
month12_gains3 = total_monthly_earnings*9.0

#Graph that shows decrases For 3 Months when planes fly empty airplanes
month2020_graph = [' Jan. ', ' Feb. ', ' March ', ' April ', ' May ', ' June ', ' July ', ' Aug. ', ' Sept. ', ' Oct. ', ' Nov. ', ' Dec. ']
line_3month = [month1_gains3, month2_gains3, month3_gains3, month4_gains3, month5_gains3, month6_gains3, month7_gains3, month8_gains3, month9_gains3, month10_gains3, month11_gains3, month12_gains3]
print(line_3month)

#Formatting the plot
plt.plot(month2020_graph, line_3month, color='Blue')
plt.xlabel('Month')
plt.ylabel('Earnings')
plt.title('Projected Earnings For 2020 From Austin Services')
plt.show()

print(line_3month)

#REPORT
print('Delta Airlines Aircraft Analyzer')
print('Determine Future Demand For Austin Intl Airport')

#Flight Data
print('\nOperations Data')
print('The first arrival into Austin is 6:00 AM and the last departure is at 12:13 AM')
print('DAL operates flights in and out of Austin for',operatingtime,'hours a day')
print('At the Austin Intl Airport DAL aircraft depart from',gates,'gates\nAn average of',avg_gates,'flights depart from each gate')

#Show route with highest revenue
if (maxflightearnings == Atlanta[9]):
    print('The highest revenue route is', Atlanta[2], 'at $',maxflightearnings, 'per flight')
elif (maxflightearnings == Boston[9]):
    print('The highest revenue route is', Boston[2], 'at $',maxflightearnings, 'per flight')
elif (maxflightearnings == Detroit[9]):
    print('The highest revenue route is', Detroit[2], 'at $',maxflightearnings, 'per flight')
elif (maxflightearnings == Los_Angeles[9]):
    print('The highest revenue route is', Los_Angeles[2], 'at $',maxflightearnings, 'per flight')
elif (maxflightearnings == New_York_City[9]):
    print('The highest revenue route is', New_York_City[2], 'at $',maxflightearnings, 'per flight')
elif (maxflightearnings == Minneapolis[9]):
    print('The highest revenue route is', Minneapolis[2], 'at $',maxflightearnings, 'per flight')
elif (maxflightearnings == Salt_Lake_City[9]):
    print('The highest revenue route is', Salt_Lake_City[2], 'at $',maxflightearnings, 'per flight')
elif (maxflightearnings == Seattle[9]):
    print('The highest revenue route is', Seattle[2], 'at $',maxflightearnings, 'per flight')
else:
    print('All flights have the same revenue')

#show route with the lowest revenue
if (minflightearnings == Atlanta[9]):
    print('The lowest revenue route is', Atlanta[2], 'at $',minflightearnings, 'per flight')
elif (minflightearnings == Boston[9]):
    print('The lowest revenue route is', Boston[2], 'at $',minflightearnings, 'per flight')
elif (minflightearnings == Detroit[9]):
    print('The lowest revenue route is', Detroit[2], 'at $',minflightearnings, 'per flight')
elif (minflightearnings == Los_Angeles[9]):
    print('The lowest revenue route is', Los_Angeles[2], 'at $',minflightearnings, 'per flight')
elif (minflightearnings == New_York_City[9]):
    print('The lowest revenue route is', New_York_City[2], 'at $',minflightearnings, 'per flight')
elif (minflightearnings == Minneapolis[9]):
    print('The lowest revenue route is', Minneapolis[2], 'at $',minflightearnings, 'per flight')
elif (minflightearnings == Salt_Lake_City[9]):
    print('The lowest revenue route is', Salt_Lake_City[2], 'at $',minflightearnings, 'per flight')
elif (minflightearnings == Seattle[9]):
    print('The lowest revenue route is', Seattle[2], 'at $',minflightearnings, 'per flight')
else:
    print('All flights have the same revenue')

#Determine most profitable route Destination[12]
if max(profit) == Atlanta[12]:
    print('Most Profitable route is', Atlanta[2], 'at $',maxprofit, 'per flight')
elif max(profit) == Boston[12]:
    print('Most Profitable route is', Boston[2], 'at $',maxprofit, 'per flight')
elif max(profit) == Detroit[12]:
    print('Most Profitable route is', Detroit[2], 'at', maxprofit, 'per flight')
elif max(profit) == Los_Angeles[12]:
    print('Most Profitable route is', Los_Angeles[2], 'at $',maxprofit, 'per flight')
elif max(profit) == New_York_City[12]:
    print('Most Profitable route is', New_York_City[2], 'at $',maxprofit, 'per flight')
elif max(profit) == Minneapolis[12]:
    print('Most Profitable route is', Minneapolis[2], 'at $',maxprofit, 'per flight')
elif max(profit) == Salt_Lake_City[12]:
    print('Most Profitable route is', Salt_Lake_City[2], 'at $',maxprofit, 'per flight')
elif max(profit) == Seattle[12]:
    print('Most Profitable route is', Seattle[2], 'at $',maxprofit, 'per flight')
else:
    print('All routes result in the same profit')

#Determine least profitable route Destination[12]
if min(profit) == Atlanta[12]:
    print('Least Profitable route is', Atlanta[2], 'at $',minprofit, 'per flight')
elif min(profit) == Boston[12]:
    print('Least Profitable route is', Boston[2], 'at $',minprofit, 'per flight')
elif min(profit) == Detroit[12]:
    print('Least Profitable route is', Detroit[2], 'at', minprofit, 'per flight')
elif min(profit) == Los_Angeles[12]:
    print('Least Profitable route is', Los_Angeles[2], 'at $',minprofit, 'per flight')
elif min(profit) == New_York_City[12]:
    print('Least Profitable route is', New_York_City[2], 'at $',minprofit, 'per flight')
elif min(profit) == Minneapolis[12]:
    print('Least Profitable route is', Minneapolis[2], 'at $',minprofit, 'per flight')
elif min(profit) == Salt_Lake_City[12]:
    print('Least Profitable route is', Salt_Lake_City[2], 'at $',minprofit, 'per flight')
elif min(profit) == Seattle[12]:
    print('Least Profitable route is', Seattle[2], 'at $',minprofit, 'per flight')
else:
    print('All routes result in the same profit')

#Aircraft Statistics
print('\nAircraft Data')
print('The average aircraft has',aircraftage_mean,'years in service with Delta')

#determine aircraft with most and least seats
if maxseating == a321[2]:
    print('The Aircraft with the most number of seats is the',a321[1],'with',maxseating,'seats')
elif maxseating == a319[2]:
    print('The Aircraft with the most number of seats is the',a319[1],'with',maxseating,'seats')
elif maxseating == b738[2]:
    print('The Aircraft with the most number of seats is the',b738[1],'with',maxseating,'seats')
elif maxseating == a320[2]:
    print('The Aircraft with the most number of seats is the',a320[1],'with',maxseating,'seats')
else:
    print('All aircraft have the same number of seats')

#determine aircraft with the least seats 
if minseating == a321[2]:
    print('The Aircraft with the least number of seats is the',a321[1],'with',minseating,'seats')
elif minseating == a319[2]:
    print('The Aircraft with the least number of seats is the',a319[1],'with',minseating,'seats')
elif minseating == b738[2]:
    print('The Aircraft with the least number of seats is the',b738[1],'with',minseating,'seats')
elif minseating == a320[2]:
    print('The Aircraft with the least number of seats is the',a320[1],'with',minseating,'seats')
else:
    print('All aircraft have the same number of seats')

#determine oldest airplane
if oldestairplane == a321[5]:
    print('The oldest airplane flying into Austin is the',a321[1])
elif oldestairplane == a319[5]:
    print('The oldest airplane flying into Austin is the',a319[1])
elif oldestairplane == b738[5]:
    print('The oldest airplane flying into Austin is the',b738[1])
elif oldestairplane == a320[5]:
    print('The oldest airplane flying into Austin is the',a320[1])
else:
    print('Airplanes are the same age')

#Atlanta Future Earnings
print('\nThe predictions for 2022 for the AUS - ATL route are listed below:')
print('By 2022 each AUS - ATL flight will have a revenue of $',atl_revenue_growth)
print('In 2 years the AUS - ATL route will see revenue gains $',atl_revenue_gains,'per flight')
print('Each AUS - ATL flight will earn a profit of $',atl_profit_growth)
print('Profits for each flight on the AUS - ATL route will see an increase of $',atl_profit_gains)
print('It is estimated that by 2022 each flight to Atlanta will carry',atl_passenger_growth,'passengers')
print('This is a gain of',atl_passenger_gains,'passengers per flight')

#ATL Aircraft Choice
def closest(lst, K):
    lst = np.asarray(lst)
    idx = (np.abs(lst + K)).argmax()
    return lst[idx]

lst = seating
K = atl_passenger_growth
newplane_atl = closest(lst, K)
if newplane_atl == a321[2]:
    print('For this route continue using the',a321[1])
elif newplane_atl == a319[2]:
    print('For this route consider using the',a319[1])
elif newplane_atl == b738[2]:
    print('For this route consider using the',b738[1])
elif newplane_atl == a320[2]:
    print('For this route consider using the',a320[1])
else:
    print('Consider purchasing newer aircraft')

#ATL ROI Calculator
print('The ROI for the AUS - ATL route is',atlROI(atl_flight_cost, atl_flight_profit),'%')

#Boston Future Earnings
print('\nThe predictions for 2022 for the AUS - BOS route are listed below:')
print('By 2022 each AUS - BOS flight will have a revenue of $',bos_revenue_growth)
print('In 2 years the AUS - BOS route will see revenue gains $',bos_revenue_gains,'per flight')
print('Each AUS - BOS flight will earn a profit of $',bos_profit_growth)
print('Profits for each flight on the AUS - BOS route will see an increase of $',bos_profit_gains)
print('It is estimated that by 2022 each flight to Boston will carry',bos_passenger_growth,'passengers')
print('This is a gain of',bos_passenger_gains,'passengers per flight')

#BOS Future Earnings
lst = seating
I = bos_passenger_growth
def closest(lst, I):
    lst = np.asarray(lst)
    idx = (np.abs(lst % I)).argmin()
    return lst[idx]

newplane_bos = closest(lst, I)
if newplane_bos == a321[2]:
    print('For this route consider using the',a321[1])
elif newplane_bos == a319[2]:
    print('For this route consider using the',a319[1])
elif newplane_bos == b738[2]:
    print('For this route consider using the',b738[1])
elif newplane_bos == a320[2]:
    print('For this route continue using the',a320[1])
else:
    print('Consider purchasing newer aircraft')

#BOS ROI Calculator
print('The ROI for the AUS - BOS route is',bosROI(bos_flight_cost, bos_flight_profit),'%')

#Detroit Future Earnings
print('\nThe predictions for 2022 for the AUS - DTW route are listed below:')
print('By 2022 each AUS - DTW flight will have a revenue of $',dtw_revenue_growth)
print('In 2 years the AUS - DTW route will see revenue gains $',dtw_revenue_gains,'per flight')
print('Each AUS - DTW flight will earn a profit of $',dtw_profit_growth)
print('Profits for each flight on the AUS - DTW route will see an increase of $',dtw_profit_gains)
print('It is estimated that by 2022 each flight to Detroit will carry',dtw_passenger_growth,'passengers')
print('This is a gain of',dtw_passenger_gains,'passengers per flight')

#DTW Future Aircraft
lst = seating
I = dtw_passenger_growth
def closest(lst, I):
    lst = np.asarray(lst)
    idx = (np.abs(lst % I)).argmin()
    return lst[idx]

newplane_dtw = closest(lst, I)
if newplane_dtw == a321[2]:
    print('For this route consider using the',a321[1])
elif newplane_dtw == a319[2]:
    print('For this route consider using the',a319[1])
elif newplane_dtw == b738[2]:
    print('For this route consider using the',b738[1])
elif newplane_dtw == a320[2]:
    print('For this route continue using the',a320[1])
else:
    print('Consider purchasing newer aircraft')

#DTW ROI Calculator
print('The ROI for the AUS - DTW route is',dtwROI(dtw_flight_cost, dtw_flight_profit),'%')

#Los Angeles Future Earnings
print('\nThe predictions for 2022 for the AUS - LAX route are listed below:')
print('By 2022 each AUS - LAX flight will have a revenue of $',lax_revenue_growth)
print('In 2 years the AUS - LAX route will see revenue gains $',lax_revenue_gains,'per flight')
print('Each AUS - LAX flight will earn a profit of $',lax_profit_growth)
print('Profits for each flight on the AUS - LAX route will see an increase of $',lax_profit_gains)
print('It is estimated that by 2022 each flight to Los Angeles will carry',lax_passenger_growth,'passengers')
print('This is a gain of',lax_passenger_gains,'passengers per flight')

#LAX Future Aircraft
lst = seating
I = lax_passenger_growth
def closest(lst, I):
    lst = np.asarray(lst)
    idx = (np.abs(lst % I)).argmin()
    return lst[idx]

newplane_lax = closest(lst, I)
if newplane_lax == a321[2]:
    print('For this route consider using the',a321[1])
elif newplane_lax == a319[2]:
    print('For this route continue using the',a319[1])
elif newplane_lax == b738[2]:
    print('For this route consider using the',b738[1])
elif newplane_lax == a320[2]:
    print('For this route consider using the',a320[1])
else:
    print('Consider purchasing newer aircraft')

#LAX ROI Calculator
print('The ROI for the AUS - LAX route is',laxROI(lax_flight_cost, lax_flight_profit),'%')

#New York City Future Earnings
print('\nThe predictions for 2022 for the AUS - JFK route are listed below:')
print('By 2022 each AUS - JFK flight will have a revenue of $',jfk_revenue_growth)
print('In 2 years the AUS - JFK route will see revenue gains $',jfk_revenue_gains,'per flight')
print('Each AUS - JFK flight will earn a profit of $',jfk_profit_growth)
print('Profits for each flight on the AUS - JFK route will see an increase of $',jfk_profit_gains)
print('It is estimated that by 2022 each flight to New York City will carry',jfk_passenger_growth,'passengers')
print('This is a gain of',jfk_passenger_gains,'passengers per flight')

#JFK Future Aircraft
lst = seating
I = jfk_passenger_growth
def closest(lst, I):
    lst = np.asarray(lst)
    idx = (np.abs(lst % I)).argmin()
    return lst[idx]

newplane_jfk = closest(lst, I)
if newplane_jfk == a321[2]:
    print('For this route consider using the',a321[1])
elif newplane_jfk == a319[2]:
    print('For this route consider using the',a319[1])
elif newplane_jfk == b738[2]:
    print('For this route consider using the',b738[1])
elif newplane_jfk == a320[2]:
    print('For this route continue using the',a320[1])
else:
    print('Consider purchasing newer aircraft')

#JFK ROI Calculator
print('The ROI for the AUS - JFK route is',jfkROI(jfk_flight_cost, jfk_flight_profit),'%')

#Minneapolis Future Earnings
print('\nThe predictions for 2022 for the AUS - MSP route are listed below:')
print('By 2022 each AUS - MSP flight will have a revenue of $',msp_revenue_growth)
print('In 2 years the AUS - MSP route will see revenue gains $',msp_revenue_gains,'per flight')
print('Each AUS - MSP flight will earn a profit of $',msp_profit_growth)
print('Profits for each flight on the AUS - MSP route will see an increase of $',msp_profit_gains)
print('It is estimated that by 2022 each flight to Minneapolis will carry',msp_passenger_growth,'passengers')
print('This is a gain of',msp_passenger_gains,'passengers per flight')

#MSP Future Aircraft
lst = seating
I = msp_passenger_growth
def closest(lst, I):
    lst = np.asarray(lst)
    idx = (np.abs(lst % I)).argmin()
    return lst[idx]

newplane_msp = closest(lst, I)
if newplane_msp == a321[2]:
    print('For this route consider using the',a321[1])
elif newplane_msp == a319[2]:
    print('For this route consider using the',a319[1])
elif newplane_msp == b738[2]:
    print('For this route consider using the',b738[1])
elif newplane_msp == a320[2]:
    print('For this route continue using the',a320[1])
else:
    print('Consider purchasing newer aircraft')

#MSP ROI Calculator
print('The ROI for the AUS - MSP route is',mspROI(msp_flight_cost, msp_flight_profit),'%')

#Salt Lake City Future Earnings
print('\nThe predictions for 2022 for the AUS - SLC route are listed below:')
print('By 2022 each AUS - SLC flight will have a revenue of $',slc_revenue_growth)
print('In 2 years the AUS - SLC route will see revenue gains $',slc_revenue_gains,'per flight')
print('Each AUS - SLC flight will earn a profit of $',slc_profit_growth)
print('Profits for each flight on the AUS - SLC route will see an increase of $',slc_profit_gains)
print('It is estimated that by 2022 each flight to Salt Lake City will carry',slc_passenger_growth,'passengers')
print('This is a gain of',slc_passenger_gains,'passengers per flight')

#SLC Future Aircraft
lst = seating
I = slc_passenger_growth
def closest(lst, I):
    lst = np.asarray(lst)
    idx = (np.abs(lst % I)).argmin()
    return lst[idx]

newplane_slc = closest(lst, I)
if newplane_slc == a321[2]:
    print('For this route consider using the',a321[1])
elif newplane_slc == a319[2]:
    print('For this route consider using the',a319[1])
elif newplane_slc == b738[2]:
    print('For this route consider using the',b738[1])
elif newplane_slc == a320[2]:
    print('For this route continue using the',a320[1])
else:
    print('Consider purchasing newer aircraft')

#SLC ROI Calculator
print('The ROI for the AUS - SLC route is',slcROI(slc_flight_cost, slc_flight_profit),'%')

#Seattle Future Earnings
print('\nThe predictions for 2022 for the AUS - SEA route are listed below:')
print('By 2022 each AUS - SEA flight will have a revenue of $',sea_revenue_growth)
print('In 2 years the AUS - SEA route will see revenue gains $',sea_revenue_gains,'per flight')
print('Each AUS - SEA flight will earn a profit of $',sea_profit_growth)
print('Profits for each flight on the AUS - SEA route will see an increase of $',sea_profit_gains)
print('It is estimated that by 2022 each flight to Seattle will carry',sea_passenger_growth,'passengers')
print('This is a gain of',sea_passenger_gains,'passengers per flight')

#SEA Future Aircraft
lst = seating
I = sea_passenger_growth
def closest(lst, I):
    lst = np.asarray(lst)
    idx = (np.abs(lst % I)).argmin()
    return lst[idx]

newplane_sea = closest(lst, I)
if newplane_sea == a321[2]:
    print('For this route consider using the',a321[1])
elif newplane_sea == a319[2]:
    print('For this route consider using the',a319[1])
elif newplane_sea == b738[2]:
    print('For this route consider using the',b738[1])
elif newplane_sea == a320[2]:
    print('For this route continue using the',a320[1])
else:
    print('Consider purchasing newer aircraft')

#SEA ROI Calculator
print('The ROI for the AUS - SEA route is',seaROI(sea_flight_cost, sea_flight_profit),'%')
