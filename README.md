# 🚗 ALEX Garage Collector Pro

전국 자동차정비업체 공공데이터(OpenAPI)를 이용하여

- 서울
- 인천

자동차 정비업체를 수집하고 Excel로 저장하는 프로그램입니다.

---

# 개발 환경

|항목|버전|
|----|----|
|Python|3.12 이상|
|Visual Studio Code|최신버전|
|Windows|10 / 11|

---

# 사용 라이브러리

- PySide6
- httpx
- pandas
- openpyxl
- python-dotenv

설치

```bash
pip install -r requirements.txt
```

---

# 프로젝트 구조

```
ALEX-GarageCollector
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── config
│     config.py
│
├── core
│     api_client.py
│     collector.py
│
├── exporter
│     excel_exporter.py
│
├── gui
│     main_window.py
│
├── utils
│     phone.py
│     address.py
│
├── input
│
├── output
│
└── logs
```

---

# Visual Studio Code 설정

## 1. 저장소 Clone

```bash
git clone https://github.com/hibiznet/ALEX-GarageCollector.git
```

또는

GitHub Desktop에서 Clone 합니다.

---

## 2. VS Code 열기

```
File
    Open Folder
```

프로젝트 폴더 선택

또는

```bash
code .
```

---

## 3. Python 가상환경 생성

Windows

```bash
python -m venv .venv
```

---

## 4. 가상환경 활성화

PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

CMD

```cmd
.venv\Scripts\activate.bat
```

---

## 5. 패키지 설치

```bash
pip install -r requirements.txt
```

---

# API Key 설정

공공데이터포털에서 발급받은 서비스키를

```
config/config.py
```

에 입력합니다.

예시

```python
SERVICE_KEY="여기에_서비스키"
```

---

# 프로그램 실행

Visual Studio Code Terminal

```bash
python app.py
```

또는

VS Code

```
Run
    Run Without Debugging
```

또는

```
Ctrl + F5
```

---

# 실행 결과

프로그램이 실행되면

```
ALEX Garage Collector Pro
```

창이 나타납니다.

버튼

```
다운로드
```

클릭

↓

전국 자동차정비업체 다운로드

↓

서울/인천 필터

↓

Excel 생성

↓

```
output/
```

폴더에

```
서울_인천_자동차정비업체.xlsx
```

파일이 생성됩니다.

---

# API

OpenAPI

```
https://api.data.go.kr/openapi/tn_pubr_public_auto_maintenance_company_api
```

응답 형식

```
JSON
```

---

# 현재 개발 진행상황

## v0.1

- 프로젝트 생성
- GUI
- API 연결
- Excel 저장

---

## v0.2

- 전체 페이지 자동 다운로드
- 진행률 표시
- 로그 저장

---

## v0.3

- 전화번호 정규화
- 주소 정규화
- 중복 제거

---

## v0.4

- Excel 서식 자동 적용
- 필터
- 열너비 자동조정

---

## v1.0

- EXE 배포
- 설정 저장
- 자동 업데이트

---

# Git 명령어

상태 확인

```bash
git status
```

추가

```bash
git add .
```

커밋

```bash
git commit -m "Commit #1"
```

업로드

```bash
git push origin main
```

---

# TODO

- [ ] OpenAPI 연결
- [ ] JSON 다운로드
- [ ] Excel 생성
- [ ] GUI 연결
- [ ] 진행률 표시
- [ ] 로그 저장
- [ ] 설정 저장
- [ ] EXE 빌드

---

# License

Private Project

Copyright © 2026 JTMOTIONLAB

All Rights Reserved.
