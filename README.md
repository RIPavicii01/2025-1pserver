# 2025-1pserver: 붓꽃 분류기 프로젝트

<img src = "front/irisimage.png">

# 2025-1pserver: 붓꽃 분류기 프로젝트

## 프로젝트 개요

이 프로젝트는 2025년 1학기 프로젝트2 과목의 일환으로 개발된 붓꽃 분류기입니다. 서버와 클라이언트를 모두 포함하고 있으며, 머신러닝 모델을 사용하여 붓꽃의 종류를 예측합니다.

## 주요 기능

- 붓꽃의 특성(꽃받침 길이, 꽃받침 너비, 꽃잎 길이, 꽃잎 너비)을 입력받아 종류 예측
- FastAPI를 이용한 백엔드 서버
- HTML/JavaScript를 이용한 프론트엔드 클라이언트
- RandomForest 분류기를 사용한 머신러닝 모델

## 기술 스택

- Backend: Python, FastAPI
- Frontend: HTML, JavaScript, jQuery
- Machine Learning: scikit-learn, pandas, numpy
- 기타: joblib (모델 저장 및 로드)

## 파일 구조

- `main.py`: FastAPI 서버 메인 파일
- `irisModel.py`: 붓꽃 분류 모델 클래스 정의
- `irisModelBase.py`: 모델 학습 및 저장 스크립트
- `iris.html`: 프론트엔드 HTML 파일
- `iris.js`: 프론트엔드 JavaScript 파일
- `iris_front.py`: 프론트엔드 테스트용 Python 스크립트

## 설치 및 실행 방법

1. 필요한 Python 패키지 설치:
   ```
   pip install fastapi uvicorn scikit-learn pandas numpy joblib
   ```

2. 서버 실행:
   ```
   python main.py
   ```

3. 브라우저에서 `iris.html` 파일을 열어 클라이언트 접속

## 사용 방법

1. 웹 인터페이스에서 붓꽃의 특성 값을 입력합니다.
2. 'Submit' 버튼을 클릭하여 예측 결과를 확인합니다.

## 개발자

- 장형준

## 동작 화면 예시 ##
<img src = "front/irisresult.png">

