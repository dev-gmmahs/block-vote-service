<template>
  <div id="vote">
    <div class="gradient-header"></div>
    <div class="panel vote-panel">
      <div class="vertical-outer">
        <div class="vertical-inner">
          <div class="vertical-area">
            <h2>{{ $store.state.voteData.name }}</h2>
            <transition name="fade" mode="out-in">
              <div class="input-area" v-if="view === 0" :key="1">
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
              <div v-if="view === 1" :key="2">
                잠시만 기다려주세요
                <div id="cube-area">
                  <div class="table-row">
                    <div class="cube cube-1"></div>
                    <div class="cube cube-2"></div>
                    <div class="cube cube-3"></div>
                  </div>
                  <div class="table-row">
                    <div class="cube cube-4"></div>
                    <div class="cube cube-5"></div>
                    <div class="cube cube-6"></div>
                  </div>
                  <div class="table-row">
                    <div class="cube cube-7"></div>
                    <div class="cube cube-8"></div>
                    <div class="cube cube-9"></div>
                  </div>
                </div>
              </div>
              <div v-if="view === 2" :key="3">
                투표에 정상적으로 참여되었습니다. 참여해주셔서 감사합니다.
              </div>
              <div v-if="view === 3" :key="4">
                <h1 class="failed">
                  <fa-icon icon="frown-open"/>
                </h1>
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
      </div>
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
      alert('잘못된 접근입니다')
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
    /**
     * @description 작업증명
     */
    proof () {
      setTimeout(() => {
        const date = new Date()
        const year = date.getFullYear()
        const month = this.toZero(date.getMonth() + 1)
        const day = this.toZero(date.getDate())
        const hour = this.toZero(date.getHours())
        const min = this.toZero(date.getMinutes())
        const sec = this.toZero(date.getSeconds())

        let data = {
          vote: btoa(encodeURIComponent(this.selectItem)), // Base64 인코딩
          currentTime: `${year}-${month}-${day} ${hour}:${min}:${sec}`,
          voteCode: this.$store.state.voteData.vote_code
        }

        // console.log(data.currentTime)
        // console.log(data.vote)
        // console.log(decodeURIComponent(atob(data.vote))) // 디코딩 및 출력 (테스트)

        // 난스
        let nonce = 0

        // 해시
        let hash = ''

        let hashingData = data['vote'] +
                          data['currentTime'] +
                          data['voteCode']

        // 해시의 맨 앞 3자리가 000인 해시데이터 찾기 (nonce를 변경해가며 찾음)
        while ((hash = sha256(hashingData + nonce)).substring(0, 3) !== '000') {
          nonce++ // 만약 해시값 앞이 000이 아니면 난스 1증가하여 다시 반복
        }

        // 제출 데이터에 해시값, 난스 추가
        data['hash'] = hash
        data['nonce'] = nonce

        // 서버로 데이터 전송
        this.$http.post('/info/send/vote', data, {
          headers: { Authorization: 'Bearer ' + this.$store.state.token }
        }).then(result => {
          if (result.data.code === 0) {
            setTimeout(() => {
              // 투표 상태 변경
              this.$store.commit('SET_VOTING_STATUS', false)
              this.view = 2
            }, 750)
          } else {
            setTimeout(() => {
              this.view = 3
            }, 750)
          }
        }).catch(e => {
          const code = e.response.data.code
          setTimeout(() => {
            this.view = 3
            if (code === 2) {
              alert('사용자 인증에 실패하였습니다. 다시 로그인 해 주세요')
              this.$store.commit('SET_VOTING_STATUS')
              this.$store.commit('LOGOUT')
              this.$router.push({ path: '/' })
            } else if (code === 3) {
              alert('투표를 찾을 수 없습니다.')
            } else if (code === 4) {
              alert('투표 참여 가능 인원이 초과 되었습니다.')
            } else if (code === 5) {
              alert('회원님은 참여자 명단에 존재하지 않습니다.')
            } else if (code === 40) {
              alert('투표 해시가 일치하지 않습니다.')
            } else if (code === 50) {
              alert('회원님은 본 투표에 이미 참여하셨습니다.')
            } else if (code === 60) {
              alert('투표 참여 기간이 만료되었습니다.')
            } else if (code === 61) {
              alert('투표 참여 기간이 시작되지 않았습니다.')
            } else if (code === 97) {
              alert('투표 데이터 추가 실패')
            } else if (code === 98) {
              alert('투표 항목이 없습니다.')
            } else {
              alert('알 수 없는 오류')
            }
          }, 750)
        })
      }, 500)
    },
    toZero (n) {
      n = n.toString()
      if (n.length === 2) {
        return n
      } else {
        return '0' + n
      }
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

#cube-area {
  display: table;
  margin: auto;
  margin-top: 50px;
}

.cube {
  display: table-cell;
  width: 30px;
  height: 30px;
  background-color: lightgray;
  opacity: 0.0;
}

.table-row {
  display: table-row;
}

.cube-1, .cube-5, .cube-9 {
  animation: loading 1s .2s alternate infinite;
}

.cube-2, .cube-6 {
  animation: loading 1s .3s alternate infinite;
}

.cube-3 {
  animation: loading 1s .4s alternate infinite;
}

.cube-4, .cube-8 {
  animation: loading 1s .1s alternate infinite;
}

.cube-7 {
  animation: loading 1s alternate infinite;
}

@keyframes loading {
  from {
    transform: scale(0);
    opacity: 0.0;
  }

  to {
    transform: scale(1);
    opacity: 1;
  }
}

.failed {
  color: tomato;
}
</style>
