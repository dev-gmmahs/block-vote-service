<template>
  <div class="item">
    {{ id }}
    <span @click="close">&#10006;</span>
  </div>
</template>

<script>
export default {
  name: 'item',
  props: ['id'],
  methods: {
    close () {
      this.$emit('close', this.id)
    }
  }
}
</script>

<style lang="scss">
.item {
  position: relative;
  padding: 5px;
  border-radius: 2px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.3);
  margin: 10px 0;

  span {
    cursor: pointer;
    position: absolute;
    display: block;
    color: crimson;
    right: 5px;
    top: 4px;
  }

  span:hover {
    color: #000;
  }
}
</style>
