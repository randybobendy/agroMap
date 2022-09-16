import folium 
import json
json_path = "/home/psadkowski/Dokumenty/Workspace/Projekty/fast_task/osadkowski_json/lokalizacje.json"
m = folium.Map(location=[19.22882080078125,
            52.231163984032676], zoom_start = 3)
# global tooltip
tooltip = 'Dowiedz się więcej'
# make markers
f = open(json_path)
json_data = json.load(f)
for single_data in json_data["features"]:
    second_coor, first_coor = (single_data["geometry"]["coordinates"])  
    # TODO dodać nazwy punktów
    place_name = single_data["properties"]["name"]
    description = single_data["properties"]["description"]
    folium.Marker([first_coor,
              second_coor],
              popup=f'<strong> {place_name}, Opis: {description}  </strong>',
              tooltip=tooltip).add_to(m)
m.save('map.html')