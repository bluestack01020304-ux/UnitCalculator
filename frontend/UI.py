import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

import backend.config as config
import Utillity.Math as Math


class ExamScoreUI(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setWindowTitle('성적 관리 시스템')
        self.resize(1200, 750)

        main_layout = QVBoxLayout()

        title = QLabel("기말고사 성적 결과표")
        title.setStyleSheet("font-size: 25px; font-weight: bold; margin: 15px;")
        title.setAlignment(Qt.AlignCenter)

        main_layout.addWidget(title)

        self.table = QTableWidget()
        self.table.setColumnCount(12)

        headers = [
            '국어', '등급',
            '수학', '등급',
            '영어', '등급',
            '사회', '등급',
            '과학', '등급',
            '평균', '석차'
        ]

        self.table.setHorizontalHeaderLabels(headers)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        main_layout.addWidget(self.table)

        # 입력 구역
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

        # 버튼
        button_layout = QHBoxLayout()

        self.confirm_btn = QPushButton("확인")
        self.confirm_btn.setFixedSize(300, 50)

        self.confirm_btn.clicked.connect(self.process_scores)

        button_layout.addStretch(1)
        button_layout.addWidget(self.confirm_btn)

        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def process_scores(self):

        try:

            scores = []

            for edit in self.inputs:

                val = edit.text()

                if val == "":
                    scores.append(0)
                else:
                    scores.append(int(val))

            # Math 모듈 사용
            print(scores)
            avg = Math.avg(scores)
            grades = Math.grade(scores)
            ranks = Math.ranking(scores)
            self.update_table(scores, grades, avg, ranks)

            for edit in self.inputs:
                edit.clear()

        except ValueError:
            QMessageBox.warning(self, "입력 오류", "숫자만 입력해주세요.")

    def update_table(self, scores, grades, average, ranks):

        row = self.table.rowCount()

        self.table.insertRow(row)

        col_idx = 0

        for i in range(5):

            self.table.setItem(row, col_idx, self.make_item(str(scores[i])))

            grade_item = self.make_item(grades[i])
            grade_item.setBackground(QColor(220, 220, 220))

            self.table.setItem(row, col_idx + 1, grade_item)

            col_idx += 2

        self.table.setItem(row, 10, self.make_item(str(average)))

        # 석차는 과목별이라 문자열로 합쳐서 표시
        rank_text = ", ".join(map(str, ranks))

        self.table.setItem(row, 11, self.make_item(rank_text))

    def make_item(self, text):

        item = QTableWidgetItem(text)

        item.setTextAlignment(Qt.AlignCenter)

        return item


def run():

    app = QApplication(sys.argv)

    window = ExamScoreUI()

    window.show()

    sys.exit(app.exec_())
    