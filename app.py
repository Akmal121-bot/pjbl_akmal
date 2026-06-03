import streamlit as st

st.set_page_config(
    page_title="matematika geometri by akmal",
    page_icon="🏆"
)

with st.sidebar:
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Pastikan file "geometri.png" berada di folder yang sama
        st.image("akmal.png")
        
    st.title("Baangun Datar")
    
    pilihan = st.selectbox(
        "pilihan bangun datar",
        ["persegi", "persegi panjang", "lingkaran", "segitiga", "trapesium"]
    )
    
    st.caption("dibuat dengan 🔥 oleh **Akmal Falah Muhadzdzib**")

match pilihan:
    case "persegi":
        st.title("persegi")
        st.markdown("menghitung luas dan keliling `persegi`")
        
        sisi = st.number_input("masukkan sisi")
        
        if st.button("hitung", type="primary"):
            luas = sisi * sisi
            keliling = 4 * sisi
            
            st.snow()
            st.success(f"luas persegi adalah {luas:.2f} dan kelilingnya adalah {keliling:.2f}")
                
    case "persegi panjang":
        st.title("persegi panjang")
        st.markdown("menghitung luas dan keliling `persegi panjang`")
        
        panjang = st.number_input("masukkan panjang")
        lebar = st.number_input("masukkan lebar")
        
        if st.button("hitung", type="primary"):
            luas = panjang * lebar
            keliling = 2 * (panjang + lebar)
            
            st.snow()
            st.success(f"luas persegi panjang adalah {luas:.2f} dan kelilingnya adalah {keliling:.2f}")
            
    case "lingkaran":
        st.title("lingkaran")
        st.markdown("menghitung luas dan keliling `lingkaran`")
        
        jari_jari = st.number_input("masukkan jari jari")
        
        if st.button("hitung", type="primary"):
            luas = 3.14 * jari_jari * jari_jari
            keliling = 2 * 3.14 * jari_jari
            
            st.snow()
            st.success(f"luas lingkaran adalah {luas:.2f} dan kelilingnya adalah {keliling:.2f}")

    case "segitiga":
        st.title("segitiga")
        st.markdown("menghitung luas dan keliling `segitiga`")
        
        alas = st.number_input("masukkan alas")
        tinggi = st.number_input("masukkan tinggi")
        sisi_a = st.number_input("masukkan sisi A (untuk keliling)")
        sisi_b = st.number_input("masukkan sisi B (untuk keliling)")
        sisi_c = st.number_input("masukkan sisi C (untuk keliling)")
        
        if st.button("hitung", type="primary"):
            luas = 0.5 * alas * tinggi
            keliling = sisi_a + sisi_b + sisi_c
            
            st.snow()
            st.success(f"luas segitiga adalah {luas:.2f} dan kelilingnya adalah {keliling:.2f}")

    case "trapesium":
        st.title("trapesium")
        st.markdown("menghitung luas dan keliling `trapesium` (sama kaki/siku-siku)")
        
        sisi_atas = st.number_input("masukkan sisi sejajar atas")
        sisi_bawah = st.number_input("masukkan sisi sejajar bawah")
        tinggi_trap = st.number_input("masukkan tinggi")
        sisi_miring1 = st.number_input("masukkan sisi miring/samping 1")
        sisi_miring2 = st.number_input("masukkan sisi miring/samping 2")
        
        if st.button("hitung", type="primary"):
            luas = 0.5 * (sisi_atas + sisi_bawah) * tinggi_trap
            keliling = sisi_atas + sisi_bawah + sisi_miring1 + sisi_miring2
            
            st.snow()
            st.success(f"luas trapesium adalah {luas:.2f} dan kelilingnya adalah {keliling:.2f}")

    case _:
        st.error("terjadi kesalahan")
