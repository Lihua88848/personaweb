import streamlit as st
with open("生物质天然气全生命周期分析11.0最终版(4)(1).pdf",'rb')as file1:
    pdf_data1 = file1.read()
    with open('简历-刘辰宇.pdf', 'rb') as file2:
        pdf_data2 = file2.read()
st.title("刘辰宇的简历网站")
st.markdown('''
<style>
 body { background:red} <style>''' , unsafe_allow_html=True)

st.image("1.jpeg",width=800)

st.download_button("点击下载我的简历",data=pdf_data2, file_name="简历_刘辰宇.pdf",mime='application/pdf')
st.download_button("点击下载《生物天然气全生命周期能耗和温室气体排放分析》",data=pdf_data1, file_name="生物质天然气全生命周期分析11.0最终版.pdf",mime='application/pdf')

column1,column2,column3= st.columns([1,1,1])
with column1:
    if st.button("荣誉证书"):
        st.image("4.jpg",width=300)
        st.image("2.png",width=300)
        st.image("3.jpg",width=300)
        st.image("5.png",width=300)
        st.image("6.jpg",width=300)
        st.image("7.jpg",width=300)
with column2:
    if st.button("项目经历"):
        st.image("9.jpg",width=300)
        st.image("10.jpg",width=300)
        st.image("11.jpg",width=300)
        st.image("12.jpg",width=300)
        st.image("13.jpg",width=300)
        st.image("14.jpg",width=300)
        st.image("15.jpg",width=300)

with column3:
    if st.button("学习经历"):
        st.image("16.jpg",width=300)
        st.image("17.jpg",width=300)
        st.image("18.jpg",width=300)
        st.image("19.jpg",width=300)
        st.image("20.jpg",width=300)
        st.image("21.jpg",width=300)
        st.image("22.jpg",width=300)
        st.image("23.jpg",width=300)

