import ui
import time
import webbrowser
import requests
import json
from datetime import datetime
from dateutil import parser


def buttonaction(sender):
		
	#Extracting data from api to display
	r = requests.get('https://api.climateclock.world/v1/clock', auth = ('user','pass'))
	
	#using json formatter to parse every json element
	data = r.json()
	
	#extract deadline
	carbonDeadline = data["data"]["modules"]["carbon_deadline_1"]["timestamp"]
	carbonDeadline = parser.parse(carbonDeadline)
	
	#extract green climate funds
	fund = data["data"]["modules"]["green_climate_fund_1"]["initial"]
		
	#extract indigenous land area
	land = int(data["data"]["modules"]["indigenous_land_1"]["initial"] * 1000000)
		
	#extract renewable percent
	percent = data["data"]["modules"]["renewables_1"]["initial"]
	dt = datetime.now()
	dt = str(dt.date())
	
	#extracting newsfeed for display		
	
	newsfeed_data = data["data"]["modules"]["newsfeed_1"]["newsfeed"]
	
	news = ''
	
	for idx in range(len(newsfeed_data)):
	 #print(newsfeed_data[idx]['headline_original'])
		news = news + newsfeed_data[idx]['headline_original']
	
		
	newsfeed_data = str(newsfeed_data)
	tz_info = carbonDeadline.tzinfo
	
	#for idx in range(len(newsfeed_data)):
	#	print(newsfeed_data[idx]['headline_original'])
		
	# Now we can subtract two variables using the same time zone info
	# For instance
	# Lets obtain the Now() datetime but for the tz_info we got before
	
	
	diff = carbonDeadline - datetime.now(tz_info)
	#print(diff)
	
	
	days = diff.days
	hours = days * 24
	minutes = hours * 60
	seconds = minutes * 60
		
	years = days // 365
		
	# Calculating months
	months = (days - years *365) // 30
	
	# Calculating days
	days = (days - years * 365 - months*30)-2
		            
		            
	remain = str(years)+' Years '+str(months)+' Months '+str(days)+' Days'
	remain2 = str(hours)+' Hours '+str(minutes)+' Minutes '+str(seconds)+' Seconds'
	remain3 = str(fund)+' Billion USD'
	remain4 = str(land)+' km sq'
	remain5 = str(percent)+' %'
			
	v["label5"].text = dt
	v["textview1"].text = remain
	v["textview2"].text = remain2
	v["label6"].text = remain3
	v["label7"].text = remain4
	v["label8"].text = remain5
	v["label10"].text = news

v = ui.load_view()
button = ui.Button(title='WELCOME TO CLIMATE CLOCK', font=('<System>', 24), flex='rwh', action = buttonaction)
button.frame = (300, 0, 450, 110)
v.add_subview(button)

v.present('sheet')
	
	

