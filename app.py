import streamlit as st
import cv2
import numpy as np

# DAVETLİ LİSTESİ (Buraya 40 kişinin kodunu ekleyebilirsin)
onayli_liste = ["ahmet123", "ayse456", "party2026", "vip_konuk"]

st.set_page_config(page_title="Party Door", page_icon="🚪")
st.title("💃 After Party Check-in")

# Kamera Bileşeni
img_file = st.camera_input("Davetiyeyi okutun")

if img_file:
    file_bytes = np.asarray(bytearray(img_file.read()), dtype=np.uint8)
    opencv_img = cv2.imdecode(file_bytes, 1)
    
    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(opencv_img)
    
    if data:
        if data in onayli_liste:
            st.balloons()
            st.success(f"✅ GİRİŞ ONAYLANDI: {data}")
            onayli_liste = [f"davetli_{i}" for i in range(1, 41)]
        else:
            st.error("❌ GEÇERSİZ KOD! Liste dışı.")
    else:
        st.warning("Karekod bulunamadı. Lütfen net bir şekilde gösterin.")