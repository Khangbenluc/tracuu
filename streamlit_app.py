import streamlit as st

# Thiết lập tiêu đề trang
st.set_page_config(page_title="Tra cứu hóa đơn thanh toán", page_icon="🧾", layout="centered")

# Tiêu đề
st.title("🧾 Tra cứu hoá đơn thanh toán")

# Ô nhập mã hóa đơn
ma_hd = st.text_input("Nhập mã tra cứu được in ở cuối hoá đơn:", placeholder="Cú pháp: EPHDxxxxxxxx")

# Dữ liệu hóa đơn mẫu
hoa_don_data = {
    "EPHD3124324N": {
        "Mã hoá đơn": "2C45EA",
        "Loại hoá đơn": "Hoá đơn thanh toán",
        "Ngày xuất": "12/10/2025",
        "Người lập": "VĨNH KHANG",
        "Khách hàng": "CLB SÁNG TÁC EPW",
        "Tên dịch vụ": "Đánh máy",
        "Đơn giá": "5% Giá Bìa",
        "Tổng": "5% Giá Bìa",
        "Hình thức thanh toán": "Thanh toán 5% giá bìa sau khi xuất bản",
        "Cam kết": "Sản phẩm đạt yêu cầu của khách hàng. Không đạt chất lượng, hoàn tiền toàn bộ hoá đơn."
    },
    "EPHD7691543W": { 
        "Mã hoá đơn": "34L5HR", 
        "Loại hoá đơn": "Hoá đơn điều chỉnh",
        "Ngày xuất": "27/10/2025", 
        "Người lập": "VĨNH KHANG", 
        "Khách hàng": "CLB SÁNG TÁC EPW", 
        "Tên dịch vụ": "Đánh máy", 
        "Đơn giá": "0% Giá Bìa", 
        "Tổng": "0% Giá Bìa", 
        "Hình thức thanh toán": "Thanh toán 0% giá bìa sau khi xuất bản", 
        "Cam kết": "Sản phẩm đạt yêu cầu của khách hàng. Không đạt chất lượng, hoàn tiền toàn bộ hoá đơn."
    }
}

# Kiểm tra mã hóa đơn
if ma_hd:
    if ma_hd in hoa_don_data:
        st.balloons()
        st.success("✅ Tìm thấy thông tin hoá đơn!")
        data = hoa_don_data[ma_hd]
        st.write(f"**Mã hoá đơn:** {data['Mã hoá đơn']}")
        st.write(f"**Loại hoá đơn:** {data['Loại hoá đơn']}")
        st.write(f"**Ngày xuất:** {data['Ngày xuất']}")
        st.write(f"**Người lập:** {data['Người lập']}")
        st.write(f"**Khách hàng:** {data['Khách hàng']}")
        st.write(f"**Tên dịch vụ:** {data['Tên dịch vụ']}")
        st.write(f"**Đơn giá:** {data['Đơn giá']}")
        st.write(f"**Tổng:** {data['Tổng']}")
        st.write(f"**Hình thức thanh toán:** {data['Hình thức thanh toán']}")
        st.markdown(f"**Cam kết:** {data['Cam kết']}")
        st.success("✅ Đây là hoá đơn thật, được chúng tôi xác nhận!")
    else:
        st.error("❌ Không có thông tin cho mã hoá đơn này. Có thể đây là hoá đơn giả hoặc thông tin chưa được cập nhật. Hãy thử lại sau!")
        st.snow()

# Footer
st.markdown(
    """
    <hr style="border: 1px solid #ccc;">
    <div style="text-align:center; color:gray; font-size:14px;">
        © CLB Sáng Tác EPW | Liên hệ khi có sự cố: 
        <a href="mailto:khangnv33@emasiplus.edu.vn">khangnv33@emasiplus.edu.vn</a>
    </div>
    """,
    unsafe_allow_html=True
)
