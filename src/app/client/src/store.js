import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    token: '',
    noticeMessage: '',
    noticeOpened: false
  },
  mutations: {
    SET_TOKEN (state, token) {
      state.token = token
    },
    LOGOUT (state) {
      state.token =  ''
    }
  },
  actions: {

  }
})
