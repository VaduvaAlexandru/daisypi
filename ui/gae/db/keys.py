'''Functions for generating Datastore keys.
'''

from google.appengine.ext import db


def co2_key():
    '''Constructs a Datastore key for a CO2 entity.'''
    return db.Key.from_path('Sensors', 'CO2')


def pressure_key():
    '''Constructs a Datastore key for a Pressure entity.'''
    return db.Key.from_path('Sensors', 'Pressure')


def temperature_key():
    '''Constructs a Datastore key for a Temperature entity.'''
    return db.Key.from_path('Sensors', 'Temperature')


def dew_point_key():
    '''Constructs a Datastore key for a DewPoint entity.'''
    return db.Key.from_path('Sensors', 'DewPoint')


def humidity_key():
    '''Constructs a Datastore key for a Humidity entity.'''
    return db.Key.from_path('Sensors', 'Humidity')


def pressure_diff_key():
    '''Constructs a Datastore key for a PressureDiff entity.'''
    return db.Key.from_path('Sensors', 'PressureDiff')


def mic_key():
    '''Constructs a Datastore key for a Mic entity.'''
    return db.Key.from_path('Sensors', 'Mic')


def status_message_key():
    '''Constructs a Datastore key for a StatusMessage entity.'''
    return db.Key.from_path('Sensors', 'StatusMessage')

