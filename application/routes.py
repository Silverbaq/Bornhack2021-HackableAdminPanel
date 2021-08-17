from flask import render_template, request
import pygeoip
from os import path

from .audio_controller import AudioController
from .models import db, HackedBy
from datetime import datetime as dt
from flask import current_app as app

basedir = path.abspath(path.dirname(__file__))
geo_lite_city = path.join(basedir, 'GeoLiteCity.dat')

gi = pygeoip.GeoIP(geo_lite_city)
audio_controller = AudioController()

passwords = ['123456', '123456789', 'qwerty', 'password', '12345', 'qwerty123', '1q2w3e', '12345678', '111111',
             '1234567890']


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        if username == "admin" and password in passwords:
            ip = request.environ['HTTP_X_FORWARDED_FOR']
            # country = gi.country_name_by_addr('8.8.8.8')
            country = gi.country_name_by_addr(ip)
            # audio_controller.hacked(data)

            hacked_by = HackedBy(
                ip=ip,
                country=country,
                password=password,
                created=dt.now(),
            )
            db.session.add(hacked_by)
            db.session.commit()

            return render_template('home.html')
    return render_template('index.html')


@app.route('/list')
def hacked_by_list():
    hacked_by = HackedBy.query.all()
    return render_template('hacked_list.html', hacks=hacked_by)
