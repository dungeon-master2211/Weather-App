from flask import Flask,render_template,request
import requests
import math
app=Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method =='POST':
        base_url='http://api.openweathermap.org/data/2.5/weather?q='
        city= request.form.get("city")
        app_id='0fb29fad54705e6307ed48183ca79109'
        url=base_url+city+'&'+'appid='+app_id
        response=requests.get(url)
        li=response.json()
        t=li['main']['temp']-273
        temp=math.floor(t)
        day=li['weather'][0]['main']
        icon=li['weather'][0]['icon']
        name=li['name']
        return render_template('index.html',temp=temp,day=day,icon=icon,name=name)
    return render_template('index.html',temp=30,day='Sunny',icon='50d',name='enter name')



