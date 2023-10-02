# graduation , score = map(float, input('졸업학점과 이수학점을 입력하시오.:').split())

# if graduation >= 2.0 and score >= 140:
#     print('졸업 가능')
# elif graduation <2.0 and score >= 140:
#     print('졸업학점 부족')
# elif graduation >=2.0 and score <140:
#     print('이수학점 부족')
# else:
#     print('둘다부족')




# str = input("출생연도입력.:")
# if str[3] == '1' or str[3] == '6':
#     print('월요일 재난 지원금 신청가능')
# elif str[3] == '2' or str[3] == '7':
#     print('화요일 재난 지원금 신청가능')
# elif str[3] == '3' or str[3] == '8':
#     print('수요일 재난 지원금 신청가능')
# elif str[3] == '4' or str[3] == '9':
#     print('목요일 재난 지원금 신청가능')
# elif str[3] == '5' or str[3] == '0':
#     print('금요일 재난 지원금 신청가능')


# str = input("출생연도입력.:")
# print(str[0])
# if int(str) > 1970 :
#     print('성인')


str = input('문자열 입력')
len1 = len(str)%2
len2 = len(str)/2

if len1 :
    print(str[round(len2)])
else:
    print(str[int(len2-1)], str[int(len2)])