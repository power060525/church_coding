from faker import Faker
import pandas as pd
import random 

# kr_KR말고도 원하는 언어 설정가능
fake = Faker("ko_KR")


data =[]
for _ in range(2):
    # 가짜 이름 생성
    fake_name = fake.name()
    # 가짜 성별 생성
    fake_Nationality = fake.random_element(elements=('Israel', 'Korea','중국','미국'))
    # 국적
    
    # 가짜 주소 생성
    # fake_address = fake.address()
    # 가짜 나이 생성
    random.randrange(10,30)
    fake_Age = random.randrange(10,30)
    # 종교 생성
    fake.random_element(elements=('Christianity','Buddhism','Catholic'))
    fake_Religion = fake.random_element(elements=('Christianity','Buddhism','Catholic'))
    
    data.append([fake_name,fake_Age,fake_Religion,fake_Nationality,])


df = pd.DataFrame(data, columns=["이름","나이", "종교", "국적"])

# 데이터프레임을 엑셀 파일로 저장
excel_filename = "fake_user.xlsx"
df.to_excel(excel_filename, index=False)

