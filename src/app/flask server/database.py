import pymysql

"""
데이터베이스 조작 모듈
20180905 / 이근혁
"""
class database_manager():
    # 초기화 메소드
    # 인스턴스 생성 시 데이터베이스 정보를 입력받고 커넥션 생성
    def __init__(self, host: str, port: int, user: str, password: str, db: str):
        self.conn = pymysql.connect(host=host, port=port, user=user, password=password, db=db)


    # 데이터베이스 쿼리 함수 SELECT
    def execute(self, query_string: str, args: tuple=None):
        cur = self.conn.cursor(pymysql.cursors.DictCursor)
        cur.execute(query_string, args)

        result = cur.fetchall()

        cur.close()

        return result

    # INSERT, UPDATE, DELETE
    def update(self, query_string: str, args: tuple=None):
        cur = self.conn.cursor(pymysql.cursors.DictCursor)
        affectedRows = cur.execute(query_string, args)

        self.conn.commit()

        cur.close()

        return affectedRows