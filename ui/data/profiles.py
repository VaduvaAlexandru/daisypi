'''Profiles definition and handling'''

import datetime

from . import DB
import entities


# Defining the thredsholds for the profiles
baby_monitoring_profile = {'key': 'baby_monitoring',
                           'mic': [0, 50],
                           'co': [0, 450],
                           'humidity': [40, 60]}

thermostat_profile = {'key': 'thermostat',
                      'temperature': [],   # [19, 26],
                      'dew_point': [],   # [10, 18],
                      'co': [],   # [0, 900],
                      'pressure': [],  # que 2h before,and if difference > 5
                      }

home_surveilance_profile = {'pressure_diff': [0, 50],
                            'pir': [0, 0]}

home_sniffer_profile = {}


def check_conditions_of_profiles(new_json):
    '''Recheck the conditions of the profiles based on the
    entities that were updated.'''
    updated_fields = set(new_json.keys())
    if set(home_sniffer_profile.keys()) & updated_fields:
        check_home_sniffer(new_json)
    if set(baby_monitoring_profile.keys()) & updated_fields:
        check_baby_monitoring(new_json)
    if set(home_surveilance_profile.keys()) & updated_fields:
        check_home_surveilance(new_json)
    if set(thermostat_profile.keys()) & updated_fields:
        check_thermostat(new_json)


def check_baby_monitoring(new_json):
    '''Based on a new update, check conditions of
    the baby monitoring profile.'''
	new_message = False
    if 'mic' in new_json:
        if new_json['mic'] > baby_monitoring_profile['mic'][1]:
            message = ('The baby might be up! The mic level is over {0}'
                       ''.format(baby_monitoring_profile['mic'][1]))
            DB.session.add(entities.ProfileMessage(message,
                           baby_monitoring_profile['key'],
                           datetime.datetime.now()))
            new_message = True
    if 'co' in new_json:
        if new_json['co'] > baby_monitoring_profile['co'][1]:
            message = ('The air is bad! The co level is over {0}'
                       ''.format(baby_monitoring_profile['co'][1]))
            DB.session.add(entities.ProfileMessage(message,
                           baby_monitoring_profile['key'],
                           datetime.datetime.now()))
            new_message = True
    if 'humidity' in new_json:
        if new_json['humidity'] > baby_monitoring_profile['humidity'][1]:
            message = ('The air is bad! The humidity level is over {0}'
                       ''.format(baby_monitoring_profile['humidity'][1]))
            DB.session.add(entities.ProfileMessage(message,
                           baby_monitoring_profile['key'],
                           datetime.datetime.now()))
            new_message = True
        if new_json['humidity'] < baby_monitoring_profile['humidity'][0]:
            message = ('The air is bad! The humidity level is below {0}'
                       ''.format(baby_monitoring_profile['humidity'][0]))
            DB.session.add(entities.ProfileMessage(message,
                           baby_monitoring_profile['key'],
                           datetime.datetime.now()))
            new_message = True
    if new_message:
        DB.session.commit()


def check_home_surveilance(new_json):
    '''Based on a new update, check conditions of
    the home surveilance profile.'''
    pass


def check_home_sniffer(new_json):
    '''Based on a new update, check conditions of
    the home sniffer profile.'''
    pass


def check_thermostat(new_json):
    '''Based on a new update, check conditions of
    the thermostat profile.'''
    temp = entities.TemperatureReading.query.all()
    if temp:
        last_temp = temp[-1].value
    dew_point = entities.DewPointReading.query.all()
    if dew_point:
        last_dew_point = dew_point[-1].value
    co = entities.CoReading.query.all()
    if co:
        last_co = co[-1].value
    pressure = entities.PressureReading.query.all()
    if pressure:
        last_pressure = pressure[-1].value
        if len(pressure) > 240:
            old_pressure = pressure[-240].value
        else:
            old_pressure = None
    
    mark_temp = 10 - (2.5 * abs(last_temp - 23))
    mark_dew_point = 10 - (2.5 * abs(last_dew_point - 14))
    mark_co = 10 - (0.025 * abs(last_co - 400))
    if old_pressure:
        mark_pressure = 2.0 * abs(abs(old_pressure - last_pressure) - 5)
    else:
        mark_pressure = 10
    new_message = False
    if mark_temp < 0:
        message = ('The temperature is unpleasent! {0}C'
                    ''.format(last_temp))
		DB.session.add(entities.ProfileMessage(message,
					   thermostat_profile['key'],
					   datetime.datetime.now()))
		new_message = True
    if mark_dew_point < 0:
        message = ('The dew point is unpleasent! {0}'
                    ''.format(last_dew_point))
		DB.session.add(entities.ProfileMessage(message,
					   thermostat_profile['key'],
					   datetime.datetime.now()))
	    new_message = True
    if mark_co < 0:
        message = ('The CO is unpleasent! {0}'
                    ''.format(last_co))
		DB.session.add(entities.ProfileMessage(message,
					   thermostat_profile['key'],
					   datetime.datetime.now()))
	    new_message = True
	if mark_pressure < 0:
		message = ('The pressure is unpleasent! {0}'
                    ''.format(last_pressure))
		DB.session.add(entities.ProfileMessage(message,
					   thermostat_profile['key'],
					   datetime.datetime.now()))
	    new_message = True
	if not new_message:
		message = 'The room atmosphere is OK'
		DB.session.add(entities.ProfileMessage(message,
					   thermostat_profile['key'],
					   datetime.datetime.now()))
    DB.session.commit()
	
    
    

