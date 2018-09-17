import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    token: '',
    noticeMessage: '',
    noticeOpened: false,
    voteCode: ''
  },
  mutations: {
    SET_TOKEN (state, token) {
      state.token = token
    },
    LOGOUT (state) {
      state.token =  ''
    },
    SET_VOTE_CODE (state, code) {
      state.voteCode = code
    },
    END_VOTE (state) {
      state.voteCode = ''
    }
  },
  actions: {

  }
})
