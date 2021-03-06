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
@import "./common.scss";

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
  @include gradient-background;
  position: fixed;
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
    width: 80%;
    height: 100px;
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

.vertical-outer {
  display: table;
  width: 100%;
  height: 100%;
}

.vertical-inner {
  display: table-cell;
  vertical-align: middle;
}

.vertical-area {
  margin-left: auto;
}

.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, .5);
  display: table;
  transition: opacity .3s ease;
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}

.modal-container {
  width: 50%;
  height: 64%;
  margin: 0px auto;
  padding: 20px 30px;
  background-color: #fff;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, .33);
  box-sizing: border-box;
  transition: all .3s ease;
  font-family: Helvetica, Arial, sans-serif;
  overflow-y: auto;
}

@media screen and (max-width: 768px) {
  .modal-container {
    width: 90%;
  }
}

.modal-header {
  margin-top: 0;
  color: #42b983;
}

.modal-body {
  margin: 20px 0;

  .user-count {
    margin: 10px auto;
  }
}

.modal-default-button {
  cursor: pointer;
  outline: none;
  border: 2px solid dodgerblue;
  padding: 8px 14px;
  background-color: transparent;
  color: #888;
  border-radius: 5px;
  transition: .5s;
}

.modal-default-button:hover {
  background-color: dodgerblue;
  color: #fff;
}

.modal-enter {
  opacity: 0;
}

.modal-leave-active {
  opacity: 0;
}

.modal-enter .modal-container,
.modal-leave-active .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}

</style>
