import streamlit as st
import cv2
import numpy as np

# DAVETLİ LİSTESİ (Buraya 40 kişinin kodunu ekleyebilirsin)
onayli_liste = [
    "Ahmet_Yilmaz", "Ayse_Kaya", "Mehmet_Demir", "Fatma_Celik", "Can_Yildiz", 
    "Ece_Aydin", "Burak_Ozkan", "Asli_Gunes", "Emre_Sahin", "Deniz_Arslan",
    "Selin_Bulut", "Mert_Kilic", "Gamze_Yavuz", "Okan_Sari", "Pelin_Aksoy",
    "Tolga_Tekin", "Irem_Unal", "Bora_Koc", "Seda_Turan", "Umut_Erdem",
    "Gizem_Akkaya", "Eren_Polat", "Derya_Korkmaz", "Arda_Guler", "Nil_Ozturk",
    "Kaan_Yaman", "Buse_Avci", "Yigit_Cetin", "Mine_Eren", "Onur_Dogan",
    "Ezgi_Kara", "Serkan_Ay", "Tugba_Guzel", "Hakan_Vural", "Ceren_Simsek",
    "Volkan_Taskin", "Dilek_Yener", "Sinan_Coskun", "Hande_Ates", "Kerem_Yigit"
]
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