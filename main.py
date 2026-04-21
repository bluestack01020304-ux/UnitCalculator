import Utillity.Scroes as Scores
import Utillity.Math as Math
import backend.config as config

def start():
    config.scores = Scores.getScores(100)

    userScore = list(map(int, input().split()))
    Scores.readScores(config.scores)

    print(config.scores[0]["국어"])

if __name__ == "__main__":
    start()