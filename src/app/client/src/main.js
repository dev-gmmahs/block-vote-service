import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import axios from 'axios'
import Chart from 'chart.js'

import { library } from '@fortawesome/fontawesome-svg-core'
import { faInfoCircle,
  faKey,
  faSignInAlt,
  faUserPlus,
  faHome,
  faUser,
  faPlusCircle,
  faHandPointLeft,
  faUserShield,
  faUsers,
  faSmileWink,
  faFrownOpen } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add([faInfoCircle,
  faKey,
  faSignInAlt,
  faUserPlus,
  faHome,
  faUser,
  faPlusCircle,
  faHandPointLeft,
  faUserShield,
  faUsers,
  faSmileWink,
  faFrownOpen])
Vue.component('fa-icon', FontAwesomeIcon)

Vue.config.productionTip = false
Vue.prototype.$http = axios
Vue.prototype.$chart = Chart

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
