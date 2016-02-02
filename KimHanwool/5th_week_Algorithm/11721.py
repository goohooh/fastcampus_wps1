#-*- coding: utf-8 -*-
"""
열 개씩 끊어 출력하기
문제집
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	761	440	387	58.371%
문제
알파벳 소문자와 대문자로만 이루어진 길이가 N인 단어가 주어진다.

한 줄에 10글자씩 끊어서 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 단어가 주어진다. 단어는 알파벳 소문자와 대문자로만 이루어져 있으며, 길이는 100을 넘지 않는다. 길이가 0인 단어는 주어지지 않는다.

출력
입력으로 주어진 단어를 열 개씩 끊어서 한 줄에 하나씩 출력한다. 단어의 길이가 10의 배수가 아닌 경우에는 마지막 줄에는 10개 이하의 글자만 출력할 수도 있다.

예제 입력  복사
BaekjoonOnlineJudge
예제 출력  복사
BaekjoonOn
lineJudge
예제 입력 2  복사
OneTwoThreeFourFiveSixSevenEightNineTen
예제 출력 2  복사
OneTwoThre
eFourFiveS
ixSevenEig
htNineTen
"""

str = list(input())
length = len(str)
for i in range(0,length,10):
    print(''.join(str[i:i+10]))




