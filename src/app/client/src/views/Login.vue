<template>
  <div id="login">
    <div class="gradient-header"></div>
    <div class="panel">
      <h2>로그인</h2>
      <form @submit.prevent="submit">
        <div class="input-area">
          <input v-model="id" placeholder="아이디" @keydown="msg = ''" required>
        </div>
        <div class="input-area">
          <input v-model="password" type="password" autocomplete="password" placeholder="비밀번호" @keydown="msg = ''" required>
        </div>
        <div class="input-area">
          <button>로그인</button>
        </div>
        <div class="login-message">
          <transition name="fade" mode="out-in">
            <p v-if="msg">{{ msg }}</p>
          </transition>
        </div>
      </form>
      <router-link to="/">홈으로 이동</router-link>
      <br><br>
      <b class="ask-account">계정이 없으신가요?</b>&nbsp;
      <router-link to="/join">회원가입</router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'login',
  data () {
    return {
      id: '',
      password: '',
      msg: ''
    }
  },
  methods: {
    /**
     * @description 서버에 로그인 요청
     */
    submit () {
      this.$http.post('/login', { id: this.id, password: this.password }).then(r => {
        this.msg = ''
        if (r.data.token) {
          this.$store.commit('SET_TOKEN', r.data.token)
          this.$router.push({ name: 'home' })
        }
      }).catch(e => {
        this.msg = e.response.data.msg
      })
    }
  }
}
</script>

<style lang="scss">
#login {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100%;
}

.login-message {
  height: 30px;
  color: indianred;
}

.ask-account {
  font-size: 0.9rem;
}
</style>
