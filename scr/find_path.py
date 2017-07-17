__author__ = "Nadia Tahiri"
__date__   = "July 2017"

"""Code a script finding the route_ids of the routes passing by the station 'Grand Central'"""

import csv
import re
import os

#==Check the presence of three files: stops.txt, stop_times.txt and trips.txt
if os.path.isfile('../dataset/stops.txt') and os.path.isfile('../dataset/stop_times.txt') and os.path.isfile('../dataset/trips.txt'):
	#==Create a set structure for stocking routes_id
	set_routes_id = set()
	with open('../dataset/stops.txt') as csvfile_stops:
		stops = csv.DictReader(csvfile_stops)
		for stop in stops:
			#==Find stop_id to 'Grand Central' in stops.txt
			if re.search('Grand Central', stop['stop_name']):
				with open('../dataset/stop_times.txt') as csvfile_stop_times:
					stop_times = csv.DictReader(csvfile_stop_times)
					for stop_time in stop_times:
						#==Find trip_id passing by 'Grand Central' in stop_times.txt
						if stop_time['stop_id']==stop['stop_id']:
							with open('../dataset/trips.txt') as csvfile_trips:
								trips = csv.DictReader(csvfile_trips)
								for trip in trips:
									#==Find route_id passing by 'Grand Central' in trips.txt
									if trip['trip_id']==stop_time['trip_id']:
										#==Stock a unique route_id on set
										set_routes_id.add(trip['route_id'])
	print(set_routes_id)
	
	#==Close txt files
	csvfile_stops.closed
	csvfile_stop_times.closed
	csvfile_trips.closed
else:
	#==Files not exist:	
	print("Files not found")