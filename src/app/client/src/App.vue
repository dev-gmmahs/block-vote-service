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
      const body = document.body || document.documentElement
      body.scrollTop = 0
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
  position: fixed;
  background: #62f760; /* Old browsers */
  background: -moz-linear-gradient(-45deg, #62f760 0%, #3b74e5 100%); /* FF3.6-15 */
  background: -webkit-linear-gradient(-45deg, #62f760 0%,#3b74e5 100%); /* Chrome10-25,Safari5.1-6 */
  background: linear-gradient(135deg, #62f760 0%,#3b74e5 100%); /* W3C, IE10+, FF16+, Chrome26+, Opera12+, Safari7+ */
  filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#62f760', endColorstr='#3b74e5',GradientType=1 ); /* IE6-9 fallback on horizontal gradient */
  width: 100%;
  height: 50%;
  top: 0px;
  left: 0px;
  z-index: -1;
}

.panel {
  padding: 16px;
  border-radius: 10px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.3);
  background-color: #fff;
  width: 50%;
  box-sizing: border-box;

  a {
    cursor: pointer;
    text-decoration: none;
    color: #888;
  }

  a:hover {
    text-decoration: underline;
  }
}

@media screen and (max-width: 768px) {
  .panel {
    width: 90%;
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
    border: 2px solid dodgerblue;
    padding: 8px 14px;
    background-color: transparent;
    color: #888;
    border-radius: 5px;
    transition: .5s;
  }

  button:hover {
    background-color: dodgerblue;
    color: #fff;
  }

  textarea {
    resize: none;
    outline: none;
    border: 2px solid #eee;
    padding: 8px 14px;
    background-color: transparent;
    color: #888;
    border-radius: 5px;
    transition: .5s;
  }

  textarea:hover {
    border: 2px solid #aaa;
  }

  label {
    margin-right: 10px;
  }

  select {
    outline: none;
    border: 2px solid #eee;
    padding: 8px 14px;
    background-color: transparent;
    color: #888;
    border-radius: 5px;
    margin-left: 10px;
  }
}

.half-input {
  width: 25%;
  margin: 0 5px;
}

.container {
  display: inline-block;
  position: relative;
  cursor: pointer;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  margin: 10px 0px;
}

.checkmark {
  position: absolute;
  top: 0;
  right: 0;
  height: 25px;
  width: 25px;
  background-color: #eee;
}

.container:hover input ~ .checkmark {
  background-color: #ccc;
}

.container input:checked ~ .checkmark {
  background-color: #2196F3;
}

.checkmark:after {
  content: "";
  position: absolute;
  display: none;
}

.container input:checked ~ .checkmark:after {
  display: block;
}

.container .checkmark:after {
  left: 9px;
  top: 5px;
  width: 5px;
  height: 10px;
  border: solid white;
  border-width: 0 3px 3px 0;
  -webkit-transform: rotate(45deg);
  -ms-transform: rotate(45deg);
  transform: rotate(45deg);
}

.disable {
  cursor: not-allowed;
  padding: 5px 10px;
  border-radius: 5px;
  outline: none;
  border: 2px solid #eee;
  background-color: transparent;
  margin: 20px 0;
}

.able {
  cursor: pointer;
  padding: 5px 10px;
  border-radius: 5px;
  outline: none;
  border: 2px solid dodgerblue;
  background-color: transparent;
  margin: 20px 0;
  transition: .5s;
}

.able:hover {
  background-color: dodgerblue;
  color: #fff;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}

.fade-enter, .fade-leave-to {
  opacity: 0;
}
</style>
