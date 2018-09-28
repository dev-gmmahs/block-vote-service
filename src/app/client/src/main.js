import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import axios from 'axios'

import { library } from '@fortawesome/fontawesome-svg-core'
import { faCoffee, faKey, faSignInAlt, faUserPlus, faHome, faUser, faPlusCircle, faHandPointLeft, faUserShield, faUsers, faSmileWink } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add([faCoffee, faKey, faSignInAlt, faUserPlus, faHome, faUser, faPlusCircle, faHandPointLeft, faUserShield, faUsers, faSmileWink])
Vue.component('fa-icon', FontAwesomeIcon)

Vue.config.productionTip = false
Vue.prototype.$http = axios

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
