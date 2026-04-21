import random

def getScores(number: int):
    """number: int
    int만큼에 국수영사과에 점수가 랜덤으로 뽑힘"""
    scores = {}
    for i in range(number):
        scores[i] = [
            random.randint(0,100), # 국어
            random.randint(0,100), # 수학
            random.randint(0,100), # 영어
            random.randint(0,100), # 사회
            random.randint(0,100), # 과학
        ]

    return scores

def readScores(data: dict):
    for k, v in data.items():
        print(k, v)