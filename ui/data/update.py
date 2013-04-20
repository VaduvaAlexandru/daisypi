
import datetime

import data
import data.entities


def update_json(sql_alchemy_db, new_json):
    '''Save a new JSON to the DB'''
    now = datetime.now()
    new_temp = data.entities.Temperature(new_json['temperature'], now)

    data.DB.session.add(new_temp)
    data.DB.session.commit()

    print(data.entities.Temperature.query.all())
