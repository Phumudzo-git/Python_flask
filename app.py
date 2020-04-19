from flask import Flask, request
from flask_restful import Resource, Api
import json
from geopy import distance

app = Flask(__name__)
api = Api(app)

def function_validate(file): #function to validate json file
   try:
      return json.loads(file)
   except ValueError as e:
      print('invalid json: %s' % e)
      return None 

x=function_validate('./data.json')
y=function_validate('./geo.json')

with open('./data.json', 'r') as jsonfile:
   file_data = json.loads(jsonfile.read())
        
with open('./geo.json', 'r') as jsonfile:
   file_2 = json.loads(jsonfile.read())

class Distance(Resource):
   def get(self):
      return "{'Distance in km'}"

#Function to return distances (in km) between latitude and longitude coordinates
class Dist(Resource): 
   def get(self, coord_1):
      for idx, row in enumerate(file_2):
         res = row['geo'].split(',')
         dist = distance.distance((float(res[0]),float(res[1])),(coord_1)).km
         file_data[idx]['distance']=dist
      sorted_obj = sorted(file_data, key=lambda x : x['distance'], reverse=False) 
      return(json.dumps(sorted_obj))

#Function to return maximum distance (in km) between latitude and longitude coordinates
class Max_dist(Resource):   
   def get(self, coord_2):
      for idx, row in enumerate(file_2):
         res = row['geo'].split(',')
         dist = distance.distance((float(res[0]),float(res[1])),(coord_2)).km
         file_data[idx]['distance']=dist
      max_obj = max(file_data, key=lambda x : x['distance']) 
      return(json.dumps(max_obj))

api.add_resource(Distance, '/')
api.add_resource(Dist, '/all_distance/<coord_1>')
api.add_resource(Max_dist,'/max_distance/<coord_2>')
        
if __name__=='__main__':
   app.run(debug=True)



