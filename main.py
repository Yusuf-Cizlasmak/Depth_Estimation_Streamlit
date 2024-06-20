import streamlit as st
from normal2depth import DepthEstimationModel
import time


st.markdown(
"""
# **Resimlerin Derinlikleri Algılama Projesi** 

""")

st.markdown("""
## **Proje Hakkında**
Bu projede ZoeDepth modeli kullanılarak resimlerin derinlik haritaları hesaplanmış ve renklendirilmiştir. Bu proje ilgili kodlara [buradan]() ulabilirsiniz.

"""
)



image = st.file_uploader(
    "Resmi  (PNG) formatında yükleyiniz", type=["jpg", "jpeg", "png"]
)

if image is None:
    st.error("Lütfen bir resim yükleyiniz.")
else:
    

    if st.button("Derinlik Haritasını Hesapla"):
        st.info("Derinlik haritası hesaplanıyor...")


        st.image(image, caption="Yüklenen Resim", use_column_width=True)


        # Derinlik haritası hesaplanacak resmin path'i
        my_bar = st.progress(0,text="Derinlik haritası hesaplanıyor... Lütfen bekleyiniz.")
        

        # DepthEstimationModel sınıfından model oluşturulur.
        model = DepthEstimationModel()

        result = model.calculate_depthmap(image, "output.png")
        for percent_complete in range(100):
            time.sleep(0.1)
            my_bar.progress(percent_complete + 1)

        
        st.success("Derinlik haritası başarıyla hesaplandı.")
        col1,col2 = st.columns([1,1])

        with col1:
            st.image(image, caption="Yüklenen Resim", use_column_width=True)
        with col2:
            st.image("output.png", caption="Renklendirilmiş Derinlik Haritası", use_column_width=True)

        st.markdown(
            """
            ## **İletişim**
            - [Linkedin](https://www.linkedin.com/in/yusuf-cizlasmak/)
            - [Github](https://github.com/Yusuf-Cizlasmak)
            """)
        
