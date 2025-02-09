# Adam Munawar Rahman, March 2020
# Creates a Flask app with the kepler.gl visualization loaded

from flask import Flask
from keplergl import KeplerGl

app = Flask(__name__)

map_1 = KeplerGl()


df = pd.read_csv('csv-data/bbl_lat_long_date.csv')
map_1.add_data(data=df, name='data_1')

@app.route('/')
def index():
    return map_1._repr_html_()

if __name__ == '__main__':
    app.run(debug=True)