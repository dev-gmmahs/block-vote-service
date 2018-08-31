CREATE TABLE UserTable (
  UserIDSeq VARCHAR(20) NOT NULL, -- 유저 고유 ID
  UserID VARCHAR(20) NOT NULL,    -- 유저 아이디
  Userpw VARCHAR(18) NOT NULL,    -- 유저 비밀번호
  UserName VARCHAR(10) NOT NULL,  -- 유저 이름
  UserNumber VARCHAR(13) NOT NULL,-- 유저 주민등록번호
  PRIMARY KEY(UserIDSeq)
);

CREATE TABLE Vote_Data (
  UniqueNumberSeq VARCHAR(20) NOT NULL, -- 투표 고유번호
  UniqueUserSeq VARCHAR(10) NOT NULL,   -- 투표 참여자 코드
  Vote_JoinDate DATETIME NOT NULL,      -- 투표 참여시간
  Vote_Item VARCHAR(300) NOT NULL,      -- 투표 항목
  nonce INT NOT NULL,                   -- 난스
  Hash VARCHAR(32) NOT NULL,            -- 해시
  Prev_Hash VARCHAR(32) NOT NULL,       -- 이전 해시
  PRIMARY KEY(Hash)
);

CREATE TABLE Vote_Information (
  UniqueNumberSeq VARCHAR(20) NOT NULL, -- 투표 고유번호
  VoteName VARCHAR(100),                -- 투표 명
  UserID VARCHAR(20) NOT NULL,          -- 투표 개설자
  Vote_JoinCode VARCHAR(10),            -- 투표 참여코드
  VoteStart DateTime NOT NULL,          -- 투표 시작일
  VoteEnd DateTime NOT NUll,            -- 투표 마감일
  VoteCreated INT NOT NULL,             -- 투표 정상적으로 생성여부
  PRIMARY KEY(UniqueNumberSeq)
);

CREATE TABLE Vote_Item (
  UniqueNumberSeq VARCHAR(20) NOT NULL, -- 투표 고유번호
  Vote_Item VARCHAR(300) NOT NULL,      -- 투표 항목
  PRIMARY KEY(UniqueNumberSeq)
);

CREATE TABLE Vote_User (
  UniqueUserSeq VARCHAR(10) NOT NULL,   -- 투표 참여자 코드
  UniqueNumberSeq VARCHAR(20) NOT NULL, -- 투표 고유번호
  JoinName VARCHAR(10) NOT NULL,        -- 투표자 명
  JoinPhone VARCHAR(11) NOT NULL,       -- 투표자 전화번호
  JoinAlready INT NOT NULL,             -- 투표 참여 여부
  PRIMARY KEY(UniqueUserSeq)
);