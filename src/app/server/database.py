import pymysql

"""
데이터베이스 조작 모듈
20180905 / 이근혁
"""
class database_manager():

    # 초기화 메소드
    # 인스턴스 생성 시 데이터베이스 정보를 입력받고 커넥션 생성
    def __init__(self, host: str, port: int, user: str, password: str, db: str):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.conn = None
        self.connect()

    
    # 커넥션 생성
    def connect(self):
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password, db=self.db)


    # 커넥션 재접속
    def reconnect(self):
        try:
            self.conn.close()
        except:
            pass
        finally:
            self.connect()


    # 데이터베이스 쿼리 함수 SELECT
    def execute(self, query_string: str, args: tuple=None):
        try:
            cur = self.conn.cursor(pymysql.cursors.DictCursor)
            cur.execute(query_string, args)

            result = cur.fetchall()

            cur.close()

            return result
        except:
            self.reconnect()
            return self.execute(query_string, args)


    # INSERT, UPDATE, DELETE
    def update(self, query_string: str, args: tuple=None):
        try:
            cur = self.conn.cursor(pymysql.cursors.DictCursor)
            affectedRows = cur.execute(query_string, args)

            self.conn.commit()

            cur.close()

            return affectedRows
        except:
            self.reconnect()
            return self.execute(query_string, args)


    # 커넥션 닫기
    def close(self):
        try:
            self.conn.close()
        except Exception as e:
            print(e)