import json
import folium
from datetime import datetime


def get_date(time):
    return datetime.utcfromtimestamp(int(int(time)/1000)).strftime('%Y-%m-%d %H:%M:%S')


path = r"PathToJSONFILE"

with open(path) as file:
    data = json.load(file)

m = folium.Map(location=[50.0403876, 19.9617782], zoom_start=12)

for index, obj in enumerate(data['timelineObjects']):

    if obj.get('activitySegment') is None:
        continue
    start_lat = obj.get('activitySegment').get('startLocation').get('latitudeE7') / (10 ** 7)
    start_long = obj.get('activitySegment').get('startLocation').get('longitudeE7') / (10 ** 7)
    end_lat = obj.get('activitySegment').get('endLocation').get('latitudeE7') / (10 ** 7)
    end_long = obj.get('activitySegment').get('endLocation').get('longitudeE7') / (10 ** 7)
    date = get_date(obj.get('activitySegment').get('duration').get('startTimestampMs'))
    folium.Marker([start_lat, start_long], popup=date).add_to(m)
    folium.Marker([end_lat, end_long], popup=date, icon=folium.Icon(color='red', icon='info-sign')).add_to(m)
    # points = [(start_lat, start_long), (end_lat, end_long)]
    # folium.PolyLine(points, popup=date,).add_to(m)

m.save('index.html')
