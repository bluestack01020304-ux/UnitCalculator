import sys
import random
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

class ExamScoreUI(QWidget):
    def __init__(self):
        super().__init__()
        # 테스트용 100명 데이터 생성 (평균 점수 비교용)
        self.other_students = [random.randint(40, 100) for _ in range(100)]
        self.initUI()

    def initUI(self):
        self.setWindowTitle('성적 관리 시스템')
        self.resize(1200, 750)

        main_layout = QVBoxLayout()

        # 1. 제목
        title = QLabel("기말고사 성적 결과표")
        title.setStyleSheet("font-size: 25px; font-weight: bold; margin: 15px;")
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)

        # 2. 표 설정 (굵은 줄 제거, 총 12열)
        self.table = QTableWidget()
        self.table.setColumnCount(12)
        headers = [
            '국어', '등급', '수학', '등급', '영어', '등급', 
            '사회', '등급', '과학', '등급', '평균', '석차'
        ]
        self.table.setHorizontalHeaderLabels(headers)
        
        # 모든 칸을 균등하게 배분
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        main_layout.addWidget(self.table)

        # 3. 입력 구역
        input_group = QGroupBox("성적 입력")
        input_layout = QHBoxLayout()

        self.inputs = []
        subjects = ['국어', '수학', '영어', '사회', '과학']
        
        for sub in subjects:
            vbox = QVBoxLayout()
            label = QLabel(sub)
            label.setAlignment(Qt.AlignCenter)
            edit = QLineEdit()
            edit.setPlaceholderText("점수")
            edit.setAlignment(Qt.AlignCenter)
            vbox.addWidget(label)
            vbox.addWidget(edit)
            input_layout.addLayout(vbox)
            self.inputs.append(edit)

        input_group.setLayout(input_layout)
        main_layout.addWidget(input_group)

        # 4. 버튼 구역 (오른쪽 정렬)
        button_layout = QHBoxLayout()
        self.confirm_btn = QPushButton("평균/등급/석차 확인 및 표 추가")
        self.confirm_btn.setFixedSize(300, 50)
        self.confirm_btn.setStyleSheet("""
            QPushButton {
                background-color: #2E7D32; 
                color: white; 
                font-weight: bold; 
                font-size: 14px; 
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #388E3C;
            }
        """)
        self.confirm_btn.clicked.connect(self.process_scores)

        button_layout.addStretch(1)
        button_layout.addWidget(self.confirm_btn)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def get_grade(self, score):
        if score >= 90: return 'A'
        elif score >= 80: return 'B'
        elif score >= 70: return 'C'
        else: return 'D'

    def calculate_rank(self, my_avg):
        rank = 1
        for other_avg in self.other_students:
            if other_avg > my_avg:
                rank += 1
        return rank

    def process_scores(self):
        try:
            scores = []
            for edit in self.inputs:
                val = edit.text()
                scores.append(int(val if val else 0))

            avg = sum(scores) / len(scores)
            rank = self.calculate_rank(avg)
            
            # 표에 데이터 추가
            self.update_table(scores, round(avg, 2), f"{rank} / 101")
            
            # 입력창 초기화
            for edit in self.inputs:
                edit.clear()

        except ValueError:
            QMessageBox.warning(self, "입력 오류", "숫자만 입력해주세요.")

    def update_table(self, scores, average, rank):
        row = self.table.rowCount()
        self.table.insertRow(row)

        col_idx = 0
        for i in range(5):
            # 점수 입력
            self.table.setItem(row, col_idx, self.make_item(str(scores[i])))
            
            # 등급 입력 (배경색을 좀 더 진한 회색으로 변경)
            grade_item = self.make_item(self.get_grade(scores[i]))
            grade_item.setBackground(QColor(220, 220, 220)) # 기존 245 -> 220으로 진하게 변경
            self.table.setItem(row, col_idx + 1, grade_item)
            
            col_idx += 2 

        # 평균과 석차
        self.table.setItem(row, 10, self.make_item(str(average)))
        self.table.setItem(row, 11, self.make_item(str(rank)))

    def make_item(self, text):
        item = QTableWidgetItem(text)
        item.setTextAlignment(Qt.AlignCenter)
        return item

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ExamScoreUI()
    window.show()
    sys.exit(app.exec_())