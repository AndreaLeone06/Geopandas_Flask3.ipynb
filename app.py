from flask import Flask, render_template, request
from geopy.geocoders import Nominatim
import contextily as ctx
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/provincia")
def provincia():
    nome_provincia = request.args.get("nome")
    ax=province[province.DEN_UTS==provUtente].to_crs(3857).plot(facecolor="none")
    x=ctx.add_basemap(ax=ax)
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)