from flask import Flask, render_template
from region import lista_r
import requests
from region import lista_r

lista_regioes = lista_r

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def Main():
  return render_template('main.html', lista_r = lista_r)

if __name__ == "__main__":
  app.run(debug= True)