# qrcode 6.0 (PIL 필요_5.2.0)

import qrcode

# 지정한 URL QR코드로 생성
# (임의의 문자열도 가능)
img = qrcode.make("https://github.com/dev-gmmahs/block-vote-service")

# 생성된 QR코드 저장
img.save("./qrcode.png")

# 닫기
img.close()
