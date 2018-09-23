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

INSERT INTO Vote_Information VALUES (
  "vote_test",
  "테스트 투표",
  "asf9sjask0sfi34hhzdf",
  "vote_code",
  "2018-01-01 10:00:00",
  "2018-01-05 12:00:00",
  0,
  10,
  1
);

SELECT VoteName, u.UserID, u.UserName, VoteStart, VoteEnd, VotePermission, VoteLimit, VoteCreated 
FROM Vote_Information i, UserTable u WHERE Vote_JoinCode = %s AND u.UserID = %s i.UserID