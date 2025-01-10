from fastapi import FastAPI, HTTPException
from datetime import datetime, date
from typing import Dict
import random

### Create FastAPI instance with custom docs and openapi url
app = FastAPI(docs_url="/api/py/docs", openapi_url="/api/py/openapi.json")

@app.get("/api/py/helloFastApi")
def hello_fast_api():
    return {"message": "Hello from FastAPI"}

@app.get("/api/py/ageCalculator/{birthday}")
def age_calculator(birthday: str) -> Dict[str, str]:
    """
    생년월일을 입력받아 만나이를 계산하는 API

    :param birthday: 생년월일 (형식: YYYY-MM-DD)
    :return: 생년월일 및 만나이를 포함한 JSON 응답
    """
    today = date.today()
    birth_date = datetime.strptime(birthday, "%Y-%m-%d").date()
    if birth_date > today:
        raise HTTPException(
            status_code=400,
            detail="The birth date cannot be in the future."
        )

    # 계산
    age = today.year - birth_date.year
    if (today.month,today.day) < (birth_date.month,birth_date.day):
        age -= 1
    
    def get_zodiac(year):
        zodiac_animals = [
                 "(🐀 쥐)","(🐂 소)","(🐅 호랑이)","(🐇 토끼)","(🐉 용)","(🐍 뱀)","(🐎 말)","(🐐 양)","(🐒 원숭이)","(🐓 닭)","(🐕 개)","(🐖 돼지)"
        ]
        base_year = 2020 # 기준 점 : 쥐띠의 헤
        index = (year - base_year)%12
        return zodiac_animals[index]

    zodiac = get_zodiac(birth_date.year)
    return {
            "birthday": birthday,
            "age": str(age),
            "basedate": str(today),
            "message": "Age calculated successfully!",
            "zodiac" : zodiac
            }
