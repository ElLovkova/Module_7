import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


page = requests.get('https://russian-trade.com/kursy-valyut/dollar-ssha/posledniy-mesyats-30-dney/')
soup = BeautifulSoup(page.text, 'html.parser')
table_rates = soup.find('table',{'class':'grid_exch'})
rates_list = table_rates.find_all('td')
#for td in rates_list:
#    print(td .text)
rates = []
dates = []
#for i in range((len(rates_list)), 3, -3):
#    rates.append(float(rates_list[i-1].text))
#    dates.append(rates_list[i - 3].text)
for i in range(0, 30, 3):
    rates.append(float(rates_list[i+2].text))
    dates.append(rates_list[i].text)
rates.reverse()
dates.reverse()
#print (rates)
#print (dates)
plt.figure(figsize=(10, 5))
plt.tick_params(axis='both', which='major', labelsize=8)
plt.plot(dates, rates)

plt.show()
