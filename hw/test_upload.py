import json
import requests
import time

reads = []
new_read = {}
new_read['temperature'] = 20.77
new_read['dew_point'] = 12.34
new_read['co'] = 200
new_read['pressure'] = 300
new_read['humidity'] = 400
new_read['mic'] = 50
new_read['pressure_diff'] = 123
new_read['light'] = 100
new_read['webcam_status'] = 'OK'
new_read['status_message'] = 'CO level is too low!'
new_read['pir'] = 0
reads.append(new_read)

new_read = {}
new_read['temperature'] = 20.77
new_read['dew_point'] = 12.34
new_read['co'] = 200
new_read['pressure'] = 300
new_read['humidity'] = 50
new_read['mic'] = 70
new_read['pressure_diff'] = 123
new_read['light'] = 100
new_read['webcam_status'] = 'OK'
new_read['status_message'] = 'CO level is too low!'
new_read['pir'] = 0
reads.append(new_read)

new_read = {}
new_read['temperature'] = 20.77
new_read['dew_point'] = 12.34
new_read['co'] = 900
new_read['pressure'] = 300
new_read['humidity'] = 50
new_read['mic'] = 40
new_read['pressure_diff'] = 123
new_read['light'] = 100
new_read['webcam_status'] = 'OK'
new_read['status_message'] = 'CO level is too low!'
new_read['pir'] = 0
reads.append(new_read)

for new_read in reads * 3:
    body = json.dumps(new_read)
    url = u'http://localhost:5000/update'
    r = requests.post(headers=[('content-type', 'application/json')],
                      url=url, data=body)
    print(r.status_code)
    print(r.text)
    time.sleep(1)
