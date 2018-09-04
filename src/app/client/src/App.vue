<template>
  <div id="app">
    <vote-header :fill="fill" :path="path"/>
    <router-view/>
  </div>
</template>

<script>
import Header from '@/components/Header.vue'

export default {
  name: 'app',
  data () {
    return {
      fill: false,
      path: 'home'
    }
  },
  components: {
    'vote-header': Header
  },
  watch: {
    '$route' (v) {
      this.path = v.name
    }
  },
  created () {
    window.addEventListener('scroll', this.handleScroll)
  },
  destroyed () {
    window.removeEventListener('scroll', this.handleScroll)
  },
  methods: {
    handleScroll (event) {
      if (window.scrollY >= 100) {
        this.fill = true
      } else {
        this.fill = false
      }
    }
  }
}
</script>

<style lang="scss">
html, body {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  width: 100%;
  height: 100%;
}

.gradient-header {
  position: absolute;
  background: #62f760; /* Old browsers */
  background: -moz-linear-gradient(-45deg, #62f760 0%, #3b74e5 100%); /* FF3.6-15 */
  background: -webkit-linear-gradient(-45deg, #62f760 0%,#3b74e5 100%); /* Chrome10-25,Safari5.1-6 */
  background: linear-gradient(135deg, #62f760 0%,#3b74e5 100%); /* W3C, IE10+, FF16+, Chrome26+, Opera12+, Safari7+ */
  filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#62f760', endColorstr='#3b74e5',GradientType=1 ); /* IE6-9 fallback on horizontal gradient */
  width: 100%;
  height: 50%;
  top: 0px;
  left: 0px;
}

.panel {
  position: absolute;
  padding: 16px;
  border-radius: 10px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.3);
  background-color: #fff;
  z-index: 2;
  margin-left: auto;
  width: 50%;
  margin-left: 25%;
  box-sizing: border-box;
}

@media screen and (max-width: 768px) {
  .panel {
    width: 80%;
    margin-left: 10%;
  }
}

.input-area {
  margin-bottom: 20px;

  input {
    outline: none;
    border: 2px solid #eee;
    padding: 8px 14px;
    background-color: transparent;
    color: #888;
    border-radius: 5px;
    transition: .5s;
  }

  input:hover {
    border: 2px solid #aaa;
  }

  button {
    cursor: pointer;
    outline: none;
    border: 2px solid #eee;
    padding: 8px 14px;
    background-color: transparent;
    color: #888;
    border-radius: 5px;
    transition: .5s;
  }

  button:hover {
    border: 2px solid #aaa;
    background-color: #aaa;
    color: #eee;
  }
}

.vertical-half {
  top: 25%;
}
</style>
