import pandas as pd
import matplotlib.pyplot as plt 
from datetime import datetime
import seaborn as sns

manictime_data = pd.read_csv('files/mytimeapp.csv') #download your application usage from manictime in csv

manictime_data['Start'] = manictime_data['Start'].str.replace('T', ' ')
manictime_data['End'] = manictime_data['Start'].str.replace('T', ' ')

manictime_data['Start'] = pd.to_datetime(manictime_data['Start'])
manictime_data['End'] = pd.to_datetime(manictime_data['End'])
print(manictime_data['Duration'][1])
# Filter the data for the specific date
specific_date = input('Enter date in yyyy-mm-dd format: ')

for thatdate in manictime_data['Start']:
    if str(thatdate.date()) == specific_date:
        print("This date data")
   

