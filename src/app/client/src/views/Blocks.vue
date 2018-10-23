<template>
  <div id="blocks">
    <transition name="fade" mode="out-in">
      <div class="block-area" v-if="loaded">
        <div class="block" v-for="(b, i) in blocks" :key="i">
          <h3>{{ (i + 1) }}</h3>
          <div class="block-wrap">
            <b>Hash</b><br>
            <div class="hash">{{ b.hash }}</div>
          </div>
          <div class="block-wrap">
            <b>Previous hash</b><br>
            <div class="hash">{{ b.previous_hash }}</div>
          </div>
          <div class="block-wrap">
            <b>Nonce</b><br>
            <div class="block-nonce">{{ b.nonce }}</div>
          </div>
          <div class="block-item">{{ decode(b.item) }}</div>
          <div class="hash">{{ b.date }}</div>
        </div>
      </div>
      <div class="loading-page" v-else>
        <div id="cube-area-block">
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
  name: 'block',
  data () {
    return {
      loaded: false,
      blocks: [],
      code: ''
    }
  },
  created () {
    let urlParams = new URLSearchParams(window.location.search)
    this.code = urlParams.get('code')
    this.getBlockData()
  },
  methods: {
    getBlockData () {
      this.$http.get('/block/' + this.code, {
        headers: { Authorization: 'Bearer ' + this.$store.state.token }
      }).then(r => {
        this.blocks = r.data.block
        this.loaded = true
      }).catch(e => {
        const code = e.response.data.code
        if (code === 2) {
          alert('접근 권한이 없습니다. 다시 로그인해주세요')
          this.$store.commit('LOGOUT')
          this.$router.push({ path: '/' })
        } else if (code === 8) {
          alert('블록 데이터가 존재하지 않습니다.')
          this.$router.push({ path: '/' })
        } else {
          alert('알 수 없는 오류가 발생하였습니다.')
          this.$router.push({ path: '/' })
        }
      })
    },
    decode (item) {
      return decodeURIComponent(atob(item))
    }
  }
}
</script>
<style lang="scss">
@import "../common.scss";

#blocks {
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

.block-area {
  padding: 70px 0;
  box-sizing: border-box;
  background-color: $main-color;

  .block {
    border-radius: 15px;
    margin: 0 auto;
    margin-top: 20px;
    width: 40%;
    background-color: #fff;
    padding: 10px;
    box-sizing: border-box;
    box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.3);

    .block-wrap {
      margin: 10px 0;
    }

    .block-item-name {
      font-weight: bold;
      margin-bottom: 10px;
    }

    .block-nonce {
      font-weight: initial;
    }

    .block-item {
      margin-bottom: 5px;
    }

    .hash {
      color: #888;
      font-size: 0.9rem;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .vote-info-code {
      cursor: text;
      color: #2f5a69;
    }
  }

  @media screen and (max-width: 768px) {
    .block {
      width: 80%;
    }
  }
}

#cube-area-block {
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
