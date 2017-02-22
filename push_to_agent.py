import requests
import time
import json

while True:
    ts = int(time.time())
    # payload = [
    #     {
    #         "endpoint": "test-endpoint",
    #         "metric": "cpu.idle",
    #         "timestamp": ts,
    #         "step": 60,
    #         "value": 90,
    #         "counterType": "GAUGE",
    #         "tags": None,
    #     },
    # ]
    payload = [{'endpoint': 'c1-d08-120-10-43.yidian.com', 'tags': 'mon=GPU,index=0', 'timestamp': 1485080761, 'metric': 'fan-speed', 'value': '27', 'counterType': 'GAUGE', 'step': 60}]
    r = requests.post("http://10.103.16.30:1988/v1/push", data=json.dumps(payload))
    print r.text
    time.sleep(60)