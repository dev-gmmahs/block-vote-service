USE Vote;

-- DROP TABLE UserTable;
-- DROP TABLE UserLogin;
-- DROP TABLE Vote_Data;
-- DROP TABLE Vote_Information;
-- DROP TABLE Vote_Item;
-- DROP TABLE Vote_User;

-- 20180905 수정 / 이근혁

CREATE TABLE UserTable (
  UserIDSeq VARCHAR(20) NOT NULL, -- 유저 고유 ID
  UserID VARCHAR(20) NOT NULL,    -- 유저 아이디
  Userpw VARCHAR(32) NOT NULL,    -- 유저 비밀번호 (암호화)
  Salt VARCHAR(16) NOT NULL,      -- 암호화 Salt
  UserName VARCHAR(10) NOT NULL,  -- 유저 이름
  UserNumber VARCHAR(13) NOT NULL,-- 유저 주민등록번호
  PRIMARY KEY(UserIDSeq)
);

CREATE TABLE UserLogin (
  UserIDSeq VARCHAR(20) NOT NULL, -- 유저 고유 ID
  Token VARCHAR(400) NOT NULL,    -- 유저 토큰
  GetTime DateTime NOT NULL,      -- 토큰 발행 시간
  PRIMARY KEY(UserIDSeq)
);

CREATE TABLE Vote_Data (
  UniqueDataSeq INT NOT NULL AUTO_INCREMENT, -- 투표 데이터 고유번호
  UniqueNumberSeq VARCHAR(20) NOT NULL,      -- 투표 고유번호
  UserIDSeq VARCHAR(20) NOT NULL,            -- 투표 참여자 고유ID
  Vote_JoinDate DATETIME NOT NULL,           -- 투표 참여시간
  Vote_Item VARCHAR(300) NOT NULL,           -- 투표 항목
  nonce INT NOT NULL,                        -- 난스
  Hash VARCHAR(32) NOT NULL,                 -- 해시
  Prev_Hash VARCHAR(32) NOT NULL,            -- 이전 해시
  PRIMARY KEY(UniqueDataSeq)
);

CREATE TABLE Vote_Information (
  UniqueNumberSeq VARCHAR(20) NOT NULL, -- 투표 고유번호
  VoteName VARCHAR(100) NOT NULL,       -- 투표 명
  UserID VARCHAR(20) NOT NULL,          -- 투표 개설자
  Vote_JoinCode VARCHAR(10),            -- 투표 참여코드
  VoteStart DateTime NOT NULL,          -- 투표 시작일
  VoteEnd DateTime NOT NUll,            -- 투표 마감일
  VotePermission INT NOT NULL,          -- 투표 참여 권한 (0: 아무나, 1: 지정한 사람만)
  VoteLimit INT NOT NULL,               -- 투표 참여 인원
  VoteCreated INT NOT NULL,             -- 투표 정상적으로 생성여부 (0: 생성X, 1: 생성O)
  PRIMARY KEY(UniqueNumberSeq)
);

CREATE TABLE Vote_Item (
  UniqueNumberSeq VARCHAR(20) NOT NULL, -- 투표 고유번호
  Vote_Item VARCHAR(300) NOT NULL,      -- 투표 항목
  PRIMARY KEY(UniqueNumberSeq)
);

CREATE TABLE Vote_User (
  UserIDSeq VARCHAR(10) NOT NULL,       -- 투표 참여자 고유 아이디
  UniqueNumberSeq VARCHAR(20) NOT NULL, -- 투표 고유번호
  JoinName VARCHAR(10) NOT NULL,        -- 투표자 명
  JoinPhone VARCHAR(11) NOT NULL,       -- 투표자 전화번호
  JoinAlready INT NOT NULL,             -- 투표 참여 여부
  PRIMARY KEY(UniqueUserSeq)
);