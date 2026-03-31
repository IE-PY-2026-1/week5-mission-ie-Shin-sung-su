# 파일이름 : 나만의 스마트 영화관 키오스크
# 작 성 자 : 60231805 신성수
age = int(input("나이를 입력하시오: "))
coupon = input("할인 구폰이 있나요? (Y/N): ")
print("--------------------------")

if age < 13 and coupon == 'Y':
  print("🍿 꼬마 VIP 고객님! 팝콘 무료 증정!")
if age >= 65 or coupon == 'Y':
  print("티켓 요금 : 무료입니다.")
else:
  print("티켓 요금 : 15,000원입니다.")