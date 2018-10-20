<template>
  <transition name="modal">
    <div class="modal-mask">
      <div class="modal-wrapper">
        <div class="modal-container">
          <div class="modal-header">
            <b>{{ data.name }}</b>
          </div>
          <div class="modal-body">
            <div class="user-count">
              <fa-icon icon="user"/>
              현재 참여자 수: <b>{{ users }}</b>명
            </div>
            <div class="chart-area">
              <b>시간대별 참여자 현황</b>
              <br>
              <br>
              <canvas id="time-chart"></canvas>
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
  name: 'vote-modal',
  props: ['data'],
  data () {
    return {
      voteData: null
    }
  },
  computed: {
    users () {
      try {
        return this.voteData['users'] || 0
      } catch (e) {
        return 0
      }
    }
  },
  created () {
    this.getVoteDetailData()
  },
  methods: {
    getVoteDetailData () {
      if (!this.data.code) {
        console.log('투표 코드가 없습니다.')
        return
      }

      this.$http.get('/info/vote/detail/' + this.data.code, {
        headers: { Authorization: 'Bearer ' + this.$store.state.token }
      }).then(r => {
        this.voteData = r.data.vote
        this.createTimeDataChart()
      }).catch(e => {
        const code = e.response.data.code
        if (code === 2) {
          alert('접근 권한이 없습니다. 다시 로그인해주세요')
          this.$store.commit('LOGOUT')
          this.$router.push({ path: '/' })
        } else if (code === 6) {
          alert('해당 투표가 존재하지 않거나 조회할 권한이 없습니다.')
        }
      })
    },
    createTimeDataChart () {
      const ctx = document.getElementById('time-chart')

      const labels = this.voteData.time.map(d => d.hour)
      const data = this.voteData.time.map(d => d.count)

      this.timeChart = new this.$chart(ctx, {
        type: 'bar',
        data: {
          labels: labels,
          datasets: [
            {
              label: '참여자 수',
              data: data,
              backgroundColor: ['#00afa8'],
              borderColor: ["#08aeea"],
              borderWidth: 2
            }
          ]
        },
        options: {
          responsive: true,
          scales: {
            yAxes: [
              {
                scaleLabel: {
                  display: true,
                  labelString: '참여 인원'
                },
                ticks: {
                  beginAtZero: true,
                  callback (value) {
                    return value + '명'
                  }
                }
              }
            ],
            xAxes: [
              {
                scaleLabel: {
                  display: true,
                  labelString: '시(Hour)'
                },
                ticks: {
                  beginAtZero: true,
                  callback (value) {
                    return value + '시'
                  }
                }
              }
            ]
          }
        }
      })
    },
    createGenderDataChart () {
      /* 성별 Pie 차트 */
    }
  }
}
</script>

<style lang="scss">
.chart-area {
  width: 100%;
  padding: 10px;
  box-sizing: border-box;
  border-radius: 5px;
  box-shadow: 0px 0px 8px rgba(0, 0, 0, .3);
  margin: 10px 0;

  canvas {
    width: 100%;
  }
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
  float: right;
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
