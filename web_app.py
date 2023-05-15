from flask import Flask, Blueprint, render_template, redirect, url_for, request
from werkzeug.middleware.proxy_fix import ProxyFix
import sys
from argparse import ArgumentParser
from cvd_model1 import *

appweb = Blueprint('hello', __name__)

@appweb.route('/')
def home():
    return render_template("index.html")

@appweb.route('/send', methods=['POST'])
def send(predict=predict):
    if request.method == 'POST':
        season = request.form['season']
        age = request.form['age']
        childish_disease = request.form['childish disease']
        accident_or_serious_trauma = request.form['accident or serious trauma']
        surgical_intervention = request.form['surgical intervention']
        high_fevers_in_the_last_year = request.form['high fevers in the last year']
        frequency_of_alcohol_consumption = request.form['frequency of alcohol consumption']
        smoking_habit = request.form['smoking habit']
        hours_spent_sitting_per_day = request.form['hours spent sitting per day']


        if(season == "winter"):
            season = -1
        elif(season == "spring"):
            season = -0.33
        elif(season == "summer"):
            season = 0.33
        else:
            season = 1




        if(childish_disease == "Yes"):
            childish_disease = 0
        else:
            childish_disease = 1




        if(accident_or_serious_trauma == "Yes"):
            accident_or_serious_trauma = 0
        else:
            accident_or_serious_trauma = 1


        if(surgical_intervention == "Yes"):
            surgical_intervention = 0
        else:
            surgical_intervention = 1



        if(high_fevers_in_the_last_year == "less than three months ago"):
            high_fevers_in_the_last_year = -1
        elif(high_fevers_in_the_last_year == "more than three months ago"):
            high_fevers_in_the_last_year = 0
        else:
            high_fevers_in_the_last_year = 1






        if(frequency_of_alcohol_consumption == "several times a day"):
            frequency_of_alcohol_consumption = 0,2
        elif(frequency_of_alcohol_consumption == "every day"):
            frequency_of_alcohol_consumption = 0.4
        elif(frequency_of_alcohol_consumption == "several times a week"):
            frequency_of_alcohol_consumption = 0.6
        elif(frequency_of_alcohol_consumption == "once a week"):
            frequency_of_alcohol_consumption = 0.8
        else:
            frequency_of_alcohol_consumption = 1



        if(smoking_habit == "less than three months ago"):
            smoking_habit = -1
        elif(smoking_habit == "more than three months ago"):
            smoking_habit = 0
        else:
            smoking_habit = 1




        # Accuracy of Model
        model.fit(x_train, y_train) #<-- this line
        acc = model.score(x_train, y_train)

        predict_real = model.predict([[season,age,childish_disease, accident_or_serious_trauma,surgical_intervention,\
                         high_fevers_in_the_last_year,frequency_of_alcohol_consumption,\
                         smoking_habit, hours_spent_sitting_per_day]])

        if(predict_real == [0]):
            predict = "The result returned with " + str(round(acc,2)*100)  + "% accuracy and you have a lower chance of getting heart disease"
        else:
            predict = "The result returned with " + str(round(acc,2)*100) + "% accuracy and you have a higher chance of getting heart disease"


        return render_template('index.html', predict=predict)

    else:
        return render_template('index.html', predict=predict)



@appweb.route('/about')
def about():
    return render_template("about.html")



if __name__ == '__main__':

    # arg parser for the standard anaconda-project options
    parser = ArgumentParser(prog="home",
                            description="Simple Flask Application")
    parser.add_argument('--anaconda-project-host', action='append', default=[],
                        help='Hostname to allow in requests')
    parser.add_argument('--anaconda-project-port', action='store', default=8086, type=int,
                        help='Port to listen on')
    parser.add_argument('--anaconda-project-iframe-hosts',
                        action='append',
                        help='Space-separated hosts which can embed us in an iframe per our Content-Security-Policy')
    parser.add_argument('--anaconda-project-no-browser', action='store_true',
                        default=False,
                        help='Disable opening in a browser')
    parser.add_argument('--anaconda-project-use-xheaders',
                        action='store_true',
                        default=False,
                        help='Trust X-headers from reverse proxy')
    parser.add_argument('--anaconda-project-url-prefix', action='store', default='',
                        help='Prefix in front of urls')
    parser.add_argument('--anaconda-project-address',
                        action='store',
                        #default='0.0.0.0',
                        help='IP address the application should listen on.')

    args = parser.parse_args()

    app = Flask(__name__)
    app.register_blueprint(appweb, url_prefix = args.anaconda_project_url_prefix)

    app.config['PREFERRED_URL_SCHEME'] = 'https'

    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.run(host=args.anaconda_project_address, port=args.anaconda_project_port)
