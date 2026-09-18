# Stock Company Analyzer

Finnhub API를 이용하여 미국 상장 기업의 정보를 조회하고
SQLite에 저장하는 Python 프로젝트입니다.

## Features

- 기업 기본 정보 조회
- 현재 주가 조회
- 과거 주가 조회
- 재무 정보 조회
- 기업 뉴스 조회
- SQLite 저장
- Python 객체를 이용한 데이터 관리
- API / Service / Model / Database 분리
- pytest를 이용한 테스트

## Project Structure

```text
stock_company_analyzer/
├── main.py
├── config/
├── api/
├── models/
├── services/
├── database/
├── utils/
└── test/
