import Utillity.Scroes as Scores
import Utillity.Math as Math
import frontend.UI as UI
import backend.config as config

def start():
    config.scores = Scores.getScores(100)
    UI.run()
    #score = list(map(int, input().split()))
    #print("당신의 평균: ", Math.avg(score))
    #print("당신의 등급: ", Math.grade(score))
    #print("당신의 석차: ", Math.ranking(score))

if __name__ == "__main__":
    start()