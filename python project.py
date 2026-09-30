import math 
from datetime import datetime
boys_hostels = { "Hostel A": (23.07551, 76.84978), "Hostel B": (23.08000, 76.85000), "Hostel C": (23.07537, 76.86017), "Hostel D": (23.07700, 76.85100) }
girls_hostels = { "Hostel A": (23.07590, 76.84920), "Hostel B": (23.07610, 76.84945), "Hostel C": (23.07560, 76.85020), "Hostel D": (23.07535, 76.85045) }
ambulances = { "Ambulance 1": { "location": (23.07551, 76.84978), "available": True, "speed": 40 },
              "Ambulance 2": { "location": (23.07400, 76.83000), "available": True, "speed": 45 },
              "Ambulance 3": { "location": (23.07400, 76.83000), "available": False, "speed": 40 } }
hospitals = { "Dr. Morepen Health Centre": { "location": (23.07551, 76.84978), "speed": 30 },
             "Kothri Kalan Dispensary": { "location": (23.07396, 76.82979), "speed": 35 },
             "Anandam Hospitals": { "location": (23.18000, 77.43000), "speed": 40 } }
def calculate_distance(point1, point2):
     lat1, lon1 = point1 
     lat2, lon2 = point2
lat1 = math.radians(lat1) 
lon1 = math.radians(lon1) 
lat2 = math.radians(lat2)
lon2 = math.radians(lon2)
dlat = lat2 - lat1 
dlon = lon2 - lon1
a = ( math.sin(dlat / 2) ** 2
    + math.cos(lat1)
    * math.cos(lat2) 
    * math.sin(dlon / 2) ** 2 )
c = 2 * math.atan2( math.sqrt(a), math.sqrt(1 - a) )
earth_radius = 6371 distance = earth_radius * c return distance
def find_nearest_ambulance(hostel_location):
     nearest_ambulance = None 
     shortest_distance = float("inf") 
     for name, data in ambulances.items():
            distance = calculate_distance( hostel_location, data["location"])
            if distance < shortest_distance:
                  shortest_distance = distance nearest_ambulance = name
                  return nearest_ambulance, shortest_distance
        def calculate_travel_time(distance, speed):
             if speed <= 0:
                 return 0 time_hours = distance / speed time_minutes = time_hours * 60 return time_minutes
             def find_nearest_hospital(hostel_location):
                 nearest_hospital = None 
                 shortest_distance = float("inf") 
                 for name, data in hospitals.items():
                      distance = calculate_distance( hostel_location, data[""] )
            