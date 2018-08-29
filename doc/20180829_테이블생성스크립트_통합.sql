CREATE TABLE UserTable (
  UserIDSeq varchar(20) NOT NULL, -- 유저 고유 ID
  UserID varchar(20) NOT NULL,    -- 유저 아이디
  Userpw varchar(18) NOT NULL,    -- 유저 비밀번호
  UserName varchar(10) NOT NULL,  -- 유저 이름
  UserNumber varchar(13) NOT NULL,-- 유저 주민등록번호
  PRIMARY KEY(UserIDSeq)
);

CREATE TABLE Vote_Data (
  UniqueNumberSeq VARCHAR(20) NOT NULL, -- 투표 고유번호
  Vote_JoinDate DATETIME NOT NULL,      -- 투표 참여시간
  Vote_Item VARCHAR(300) NOT NULL,      -- 투표 항목
  nonce INT NOT NULL,                   -- 난스
  Hash VARCHAR(32) NOT NULL,            -- 해시
  Prev_Hash VARCHAR(32) NOT NULL,       -- 이전 해시
  PRIMARY KEY(UniqueNumberSeq)
);

CREATE TABLE Vote_Information (
  UniqueNumberSeq varchar(20) NOT NULL, -- 투표 고유번호
  VoteName varchar(100),                -- 투표 명
  UserID varchar(20) NOT NULL,          -- 투표 개설자
  Vote_JoinCode varchar(10),            -- 투표 참여코드
  VoteStart DateTime NOT NULL,          -- 투표 시작일
  VoteEnd DateTime NOT NUll,            -- 투표 마감일
  PRIMARY KEY(UniqueNumberSeq)
);

CREATE TABLE Vote_Item (
  UniqueNumberSeq VARCHAR(20), -- 투표 고유번호
  Vote_Item VARCHAR(300),      -- 투표 항목
  PRIMARY KEY(UniqueNumberSeq)
);