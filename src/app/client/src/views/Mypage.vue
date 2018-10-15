<template>
  <div id="mypage">
    <transition name="fade" mode="out-in">
      <div v-if="loaded">
        Finish
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

  }
}
</script>
<style lang="scss">
@import "../common.scss";

#mypage {
  .loading-page {
    position: fixed;
    top: 0px;
    left: 0px;
    width: 100%;
    height: 100%;
    background-color: $main-color;
    display: table;
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
