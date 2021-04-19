from datetime import datetime, timedelta
from random import randint

def get_sample_data():
    basic_f1 = {
        "cups": "ES00123400220F", "r4_fact": 0, "quality_ai": 0, "cch_fact": False, "ae": 28290, "ai" : 0,
        "season" : "W", "r3_fact" : 0, "quality_ae": 0, "r2_fact" : 0, "r1" : 0, "r4" : 0, "name" : "50148869",
        "r2" : 4880, "r3" : 0, "ai_fact": 0, "type" : "p", "cch_bruta" : True, "quality_r2" : 0, "quality_r3" : 0,
        "quality_r1" : 0, "quality_r4" : 0, "timestamp": "2020-01-01 00:00:00", "firm_fact": False, "r1_fact": 0,
        "ae_fact": 0, "quality_res": 0, "quality_res2": 0
    }
    ts = "2020-01-01 00:00:00"
    data_f1 = []
    for x in range(50):
        datas = basic_f1.copy()
        ts = (datetime.strptime(ts, '%Y-%m-%d %H:%M:%S') + timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')
        ai = randint(0, 5000)
        ae = randint(0, 2)
        r1 = randint(0, 30)
        r2 = randint(0, 4999)
        datas.update({'timestamp': ts, 'ai': ai, 'ae': ae, 'r1': r1})
        data_f1.append(datas)

    cups = "ES00123400230F"
    ts = "2020-01-01 00:00:00"
    for x in range(70):
        datas = basic_f1.copy()
        ts = (datetime.strptime(ts, '%Y-%m-%d %H:%M:%S') + timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')
        ai = randint(0, 5000)
        ae = randint(0, 2)
        r1 = randint(0, 30)
        r2 = randint(0, 10)
        datas.update({'timestamp': ts, 'ai': ai, 'ae': ae, 'r1': r1, 'cups': cups})
        data_f1.append(datas)
    return data_f1