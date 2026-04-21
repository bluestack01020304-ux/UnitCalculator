import backend.config as config
import math

def avg(score: list) -> int:
    """유저의 점수 평균을 구하는 함수"""
    #if config.secores == {}: raise ValueError
    if score == []: raise ValueError

    return sum(score)//len(score)

def grade(score: list[int]) -> list[str]:

    result = []

    for s in score:
        if s > 90: result.append("A")
        elif s > 80: result.append("B")
        elif s > 70: result.append("C")
        elif s > 60: result.append("D")
        elif s > 50: result.append("E")
        else: result.append("F")

    return result

def ranking(score: list[int]):

    subjects = list(zip(*config.scores))
    ranks = []

    for i, subject in enumerate(subjects):

        rank = 1
        for s in subject:
            if s > score[i]:
                rank += 1

        ranks.append(rank)

    return ranks
        