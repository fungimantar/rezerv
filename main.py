import datetime
import os
import json
import locale

from flask import Flask,redirect,url_for,render_template,request,session,flash
app = Flask(__name__)
app.secret_key='naber'
app.static_folder = 'static'
buton = []
global btns
global btn
global action
global f
f=''
btns=''
btn=''
action=''
sayfa_rez = 0
sayfa_rez_takip=0
if os.path.exists('static/rez.json'):
    with open('static/rez.json') as json_file:
           dat_rez = json.load(json_file)
else:
    dat_rez={}

@app.route("/rezarvasyon" , methods=["POST","GET"])
def rez():
    global sayfa_rez,buton

    base = datetime.datetime.today()
    date_list = [(base +datetime.timedelta(days=x)).date() for x in range(36)]


    locale.setlocale(locale.LC_TIME, "tr_TR")
    date_list_name=[(i.strftime("%A")) for i in date_list]
    if request.method == "POST" :
        btns=(request.form.get("submit",""))
        try:
            f = request.form['foo']
            buton.append(btns)
            buton.append(f)
        except:
            pass
        if ":" in btns:
            return redirect(url_for("rez_kayit"))
        if ">" in btns and sayfa_rez<28:
            sayfa_rez=sayfa_rez+7
        if btns == "<" and sayfa_rez>=7:
            sayfa_rez = sayfa_rez - 7
        if btns =='rezarvasyon katip ekrani':
            return redirect(url_for("rez_takip"))
    return render_template('rez.html',gün=range(sayfa_rez+1,8+sayfa_rez),date=date_list,günler=date_list_name,rez=[i for i in dat_rez.keys()])
@app.route("/rez_kayit" , methods=["POST","GET"])
def rez_kayit():
    global buton
    btnn=buton[-2]
    f=buton[-1]
    data=[]
    if request.method == "POST":
        btns = (request.form.get("submit", ""))
        if btns == 'Kaydet':
            isim = request.form["isim"]
            soyad = request.form["soyad"]
            Dogumtarihi = request.form["dogum"]
            mail = request.form["email"]
            tc = request.form["tc"]
            tel = request.form["telefon"]
            data=[isim,soyad,Dogumtarihi,mail,tc,tel]
            data=['-' if x == '' else x for x in data]
            dat_rez[(str(f)+str(btnn))] = data
            with open('static/rez.json', 'w+') as ff:
                json.dump(dat_rez, ff)
            return redirect(url_for("rez"))
        if btns == 'Iptal':
            return redirect(url_for("rez"))
        if btns == 'Tümünü Sifirla':
            return redirect(url_for("rez_kayit"))
    return  render_template("rez_kayit.html",btnn=btnn,f=f ,data=data)


if __name__== "__main__":
  app.run(debug=True)
