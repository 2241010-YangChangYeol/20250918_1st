import streamlit as st
import pandas as pd
import numpy as np

st.title('Streamlit 그래프 데모')

st.header('Line Chart')
data = np.random.randn(20, 3)
st.line_chart(data)

st.header('Bar Chart')
df = pd.DataFrame(
	np.random.randint(1, 100, size=(10, 3)),
	columns=['A', 'B', 'C']
)
st.bar_chart(df)

st.header('사용자 입력 기반 그래프')
num_points = st.slider('데이터 포인트 수', 5, 50, 20)
user_data = np.cumsum(np.random.randn(num_points))
st.line_chart(user_data)

