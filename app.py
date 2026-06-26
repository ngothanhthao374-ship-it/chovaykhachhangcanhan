import streamlit as st

st.set_page_config(page_title="Thẩm định vay vốn cá nhân", page_icon="💰")

st.title("💰 Ứng dụng thẩm định vay vốn cá nhân")

# Nhập dữ liệu
STV = st.number_input("Nhập số tiền vay (triệu đồng)", min_value=0.0, step=1.0)
TGV = st.number_input("Nhập thời gian vay (năm)", min_value=1.0, step=1.0)
LSV = st.number_input("Nhập lãi suất vay (dạng số thập phân, ví dụ: 0.12)", min_value=0.0, step=0.01)
TN = st.number_input("Nhập thu nhập (triệu đồng/tháng)", min_value=0.0, step=1.0)
SNTGD = st.number_input("Nhập số người trong gia đình", min_value=1, step=1)
PHAITRAMONCU = st.number_input("Nhập số tiền phải trả cho khoản vay cũ (triệu đồng/tháng)", min_value=0.0, step=0.1)
GTTSDB = st.number_input("Nhập giá trị tài sản đảm bảo (triệu đồng)", min_value=0.0, step=1.0)

CPSH = 5  # Chi phí sinh hoạt cố định

if st.button("Thẩm định khoản vay"):
    if GTTSDB == 0:
        st.error("Giá trị tài sản đảm bảo phải lớn hơn 0.")
    else:
        # Tính toán
        LTV = STV / GTTSDB
        PHAITRAMONMOI = (STV / (TGV * 12)) + (STV * (LSV / 12))
        DTI = (PHAITRAMONCU + PHAITRAMONMOI) / (TN - CPSH * SNTGD)

        # Hiển thị kết quả
        st.subheader("Kết quả tính toán")
        st.write(f"**LTV:** {LTV:.2%}")
        st.write(f"**DTI:** {DTI:.2%}")

        # Đưa ra quyết định
        if DTI <= 0.7 and LTV < 0.7:
            st.success("✅ Khách hàng được vay")
        else:
            st.error("❌ Khách hàng không được vay")
