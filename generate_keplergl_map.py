# Adam Munawar Rahman, March 2020
# Adds the generated .csv files as data to a kepler.gl map

# Load an empty map
from keplergl import KeplerGl
map_1 = KeplerGl()
map_1

# DataFrame
df = pd.read_csv('csv-data/bbl_lat_long_date.csv')
map_1.add_data(data=df, name='data_1')

# # CSV
# with open('csv-data/bbl_lat_long_date.csv', 'r') as f:
#     csvData = f.read()
# map_2.add_data(data=csvData, name='data_2')

map_1.save_to_html(file_name='heattweets.html')