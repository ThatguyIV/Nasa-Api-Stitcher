import requests
import json
import urllib

def getImage(lat, lon, date):
    """
    given the latitude, longitude, and the date (YYYY-MM-DD) of an image,
    returns the image. Returns False if no image
    """
    apiKey = '7LilumMYHKX592lqb1yr7XukXOiYkYKGshDaGzLV'
    assetsData = requests.get('https://api.nasa.gov/planetary/earth/imagery/?lon='+ str(lon) +'&lat='+ str(lat) +'&date='+ date +'&cloud_score=True&api_key='+ apiKey)
    imageryData = requests.get('https://api.nasa.gov/planetary/earth/imagery/?lon='+ str(lon) +'&lat='+ str(lat) +'&date='+ date +'&cloud_score=True&api_key='+ apiKey)
    print(assetsData.content)
getImage(34,118,'2018-6-10')
#Requests must be made over HTTPS. Try accessing the API at: https://api.nasa.gov/planetary/earth/imagery/?lon=112&lat=36&date=2018-6-10&cloud_score=True&api_key=7LilumMYHKX592lqb1yr7XukXOiYkYKGshDaGzLV
