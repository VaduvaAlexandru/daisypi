import datetime

from . import DB
import entities


def update_json(new_json):
    '''Parse a received JSON and save the corresponding
    entities to the DB.'''
    now = datetime.datetime.now()

    if 'temperature' in new_json:
        DB.session.add(entities.TemperatureReading(new_json['temperature'],
                                                   now))
    if 'dew_point' in new_json:
        DB.session.add(entities.DewPointReading(new_json['dew_point'], now))
    if 'co' in new_json:
        DB.session.add(entities.CoReading(new_json['co'], now))
    if 'pressure' in new_json:
        DB.session.add(entities.PressureReading(new_json['pressure'], now))
    if 'humidity' in new_json:
        DB.session.add(entities.HumidityReading(new_json['humidity'], now))
    if 'mic' in new_json:
        DB.session.add(entities.MicReading(new_json['mic'], now))
    if 'pressure_diff' in new_json:
        DB.session.add(entities.PressureDiffReading(new_json['pressure_diff'],
                                                    now))
    if 'light' in new_json:
        DB.session.add(entities.LightReading(new_json['light'], now))
    if 'webcam_status' in new_json:
        DB.session.add(entities.WebcamStatus(new_json['webcam_status'], now))
    if 'status_message' in new_json:
        DB.session.add(entities.StatusMessage(new_json['status_message'], now))

    DB.session.commit()


def test_upload():
    '''print the last entry from each db'''
    pass
