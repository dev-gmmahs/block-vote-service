<template>
  <transition name="modal">
    <div class="modal-mask">
      <div class="modal-wrapper">
        <div class="modal-container-2">
          <div class="modal-header">
            <b></b>
          </div>
          <div class="modal-body">
            <div v-if="view === 1">
              <img class="info-img" src="@/assets/everyone.png">
              <br>
              회원가입 후 투표에 참여하실 수 있습니다.<br><br>
              나이/성별 제한 없이 투표에 참여할 수 있으며<br>
              투표도 생성하여 결과를 확인할 수 있습니다.
            </div>
            <div v-if="view === 2">
              <img class="info-img" src="@/assets/security.png">
              <br>
              블록체인의 작업증명 알고리즘을 적용하여 안전합니다.<br><br>
              투표 데이터는 암호화되어 전달되며<br>
              서버에서 검증을 마친 후 저장합니다.
            </div>
            <div v-if="view === 3">
              <img class="info-img" src="@/assets/simple.png">
              <br>
              투표에 쉽게 참여할 수 있습니다.<br><br>
              투표소에 이동하지 않아도 PC, 태블릿, 모바일 등<br>
              여러 환경의 플랫폼에서 간단하게 참여 가능합니다.
            </div>
          </div>
          <button class="modal-default-button" @click="$emit('close')">확인</button>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
export default {
  name: 'vote-info-modal',
  props: ['view']
}
</script>

<style lang="scss">

.modal-container-2 {
  width: 50%;
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

.info-img {
  width: 50%;
}

.hover-menu {
  position: relative;
  margin: 5px auto;
  cursor: pointer;
  width: 200px;

  .hidden {
    pointer-events: none;
    position: absolute;
    padding: 10px;
    box-sizing: border-box;
    top: -120px;
    width: 200px;
    left: 0px;
    background-color: rgba(0, 0, 0, .8);
    color: #fff;
    opacity: 0;
    transition: .3s;
  }

  &:hover {

    .hidden {
      opacity: 1;
    }
  }
}

</style>
