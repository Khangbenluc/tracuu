import streamlit as st

# Thiết lập tiêu đề trang
st.set_page_config(page_title="Tra cứu hóa đơn thanh toán", page_icon="🧾", layout="centered")

# Tiêu đề
st.title("🧾 Tra cứu hoá đơn thanh toán")

# Ô nhập mã hóa đơn
ma_hd = st.text_input("Nhập mã hoá đơn:")

# Dữ liệu hóa đơn mẫu
hoa_don_data = {
    "EPHD3124324N": {
        "Mã hoá đơn": "2C45EA",
        "Ngày xuất": "12/10/2025",
        "Người lập": "VĨNH KHANG",
        "Khách hàng": "CLB SÁNG TÁC EPW",
        "Tên dịch vụ": "Đánh máy",
        "Đơn giá": "5% G.B",
        "Tổng": "5% G.B",
        "Hình thức thanh toán": "Thanh toán 5% giá bìa sau khi xuất bản",
        "Cam kết": "Sản phẩm đạt yêu cầu của khách hàng. Không đạt chất lượng, hoàn tiền toàn bộ hoá đơn."
    }
}

# Kiểm tra mã hóa đơn
if ma_hd:
    if ma_hd in hoa_don_data:
        st.success("✅ Tìm thấy thông tin hoá đơn!")
        data = hoa_don_data[ma_hd]
        st.write(f"**Mã hoá đơn:** {data['Mã hoá đơn']}")
        st.write(f"**Ngày xuất:** {data['Ngày xuất']}")
        st.write(f"**Người lập:** {data['Người lập']}")
        st.write(f"**Khách hàng:** {data['Khách hàng']}")
        st.write(f"**Tên dịch vụ:** {data['Tên dịch vụ']}")
        st.write(f"**Đơn giá:** {data['Đơn giá']}")
        st.write(f"**Tổng:** {data['Tổng']}")
        st.write(f"**Hình thức thanh toán:** {data['Hình thức thanh toán']}")
        st.markdown(f"**Cam kết:** {data['Cam kết']}")
    else:
        st.error("❌ Không có thông tin cho mã hoá đơn này.")
