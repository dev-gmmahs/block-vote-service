<template>
  <div id="nav">
    <router-link to="/login" id="login-link">로그인</router-link> | 
    <router-link to="/join" id="join-link">회원가입</router-link>
  </div>
</template>

<script>
export default {
  name: 'vote-header',
  props: ['fill'],
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
      if (this.fill) {
        nav.style['background-color'] = '#fff'
        nav.style['box-shadow'] = '0px 0px 10px rgba(0, 0, 0, 0.3)'
        login.style['color'] = join.style['color'] = '#aaa'
      } else {
        nav.style['background-color'] = 'transparent'
        nav.style['box-shadow'] = 'none'
        login.style['color'] = join.style['color'] = '#fff'
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
  }

  a:hover {
    color: #fff;
  }
}
</style>
