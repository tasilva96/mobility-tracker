import json
import os
import sys
import urllib.request
import pandas as pd
from pandas import json_normalize
import plotly.graph_objects as go
import plotly.io as pio

path = "data/"

def mobility_tracker(feature):
    data = pd.read_csv(os.path.join(path, feature + ".csv"))

    df = data[data["date"] == "2020-04-05"]

    fig = go.Figure(data=go.Choropleth(
        locations=df['ST'], # Spatial coordinates
        z = df['value'].astype(float), # Data to be color-coded
        locationmode = 'USA-states', # set of locations match entries in `locations`
        colorscale = 'Reds',
        colorbar_title = "Changed since Feb"    , reversescale=True
    ))


    fig.update_layout(
        title_text = "Google Mobility - " + feature + " Trips",
        geo_scope='usa', # limite map scope to USA
    )

    #fig.show()
    if not os.path.exists("html"):
        os.mkdir("html")

    pio.write_html(fig, file="html/" + feature + ".html", auto_open=True)

    if not os.path.exists("images"):
        os.mkdir("images")

    fig.write_image("images/" + feature + ".jpeg")

if __name__ == "__main__":
    a = sys.argv[1]
    mobility_tracker(a)