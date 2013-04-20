'''Classes for modeling the entities.
'''

from google.appengine.ext import db


class CO2(db.Model):
    '''Models an individual CO2 entry,
    with the value and the timestamp.'''
    value = db.IntegerProperty()
    date = db.DateTimeProperty(auto_now_add=True)


class Pressure(db.Model):
    '''Models an individual pressure entry,
    with the value and the timestamp.'''
    value = db.IntegerProperty()
    date = db.DateTimeProperty(auto_now_add=True)


class Temperature(db.Model):
    '''Models an individual temperature entry,
    with the value and the timestamp.'''
    value = db.FloatProperty()
    date = db.DateTimeProperty(auto_now_add=True)


class DewPoint(db.Model):
    '''Models an individual dew point entry,
    with the value and the timestamp.'''
    value = db.FloatProperty()
    date = db.DateTimeProperty(auto_now_add=True)


class Humidity(db.Model):
    '''Models an individual humidity entry,
    with the value and the timestamp.'''
    value = db.IntegerProperty()
    date = db.DateTimeProperty(auto_now_add=True)


class PressureDiff(db.Model):
    '''Models an individual pressure difference entry,
    with the value and the timestamp.'''
    value = db.IntegerProperty()
    date = db.DateTimeProperty(auto_now_add=True)


class Mic(db.Model):
    '''Models an individual humidity entry,
    with the value and the timestamp.'''
    value = db.IntegerProperty()
    date = db.DateTimeProperty(auto_now_add=True)


class StatusMessage(db.Model):
    '''Models an individual status message entry,
    with the text and the timestamp.'''
    text = db.StringProperty(multiline=True)
    date = db.DateTimeProperty(auto_now_add=True)
