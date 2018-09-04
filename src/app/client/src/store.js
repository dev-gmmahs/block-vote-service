import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    token: '',
    name: ''
  },
  mutations: {
    SET_TOKEN (state, token) {
      state.token = token
    },
    SET_NAME (state, name) {
      state.name = name
    }
  },
  actions: {

  }
})
