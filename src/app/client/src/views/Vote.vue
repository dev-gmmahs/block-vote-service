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
          투표 데이터를 검증하고있습니다. 잠시만 기다려주세요
        </div>
        <div v-if="view === 2">
          투표에 정상적으로 참여되었습니다. 참여해주셔서 감사합니다.
        </div>
        <div v-if="view === 3">
          투표 참여 중 문제가 발생했습니다.
        </div>
      </transition>
      <div class="message-area">
        <transition name="fade" mode="out-in">
          <b v-if="msg" :style="ask ? 'color: green' : ''">{{ msg }}</b>
        </transition>
      </div>
      <div class="message-area">
        <a v-if="view > 1" @click="back">뒤로</a>
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
      const selected = this.selectItem
      const currentTime = new Date()
      let nonce = 0
      console.log(sha256(nonce))
    },
    back () {
      console.log('back')
    }
  }
}
</script>

<style>
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
