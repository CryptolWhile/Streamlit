import streamlit as st
#Thêm tiêu đề cho ứng dụng
st.title("Website Tính toán cơ bản")

#Thêm mô tả
st.write("Đây là một ứng dụng đơn giản để tính tổng và tích hai số")

#Nhập dữ liệu từ người dùng
a = st.text_input("Nhập số thứ nhất:", "0")
b = st.text_input("Nhập số thứ hai:", "0")

#Chuyển đổi dữ liệu thành số nguyên
a = int(a) if a.isdigit() else 0
b = int(b) if b.isdigit() else 0

#Nút tính toán
if st.button("Tính tổng và tích"):
    tong = a + b
    tich = a * b
    st.write(f"Tổng của hai số là: {tong}")
    st.write(f"Tích của hai số là: {tich}")