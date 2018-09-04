<template>
  <div id="nav">
    <router-link to="/" id="join-link" v-if="path !== 'home'">홈</router-link>
    <router-link to="/login" id="login-link" v-if="path === 'home'">로그인</router-link>
    <router-link to="/join" id="home-link" v-if="path === 'home'">회원가입</router-link>
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
  methods: {
    updateFillStatus () {
      const nav = document.getElementById('nav')
      const login = document.getElementById('login-link')
      const join = document.getElementById('join-link')
      const home = document.getElementById('home-link')
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
      }
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
  z-index: 1;
  width: 100%;
  padding: 20px 0;
  color: #eee;
  transition: .5s;

  a {
    text-decoration: none;
    color: #fff;
    margin: 0 5px;
  }

  a:hover {
    color: #fff;
  }
}
</style>
