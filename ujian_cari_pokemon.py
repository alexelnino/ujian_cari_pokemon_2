from flask import redirect, request, Flask, render_template, url_for
import json, requests

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('home.html')

@app.route('/hasil', methods=['POST','GET'])
def post():
    name=request.form['nama']
    url='https://pokeapi.co/api/v2/pokemon/'+name
    poke=requests.get(url)
    if str(poke)=='<Response [404]>':
        return redirect('/NotFound')
    filenama=poke.json()['forms']
    nama=filenama[0]['name'].replace(filenama[0]['name'][0],filenama[0]['name'][0].lower())
    gbr=poke.json()['sprites']
    gambar=gbr['front_default']
    id=poke.json()['id']
    berat=poke.json()['weight']
    tinggi=poke.json()['height']
    return render_template('hasil.html',x=[nama,gambar,id,berat,tinggi])

@app.route('/NotFound')
def notFound():
    return render_template('error.html')

@app.errorhandler(404)
def notFound404(error):
    return render_template('error.html')

if __name__=='__main__':
    app.run(debug=True)

