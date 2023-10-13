import folium


def create_map_from_file(filename):
    m = folium.Map(location=[37.0902, -95.7129], zoom_start=4)
    #latitude,longitude,zoom can change if need a different center

    with open(filename, 'r') as f:
        for line in f:
            lat, lon, title, img_path = line.strip().split(',')

            popup_content = f'<strong>{title}</strong><br><img src="{img_path}" alt="Image" width="200">'
            popup = folium.Popup(popup_content, max_width=2650)
            folium.Marker(
                [float(lat), float(lon)],
                popup=popup,
                icon=folium.Icon(color="red")
            ).add_to(m)

    return m


map_obj = create_map_from_file('locations.txt')
map_obj.save('us_map.html')