import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    token: '',
    noticeMessage: '',
    noticeOpened: false,
    voteCode: '',
    voteData: {},
    voting: false
  },
  mutations: {
    SET_TOKEN (state, token) {
      state.token = token
    },
    LOGOUT (state) {
      state.token = ''
    },
    SET_VOTE_CODE (state, code) {
      state.voteCode = code
    },
    SET_VOTE_DATA (state, data) {
      state.voteData = data
    },
    SET_VOTING_STATUS (state, status) {
      state.voting = status
    },
    END_VOTE (state) {
      state.voteCode = ''
    }
  },
  actions: {

  }
})
