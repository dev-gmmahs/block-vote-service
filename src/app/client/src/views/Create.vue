<template>
  <div id="create">
    <div class="gradient-header"></div>
    <div class="panel create-panel">
      <h2>새 투표 생성</h2>
      <transition name="fade" mode="out-in">
        <div v-if="view === 0" :key="1">
          <h3>투표 정보 작성</h3>
          <div class="input-area">
            <input v-model.trim="voteName" placeholder="투표 명">
          </div>
          <div class="input-area">
            <textarea v-model.trim="voteIntro" placeholder="투표 설명"/>
          </div>
          <div class="input-area">
            <label>시작일</label>
            <input type="date" v-model="startDate">
            <select v-model.number="startTime">
              <option disabled value="">시간</option>
              <option v-for="hour in hours" :key="hour">{{ hour }}</option>
            </select>
            <b> 시</b>
          </div>
          <div class="input-area">
            <label>마감일</label>
            <input type="date" v-model="endDate">
            <select v-model.number="endTime">
              <option disabled value="">시간</option>
              <option v-for="hour in hours" :key="hour">{{ hour }}</option>
            </select>
            <b> 시</b>
          </div>
          <button :class="!voteCheck ? 'disable' : 'able'" @click="view = voteCheck ? 1 : 0">다음</button>
        </div>
        <div v-else-if="view === 1" :key="2">
          <h3>투표 옵션 및 항목 작성</h3>
          <form @submit.prevent="submit">
            <div class="option-area">
              <b class="option-title">참여 인원</b>
              <br><br>
              <label>제한없음</label>
              <input type="radio" name="limit" v-model.number="limit" value="0">
              &nbsp;
              <label>직접 지정</label>
              <input type="radio" name="limit" v-model.number="limit" value="1">
            </div>
            <transition name="fade" mode="out-in">
              <div class="input-area" v-if="limit === 1">
                <input type="number" min="5" v-model.number="limitCount">
              </div>
            </transition>
            <hr>
            <div class="option-area">
              <b class="option-title">참여자</b>
              <br><br>
              <label>누구나</label>
              <input type="radio" name="target" v-model.number="voteTarget" value="0">
              &nbsp;
              <label>직접 지정</label>
              <input type="radio" name="target" v-model.number="voteTarget" value="1">
            </div>
            <transition name="fade" mode="out-in">
              <div class="vote-target-area" id="target-area" v-if="voteTarget === 1">
                <item v-for="target in targetList" :key="target" :id="target" @close="removeTarget"/>
                <div class="already-area">
                  <transition name="fade" mode="out-in">
                    <b v-if="alreadyInList">이미 존재하는 아이디입니다.</b>
                  </transition>
                </div>
                <div class="input-area">
                  <input v-model.trim="targetTemp" placeholder="참여자 ID" @keydown="targetKeyDown" style="margin-bottom: 5px;">
                  <button type="button" @click="targetKeyDown('click')" class="add-btn">추가</button>
                </div>
                <b>{{ targetList.length }} / {{ limit === 1 ? limitCount + '명' : '제한없음' }}</b>
              </div>
            </transition>
            <button :class="voteItemCheck ? 'able' : 'disable'">생성하기</button>
          </form>
        </div>
        <div v-else-if="view === 2">
          <h3>{{ msg }}</h3>
          <button class="able" @click="view = 1">뒤로가기</button>
        </div>
        <div v-else-if="view === 3">
          <h2>투표가 생성되었습니다</h2>
          <div class="message-area">
            <p>투표 코드</p>
            <h1>{{ voteCode }}</h1>
          </div>
        </div>
      </transition>
      <div class="message-area">
        <transition name="fade" mode="out-in">
          <b v-if="msg">{{ msg }}</b>
        </transition>
      </div>
      <div class="message-area">
        <a v-if="view !== 0" @click="back">뒤로</a>
      </div>
      <router-link to="/">홈으로 이동</router-link>
    </div>
  </div>
</template>

<script>
import Item from '@/components/VoteItem.vue'

export default {
  name: 'create',
  data () {
    return {
      view: 0,
      hours: [],
      targetList: [],
      items: [],
      voteName: '',
      voteIntro: '',
      startDate: '',
      startTime: '',
      endDate: '',
      endTime: '',
      voteTarget: 0,
      targetTemp: '',
      limit: 0,
      limitCount: 5,
      alreadyInList: false,
      msg: '',
      voteCode: ''
    }
  },
  components: {
    'item': Item
  },
  created () {
    for (let i = 0; i < 24; i++) {
      this.hours.push(i)
    }
    const currentTime = new Date()
    const y = currentTime.getFullYear()
    const m = this.toZero(currentTime.getMonth() + 1)
    const d = this.toZero(currentTime.getDate())
    this.startDate = this.endDate = `${y}-${m}-${d}`
    this.startTime = this.endTime = currentTime.getHours()
  },
  computed: {
    voteCheck () {
      return this.check()
    },
    voteItemCheck () {
      return this.itemCheck()
    }
  },
  methods: {
    check () {
      if (!this.voteName.match(/^[a-zA-Z가-힣0-9 ]{5,50}$/)) {
        this.msg = '투표 명은 영문, 한글, 숫자 조합으로 5~50길이 입니다.'
        return false
      }

      if (!this.voteIntro.match(/^[a-zA-Z가-힣0-9 ]{10,100}$/)) {
        this.msg = '투표 설명은 영문, 한글, 숫자 조합으로 10~100길이 입니다.'
        return false
      }

      if (!(this.startDate && this.startTime)) {
        this.msg = '투표 시작일과 시작 시간을 지정해주세요'
        return false
      }

      if (!(this.endDate && this.endTime)) {
        this.msg = '투표 마감일과 종료 시간을 지정해주세요'
        return false
      }

      const date = new Date()
      const y = date.getFullYear()
      const m = date.getMonth() + 1
      const d = date.getDate()
      const h = date.getHours()

      const Sdate = new Date(this.startDate)
      const Edate = new Date(this.endDate)

      if (y > Sdate.getFullYear()) {
        this.msg = '지정한 년도(Year)는 시작일에 사용할 수 없습니다.'
        return false
      }

      if (m > Sdate.getMonth() + 1) {
        this.msg = '지정한 월(Month)는 시작일에 사용할 수 없습니다.'
        return false
      }

      if (d > Sdate.getDate() && m === Sdate.getMonth() + 1 && y >= Sdate.getFullYear()) {
        this.msg = '지정한 일(Day)는 시작일에 사용할 수 없습니다.'
        return false
      }

      if (h > this.startTime && d === Sdate.getDate() && m === Sdate.getMonth() + 1) {
        this.msg = '지정한 시간에 시작할 수 없습니다.'
        return false
      }

      if (Edate.getFullYear() < Sdate.getFullYear()) {
        this.msg = '마감일은 시작일과 같거나 빠를 수 없습니다.'
        return false
      }

      if (Edate.getMonth() < Sdate.getMonth() && Edate.getFullYear() === Sdate.getFullYear()) {
        this.msg = '마감일은 시작일과 같거나 빠를 수 없습니다.'
        return false
      }

      if (Edate.getMonth() === Sdate.getMonth() &&
          Edate.getFullYear() === Sdate.getFullYear() &&
          Edate.getDate() < Sdate.getDate()) {
        this.msg = '마감일은 시작일과 같거나 빠를 수 없습니다.'
        return false
      }

      if (Edate.getMonth() === Sdate.getMonth() &&
          Edate.getFullYear() === Sdate.getFullYear() &&
          Edate.getDate() === Sdate.getDate()) {
        if (this.endTime <= this.startTime) {
          this.msg = '마감일은 시작일과 같거나 빠를 수 없습니다.'
          return false
        }
      }

      this.msg = ''
      return true
    },
    itemCheck () {
      if (this.limit === 1 && this.voteTarget === 1 && this.limitCount > this.targetList.length) {
        this.msg = '참여자 ID를 모두 입력해주세요'
        return false
      }

      this.msg = ''
      return true
    },
    toZero (n) {
      n = n.toString()
      if (n.length !== 2) {
        return '0' + n
      } else {
        return n
      }
    },
    targetKeyDown (e) {
      this.alreadyInList = false
      if (this.limit === 1 && this.limitCount <= this.targetList.length) {
        return
      }

      if (this.targetList.indexOf(this.targetTemp) !== -1) {
        this.alreadyInList = true
        return
      }

      if ((e.keyCode === 13 && this.targetTemp) || e === 'click') {
        this.targetList.push(this.targetTemp)
        this.targetTemp = ''
        const area = document.getElementById('target-area')
        area.scrollTop = area.scrollHeight
      }
    },
    /**
     * @description 새 투표 생성 데이터 제출
     */
    submit () {
      this.$http.post('/create/vote', {
        vote_name: this.voteName,
        vote_start: this.startDate,
        vote_start_time: this.startTime,
        vote_end: this.endDate,
        vote_end_time: this.endTime,
        vote_permission: this.voteTarget,
        vote_limit: this.limitCount,
        vote_target: this.targetList,
        vote_item: this.items
      }, {
        headers: { Authorization: 'Bearer ' + this.$store.state.token }
      }).then(result => {
        if (result.data.success) {
          this.voteCode = result.data.code
          this.view = 3
        } else {
          this.msg = '투표를 생성하지 못했습니다.'
          this.view = 2
        }
      }).catch(e => {
        this.msg = e.message
        this.view = 2
      })
    },
    /**
     * @description 참여자 아이디 요소 삭제
     */
    removeTarget (value) {
      const idx = this.targetList.indexOf(value)
      if (idx !== -1) {
        this.targetList.splice(idx, 1)
      }
    },
    /**
     * @description 화면 이전으로 이동
     */
    back () {
      if (this.view === 0) {
        return
      }
      this.view--
    }
  }
}
</script>

<style lang="scss">
#create {
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  width: 100%;
  height: 100%;
}

.create-panel {
  height: 56%;
  overflow-y: auto;
}

.vote-target-area {
  padding: 10px;
  border: 2px solid #eee;
  border-radius: 5px;
  width: 60%;
  margin: 20px auto;
  height: 400px;
  overflow-y: auto;
}

.terms-area {
  padding: 10px;
  border-radius: 5px;
  background-color: #eee;
  height: 150px;
  overflow-y: auto;
  text-align: left;
  font-size: 0.8rem;
}

.message-area {
  font-weight: bold;
  font-size: 0.9rem;
  margin: 10px 0;
  height: 30px;
  color: indianred;
}

@media screen and (max-width: 768px) {
  .create-panel {
    height: 70%;
    margin-top: 10%;
  }

  .vote-target-area {
    width: 90%;
  }
}

hr {
  display: block;
  height: 1px;
  border: 0;
  border-top: 1px solid #ccc;
  margin: 1em 0;
  padding: 0;
}

.option-area {
  margin: 25px 0;
}

.add-btn {
  height: 30px;
  margin-left: 5px;
  line-height: 12px;
}

.already-area {
  height: 30px;
}

.option-title {
  padding: 5px 10px;
  border-radius: 25px;
  background-color: dodgerblue;
  color: #fff;
  margin: 10px 0;
}
</style>
