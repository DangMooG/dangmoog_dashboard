import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from sqlalchemy import create_engine

# SQLAlchemy 엔진 생성
# f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
engine = create_engine(os.environ.get("DB_CONNECT"))
#
# Streamlit 앱 타이틀
st.title("도토릿 KPI 대쉬보드")


# 데이터베이스에서 데이터 조회
@st.cache_data
def get_data(query):
    with engine.connect() as conn:
        return pd.read_sql(query, conn)


# 예시 쿼리 (실제 쿼리는 필요에 따라 수정)
data = get_data('SELECT * FROM post')

# Matplotlib 차트
st.subheader('Matplotlib 차트 예시')
fig, ax = plt.subplots()
ax.plot(data['post_id'], data['price'])
st.pyplot(fig)

# Plotly 차트
st.subheader('Plotly 차트 예시')
fig = px.line(data, x='post_id', y='price', title='Plotly 차트')
st.plotly_chart(fig)

# 데이터 테이블 표시
st.subheader('데이터 테이블')
st.write(data)
