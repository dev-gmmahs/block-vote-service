<template>
  <transition name="modal">
    <div class="modal-mask">
      <div class="modal-wrapper">
        <div class="modal-container">
          <div class="modal-header">
            <b>{{ data.name }}</b>
          </div>
          <div class="modal-body" v-if="data.finished">
            <div class="chart-area">
              <b>투표 결과</b>
              <br>
              <br>
              <canvas id="vote-chart"></canvas>
            </div>
          </div>
          <div class="modal-body" v-else>
            <div class="user-count">
              <fa-icon icon="user"/>
              현재 참여자 수: <b>{{ users }}</b>명
            </div>
            <div class="chart-area">
              <b>투표 현황</b>
              <br>
              <br>
              <canvas id="vote-chart"></canvas>
            </div>
            <div class="chart-area">
              <b>시간대별 참여자 현황</b>
              <br>
              <br>
              <canvas id="time-chart"></canvas>
            </div>
            <div class="chart-area">
              <b>참여자 성별 현황</b>
              <br>
              <br>
              <canvas id="gender-chart"></canvas>
            </div>
          </div>
          <button class="modal-default-button" @click="showBlocks">블록 데이터 보기</button>
          <br>
          <br>
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
    /* 컴포넌트 생성 직후 데이터 불러오기 */
    this.getVoteDetailData()
  },
  methods: {
    /**
     * @description 투표 상세정보 데이터를 조회합니다 
     * (참여자 수, 참여 시간 분포, 참여자 성별 현황)
     */
    getVoteDetailData () {
      if (!this.data.code) {
        console.log('투표 코드가 없습니다.')
        return
      }

      /* GET /info/vote/detail */
      this.$http.get('/info/vote/detail/' + this.data.code, {
        // 인증 헤더 (토큰)
        headers: { Authorization: 'Bearer ' + this.$store.state.token }
      }).then(r => {
        this.voteData = r.data.vote

        // 만료된 투표인 경우 결과 데이터 조회
        if (this.voteData.finished) {
          this.getVoteResult().then(r => {
            const d = r.data.result
            if (d) {
              this.createVoteResultChart(d)
            } else {
              alert('투표 결과 데이터가 존재하지 않습니다. 관리자에게 문의해주세요')
            }
          }).catch(e => {
            const code = e.response.data.code
            if (code === 2) {
              alert('접근 권한이 없습니다. 다시 로그인해주세요')
              this.$store.commit('LOGOUT')
              this.$router.push({ path: '/' })
            } else if (code === 6) {
              alert('해당 투표가 존재하지 않거나 조회할 권한이 없습니다.')
            } else if (code === 7) {
              alert('해당 투표는 아직 진행중입니다.')
            } else {
              alert('알 수 없는 오류가 발생했습니다.')
            }
          })
        } else {
          // 만료된 투표가 아닌 경우 상태 그래프 그리기
          this.createVoteDataChart()
          this.createTimeDataChart()
          this.createGenderDataChart()
        }
      }).catch(e => {
        const code = e.response.data.code
        if (code === 2) {
          alert('접근 권한이 없습니다. 다시 로그인해주세요')
          this.$store.commit('LOGOUT')
          this.$router.push({ path: '/' })
        } else if (code === 6) {
          alert('해당 투표가 존재하지 않거나 조회할 권한이 없습니다.')
        } else {
          alert('알 수 없는 오류가 발생했습니다.')
        }
      })
    },
    /**
     * @description 투표 결과 조회 요청 Promise
     */
    getVoteResult () {
      return this.$http.get('/info/vote/result/' + this.data.code, {
        headers: { Authorization: 'Bearer ' + this.$store.state.token }
      })
    },
    /**
     * @description 투표 결과 차트 생성
     */
    createVoteResultChart (data) {
      const ctx = document.getElementById('vote-chart')

      let labels = [], datas = []
      data.forEach(d => {
        labels.push(d.item)
        datas.push(d.count)
      })

      new this.$chart(ctx, {
        type: 'pie',
        data: {
          labels: labels,
          datasets: [
            {
              data: datas,
              backgroundColor: ['#f44336',
                                '#1e88e5',
                                '#ffeb3b',
                                '#43a047',
                                '#cddc39',
                                '#8e24aa',
                                '#ff4081',
                                '#009688',
                                '#ffca28',
                                '#29b6f6'] // 색상 코드
            }
          ]
        },
        options: {
          responsive: true
        }
      })
    },
    /**
     * @description 투표 결과 그래프 (미검증된 임시 결과)
     */
    createVoteDataChart () {
      const ctx = document.getElementById('vote-chart')

      const labels = this.voteData.vote.map(d => d.item)
      const data = this.voteData.vote.map(d => d.count)

      new this.$chart(ctx, {
        type: 'pie',
        data: {
          labels: labels,
          datasets: [
            {
              data: data,
              backgroundColor: ['#f44336',
                                '#1e88e5',
                                '#ffeb3b',
                                '#43a047',
                                '#cddc39',
                                '#8e24aa',
                                '#ff4081',
                                '#009688',
                                '#ffca28',
                                '#29b6f6'] // 색상 코드
            }
          ]
        },
        options: {
          responsive: true
        }
      })
    },
    /**
     * @description 시간 분포 그래프
     */
    createTimeDataChart () {
      const ctx = document.getElementById('time-chart')

      const labels = this.voteData.time.map(d => d.hour)
      const data = this.voteData.time.map(d => d.count)

      new this.$chart(ctx, {
        type: 'bar',
        data: {
          labels: labels,
          datasets: [
            {
              label: '참여자 수',
              data: data,
              backgroundColor: '#00afa8'
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
                  steps: 1,
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
    /**
     * @description 성별 비율 그래프
     */
    createGenderDataChart () {
      const ctx = document.getElementById('gender-chart')

      const labels = this.voteData.gender.map(d => {
        if (d.gender === 0) {
          return '남성'
        } else if (d.gender === 1) {
          return '여성'
        } else {
          return '기타'
        }
      })
      const colors = this.voteData.gender.map(d => {
        if (d.gender === 0) {
          return '#36a2eb'
        } else if (d.gender === 1) {
          return '#ff6384'
        } else {
          return '#ffcd56'
        }
      })
      const data = this.voteData.gender.map(d => d.count)

      this.timeChart = new this.$chart(ctx, {
        type: 'doughnut',
        data: {
          labels: labels,
          datasets: [
            {
              data: data,
              backgroundColor: colors
            }
          ]
        },
        options: {
          responsive: true
        }
      })
    },
    /**
     * @description 투표 참여코드의 블록 데이터 조회
     * 이동: /blocks?code=***
     */
    showBlocks () {
      this.$router.push({
        path: 'blocks',
        query: {
          code: this.data.code
        }
      })
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
