import folium
import pandas

map = folium.Map(location=[38.58,-99.09], zoom_start= 6, tiles = "Mapbox Bright")

""" always add layers on the map between the Map loading and Map save method"""
""" add_child is used to add layers"""
""" use FeatureGroup to add various features/layers together. Keeps the code organized"""

fg_marker = folium.FeatureGroup(name = "Marker")
fg_geo = folium.FeatureGroup(name = "Population")

vol_data = pandas.read_csv("Volcanoes_USA.txt")
vod_data = vol_data.set_index("NUMBER")

"""vol_data[Coordinates] = vol_data["LAT"] + ", " vol_data["LON"]"""

"""
for i in vol_data.index:
    fg.add_child(folium.Marker(location=vol_data.iloc[i,8:], popup = folium.Popup(str(el)) , icon = folium.Icon(color = "red")))
map.add_child(fg)"""
"""Another method to do the same task is to use the zip method"""
x = list(vol_data["LAT"])
y = list(vol_data["LON"])
z = list(vol_data["ELEV"])

def color_changer(e1):
    if e1 <1500:
        return "green"
    elif 1500<= e1 <2500:
        return "blue"
    else:
        return "red"




for i, j, e in zip(x,y,z):
    fg_marker.add_child(folium.CircleMarker(location =[i,j], radius = 8, fill = True, fill_color = color_changer(e), fill_opacity = 1, popup = folium.Popup(str(e), parse_html = True)))

fg_geo.add_child(folium.GeoJson(data =open('world.json', 'r', encoding ='utf-8-sig').read(),name = "mygeo", overlay = True, control = True, smooth_factor = 0.8,
style_function = lambda x: {'fillColor' : 'black' if
                            x['properties']['POP2005'] < 1000000
                            else 'red' if 1000000<= x['properties']['POP2005'] < 2000000
                            else 'blue'}))

map.add_child(fg_marker)
map.add_child(fg_geo)

"""always add the LayerControl layer after you have added the childs in the map. The reason is the LayerControl add the layer control icon on the final map."""
map.add_child(folium.LayerControl())
"""this will treat the final map as the complete layer. hence we wont be able to consider the polygon line and the markers as the separate layer
"""


map.save("Map1.html")
