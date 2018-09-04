<template>
  <div id="login">
    <div class="gradient-header"></div>
    <div class="panel vertical-half">
      <h2>로그인</h2>
      <form @submit.prevent="submit">
        <div class="input-area">
          <input v-model="id" placeholder="ID" required>
        </div>
        <div class="input-area">
          <input v-model="password" type="password" autocomplete="password" placeholder="Password" required>
        </div>
        <div class="input-area">
          <button>로그인</button>
        </div>
      </form>
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
      password: ''
    }
  },
  methods: {
    submit () {
      this.$http.post('/login', { id: this.id, password: this.password }).then(r => {
        if (r.token) {
          console.log(r)
          this.$state.commt('SET_TOKEN', r.token)
          this.$state.commt('SET_NAME', r.name)
        }
      }).catch(e => {
        console.log(e)
      })
    }
  }
}
</script>

<style lang="scss">
#login {
  position: relative;
  width: 100%;
  height: 100%;

  .panel {
    a {
      cursor: pointer;
      text-decoration: none;
      color: #888;
    }

    a:hover {
      text-decoration: underline;
    }
  }
}
</style>
