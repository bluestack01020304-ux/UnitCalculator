import backend.config as config
import math

def avg(score: list) -> int:
    """유저의 점수 평균을 구하는 함수"""
    #if config.secores == {}: raise ValueError
    if score == []: raise ValueError

    return sum(score)//len(score)

def grade(score: list) -> list:
    """유저의 각 점수 별 등급을 구하는 함수"""
    for i in range(len(score)):
        if score[i]>90: score[i] = "A"
        elif score[i]>80: score[i] = "B"
        elif score[i]>70: score[i] = "C"
        elif score[i]>60: score[i] = "D"
        else: score[i] = "F"

    return score

def ranking(score: list):
    """유저의 각 석차를 구하는 함수"""

    noTost = {"국어": 0, "수학": 1, "영어": 2, "사회": 3, "과학": 4}
    all = []
    for i in config.scores:
        for j, k in i.items():
            all[j] += k