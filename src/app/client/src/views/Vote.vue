<template>
  <div id="vote">
    <div class="gradient-header"></div>
    <div class="panel vote-panel">
      <h2>{{ $store.state.voteData.name }}</h2>
      <transition name="fade" mode="out-in">
        <div class="input-area" v-if="view === 0">
          <div class="vote-time">
            <b>투표 진행 기간</b>
            <br>
            {{ $store.state.voteData.start }} ~ {{ $store.state.voteData.end }}
          </div>
          <div class="vote-select-item" v-for="item in $store.state.voteData.items" :key="item" @click="itemClick(item)">
            {{ item }}
            <img class="select-mark" src="@/assets/mark.png" v-if="selectItem === item">
          </div>
          <button @click="submit">{{ ask ? '예, 제출합니다' : '제출' }}</button>
        </div>
        <div v-if="view === 1">
          잠시만 기다려주세요
          <!-- 애니메이션 추가(또는 로딩 이미지) -->
        </div>
        <div v-if="view === 2">
          투표에 정상적으로 참여되었습니다. 참여해주셔서 감사합니다.
        </div>
        <div v-if="view === 3">
          투표 참여 중 문제가 발생했습니다. 다시 참여해주세요
        </div>
      </transition>
      <div class="message-area">
        <transition name="fade" mode="out-in">
          <b v-if="msg" :style="ask ? 'color: green' : ''">{{ msg }}</b>
        </transition>
      </div>
      <router-link to="/" v-if="view !== 1">홈으로 이동</router-link>
    </div>
  </div>
</template>

<script>
import sha256 from 'sha256'

export default {
  name: 'vote',
  data () {
    return {
      verified: false,
      msg: '',
      view: 0,
      selectItem: '',
      ask: false
    }
  },
  created () {
    if (!this.$store.state.voteCode || this.$store.state.voteData === {}) {
      alert('잘못된 접근')
      this.$router.push({ path: '/' })
    }
  },
  methods: {
    itemClick (item) {
      this.selectItem = item
      this.msg = ''
      this.ask = false
    },
    submit () {
      if (this.ask && this.selectItem) {
        this.$store.commit('SET_VOTING_STATUS', true)
        this.ask = false
        this.msg = ''
        this.view = 1
        this.proof()
        return
      }

      if (this.selectItem) {
        this.ask = true
        this.msg = '정말 제출하시겠습니까?'
      } else {
        this.msg = '투표항목을 선택해주세요'
      }
    },
    proof () {
      setTimeout(() => {
        let data = {
          vote: btoa(encodeURIComponent(this.selectItem)), // Base64 인코딩
          currentTime: new Date()
        }

        console.log(decodeURIComponent(atob(data.vote))) // 디코딩 및 출력 (테스트)

        // 난스
        let nonce = 0

        // 해시
        let hash = ''

        // 해시의 맨 앞 3자리가 000인 해시데이터 찾기 (nonce를 변경해가며 찾음)
        while ((hash = sha256(data['vote'] +
                             data['currentTime'] +
                             nonce)).substring(0, 3) !== '000') {
          nonce++ // 만약 해시값 앞이 000이 아니면 난스 1증가하여 다시 반복
        }

        // 제출 데이터에 해시값, 난스 추가
        data['hash'] = hash
        data['nonce'] = nonce

        // 서버로 데이터 전송
        this.$http.post('/info/send/vote', data, {
          headers: { Authorization: 'Bearer ' + this.$store.state.token }
        }).then(result => {
          console.log(result)
          setTimeout(() => {
            this.view = 2
          }, 750)
        }).catch(e => {
          console.log(e)
          setTimeout(() => {
            this.view = 3
          }, 750)
        })
      }, 500)
    }
  }
}
</script>

<style lang="scss">
@import "../common.scss";

#vote {
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  width: 100%;
  height: 100%;
}

.vote-panel {
  height: 56%;
  overflow-y: auto;
}

@media screen and (max-width: 768px) {
  .vote-panel {
    height: 76%;
    overflow-y: auto;
  }
}

.vote-select-item {
  cursor: pointer;
  position: relative;
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #eee;
  width: 200px;
  margin: 10px auto;
  transition: .3s;
}

.vote-select-item:hover {
  background-color: #eee;
}

.select-mark {
  position: absolute;
  right: 5px;
  top: 8px;
  width: 25px;
  height: 25px;
  border-radius: 50%;
  display: block;
}

.vote-time {
  font-size: 0.8rem;
  color: #aaa;
}
</style>
