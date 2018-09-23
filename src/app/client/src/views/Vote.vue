<template>
  <div id="vote">
    <div class="gradient-header"></div>
    <div class="panel vote-panel">
      <h2>투표</h2>
      <transition name="fade" mode="out-in">
        <div v-if="view === 0">
          1
        </div>
        <div v-if="view === 1">
          2
        </div>
      </transition>
      <div class="message-area">
        <transition name="fade" mode="out-in">
          <b v-if="msg">{{ msg }}</b>
        </transition>
      </div>
      <div class="message-area">
        <a v-if="view !== 0" @click="back">뒤로</a>
      </div>
      <router-link to="/">홈으로 이동</router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'vote',
  data () {
    return {
      verified: false,
      msg: '',
      view: 0,
      voteName: '',
      voteFounder: '',
      voteStart: null,
      voteEnd: null,
      voteItems: []
    }
  },
  created () {
    if (!this.$store.state.voteCode) {
      alert('잘못된 접근')
      this.$router.push({ path: '/' })
      return
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
</style>
