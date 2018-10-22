<template>
  <div id="mypage">
    <modal v-if="open" @close="open = false" :data="currentVote">
      <b slot="header">{{ currentVoteName }}</b>
    </modal>
    <transition name="fade" mode="out-in">
      <div class="mypage-area" v-if="loaded">
        <div v-if="votes">
          <h3>생성한 투표</h3>
          <div class="vote-item" v-for="vote in votes" :key="vote.code" @click="showDetail(vote)" v-if="votes">
            <div class="vote-info-name">{{ vote.name }}</div>
            <div class="vote-info-term">{{ vote.start }}~{{ vote.end }}</div>
            <div class="vote-info-code">{{ vote.code }}</div>
          </div>
        </div>
        <div class="vote-item" v-else>
          <div class="vote-info-code">생성한 투표가 존재하지 않습니다.</div>
        </div>
        <hr>
        <div>
          <div v-if="joinVotes">
            <h3>참여한 투표</h3>
            <div class="vote-item" v-for="vote in joinVotes" :key="vote.code" @click="showDetail(vote)" v-if="joinVotes">
              <div class="vote-info-name">{{ vote.name }}</div>
              <div class="vote-info-term">{{ vote.start }}~{{ vote.end }}</div>
              <div class="vote-info-code">{{ vote.finished === 0 ? '진행 중' : '종료 됨' }}</div>
            </div>
          </div>
          <div class="vote-item" v-else>
            <div class="vote-info-code">참여한 투표가 존재하지 않습니다.</div>
          </div>
        </div>
      </div>
      <div class="loading-page" v-else>
        <div id="cube-area-mypage">
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
    </transition>
  </div>
</template>

<script>
import Modal from '@/components/Modal.vue'

export default {
  name: 'my-page',
  data () {
    return {
      loaded: false,
      voteToggle: true,
      votes: [],
      joinVotes: [],
      currentVote: {},
      open: false
    }
  },
  components: {
    'modal': Modal
  },
  created () {
    this.$http.get('/access', {
      headers: { Authorization: 'Bearer ' + this.$store.state.token }
    }).then(r => {
      this.getVoteData().then(r => {
        this.votes = r.data.vote
        return this.getJoinVoteData()
      }).then(r => {
        this.joinVotes = r.data.vote
        this.loaded = true
      }).catch(e => {
        const code = e.response.data.code
        if (code === 2) {
          alert('접근 권한이 없습니다. 다시 로그인해주세요')
          this.$store.commit('LOGOUT')
          this.$router.push({ path: '/' })
        } else {
          alert('알 수 없는 오류가 발생하였습니다.')
        }
      })
    }).catch(e => {
      alert('접근 권한이 없습니다. 다시 로그인해주세요')
      this.$store.commit('LOGOUT')
      this.$router.push({ path: '/' })
    })
  },
  methods: {
    getVoteData () {
      return this.$http.get('/info/vote/created', {
        headers: { Authorization: 'Bearer ' + this.$store.state.token }
      })
    },
    getJoinVoteData () {
      return this.$http.get('/info/vote/joined', {
        headers: { Authorization: 'Bearer ' + this.$store.state.token }
      })
    },
    showDetail (vote) {
      this.currentVote = vote
      this.open = true
    },
    viewToggleEvent () {
      console.log(!this.viewToggle)
      this.viewToggle = !this.viewToggle
    }
  }
}
</script>
<style lang="scss">
@import "../common.scss";

#mypage {
  width: 100%;
  height: 100%;
  background-color: $main-color;

  .loading-page {
    position: fixed;
    top: 0px;
    left: 0px;
    width: 100%;
    height: 100%;
    display: table;
  }
}

.data-none {
  color: #fff;
  margin-top: 200px;
}

.mypage-area {
  padding: 70px 0;
  box-sizing: border-box;
  background-color: $main-color;

  .vote-item {
    cursor: pointer;
    border-radius: 15px;
    margin: 0 auto;
    margin-top: 20px;
    width: 40%;
    background-color: #fff;
    padding: 10px;
    box-sizing: border-box;
    box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.3);

    &:hover {
      box-shadow: 0px 0px 25px rgba(0, 0, 0, 0.5);
    }

    .vote-info-name {
      font-weight: bold;
      margin-bottom: 10px;
    }

    .vote-info-term {
      color: #888;
      font-size: 0.9rem;
    }

    .vote-info-code {
      cursor: text;
      color: #2f5a69;
    }
  }

  @media screen and (max-width: 768px) {
    .vote-item {
      width: 80%;
    }
  }
}

#cube-area-mypage {
  display: table-cell;
  vertical-align: middle;
  padding-left: calc(50% - 45px);
  box-sizing: border-box;

  .table-row {
    .cube {
      background-color: #fff;
    }
  }
}

.btn {
  cursor: pointer;
  outline: none;
  border: 2px solid #fff;
  padding: 8px 14px;
  background-color: transparent;
  color: #444;
  border-radius: 5px;
  transition: .5s;

  &:hover {
    background-color: #fff;
  }
}

</style>
