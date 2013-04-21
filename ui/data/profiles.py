'''Profiles definition and handling'''

import datetime

from . import DB
import entities


# Defining the thredsholds for the profiles
baby_monitoring_profile = {'key': 'baby_monitoring',
                           'mic': [0, 50],
                           'co': [0, 450],
                           'humidity': [40, 60]}

thermostat_profile = {'temperature': [],   # [19, 26],
                      'dew_point': [],   # [10, 18],
                      'co': [],   # [0, 900],
                      'prepressure': [],  # que 2h before,and if difference > 5
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
    pass

