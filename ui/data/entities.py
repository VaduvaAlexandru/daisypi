from data import DB


class Temperature(DB.Model):
    '''Model a temperature reading.'''

    value = DB.Column(DB.Integer)
    date = DB.DateTime( primary_key=True)

    def __init__(self, value, date):
        self.value = value

    def __repr__(self):
        return '<Temperature entry %r>' % self.date
