import streamlit as st

# --- Cấu hình trang ---
st.set_page_config(page_title="Tra cứu hóa đơn thanh toán", page_icon="🧾", layout="centered")

# --- CSS cho giao diện đẹp hơn ---
st.markdown("""
    <style>
    .invoice-card {
        background-color: #f9f9f9;
        border-radius: 15px;
        padding: 25px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        margin-top: 20px;
        font-family: 'Segoe UI', sans-serif;
    }
    .invoice-title {
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        color: #333333;
        margin-bottom: 15px;
    }
    .invoice-field {
        font-size: 16px;
        margin: 6px 0;
        color: #222222;
    }
    .invoice-highlight {
        color: #007BFF;
        font-weight: 600;
    }
    .footer {
        text-align: center;
        color: gray;
        font-size: 14px;
        margin-top: 40px;
        padding-top: 10px;
        border-top: 1px solid #ccc;
    }
    </style>
""", unsafe_allow_html=True)

# --- Tiêu đề chính ---
st.title("🧾 Tra cứu hoá đơn thanh toán")

# --- Ô nhập mã hoá đơn ---
ma_hd = st.text_input("Nhập mã tra cứu được in ở cuối hoá đơn:", placeholder="Cú pháp: EPHDxxxxxxxx")

# --- Dữ liệu hoá đơn ---
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

# --- Xử lý tra cứu ---
if ma_hd:
    if ma_hd in hoa_don_data:
        st.balloons()
        st.success("✅ Tìm thấy thông tin hoá đơn hợp lệ!")

        data = hoa_don_data[ma_hd]

        # --- Hiển thị trong thẻ đẹp ---
        st.markdown("<div class='invoice-card'>", unsafe_allow_html=True)
        st.markdown("<div class='invoice-title'>THÔNG TIN HOÁ ĐƠN</div>", unsafe_allow_html=True)

        for key, value in data.items():
            st.markdown(f"<div class='invoice-field'><b>{key}:</b> <span class='invoice-highlight'>{value}</span></div>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)
        st.success("✅ Đây là hoá đơn thật, được chúng tôi xác nhận!")
    else:
        st.error("❌ Không có thông tin cho mã hoá đơn này. Có thể đây là hoá đơn giả!")
        st.snow()

# --- Footer ---
st.markdown("""
<div class="footer">
© 2025 CLB Sáng Tác EPW | Liên hệ khi có sự cố: 
<a href="mailto:khangnv33@emasiplus.edu.vn">khangnv33@emasiplus.edu.vn</a>
</div>
""", unsafe_allow_html=True)
