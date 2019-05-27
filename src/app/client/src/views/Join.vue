<template>
  <div id="join">
    <div class="gradient-header"></div>
    <div class="panel">
      <h2>회원가입</h2>
      <transition name="fade" mode="out-in">
        <div v-if="view === 0" :key="1">
          <p>이용약관</p>
          <div class="terms-area">
          <h2>제 1 장 총칙 (임의 약관입니다)</h2>
          <br>
          <h3>제 1 조 (목적)</h3>
          <p>본 약관은 GMMAHS 근자감팀이 운영하는 웹 사이트 (https://coidroid.com)의 제반 서비스의 이용조건 및 절차에 관한 사항 및 기타 필요한 사항을 규정함을 목적으로 한다.</p>
          <br>
          <h3>제 2 조 (용어의 정의)</h3>
          <p>본 약관에서 사용하는 용어는 다음과 같이 정의한다.<br>
          ①회원 : 기본 회원 정보를 입력하였고, 회사와 서비스 이용계약을 체결하여 아이디를 부여받은 개인<br>
          ②아이디(ID) : 회원식별과 회원의 서비스 이용을 위해 회원이 선정하고 회사가 승인하는 문자와 숫자의 조합<br>
          ③비밀번호(Password) : 회원이 통신상의 자신의 비밀을 보호하기 위해 선정한 문자와 숫자의 조합<br>
          ④해지 : 회사 또는 회원에 의한 이용계약의 종료</p>
          <br>
          <h3>제 3 조 (약관의 공시 및 효력과 변경)</h3>
          <p>①본 약관은 회원가입 화면에 게시하여 공시하며 회사는 사정변경 및 영업상 중요한 사유가 있을 경우 약관을 변경할 수 있으며 변경된 약관은 공지사항을 통해 공시한다<br>
          ②본 약관 및 차후 회사사정에 따라 변경된 약관은 이용자에게 공시함으로써 효력을 발생한다.</p>
          <br>
          <h3>제 4 조 (약관 외 준칙)</h3>
          <p>본 약관에 명시되지 않은 사항이 전기통신기본법, 전기통신사업법, 정보통신촉진법, ‘전자상거래등에서의 소비자 보호에 관한 법률’,
          ‘약관의 규제에관한법률’, ‘전자거래기본법’, ‘전자서명법’, ‘정보통신망 이용촉진등에 관한 법률’,
          ‘소비자보호법’ 등 기타 관계 법령에 규정되어 있을 경우에는 그 규정을 따르도록 한다.</p>
          <br><br>
          <h2>제 2 장 이용계약</h2>
          <br>
          <h3>제 5 조 (이용신청)</h3>
          <p>①이용신청자가 회원가입 안내에서 본 약관과 개인정보보호정책에 동의하고 등록절차(회사의 소정 양식의 가입 신청서 작성)를 거쳐 '확인' 버튼을 누르면 이용신청을 할 수 있다.<br>
          ②이용신청자는 반드시 실명과 실제 정보를 사용해야 하며 1개의 생년월일에 대하여 1건의 이용신청을 할 수 있다.<br>
          ③실명이나 실제 정보를 입력하지 않은 이용자는 법적인 보호를 받을 수 없으며, 서비스 이용에 제한을 받을 수 있다.</p>
          <br>
          <h3>제 6 조 (이용신청의 승낙)</h3>
          <p>①회사는 제5조에 따른 이용신청자에 대하여 제2항 및 제3항의 경우를 예외로 하여 서비스 이용을 승낙한다.<br>
          ②회사는 아래 사항에 해당하는 경우에 그 제한사유가 해소될 때까지 승낙을 유보할 수 있다.<br></p>
          &nbsp;가. 서비스 관련 설비에 여유가 없는 경우<br>
          &nbsp;나. 기술상 지장이 있는 경우<br>
          &nbsp;다. 기타 회사 사정상 필요하다고 인정되는 경우<br>
          <br>
          ③회사는 아래 사항에 해당하는 경우에 승낙을 하지 않을 수 있다.<br>
          &nbsp;가. 다른 사람의 명의를 사용하여 신청한 경우<br>
          &nbsp;나. 이용자 정보를 허위로 기재하여 신청한 경우<br>
          &nbsp;다. 사회의 안녕질서 또는 미풍양속을 저해할 목적으로 신청한 경우<br>
          &nbsp;라. 기타 회사가 정한 이용신청 요건이 미비한 경우<br>
          <br>
          <h2>제 3 장 계약 당사자의 의무</h2>
          <br>
          <h3>제 7 조 (회사의 의무)</h3>
          <p>①회사는 사이트를 안정적이고 지속적으로 운영할 의무가 있다.<br>
          ②회사는 이용자로부터 제기되는 의견이나 불만이 정당하다고 인정될 경우에는 즉시 처리해야 한다.<br>
          단, 즉시 처리가 곤란한 경우에는 이용자에게 그 사유와 처리일정을 공지사항 또는 전자우편을 통해 통보해야 한다.<br>
          ③제1항의 경우 수사상의 목적으로 관계기관 및 정보통신윤리위원회의 요청이 있거나 영장 제시가 있는 경우, 기타 관계 법령에 의한 경우는 예외로 한다.</p>
          <br>
          <h3>제 8 조 (이용자의 의무)</h3>
          <p>①이용자는 본 약관 및 회사의 공지사항, 사이트 이용안내 등을 숙지하고 준수해야 하며 기타 회사의 업무에 방해되는 행위를 해서는 안된다.<br>
          ②이용자는 회사의 사전 승인 없이 본 사이트를 이용해 어떠한 영리행위도 할 수 없다.<br>
          ③이용자는 본 사이트를 통해 얻는 정보를 회사의 사전 승낙 없이 복사, 복제, 변경, 번역, 출판, 방송 및 기타의 방법으로 사용하거나 이를 타인에게 제공할 수 없다.</p>
          <br>
          <h2>제 4 장 서비스의 제공 및 이용</h2>
          <br>
          <h3>제 9 조 (서비스 이용)</h3>
          <p>①이용자는 본 약관의 규정된 사항을 준수해 사이트를 이용한다.<br>
          ②본 약관에 명시되지 않은 서비스 이용에 관한 사항은 회사가 정해 '공지사항'에 게시하거나 또는 별도로 공지하는 내용에 따른다.</p>
          <br>
          <h3>제 10 조 (정보의 제공)</h3>
          <p>회사는 회원이 서비스 이용 중 필요하다고 인정되는 다양한 정보에 대하여 전자메일이나 서신우편 등의 방법으로 회원에게 정보를 제공할 수 있다.</p>
          <br>
          <h3>제 11 조 (광고게재)</h3>
          <p>①회사는 서비스의 운용과 관련하여 서비스 화면, 홈페이지, 전자우편 등에 광고 등을 게재할 수 있다.<br>
          ②회사는 사이트에 게재되어 있는 광고주의 판촉활동에 회원이 참여하거나 교신 또는 거래의 결과로서 발생하는 모든 손실 또는 손해에 대해 책임을 지지 않는다.</p>
          <br>
          <h3>제 12 조 (서비스 이용의 제한)</h3>
          <p>본 사이트 이용 및 행위가 다음 각 항에 해당하는 경우 회사는 해당 이용자의 이용을 제한할 수 있다.<br>
          &nbsp;①공공질서 및 미풍양속, 기타 사회질서를 해하는 경우<br>
          &nbsp;②범죄행위를 목적으로 하거나 기타 범죄행위와 관련된다고 객관적으로 인정되는 경우<br>
          &nbsp;③타인의 명예를 손상시키거나 타인의 서비스 이용을 현저히 저해하는 경우<br>
          &nbsp;④타인의 의사에 반하는 내용이나 광고성 정보 등을 지속적으로 전송하는 경우<br>
          &nbsp;⑤해킹 및 컴퓨터 바이러스 유포 등으로 서비스의 건전한 운영을 저해하는 경우<br>
          &nbsp;⑥다른 이용자 또는 제3자의 지적재산권을 침해하거나 지적재산권자가 지적 재산권의 침해를 주장할 수 있다고 판단되는 경우<br>
          &nbsp;⑦타인의 아이디 및 비밀번호를 도용한 경우<br>
          &nbsp;⑧기타 관계 법령에 위배되는 경우 및 회사가 이용자로서 부적당하다고 판단한 경우</p>
          <br>
          <h3>제 13 조 (서비스 제공의 중지)</h3>
          <p>회사는 다음 각 호에 해당하는 경우 서비스의 전부 또는 일부의 제공을 중지할 수 있다.<br>
          &nbsp;①전기통신사업법 상에 규정된 기간통신 사업자 또는 인터넷 망 사업자가 서비스를 중지했을 경우<br>
          &nbsp;②정전으로 서비스 제공이 불가능할 경우<br>
          &nbsp;③설비의 이전, 보수 또는 공사로 인해 부득이한 경우<br>
          &nbsp;④서비스 설비의 장애 또는 서비스 이용의 폭주 등으로 정상적인 서비스 제공이 어려운 경우<br>
          &nbsp;⑤전시, 사변, 천재지변 또는 이에 준하는 국가비상사태가 발생하거나 발생할 우려가 있는 경우</p>
          <br>
          <h3>제 14 조 (게시물 관리)</h3>
          <p>회사는 건전한 통신문화 정착과 효율적인 사이트 운영을 위하여 이용자가 게시하거나<br>
          제공하는 자료가 제12조에 해당한다고 판단되는 경우에 임의로 삭제, 자료이동, 등록거부를 할 수 있다.</p>
          <br>
          <h3>제 15 조 (서비스 이용 책임)</h3>
          <p>이용자는 회사에서 권한 있는 사원이 서명한 명시적인 서면에 구체적으로 허용한 경우를 제외하고는<br>
          서비스를 이용하여 불법상품을 판매하는 영업활동을 할 수 없으며 특히 해킹, 돈벌기 광고, 음란 사이트를 통한 상업행위, 상용 S/W 불법제공 등을 할 수 없다.<br>
          이를 어기고 발생한 영업활동의 결과 및 손실, 관계기관에 의한 구속 등 법적 조치 등에 관해서는 회사가 책임을 지지 않는다.</p>
          <br>
          <h2>제 6 장 기타</h2>
          <br>
          <h3>제 19 조 (면책 및 손해배상)</h3>
          <p>①천재지변 또는 이에 준하는 불가항력으로 인하여 서비스를 제공할 수 없는 경우에는 회사의 서비스 제공 책임이 면제된다.<br>
          ②회사는 이용자간 또는 이용자와 제3자간의 상호거래 관계에서 발생되는 결과에 대하여 어떠한 책임도 부담하지 않는다.<br>
          ③회사는 이용자가 게시판에 게재한 정보, 자료, 내용 등에 관하여 사실의 정확성, 신뢰도 등에 어떠한 책임도 부담하지 않으며 이용자는 본인의 책임 아래 본 사이트를 이용해야 한다.<br>
          ④이용자가 게시 또는 전송한 자료 등에 관하여 손해가 발생하거나 자료의 취사선택, 기타 무료로 제공되는 서비스 이용과 관련해 어떠한 불이익이 발생하더라도 이에 대한 모든 책임은 이용자에게 있다.<br>
          ⑤아이디와 비밀번호의 관리 및 이용자의 부주의로 인하여 발생되는 손해 또는 제3자에 의한 부정사용 등에 대한 책임은 이용자에게 있다.<br>
          ⑥이용자가 본 약관의 규정을 위반함으로써 회사에 손해가 발생하는 경우 이 약관을 위반한 이용자는 회사에 발생한 모든 손해를 배상해야 하며 동 손해로부터 회사를 면책시켜야 한다.</p>
          <br>
          <h3>제 20 조 (개인신용정보 제공 및 활용에 대한 동의서)</h3>
          <p>회사가 회원 가입과 관련해 취득한 개인 신용 정보는 신용정보의 이용 및 보호에 관한 법률 제23조의 규정에 따라<br>
          타인에게 제공 및 활용 시 이용자의 동의를 얻어야 한다.<br>
          이용자의 동의는 회사가 회원으로 가입한 이용자의  신용정보를 신용정보기관, 신용정보업자 및 기타 이용자 등에게 제공해<br>
          이용자의 신용을 판단하기 위한 자료로서 활용하거나 공공기관에서 정책자료로 활용하는데 동의하는 것으로 간주한다.</p>
          <br>
          <h3>제 21 조 (분쟁의 해결)</h3>
          <p>&nbsp;①회사와 이용자는 본 사이트 이용과 관련해 발생한 분쟁을 원만하게 해결하기 위하여 필요한 모든 노력을 해야 한다.<br>
          &nbsp;②제1항의 규정에도 불구하고 동 분쟁으로 인하여 소송이 제기될 경우 동 소송은 회사의 본사 소재지를 관할하는 법원의 관할로 본다.<br></p>
          <br>
          <h3>기타</h3>
          <p>본 약관은 2018년 09월 01일부터 적용한다.</p>
          </div>
          <label class="container">
            동의합니다&nbsp;
            <input type="checkbox" v-model="agree">
            <span class="checkmark"></span>
          </label>
          <br>
          <button :class="!agree ? 'disable' : 'able'" @click="view = agree ? 1 : 0">다음</button>
        </div>
        <div v-else-if="view === 1" :key="2">
          <form @submit.prevent="submit">
            <div class="input-area">
              <input v-model="id" @keydown="idChecked = false" placeholder="아이디" maxlength="20" required>
              <br>
              <br>
              <button type="button" @click="checkId">중복확인</button>
            </div>
            <div class="input-area">
              <input v-model="password_1" type="password" maxlength="18" placeholder="비밀번호" required>
            </div>
            <div class="input-area">
              <input v-model="password_2" type="password" maxlength="18" placeholder="비밀번호 재입력" required>
            </div>
            <div class="input-area">
              <input v-model="name" placeholder="성명" maxlength="5" required>
            </div>
            <div class="input-area">
              <select v-model="sex">
                <option value="0">남성</option>
                <option value="1">여성</option>
                <option value="2">기타</option>
              </select>
            </div>
            <transition name="fade" mode="out-in">
              <p class="message-area" v-if="msg">{{ msg }}</p>
            </transition>
            <button type="submit" :class="done ? 'able' : 'disable'">가입</button>
          </form>
        </div>
        <div v-else-if="view === 2">
          <h2>{{ msg }}</h2>
          <button class="able" @click="view = 1">뒤로가기</button>
        </div>
        <div v-else-if="view === 3">
          <h2>{{ name }}님 환영합니다</h2>
        </div>
      </transition>
      <router-link to="/">홈으로 이동</router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'join',
  data () {
    return {
      view: 0, // 뷰 데이터 (0: 첫 화면, 1: 두 번째 화면..)
      agree: false, // 약관 동의 여부
      id: '', // 유저 아이디
      idChecked: false, // 유저 아이디 체크 확인
      password_1: '', // 비밀번호
      password_2: '', // 비밀번호 재입력
      name: '', // 성명
      sex: 0, // 성별
      msg: '', // 메시지
      alreadySubmit: false // 제출 여부 확인
    }
  },
  computed: {
    done () {
      return this.check()
    }
  },
  methods: {
    /**
     * @description 폼 입력 검증
     */
    check () {
      if (!this.id.match(/^[a-z0-9]{6,20}$/)) {
        this.msg = '아이디는 영문 소문자, 숫자 조합으로 6~20길이 입니다.'
        return false
      }

      if (!this.idChecked) {
        this.msg = '아이디 중복확인을 해주세요'
        return false
      }

      if (!this.password_1.match(/^[a-z0-9]{8,18}$/)) {
        this.msg = '비밀번호는 영문 소문자, 숫자 조합으로 8~18길이 입니다.'
        return false
      }

      if (this.password_1 !== this.password_2) {
        this.msg = '비밀번호를 한번 더 입력해주세요'
        return false
      }

      if (!this.name.match(/^[가-힣]{2,5}$/)) {
        this.msg = '성명은 한글로 최소 2글자 입니다.'
        return false
      }

      this.msg = ''
      return true
    },
    /**
     * @description 아이디 중복 확인
     */
    checkId () {
      this.$http.post('/check/id', {
        id: this.id
      }).then(r => {
        alert('사용 가능한 아이디입니다.')
        this.idChecked = true
      }).catch(e => {
        this.idChecked = false
        const code = e.response.data.code
        if (code === 51) {
          alert('이미 존재하는 아이디입니다.')
        } else {
          alert('알 수 없는 오류 발생')
        }
      })
    },
    /**
     * @description 서버에 회원가입 요청
     */
    submit () {
      if (this.alreadySubmit) {
        return
      }

      if (!this.check()) {
        return
      }

      this.alreadySubmit = true
      this.$http.post('/info/login/regist', {
        id: this.id,
        password: this.password_1,
        name: this.name,
        sex: this.sex
      }).then(r => {
        if (r.data.success) {
          this.msg = this.name + '님 환영합니다'
          this.view = 3
        } else {
          this.msg = r.data.message
          this.view = 2
        }
      }).catch(e => {
        this.view = 2
        console.error(e)
        this.msg = e.message
      }).finally(() => {
        this.alreadySubmit = false
      })
    }
  }
}
</script>

<style lang="scss">
#join {
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  width: 100%;
  height: 100%;
}

.terms-area {
  padding: 10px;
  border-radius: 5px;
  background-color: #eee;
  height: 200px;
  overflow-y: auto;
  text-align: left;
  font-size: 0.8rem;
}

.message-area {
  font-weight: bold;
  font-size: 0.9rem;
}
</style>
