"""
Crontab 작업

0 * * * * python3 result.py
"""

from database import database_manager
import threading
import datetime
import hashlib
import base64
import urllib.parse

class ResultManager():

    def __init__(self, host, port, user, password, database):
        self.db = database_manager(host, port, user, password, database)
        self.log_file_name = datetime.datetime.now().strftime("%Y-%m-%d %H_%M_%S") + "_result.log"


    def log(self, msg):
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        log_message = "- - - [{}] {}".format(date, msg)

        # 로그 기록 저장
        try:
            with open("./log/" + self.log_file_name, "a", encoding="utf-8") as f:
                f.write(log_message + "\n")
        except Exception as e:
            print(e)

        print(log_message)
    

    def checkTime(self):
        now = datetime.datetime.now()

        self.log("Vote result check")

        now = datetime.datetime.now()
        result = self.db.execute("""
        SELECT UniqueNumberSeq
        FROM Vote_Information
        WHERE VoteEnd <= %s
              AND VoteFinished = 0
        """, (now))

        for vote in result:
            vote_id = vote["UniqueNumberSeq"]
            self.log("Vote ended: {}".format(vote_id))
            vote_datas = self.db.execute("""
            SELECT Vote_Item AS item,
                   Vote_JoinDate AS date,
                   UniqueNumberSeq AS v_id,
                   nonce,
                   Hash AS hash,
                   Prev_Hash AS prev,
                   intergrated_hash AS inter
            FROM Vote_Data
            WHERE UniqueNumberSeq = %s
            ORDER BY Vote_JoinDate
            """, (vote_id))

            count = {}
            prev_hash = ""
            for data in vote_datas:
                item = str(data["item"])
                string = item +\
                         str(data["date"]) +\
                         str(data["v_id"]) +\
                         str(data["nonce"])

                hash = hashlib.sha256(string.encode("utf-8")).hexdigest()
                intergrated_hash = hashlib.sha256(str(data["hash"] + prev_hash).encode("utf-8")).hexdigest()
                self.log(intergrated_hash)
                self.log(data["inter"])
                if hash == data["hash"] and prev_hash == data["prev"] and data["inter"] == intergrated_hash:
                    if item in count:
                        count[item] += 1
                    else: 
                        count[item] = 1
                else:
                    self.log("Hash is incorrect")

                prev_hash = data["hash"]

            # 결과 DB에 개표결과 저장
            for k in count.keys():
                self.db.execute("""
                INSERT INTO Vote_Result
                VALUES (%s, %s, %s)
                """, (vote_id, urllib.parse.unquote(base64.b64decode(k).decode()), count[k]))

            # 투표 종료
            self.db.update("""
            UPDATE Vote_Information
            SET VoteFinished = 1
            WHERE UniqueNumberSeq = %s
            """, (vote_id))

    
    def close(self):
        try:
            self.db.close()
        except Exception as e:
            print(e)


result_manager = ResultManager("localhost", 3306, "root", "1234", "vote")
result_manager.checkTime()
result_manager.close()
