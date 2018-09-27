<template>
  <div id="nav">
    <router-link to="/" id="join-link" v-if="path !== 'home' && !$store.state.voting">홈</router-link>
    <router-link to="/login" id="login-link" v-if="path === 'home' && !isLogined">로그인</router-link>
    <router-link to="/join" id="home-link" v-if="path === 'home' && !isLogined">회원가입</router-link>
    <a id="logout-link" v-if="path === 'home' && isLogined" @click="logout">로그아웃</a>
    <router-link to="/mypage" id="info-link" v-if="path === 'home' && isLogined">내 정보</router-link>
    <router-link to="/create" id="info-link" v-if="path === 'home' && isLogined">투표 생성</router-link>
  </div>
</template>

<script>
export default {
  name: 'vote-header',
  props: ['fill', 'path'],
  watch: {
    fill () {
      this.updateFillStatus()
    }
  },
  computed: {
    /**
     * @description 로그인 여부 확인
     */
    isLogined () {
      return this.$store.state.token ? true : false
    }
  },
  methods: {
    /**
     * @description 스크롤 상태에 따라 헤더 링크 스타일 변경
     */
    updateFillStatus () {
      const nav = document.getElementById('nav')
      const login = document.getElementById('login-link')
      const join = document.getElementById('join-link')
      const home = document.getElementById('home-link')
      const logout = document.getElementById('logout-link')
      const info = document.getElementById('info-link')
      if (this.fill) {
        nav.style['background-color'] = '#fff'
        nav.style['box-shadow'] = '0px 0px 10px rgba(0, 0, 0, 0.3)'
        try {
          login.style['color'] = '#aaa'
        } catch (e) { }

        try {
          join.style['color'] = '#aaa'
        } catch (e) { }

        try {
          home.style['color'] = '#aaa'
        } catch (e) { }

        try {
          logout.style['color'] = '#aaa'
        } catch (e) { }

        try {
          info.style['color'] = '#aaa'
        } catch (e) { }
      } else {
        nav.style['background-color'] = 'transparent'
        nav.style['box-shadow'] = 'none'
        try {
          login.style['color'] = '#fff'
        } catch (e) { }

        try {
          join.style['color'] = '#fff'
        } catch (e) { }

        try {
          home.style['color'] = '#fff'
        } catch (e) { }

        try {
          logout.style['color'] = '#fff'
        } catch (e) { }

        try {
          info.style['color'] = '#fff'
        } catch (e) { }
      }
    },
    /**
     * @description 서버에 로그아웃 요청
     */
    logout () {
      console.log('로그아웃')
      this.$store.commit('LOGOUT')
    }
  }
}
</script>

<style lang="scss">
#nav {
  position: fixed;
  text-align: center;
  top: 0px;
  left: 0px;
  z-index: 9999;
  width: 100%;
  padding: 20px 0;
  color: #eee;
  transition: .5s;

  a {
    cursor: pointer;
    text-decoration: none;
    color: #fff;
    margin: 0 5px;
  }

  a:hover {
    color: #fff;
  }
}
</style>
