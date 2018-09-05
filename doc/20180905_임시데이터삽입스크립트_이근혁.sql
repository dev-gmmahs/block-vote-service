INSERT INTO UserTable VALUES (
  "asf9sjask0sfi34hhzdf",
  "test123",
  HEX(AES_ENCRYPT("password123", SHA2("test_salt", 256))),
  "test_salt",
  "김지빡",
  "0001011234567"
);

SELECT UserIDSeq FROM UserTable
WHERE UserID = "test123" -- 인증할 유저 아이디
AND AES_DECRYPT(UNHEX(Userpw), SHA2( -- 비밀번호를 복호화하여 비밀번호가 같은지 비교
  (SELECT Salt FROM UserTable
   WHERE UserID = "test123"), -- 인증할 유저의 Salt 값 가져오기
256)) = "password123"; -- 입력한 비밀번호