<template>
  <div id="mypage">
    <transition name="fade" mode="out-in">
      <div class="mypage-area" v-if="loaded">
        <div v-if="false">
          <div class="vote-item">A</div>
          <div class="vote-item">A</div>
          <div class="vote-item">A</div>
          <div class="vote-item">A</div>
          <div class="vote-item">A</div>
          <div class="vote-item">A</div>
          <div class="vote-item">A</div>
          <div class="vote-item">A</div>
          <div class="vote-item">A</div>
          <div class="vote-item">A</div>
          <div class="vote-item">A</div>
        </div>
        <div class="data-none">
          <h2>투표 데이터가 없습니다</h2>
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
export default {
  name: 'my-page',
  data () {
    return {
      loaded: false
    }
  },
  created () {
    this.$http.get('/access', {
      headers: { Authorization: 'Bearer ' + this.$store.state.token }
    }).then(r => {
      this.loaded = true
    }).catch(e => {
      console.log(e)
      alert('접근할 수 없습니다. 다시 로그인해주세요')
      this.$store.commit('LOGOUT')
      this.$router.push({ path: '/' })
    })
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
    height: 80px;
    background-color: #fff;
    padding: 10px;
    box-sizing: border-box;
    box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.3);

    &:hover {
      box-shadow: 0px 0px 25px rgba(0, 0, 0, 0.5);
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

</style>
