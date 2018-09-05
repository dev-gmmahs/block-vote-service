# PyMysql 0.9.2

import pymysql

# DB 커넥션 생성
conn = pymysql.connect(host="localhost", port=3306, user="root", password="1234", db="vote")

# 커서 객체 (실제 쿼리는 커서에서 진행)
cur = conn.cursor(pymysql.cursors.DictCursor)

# 커서의 execute 메소드로 원하는 쿼리 실행
cur.execute("SHOW TABLES")

# 쿼리 실행 후 fetch
result = cur.fetchall()

# 쿼리 결과 출력
print(result)

cur.execute("INSERT INTO test VALUES (%s)", ("test_v"))
print(cur.execute("INSERT INTO test VALUES (%s)", ("test_v")))

# 사용 후 close()
cur.close()
conn.close()
