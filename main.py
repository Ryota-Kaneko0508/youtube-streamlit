import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  latest_iteration.text(f'Iteration {i + 1}')
  bar.progress(i + 1)
  time.sleep(0.1)
  
left_column, rignt_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
  rignt_column.write('右')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く') 
# text = st.text_input('あなたの趣味は？')


# condition = st.slider('あなたの今の調子は？', 0, 100, 50)


# 'あなたの趣味:', text
# 'コンディション', condition
# if st.checkbox('Show Image'):
#   img = Image.open('顔写真.jpg')
#   st.image(img, caption='Ryota', use_column_width=True)




