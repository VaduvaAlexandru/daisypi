
from data import DB


class TemperatureReading(DB.Model):
    '''Model a temperature reading.'''
    id = DB.Column(DB.Integer, primary_key=True)
    value = DB.Column(DB.Float)
    date = DB.Column(DB.DateTime())

    def __init__(self, value, date):
        self.value = value
        self.date = date

    def __repr__(self):
        return '<Temperature entry %r>' % self.date


class DewPointReading(DB.Model):
    '''Model a dew point reading.'''
    id = DB.Column(DB.Integer, primary_key=True)
    value = DB.Column(DB.Float)
    date = DB.Column(DB.DateTime())

    def __init__(self, value, date):
        self.value = value
        self.date = date

    def __repr__(self):
        return '<Dew point entry %r>' % self.date


class CoReading(DB.Model):
    '''Model a co reading.'''
    id = DB.Column(DB.Integer, primary_key=True)
    value = DB.Column(DB.Integer)
    date = DB.Column(DB.DateTime())

    def __init__(self, value, date):
        self.value = value
        self.date = date

    def __repr__(self):
        return '<CO entry %r>' % self.date


class PressureReading(DB.Model):
    '''Model a pressure reading.'''
    id = DB.Column(DB.Integer, primary_key=True)
    value = DB.Column(DB.Integer)
    date = DB.Column(DB.DateTime())

    def __init__(self, value, date):
        self.value = value
        self.date = date

    def __repr__(self):
        return '<Pressure entry %r>' % self.date


class HumidityReading(DB.Model):
    '''Model a humidity reading.'''
    id = DB.Column(DB.Integer, primary_key=True)
    value = DB.Column(DB.Integer)
    date = DB.Column(DB.DateTime())

    def __init__(self, value, date):
        self.value = value
        self.date = date

    def __repr__(self):
        return '<Humidity entry %r>' % self.date


class MicReading(DB.Model):
    '''Model a mic reading.'''
    id = DB.Column(DB.Integer, primary_key=True)
    value = DB.Column(DB.Integer)
    date = DB.Column(DB.DateTime())

    def __init__(self, value, date):
        self.value = value
        self.date = date

    def __repr__(self):
        return '<Mic entry %r>' % self.date


class PressureDiffReading(DB.Model):
    '''Model a pressure diff reading.'''
    id = DB.Column(DB.Integer, primary_key=True)
    value = DB.Column(DB.Integer)
    date = DB.Column(DB.DateTime())

    def __init__(self, value, date):
        self.value = value
        self.date = date

    def __repr__(self):
        return '<Pressure diff entry %r>' % self.date


class LightReading(DB.Model):
    '''Model a light reading.'''
    id = DB.Column(DB.Integer, primary_key=True)
    value = DB.Column(DB.Integer)
    date = DB.Column(DB.DateTime())

    def __init__(self, value, date):
        self.value = value
        self.date = date

    def __repr__(self):
        return '<Light entry %r>' % self.date


class WebcamStatus(DB.Model):
    '''Model a webcam status message.'''
    id = DB.Column(DB.Integer, primary_key=True)
    value = DB.Column(DB.String(50))
    date = DB.Column(DB.DateTime())

    def __init__(self, value, date):
        self.value = value
        self.date = date

    def __repr__(self):
        return '<Webcam status %r>' % self.value


class StatusMessage(DB.Model):
    '''Model a DaisyPi status message.'''
    id = DB.Column(DB.Integer, primary_key=True)
    value = DB.Column(DB.String(200))
    date = DB.Column(DB.DateTime())

    def __init__(self, value, date):
        self.value = value
        self.date = date

    def __repr__(self):
        return '<DaisyPi status message %r>' % self.value


class ProfileMessage(DB.Model):
    '''Model a notification triggered by one of the profiles.'''
    id = DB.Column(DB.Integer, primary_key=True)
    value = DB.Column(DB.String(200))
    ack = DB.Column
    date = DB.Column(DB.DateTime())

    def __init__(self, value, date, ack=False):
        self.value = value
        self.date = date
        self.ack = ack

    def __repr__(self):
        return '<Notification message %r>' % self.value


# class DaisyReading(DB.Model):
#     '''Model a temperature reading.'''

#     id = DB.Column(DB.Integer, primary_key=True)
#     co = DB.Column(DB.Integer)
#     pressure = DB.Column(DB.Integer)
#     temperature = DB.Column(DB.Float)
#     humidity = DB.Column(DB.Integer)
#     webcam_status = DB.Column(DB.String(20))
#     dew_point = DB.Column(DB.Float)
#     mic = DB.Column(DB.Integer)
#     pressure_diff = DB.Column(DB.Integer)
#     status_meesage = DB.Column(DB.String(200))
#     date = DB.DateTime()

#     def __init__(self, co=0, pressure=0, temperature=0.0,
#                  humidity=0, webcam_status='', dew_point=0.0,
#                  mic=0, pressure_diff=0, status_meesage='', date=0):
#         self.co = co
#         self.pressure = pressure
#         self.temperature = temperature
#         self.humidity = humidity
#         self.webcam_status = webcam_status
#         self.dew_point = dew_point
#         self.mic = mic
#         self.pressure_diff = pressure_diff
#         self.status_meesage = status_meesage
#         self.date = datetime.datetime.now()

#     def __repr__(self):
#         return '<Temperature entry %r>' % self.date
