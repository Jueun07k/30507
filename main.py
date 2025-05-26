import streamlit as st
import pandas as pd
import plotly.express as px

# Google Drive에서 직접 불러오기
file_url = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"

@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    return df

# 데이터 로드
df = load_data(file_url)

# 데이터 확인
st.title("Plotly 시각화 웹앱")
st.write("업로드된 데이터 미리보기:")
st.dataframe(df)

# 사용자 선택을 통해 컬럼 지정
x_column = st.selectbox("X축에 사용할 열 선택", df.columns)
y_column = st.selectbox("Y축에 사용할 열 선택", df.columns)

# 그래프 그리기
fig = px.line(df, x=x_column, y=y_column, title=f"{y_column} vs {x_column}")
st.plotly_chart(fig)
