
from PySide6.QtWidgets import (
    QMainWindow,QWidget,QVBoxLayout,QHBoxLayout,
    QPushButton,QCheckBox,QProgressBar,QPlainTextEdit,QLabel
)
from core.collector import Collector

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ALEX Garage Collector Pro v0.1")
        self.resize(900,600)

        c=QWidget()
        self.setCentralWidget(c)
        v=QVBoxLayout(c)

        h=QHBoxLayout()
        self.chk_seoul=QCheckBox("서울")
        self.chk_incheon=QCheckBox("인천")
        self.chk_seoul.setChecked(True)
        self.chk_incheon.setChecked(True)
        h.addWidget(self.chk_seoul)
        h.addWidget(self.chk_incheon)
        v.addLayout(h)

        self.btn=QPushButton("엑셀 생성")
        self.btn.clicked.connect(self.run)
        v.addWidget(self.btn)

        self.progress=QProgressBar()
        v.addWidget(self.progress)

        self.log=QPlainTextEdit()
        self.log.setReadOnly(True)
        v.addWidget(QLabel("로그"))
        v.addWidget(self.log)

    def run(self):
        self.log.appendPlainText("수집 시작...")
        c=Collector()
        count=c.collect(
            include_seoul=self.chk_seoul.isChecked(),
            include_incheon=self.chk_incheon.isChecked()
        )
        self.progress.setValue(100)
        self.log.appendPlainText(f"완료 : {count}건 저장")
