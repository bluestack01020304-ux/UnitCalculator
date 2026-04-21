import random

def getScores(number: int):
    """number: int
    int만큼에 국수영사과에 점수가 랜덤으로 뽑힘"""
    scores = []
    for i in range(number):
        scores.append([
            random.randint(40,100), # 국어
            random.randint(40,100), # 수학
            random.randint(40,100), # 영어
            random.randint(40,100), # 사회
            random.randint(40,100), # 과학
            ])

    return scores

def readScores(data: list):
    for v in data:
        for i in v:
            print(i, end=" ")