import streamlit as st

st.title('Streamlit 요소 데모')

st.header('텍스트 요소')
st.write('이것은 일반 텍스트입니다.')
st.markdown('**마크다운** _스타일_')
st.code('print("Hello, Streamlit!")', language='python')

st.header('입력 요소')
name = st.text_input('이름을 입력하세요')
age = st.number_input('나이', min_value=0, max_value=120, value=25)
option = st.selectbox('좋아하는 색상', ['빨강', '파랑', '초록'])
agree = st.checkbox('동의합니다')

st.header('버튼')
if st.button('클릭!'):
    st.success('버튼이 눌렸습니다!')

st.header('슬라이더')
value = st.slider('값을 선택하세요', 0, 100, 50)
st.write(f'선택한 값: {value}')

st.header('이미지')
from PIL import Image
import numpy as np
img = Image.fromarray(np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8))
st.image(img, caption='랜덤 이미지', use_column_width=True)

st.header('그래프')
import matplotlib.pyplot as plt
import numpy as np
x = np.array([1, 2, 3])
y = np.array([10, 20, 5])
fig, ax = plt.subplots()
ax.plot(x, y, marker='o')
ax.set_xlabel('X축')
ax.set_ylabel('Y축')
ax.set_title('예시 그래프')
st.pyplot(fig)

st.header('데이터프레임')
import pandas as pd
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})
st.dataframe(df)
