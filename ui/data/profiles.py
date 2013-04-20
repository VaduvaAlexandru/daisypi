'''Profiles definition and handling'''

# Defining the thredsholds for the profiles
baby_monitoring_profile = {}

thermostat_profile = {}

home_surveilance_profile = {}

home_sniffer_profile = {}


def chec_conditions_of_profiles(new_json):
    '''Recheck the conditions of the profiles based on the
    entities that were updated.'''
    updated_fields = set(new_json.keys())
    if set(home_sniffer_profile.keys()) & updated_fields:
        check_home_sniffer()
    if set(baby_monitoring_profile.keys()) & updated_fields:
        check_baby_monitoring()
    if set(home_surveilance_profile.keys()) & updated_fields:
        check_home_surveilance()
    if set(thermostat_profile.keys()) & updated_fields:
        check_thermostat()


def check_baby_monitoring(new_json):
    '''Based on a new update, check conditions of
    the baby monitoring profile.'''
    pass


def check_home_surveilance():
    '''Based on a new update, check conditions of
    the home surveilance profile.'''
    pass


def check_home_sniffer():
    '''Based on a new update, check conditions of
    the home sniffer profile.'''
    pass


def check_thermostat():
    '''Based on a new update, check conditions of
    the thermostat profile.'''
    pass

