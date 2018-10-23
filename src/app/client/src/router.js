import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Login from './views/Login.vue'
import Join from './views/Join.vue'
import Create from './views/Create.vue'
import Vote from './views/Vote.vue'
import Mypage from './views/Mypage.vue'
import Blocks from './views/Blocks.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/join',
      name: 'join',
      component: Join
    },
    {
      path: '/create',
      name: 'create',
      component: Create
    },
    {
      path: '/vote',
      name: 'vote',
      component: Vote
    },
    {
      path: '/mypage',
      name: 'mypage',
      component: Mypage
    },
    {
      path: '/blocks',
      name: 'blocks',
      component: Blocks
    }
  ]
})
