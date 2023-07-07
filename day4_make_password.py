# 실습 문제

naver = "http://naver.com"
daum = "http://daum.net"
google = "http://google.com"
youtube = "http://youtube.com"

# 1~2번 사이트 이름만 남기고 제거
naver_s = naver[7:-4]
daum_s = daum[7:-4]
google_s = google[7:-4]
youtube_s = youtube[7:-4]

# 3번 처음 세 자리 + 글자 개수 + 글자 내 'e' 개수 + "!"
print( naver + "의 비밀번호는 " + naver_s[:3] + str(len(naver_s)) + str(naver_s.count("e")) + "!입니다." )
print( daum + "의 비밀번호는 " + daum_s[:3] + str(len(daum_s)) + str(daum_s.count("e")) + "!입니다." )
print( google + "의 비밀번호는 " +google_s[:3] + str(len(google_s)) + str(google_s.count("e")) + "!입니다." )
print( youtube + "의 비밀번호는 " + youtube_s[:3] + str(len(youtube_s)) + str(youtube_s.count("e")) + "!입니다." )
