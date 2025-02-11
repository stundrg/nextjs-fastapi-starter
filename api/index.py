from fastapi import FastAPI, HTTPException
from datetime import datetime, date
from typing import Dict
import random
import korean_age_calculator as kac
import sys
import platform

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
        return {"age": "넌 미래에서 왔니?"}
        

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
    def getStudent():
        studentlist = [
            "안재영", "조민규", "강현룡", "백지원", "서민혁",
            "권오준", "조성근", "전희진", "배형균", "민경국"
        ]
        return random.choice(studentlist)
    
    student = getStudent()
    zodiac = get_zodiac(birth_date.year)
    kage = kac.how_korean_age(year_of_birth=birth_date.year)
    os_info = {
        "system": platform.system(),
        "release": platform.release(),
        "version": platform.version(),
        "processor": platform.processor()
    }


    # python 버전 추가
    version = sys.version
    return {
            "birthday": birthday,
            "age": str(age) ,
            "kage" : str(kage),
            "speaker": "홍길동",
            "basedate": str(today),
            "message": "Age calculated successfully!",
            "os_info": str(os_info),
            "version": version,
            "student": student,
            "zodiac" : zodiac
            }

'''
    return
    {
    "os-name": get_os_pretty_name()
            }
def get_os_pretty_name() -> str: 
    with open('/etc/os-release', 'r') as f:
        for line in f:
            if line.startswith('PRETTY_NAME='):
                return line.split('=')[1].replace('\n', '').strip('"')
    return None
    '''
