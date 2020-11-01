<template>
  <div class="home">
    <info-modal :view="modalView" v-if="open" @close="open = false"/>
    <div class="gradient-panel">
      <img src="@/assets/vote.png" class="vote-image">
      <div class="vote-code-area">
        <h1 class="vote-join-text">투표에 참여하세요!!</h1>
        <div class="code-input-area">
          <input type="text" v-model.trim="joinCode" @keydown="keydown" placeholder="참여코드">
          <button @click="join"><fa-icon icon="hand-point-left"/></button>
        </div>
      </div>
      <div class="bottom-area">
        <img src="@/assets/arrow.png">
      </div>
    </div>
    <div>
      <h2>정보</h2>
    </div>
    <div class="content">
      <div class="info-image first" @click="modal(1)">
        <fa-icon icon="users"/>
        <br>
        <div>
          <p class="img-title">투표</p>
          누구나 참여할 수 있습니다
        </div>
      </div>
      <div class="info-image second" @click="modal(2)">
        <fa-icon icon="user-shield"/>
        <br>
        <div>
          <p class="img-title">보안</p>
          안전하게 저장합니다
        </div>
      </div>
      <div class="info-image third" @click="modal(3)">
        <fa-icon icon="smile-wink"/>
        <br>
        <div>
          <p class="img-title">편리</p>
          빠르고 쉽게 참여가능합니다
        </div>
      </div>
    </div>
    <div class="content">
      <div class="create-vote-info">
        <h2>투표 생성하기</h2>
        <hr>
        <div v-if="this.$store.state.token.trim()">
          상단의 투표생성 메뉴를 선택하세요!
        </div>
        <div v-else>
          로그인 후 이용 가능합니다
        </div>
      </div>
    </div>
    <footer>
      <div class="project-info" @click="github"><fa-icon icon="info-circle"/> 프로젝트 정보</div>
      <h5>Copyright ⓒ 2018 GMMAHS Community</h5>
    </footer>
  </div>
</template>

<script>
import InfoModal from '@/components/InfoModal.vue'

export default {
  name: 'home',
  data () {
    return {
      // 투표 참여 코드
      joinCode: '',
      // 모달 열기/닫기
      open: false,
      // 모달 뷰 번호
      modalView: 1
    }
  },
  components: {
    'info-modal': InfoModal
  },
  methods: {
    /**
     * @description 투표 참여 ENTER키 이벤트
     */
    keydown (ev) {
      if (ev.keyCode === 13) {
        this.join()
      }
    },
    /**
     * @description 투표 참여 요청
     */
    join () {
      if (!this.joinCode) {
        alert('코드를 정확하게 입력해주세요')
        return
      }

      if (!this.$store.state.token) {
        alert('로그인 후 사용가능한 서비스입니다.')
        return
      }

      const auth = 'Bearer '.concat(this.$store.state.token)
      this.$http.get('/join/' + this.joinCode, {
        headers: { Authorization: auth }
      }).then(result => {
        /*
        result.data.data : 서버로부터 받은 투표형식 데이터 (투표 명, 투표 항목 등)
        데이터 형식 :

        {
          name: 'XX 찬/반 투표',
          founder: '홍길동(test123)',
          start: '2018-01-01 10:00:00',
          end: '2018-01-02 12:00:00',
          vote_code: 'test',
          items: [
            '후보1',
            '후보2',
            '후보3'
          ]
        }

        */
        this.$store.commit('SET_VOTE_CODE', this.joinCode)
        this.$store.commit('SET_VOTE_DATA', result.data.data)
        this.$router.push({ path: '/vote' })
      }).catch(e => {
        const code = e.response.data.code
        if (code === 2) {
          alert('사용자 인증에 실패하였습니다. 다시 로그인해주세요')
          this.$store.commit('LOGOUT')
        } else if (code === 3) {
          alert('해당 코드의 투표가 없습니다.')
        } else if (code === 4) {
          alert('본 투표에 참여 가능한 인원이 초과되었습니다.')
        } else if (code === 5) {
          alert('회원님은 본 투표에 참여할 권한이 존재하지 않습니다.')
        } else if (code === 50) {
          alert('회원님은 본 투표에 이미 참여하셨습니다.')
        } else if (code === 60) {
          alert('참여기간이 만료 되었습니다.')
        } else if (code === 61) {
          alert('참여기간이 아닙니다.')
        } else {
          alert('알 수 없는 오류가 발생하였습니다.')
        }
      })
    },
    modal (view) {
      this.open = true
      this.modalView = view
    },
    github () {
      window.open('https://github.com/dev-gmmahs/block-vote-service', '_blank')
    }
  }
}
</script>

<style lang="scss">
@import "../common.scss";

.img-title {
  font-size: 1.5rem;
  font-weight: bold;
}

.home {
  width: 100%;
  height: 100%;

  .content {
    position: relative;
    padding: 20px;

    .create-vote-info {
      width: 80%;
      padding: 20px;
      box-sizing: border-box;
      color: #fff;
      margin: auto;
      margin-top: 20px;
      margin-bottom: 20px;
      background-color: plum;

      hr {
        border-color: #fff;
      }
    }

    .info-image {
      cursor: pointer;
      display: inline-block;
      padding: 20px;
      border-radius: 12px;
      width: 20%;
      margin: 15px;
      transition: .4s;

      &:hover {
        transform: translateY(-10px);

        &.first {
          box-shadow: 0px 14px 20px rgba(255, 163, 163, 0.8);
        }

        &.second {
          box-shadow: 0px 14px 20px rgba(255, 243, 132, 0.8);
        }

        &.third {
          box-shadow: 0px 14px 20px rgba(115, 241, 203, 0.8);
        }
      }

      &.first {
        background-color: #ffa3a3;
        box-shadow: 0px 0px 20px rgba(255, 163, 163, 0.75);
      }

      &.second {
        background-color: #fff384;
        box-shadow: 0px 0px 20px rgba(255, 243, 132, 0.75);
      }

      &.third {
        background-color: #73f1cb;
        box-shadow: 0px 0px 20px rgba(115, 241, 203, 0.75);
      }

      div {
        display: inline-block;
      }

      svg {
        font-size: 5rem;
      }
    }

    @media screen and (max-width: 768px) {
      .info-image {
        display: inline-block;
        width: 82%;
        margin: 0;
        margin-bottom: 30px;
      }

      .create-vote-info {
        width: 96%;
      }
    }
  }

  footer {
    background-color: #3b74e5;
    padding: 20px 0;
    color: #fff;
  }

  .gradient-panel {
    // @include gradient-background;
    background-color: $main-color;
    position: relative;
    width: 100%;
    height: 100%;

    .vote-image {
      position: absolute;
      width: 30%;
      left: 35%;
      top: 20%;
      z-index: 0;
    }

    @media screen and (max-width: 768px) {
      .vote-image {
        top: 24%;
        width: 70%;
        left: 15%;
      }
    }

    .vote-code-area {
      position: absolute;
      top: 28%;
      left: 50%;
      box-sizing: border-box;
      color: #333;
      width: 320px;
      margin-left: -160px;

      .code-input-area {
        position: relative;
        display: inline-block;
        background-color: rgba(255, 255, 255, 0.5);
        padding: 50px;
        box-sizing: border-box;

        input {
          outline: none;
          border: 2px solid #fff;
          padding: 8px 14px;
          background-color: transparent;
          border-top-left-radius: 10px;
          border-bottom-left-radius: 10px;
          color: #000;
          transition: .5s;
        }

        input:focus {
          box-shadow: 0px 0px 20px rgba(255, 255, 255, 0.5);
        }

        button {
          position: absolute;
          right: 35px;
          cursor: pointer;
          outline: none;
          border: none;
          background-color: #fff;
          width: 35px;
          height: 35px;
          color: dodgerblue;
          font-weight: bold;
          font-size: 1rem;
          border-top-right-radius: 10px;
          border-bottom-right-radius: 10px;
        }

        button:hover {
          background-color: #eee;
        }
      }
    }

    .bottom-area {
      position: absolute;
      bottom: 0px;
      left: 50%;
      margin-left: -40px;
      animation: arrow .8s alternate infinite;
    }
  }
}

@keyframes arrow {
  100% {
    bottom: 16px;
  }
}

.vote-join-text {
  color: antiquewhite;
}

.project-info {
  margin-top: 10px;
  cursor: pointer;

  &:hover {
    text-decoration: underline;
  }
}
</style>
