import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

class ExamScoreUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 화면 크기 설정 (과목별 등급 칸 때문에 가로를 넓게 설정)
        self.setWindowTitle('성적 관리 시스템 UI')
        self.resize(1200, 600)

        layout = QVBoxLayout()

        # 제목
        title = QLabel("기말고사 성적 결과표")
        title.setStyleSheet("font-size: 25px; font-weight: bold; margin: 10px;")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # 표 설정: 과목(5) + 각 등급(5) + 평균(1) + 석차(1) = 총 12열
        self.table = QTableWidget()
        self.table.setColumnCount(12)
        headers = [
            '국어', '등급', '수학', '등급', '영어', '등급', 
            '사회', '등급', '과학', '등급', '평균', '석차'
        ]
        self.table.setHorizontalHeaderLabels(headers)
        
        # 엑셀처럼 칸을 꽉 채우기
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.table)

        self.setLayout(layout)

    def get_grade(self, score):
        """과목별 점수에 따른 등급 판정"""
        if score >= 90: return 'A'
        elif score >= 80: return 'B'
        elif score >= 70: return 'C'
        else: return 'D'

    def update_table(self, scores, average, rank):
        """
        외부에서 계산된 값을 받아 표에 추가하는 함수
        scores: [국어, 수학, 영어, 사회, 과학] 리스트
        average: 계산된 평균값
        rank: 계산된 석차
        """
        row = self.table.rowCount()
        self.table.insertRow(row)

        col_idx = 0
        # 0번부터 4번까지 과목 점수와 등급을 세트로 입력
        for i in range(5):
            # 점수 칸
            score_item = QTableWidgetItem(str(scores[i]))
            score_item.setTextAlignment(Qt.AlignCenter)
            self.table.setItem(row, col_idx, score_item)
            
            # 등급 칸 (배경색을 넣어 구분)
            grade_val = self.get_grade(scores[i])
            grade_item = QTableWidgetItem(grade_val)
            grade_item.setTextAlignment(Qt.AlignCenter)
            grade_item.setBackground(QColor(245, 245, 245)) 
            self.table.setItem(row, col_idx + 1, grade_item)
            
            col_idx += 2 # 점수+등급 다음 칸으로 이동

        # 평균과 석차 입력
        avg_item = QTableWidgetItem(str(average))
        avg_item.setTextAlignment(Qt.AlignCenter)
        self.table.setItem(row, 10, avg_item)

        rank_item = QTableWidgetItem(str(rank))
        rank_item.setTextAlignment(Qt.AlignCenter)
        self.table.setItem(row, 11, rank_item)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ExamScoreUI()
    window.show()
    
    
   


    sys.exit(app.exec_())

    