"""
2007년
문제집
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
2 초	128 MB	3434	1627	1441	49.214%
문제
오늘은 2007년 1월 1일 월요일이다. 그렇다면 2007년 x월 y일은 무슨 요일일까? 이를 알아내는 프로그램을 작성하시오.

입력
첫째 줄에 빈 칸을 사이에 두고 x(1≤x≤12)와 y(1≤y≤31)이 주어진다. 참고로 2007년에는 1, 3, 5, 7, 8, 10, 12월은 31일까지, 4, 6, 9, 11월은 30일까지, 2월은 28일까지 있다.

출력
첫째 줄에 x월 y일이 무슨 요일인지에 따라 SUN, MON, TUE, WED, THU, FRI, SAT중 하나를 출력한다.

예제 입력  복사
1 1
예제 출력  복사
MON
"""

month,day = map(int,input().split(" "))
days = 0
day_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_list = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

days = sum(day_of_month[:month-1]) + day
print(day_list[int(days%7)])
