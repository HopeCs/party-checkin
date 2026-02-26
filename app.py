import streamlit as st
import cv2
import numpy as np
import os

# 1. DAVETLİ LİSTESİ (Daha önce oluşturduğumuz isimler)
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

# 2. Giriş Yapanları Kaydetmek İçin Dosya Kontrolü
LOG_FILE = "giris_yapanlar.txt"
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w") as f:
        f.write("") # Dosya yoksa oluştur

def kontrol_et_ve_kaydet(kod):
    with open(LOG_FILE, "r") as f:
        kayitlar = f.read().splitlines()
    
    if kod in kayitlar:
        return "tekrar"
    else:
        with open(LOG_FILE, "a") as f:
            f.write(kod + "\n")
        return "yeni"

# Arayüz Ayarları
st.set_page_config(page_title="Party Door Security", page_icon="🛡️")
st.title("🛡️ After Party Güvenlik")

img_file = st.camera_input("Davetiyeyi okutun")

if img_file:
    file_bytes = np.asarray(bytearray(img_file.read()), dtype=np.uint8)
    opencv_img = cv2.imdecode(file_bytes, 1)
    detector = cv2.QRCodeDetector()
    data, _, _ = detector.detectAndDecode(opencv_img)
    
    if data:
        if data in onayli_liste:
            durum = kontrol_et_ve_kaydet(data)
            
            if durum == "yeni":
                st.balloons()
                st.success(f"✅ GİRİŞ ONAYLANDI: {data}")
                st.info("İlk kez giriş yapıldı. Hoş geldiniz!")
            else:
                st.warning(f"⚠️ DİKKAT: {data} kodu daha önce kullanılmış!")
                st.error("Bu davetiye ile tekrar giriş yapılamaz.")
        else:
            st.error("❌ GEÇERSİZ KOD: Bu isim davetli listesinde yok.")