import folium
import json
from urllib.request import urlopen
from IPython.display import display



m = folium.Map(location=[39, 35], zoom_start=6)


data=urlopen("https://raw.githubusercontent.com/alpers/Turkey-Maps-GeoJSON/master/tr-cities.json").read()
data=json.loads(data)

election_results = {
    'Adana': 'CHP',
'Adıyaman': 'CHP',
'Afyon': 'CHP',
'Ağrı': 'DEM',
'Amasya': 'CHP',
'Ankara': 'CHP',
'Antalya': 'CHP',
'Artvin': 'CHP',
'Aydın': 'CHP',
'Balıkesir': 'CHP',
'Bilecik': 'CHP',
'Bingöl': 'AKP',
'Bitlis': 'AKP',
'Bolu': 'CHP',
'Burdur': 'CHP',
'Bursa': 'CHP',
'Çanakkale': 'CHP',
'Çankırı': 'MHP',
'Çorum': 'AKP',
'Denizli': 'CHP',
'Diyarbakır': 'DEM',
'Edirne': 'CHP',
'Elazığ': 'AKP',
'Erzincan': 'MHP',
'Erzurum': 'AKP',
'Eskişehir': 'CHP',
'Gaziantep': 'AKP',
'Giresun': 'CHP',
'Gümüşhane': 'MHP',
'Hakkari': 'DEM',
'Hatay': 'AKP',
'Isparta': 'AKP',
'Mersin': 'CHP',
'İstanbul': 'CHP',
'İzmir': 'CHP',
'Kars': 'MHP',
'Kastamonu': 'CHP',
'Kayseri': 'AKP',
'Kırklareli': 'MHP',
'Kırşehir': 'CHP',
'Kocaeli': 'AKP',
'Konya': 'AKP',
'Kütahya': 'CHP',
'Malatya': 'AKP',
'Manisa': 'CHP',
'Kahramanmaraş': 'AKP',
'Mardin': 'DEM',
'Muğla': 'CHP',
'Muş': 'DEM',
'Nevşehir': 'İYİ',
'Niğde': 'AKP',
'Ordu': 'AKP',
'Rize': 'AKP',
'Sakarya': 'AKP',
'Samsun': 'AKP',
'Siirt': 'DEM',
'Sinop': 'CHP',
'Sivas': 'BBP',
'Tekirdağ': 'CHP',
'Tokat': 'MHP',
'Trabzon': 'AKP',
'Tunceli': 'DEM',
'Şanlıurfa': 'YRP',
'Uşak': 'CHP',
'Van': 'DEM',
'Yozgat': 'YRP',
'Zonguldak': 'CHP',
'Aksaray': 'AKP',
'Bayburt': 'AKP',
'Karaman': 'MHP',
'Kırıkkale': 'CHP',
'Batman': 'DEM',
'Şırnak': 'AKP',
'Bartın': 'CHP',
'Ardahan': 'CHP',
'Iğdır': 'DEM',
'Yalova': 'CHP',
'Karabük': 'AKP',
'Kilis': 'CHP',
'Osmaniye': 'MHP',
'Düzce': 'AKP'
}


party_colors = {
    'CHP': 'red',
    'AKP': 'yellow',
    'MHP': 'brown',
    'YRP': 'green',
    'İYİ': 'blue',
    'BBP': 'black',
    'DEM': 'Purple'
    
    
}


def color_function(feature):
    il_adi = feature['properties']['name']
    if il_adi in election_results:
        party = election_results[il_adi]
        return party_colors.get(party, 'gray')
    return 'gray'

folium.GeoJson(
    data,
    name='2024 Belediye Seçimleri',
 style_function=lambda feature: {
        'fillColor': color_function(feature),
        'color': 'black',
        'weight': 1,
        'fillOpacity': 0.7,
    },
    tooltip=folium.GeoJsonTooltip(
        fields=['name'],
        aliases=['İl:'],
        localize=True,
        sticky=False,
        labels=True,
        style="""
            background-color: #F0EFEF;
            border: 2px solid black;
            border-radius: 3px;
            box-shadow: 3px;
        """,
        max_width=800,
    )
).add_to(m)

# Lejant ekle
legend_html = '''
    <div style="position: fixed; bottom: 50px; left: 50px; width: 120px; height: 180px; 
    border:2px solid grey; z-index:9999; font-size:14px; background-color:white;
    ">&nbsp; <b>Partiler</b> <br>
    &nbsp; CHP &nbsp; <i class="fa fa-square fa-2x" style="color:#ff0000"></i><br>
    &nbsp; AKP &nbsp; <i class="fa fa-square fa-2x" style="color:#ffa500"></i><br>
    &nbsp; MHP &nbsp; <i class="fa fa-square fa-2x" style="color:#808080"></i><br>
    &nbsp; DEM &nbsp; <i class="fa fa-square fa-2x" style="color:#800080"></i><br>
    &nbsp; İYİ &nbsp; <i class="fa fa-square fa-2x" style="color:#0000ff"></i><br>
    &nbsp; BBP &nbsp; <i class="fa fa-square fa-2x" style="color:#8b4513"></i><br>
    &nbsp; YRP &nbsp; <i class="fa fa-square fa-2x" style="color:#ffff00"></i>
    </div>
'''
m.get_root().html.add_child(folium.Element(legend_html))

# Haritayı göster
display(m)
