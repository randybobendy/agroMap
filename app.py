import folium 
from folium import features
import json
json_path = "/home/psadkowski/Dokumenty/Workspace/Projekty/fast_task/osadkowski_json/lokalizacje.json"
m = folium.Map(location=[19.22882080078125,
            52.231163984032676], zoom_start = 3)
# global tooltip
tooltip = 'Dowiedz się więcej'
# make markers
f = open(json_path)
json_data = json.load(f)
harvIcon = folium.features.CustomIcon('/home/psadkowski/Dokumenty/Workspace/Projekty/fast_task/icon/harv.png', icon_size=(20,20))
for single_data in json_data["features"]:
    second_coor, first_coor = (single_data["geometry"]["coordinates"])  
    # TODO dodać nazwy punktów
    place_name = single_data["properties"]["name"]
    description = single_data["properties"]["description"]
    harvIcon = folium.features.CustomIcon('/home/psadkowski/Dokumenty/Workspace/Projekty/fast_task/icon/harv.png', icon_size=(30,30))
    folium.Marker([first_coor,
              second_coor],
              popup=f'<strong> {place_name}, Opis: {description}  </strong>',
            #   icon=folium.Icon(icon_size=(20,20)),
              tooltip=tooltip).add_to(m) 
m.save('map.html')