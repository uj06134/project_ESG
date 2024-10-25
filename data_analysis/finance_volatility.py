# 분기별 주가 데이터 변동률 계산

import pandas as pd

# 데이터 불러오기 (분기별 데이터 파일)
df = pd.read_csv("../data_cleaning/cleaned_data/finance_data/finance_year_quarter_filtered_data.csv")

# '연도'를 문자열로 변환
df['연도'] = df['연도'].astype(str)

# '분기'에서 'Q' 뒤의 숫자만 추출 (예: 'Q1' -> '1')
df['분기'] = df['분기'].str[-1]

# 연도와 분기 숫자를 합쳐서 'yyyy-q' 형식으로 생성
df['연도-분기'] = df['연도'] + '-' + df['분기']

# 주가 수익률 계산 (이전 분기 대비 수익률)
df = df.sort_values(by=['종목명', '연도-분기'])
df['수익률'] = df.groupby('종목명')['종가'].pct_change()

# 수익률의 표준편차 계산 (변동성)
volatility = df.groupby('종목명')['수익률'].std()

print("종목별 분기 수익률 변동성:")
print(volatility)

# df와 volatility를 CSV 파일로 저장
df.to_csv("분기별_주가_데이터.csv", index=False)
volatility.to_csv("종목별_변동성.csv", header=['변동성'], index=True)