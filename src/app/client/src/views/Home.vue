<template>
  <div class="home">
    <div class="gradient-panel">
      <div class="vote-code-area">
        <h1>투표에 참여하세요!</h1>
        <div class="code-input-area">
          <input type="text" placeholder="참여코드">
          <button>V</button>
        </div>
      </div>
      <div class="bottom-area">
        <img src="@/assets/arrow.png">
      </div>
    </div>
    <div class="content">
      <h2>정보</h2>
      <div class="info-image">
        <img src="@/assets/vote.png">
        <br>
        <div>
          <p class="img-title">투표</p>
          누구나 참여할 수 있습니다
        </div>
      </div>
      <div class="info-image">
        <img src="@/assets/lock.png">
        <br>
        <div>
          <p class="img-title">보안</p>
          안전하게 검증한 후 저장합니다
        </div>
      </div>
      <div class="info-image">
        <img src="@/assets/smile.png">
        <br>
        <div>
          <p class="img-title">편리</p>
          회원가입 후 간편하게 참여가능합니다
        </div>
      </div>
    </div>
    <div class="content darker">
      Hello
    </div>
    <footer>
      <div>Copyright (c) 2018 GMMAHS Community</div>
    </footer>
  </div>
</template>

<script>

export default {
  name: 'home'
}
</script>

<style lang="scss">

.img-title {
  font-size: 1.5rem;
  font-weight: bold;
}

.home {
  width: 100%;
  height: 100%;

  .content {
    padding: 20px;

    &.darker {
      background-color: #eee;
    }

    .info-image {
      display: inline-block;
      box-sizing: border-box;
      width: 20%;
      padding: 5%;
      margin: 15px;
      box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);
      border-radius: 10px;

      img {
        width: 100%;
      }

      div {
        display: inline-block;
      }
    }

    @media screen and (max-width: 768px) {
      .info-image {
        display: block;
        width: 100%;
        margin: 0;
        margin-bottom: 30px;

        img {
          width: 60%;
        }
      }
    }
  }

  footer {
    background-color: #3b74e5;
    padding: 20px 0;
    color: #fff;
  }

  .gradient-panel {
    position: relative;
    width: 100%;
    height: 100%;
    background: #62f760; /* Old browsers */
    background: -moz-linear-gradient(-45deg, #62f760 0%, #3b74e5 100%); /* FF3.6-15 */
    background: -webkit-linear-gradient(-45deg, #62f760 0%,#3b74e5 100%); /* Chrome10-25,Safari5.1-6 */
    background: linear-gradient(135deg, #62f760 0%,#3b74e5 100%); /* W3C, IE10+, FF16+, Chrome26+, Opera12+, Safari7+ */
    filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#62f760', endColorstr='#3b74e5',GradientType=1 ); /* IE6-9 fallback on horizontal gradient */

    .vote-code-area {
      position: absolute;
      top: 28%;
      left: 50%;
      box-sizing: border-box;
      color: #fff;
      width: 276px;
      margin-left: -138px;

      .code-input-area {
        position: relative;
        display: inline-block;

        input {
          outline: none;
          border: 2px solid #fff;
          padding: 8px 14px;
          background-color: transparent;
          border-top-left-radius: 10px;
          border-bottom-left-radius: 10px;
          color: #fff;
          transition: .5s;
        }

        input:focus {
          box-shadow: 0px 0px 20px rgba(255, 255, 255, 0.5);
        }

        button {
          position: absolute;
          right: -8px;
          cursor: pointer;
          outline: none;
          border: none;
          background-color: #fff;
          width: 35px;
          height: 35px;
          color: dodgerblue;
          font-weight: bold;
          font-size: 1rem;
          border-top-right-radius: 10px;
          border-bottom-right-radius: 10px;
        }

        button:hover {
          background-color: #eee;
        }
      }
    }

    .bottom-area {
      position: absolute;
      bottom: 0px;
      left: 50%;
      margin-left: -40px;
      animation: arrow .8s alternate infinite;
    }
  }
}

@keyframes arrow {
  100% {
    bottom: 16px;
  }
}

</style>
