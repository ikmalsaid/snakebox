# Project   : snakebox-api
# Author    : Muhamad Nur Ikmal bin Mohd Said
# Source    : https://github.com/ikmalsaid/snakebox-api
# Date      : 30/09/2022
#
# Changelog:
#    [30/09/22]
#    - First release! Woohoo!
#    - Implementation of all essential HTTP methods.
#    - Code rewrite and optimizations.
#

import IP2Location, os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource
from datetime import datetime

snakebx = Flask(__name__)
snakebx.config['JSON_SORT_KEYS'] = False
snakebx.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
snakebx.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///snakebox-api_data/snakebox-api-database.db'

magical = IP2Location.IP2Location(os.path.join('snakebox-api_data', 'IP2LOCATION-LITE-DB3.BIN'))
homerun = {'project':'snakebox-api (contest version) by ikmalsaid',
           'description':'A quick and simple messaging API with IP2Location integration.',
           'message':'Welcome! Please refer README.MD for usage instructions.'}
err_msg = {'message':'Something went wrong. Please try again.'}
sb_data = SQLAlchemy(snakebx)
marilyn = Marshmallow(snakebx)
abigail = Api(snakebx)

class SnakeBox(sb_data.Model):
    message_id      = sb_data.Column(sb_data.Integer, primary_key=True)
    creation_time   = sb_data.Column(sb_data.DateTime, default=datetime.utcnow)
    sender_name     = sb_data.Column(sb_data.Text, nullable=False)
    sender_message  = sb_data.Column(sb_data.Text, nullable=False)
    sender_ip       = sb_data.Column(sb_data.Text, nullable=False)
    sender_country  = sb_data.Column(sb_data.Text, nullable=False)
    sender_region   = sb_data.Column(sb_data.Text, nullable=False)
    sender_city     = sb_data.Column(sb_data.Text, nullable=False)

    def __repr__(self):
        return f"snakebox-api-database -> ('{self.message_id}', '{self.sender_name}', '{self.sender_message}')"

class SnakeBoxSchema(marilyn.SQLAlchemyAutoSchema):
    class Meta:
        model   = SnakeBox
        ordered = True

singular = SnakeBoxSchema()
plural   = SnakeBoxSchema(many=True)

def magic_wand():
    global ip_address, country, region, city
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None: ip_address = request.environ['REMOTE_ADDR']
    else: ip_address = request.environ['HTTP_X_FORWARDED_FOR']
    if ip_address == '127.0.0.1': ip_address = '1.1.1.1' # Fallback IP for when using localhost address
    results = magical.get_all(ip_address)
    country = results.country_short
    region  = results.region
    city    = results.city

class Homerun(Resource):
    def get(self):
        return homerun

class MessagesBasic(Resource):
    def get(self):
        messages = SnakeBox.query.all()
        return plural.dump(messages)

    def post(self):
        magic_wand()
        message = SnakeBox(
            sender_name     = request.json['sender_name'],
            sender_message  = request.json['sender_message'],
            sender_ip       = ip_address,
            sender_country  = country,
            sender_region   = region,
            sender_city     = city)

        try:
            sb_data.session.add(message)
            sb_data.session.commit()
            return singular.dump(message)

        except:
            return err_msg

class MessagesAdvanced(Resource):
    def get(self, message_id):
        message = SnakeBox.query.get_or_404(message_id)
        return singular.dump(message)

    def patch(self, message_id):
        message = SnakeBox.query.get_or_404(message_id)

        if 'sender_name' in request.json:
            message.sender_name = request.json['sender_name']
        if 'sender_message' in request.json:
            message.sender_message = request.json['sender_message']

        try:
            sb_data.session.commit()
            return singular.dump(message)

        except:
            return err_msg

    def delete(self, message_id):
        message = SnakeBox.query.get_or_404(message_id)

        try:
            sb_data.session.delete(message)
            sb_data.session.commit()
            return '', 204

        except:
            return err_msg

abigail.add_resource(Homerun, '/')
abigail.add_resource(MessagesBasic, '/messages')
abigail.add_resource(MessagesAdvanced, '/messages/<int:message_id>')

if __name__ == '__main__':
    snakebx.run(host='0.0.0.0', port=5000)
