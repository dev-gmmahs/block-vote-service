# schedule 0.5.0

import schedule
import time

def job():
    print("호출 됨")

# 1분마다 호출
schedule.every().minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)