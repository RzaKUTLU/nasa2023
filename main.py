import streamlit as st
from streamlit_image_comparison import image_comparison
from PIL import Image
import cv2


# Ana Sayfa
def ana_sayfa():
    image = Image.open("/Users/kutlu/PycharmProjects/Streamlit-NASA/Adsız_tasarım-4-removebg-preview.png")
    # Resmi göster, belirli bir yüzde oranında küçült
    st.image(image, use_column_width=True, width=image.width // 10)

    page_by_img = """
            <style>
            [data-testid="stAppViewContainer"]{
            background: url("https://shiftdelete.net/wp-content/uploads/2021/07/atesi-ates-ile-sonduren-drone-orman-yanginlarini-cozumu-olabilir-3.jpg");
            background-size: cover;top: 0px}

            [data-testid="stHeader"]{
            background-color: rgba(0,0,0,0);
             }

            [data-testid="stToolbar"]{
            right: 2rem;}
            </style>
             """
    st.markdown(page_by_img, unsafe_allow_html=True)
    st.text("")
    st.text("")

    # st.markdown("<h2 style='color:white; font-weight: bold;font-size:35px;'>METİN</h2>",
    #   unsafe_allow_html=True)

    # Başlık metnini beyaz renkte görüntülemek için CSS kullanma / st.markdown('<div style="color: white;font-size: 32px;font-weight: bold;">🔥Yangına Drone ile Müdahele</div>', unsafe_allow_html=True)
    st.markdown('<div style="color: white;font-size: 32px;font-weight: bold;">Yangına Drone ile Müdahele</div>',
                unsafe_allow_html=True)

    st.write("")
    text = """ is a project developed to improve fire extinguishing processes and provide a more effective fire response. 
    This project aims to control and extinguish fires with unmanned aerial vehicles (drones), especially in areas where fire types and access to fire zones are difficult. Drones can quickly reach the scene of a fire and use high-resolution cameras and equipment to monitor the spread of the fire, surveil the fire and provide data to intervene. This project aims to improve fire safety and effectiveness by providing firefighters with more information and resources. The images below are intended to illustrate the situation caused by fires in some regions in our country and around the world.
      ."""

    # Yazıyı beyaz renkte, arka planı kaldırmak ve yazıyı kalın yapmak için stil özellikleri kullanarak HTML kullanımı
    st.markdown(f'<div style="color: white; font-weight: bold;">{text}</div>', unsafe_allow_html=True)
    st.write("")

    st.markdown('<div style="color: white;font-size: 24px;font-weight: bold;">Marmaris', unsafe_allow_html=True)

    image_comparison(
        img1="https://i01.sozcucdn.com/wp-content/uploads/2021/08/02/marmaris-yangin2-once-sonra.jpg",
        img2="https://i01.sozcucdn.com/wp-content/uploads/2021/08/02/marmaris-yangin3-once-sonra.jpg",
        label1="After",
        label2="Before",

    )

    st.markdown('<div style="color: white;font-size: 24px;font-weight: bold;">Kalkan', unsafe_allow_html=True)
    image_comparison(
        img1="http://www.detaykibris.com/d/gallery/514_2.jpg",
        img2="http://www.detaykibris.com/d/gallery/514_3.jpg",
        label1="After",
        label2="Before",
    )

    st.markdown('<div style="color: white;font-size: 24px;font-weight: bold;">Santa Rosa, Kaliforniya',
                unsafe_allow_html=True)
    image_comparison(
        img1="https://static01.nyt.com/newsgraphics/2017/10/09/cali-fires/6aac41a1a254730e98581e3614f8a4aaebd48ee1/coffey-park-after.jpg",
        img2="https://static01.nyt.com/newsgraphics/2017/10/09/cali-fires/6aac41a1a254730e98581e3614f8a4aaebd48ee1/coffey-park-before.jpg",
        label1="After",
        label2="Before",
    )
    st.markdown('<div style="color: white;font-size: 24px;font-weight: bold;">Fountaingrove Round Barn',
                unsafe_allow_html=True)
    image_comparison(
        img1="https://static01.nyt.com/newsgraphics/2017/10/09/cali-fires/6aac41a1a254730e98581e3614f8a4aaebd48ee1/barn-before.jpg",
        img2="https://static01.nyt.com/newsgraphics/2017/10/09/cali-fires/6aac41a1a254730e98581e3614f8a4aaebd48ee1/barn-after.jpg",
        label1="After",
        label2="Before",
    )
    st.markdown('<div style="color: white;font-size: 24px;font-weight: bold;">Santa Rosa, Fountaingrove bölgesi',
                unsafe_allow_html=True)
    image_comparison(
        img1="https://static01.nyt.com/newsgraphics/2017/10/09/cali-fires/6aac41a1a254730e98581e3614f8a4aaebd48ee1/hilton-after.jpg",
        img2="https://static01.nyt.com/newsgraphics/2017/10/09/cali-fires/6aac41a1a254730e98581e3614f8a4aaebd48ee1/hilton-before.jpg",
        label1="After",
        label2="Before",
    )
    st.markdown('<div style="color: white;font-size: 24px;font-weight: bold;">Avustralya/Flinders Chase Ulusal Parkı',
                unsafe_allow_html=True)
    image_comparison(
        img1="https://ichef.bbci.co.uk/news/800/cpsprodpb/9488/production/_110542083_058989880.jpg",
        img2="https://ichef.bbci.co.uk/news/800/cpsprodpb/12902/production/_110543067_gettyimages-186613189.jpg",
        label1="After",
        label2="Before",
    )

    st.write("Bu ana sayfadaki içerik...")


# Hakkımızda Sayfası
def hakkimizda():
    image = Image.open("/Users/kutlu/PycharmProjects/Streamlit-NASA/biz kimiz.png")
    st.image(image, caption="PNG Resmi", use_column_width=True)
    page_by_img = """
               <style>
               [data-testid="stAppViewContainer"]{
               background: url("https://shiftdelete.net/wp-content/uploads/2021/07/atesi-ates-ile-sonduren-drone-orman-yanginlarini-cozumu-olabilir-3.jpg");
               background-size: cover;top: 0px}

               [data-testid="stHeader"]{
               background-color: rgba(0,0,0,0);
                }

               [data-testid="stToolbar"]{
               right: 2rem;}
               </style>
                """
    st.markdown(page_by_img, unsafe_allow_html=True)


# Yangın Nedir Sayfası
import streamlit as st


def drone():
    page_by_img = """
             <style>
             [data-testid="stAppViewContainer"]{
             background: url("https://i.gazeteoksijen.com/storage/files/images/2022/06/01/yasamak-bir-orman-gibi-kardescesine-GDL0.jpg");
             background-size: cover;top: 0px}

             [data-testid="stHeader"]{
             background-color: rgba(0,0,0,0);
              }

             [data-testid="stToolbar"]{
             right: 2rem;}
             </style>
              """
    st.markdown(page_by_img, unsafe_allow_html=True)
    st.text("")
    st.text("")

    st.markdown('<div style="color: white;font-size: 32px;font-weight: bold;">front cover  </div>',
                unsafe_allow_html=True)

    # YouTube video linki
    video_link = "https://www.youtube.com/watch?v=wCNlORnXpe8"
    st.video(video_link)

    ###2

    st.markdown('<div style="color: white;font-size: 32px;font-weight: bold;">Back cover  </div>',
                unsafe_allow_html=True)

    # YouTube video linki
    video_link = "https://www.youtube.com/watch?v=KPRjJ67nd2A&ab_channel=BurakhanAlimÇay"
    st.video(video_link)

    ### 3

    st.markdown('<div style="color: white;font-size: 32px;font-weight: bold;">Drone</div>', unsafe_allow_html=True)

    # YouTube video linki
    video_link = "https://www.youtube.com/watch?v=0SGDBw_JWAo&ab_channel=BurakhanAlim%C3%87ay"
    st.video(video_link)

    st.markdown('<div style="color: white;font-size: 32px;font-weight: bold;">Watchtower camera </div>',
                unsafe_allow_html=True)

    # YouTube video linki
    video_link = "https://www.youtube.com/watch?v=Hawl2DU7MB0&ab_channel=BurakhanAlim%C3%87ay"
    st.video(video_link)

    # Yazıyı beyaz renkte, arka planı kaldırmak ve yazıyı kalın yapmak için stil özellikleri kullanarak HTML kullanım


def yangin_nedir():
    page_by_img = """
             <style>
             [data-testid="stAppViewContainer"]{
             background: url("https://i.gazeteoksijen.com/storage/files/images/2022/06/01/yasamak-bir-orman-gibi-kardescesine-GDL0.jpg");
             background-size: cover;top: 0px}

             [data-testid="stHeader"]{
             background-color: rgba(0,0,0,0);
              }

             [data-testid="stToolbar"]{
             right: 2rem;}
             </style>
              """
    st.markdown(page_by_img, unsafe_allow_html=True)

    st.text("")
    st.text("")

    st.markdown('<div style="color: white;font-size: 32px;font-weight: bold;">Tree burn times ?</div>',
                unsafe_allow_html=True)

    st.write("")
    textd = ("\n"
             "Tree burn times ;  \n"
             "Burning times of trees can vary greatly in minutes and depend on many factors. Generally, thin branches or leaves burn quickly and are extinguished within a few minutes, while thicker wood or the trunk may burn longer and may last for hours or even days. In addition, the severity of the fire, moisture content in the tree and other environmental conditions can also affect the burn time. It is therefore difficult to give a more precise burn time in minutes for a particular tree species or conditions. \n"
             "The burn times of trees can vary greatly depending on factors such as the type of tree, moisture content, size and severity of the fire. Below you can find general information about the approximate burn times of common tree species, but these times can vary depending on the conditions: \n"
             "<br>1. Pine Trees: They can burn for around 20-30 minutes. \n"
             "<br>2. Oak Trees: Due to their denser wood they can burn longer, measured in hours. \n"
             "<br>3. Maple Trees: They can burn for about 30-45 minutes. \n"
             "<br>4. Sycamore Trees: A medium-sized plane tree can burn for about 30 minutes to an hour. \n"
             "<br>5. Alder Trees: Alder trees, due to their denser wood, can also burn for a long time, in hours. \n"
             "<br>6. Shrubs and Thin Branches: They burn faster and usually go out within minutes.     \n"
              "<br>However, these times can vary greatly depending on factors such as environmental conditions, moisture content and fire severity.To estimate burn times more precisely, fire scientists and experts conduct laboratory tests and field experiments.Care must always be taken in terms of fire safety and appropriate equipment and precautions must be taken to control fires."
             """
             <br><br><br>
             <div style="color: white;font-size: 32px;font-weight: bold;">Chemical ingredients to be used in drones </div>
             
The main ingredients in an ABC class A fire extinguisher (chemical fire extinguisher) usually include the following: 
 
1. Monoammonium Phosphate (NH4H2PO4): This substance is an effective chemical component for extinguishing solid fires (Class A). It absorbs heat during the combustion of solid materials and cools the fire. 
 
2. Monoammonium Sulfate [(NH4)2SO4]: Monoammonium sulfate is another chemical compound used to extinguish solid fires. It absorbs heat and cools during a fire. 
 
3. Super Active Potassium Sulfate (Super Active K): This is an additive used in ABC fire extinguishers to extinguish Class A fires more effectively. It provides faster and more effective fire extinguishing. 
 
4. Gas Pressure: ABC fire extinguishers need pressure to spray the chemical powders they contain. Inactive gases such as nitrogen or carbon dioxide are usually used. 
 
These components ensure the functionality of ABC fire extinguishers and help them to be used effectively against different types of fires. However, the contents and performance of the extinguisher can vary from manufacturer to manufacturer, so it is important to carefully read the contents and instructions for use of a particular product. Furthermore, fire extinguishers should be periodically checked and maintained so that they work reliably when they need to be used.
             """)
    st.write("")
    st.markdown(f'<div style="color: white;font-size: 22px; font-weight: bold;">{textd}</div>', unsafe_allow_html=True)
    image_url = "/Users/kutlu/PycharmProjects/Streamlit-NASA/ABCDK 2 WEB.jpg"



def termal_kamera():
    page_by_img = """
             <style>
             [data-testid="stAppViewContainer"]{
             background: url("https://i.gazeteoksijen.com/storage/files/images/2022/06/01/yasamak-bir-orman-gibi-kardescesine-GDL0.jpg");
             background-size: cover;top: 0px}

             [data-testid="stHeader"]{
             background-color: rgba(0,0,0,0);
              }

             [data-testid="stToolbar"]{
             right: 2rem;}
             </style>
              """
    st.markdown(page_by_img, unsafe_allow_html=True)
    st.text("")
    st.text("")

    #########################################
    st.html('<div style="color: white;font-size: 32px;font-weight: bold;">Thermal camera working principle </div>',
            unsafe_allow_html=True)

    text2 = """ helps the user to assess the fire risk of each pixel clicked in a thermal image based on the HSV color space. If the clicked region is within a certain color range, it is indicated that this region may be at risk of fire. This can be used for fire detection or intervention in fire zones."""

    # Yazıyı beyaz renkte, arka planı kaldırmak ve yazıyı kalın yapmak için stil özellikleri kullanarak HTML kullanımı
    st.html(f'<div style="color: white; font-weight: bold;">{text2}</div>', unsafe_allow_html=True)
    youtube_url = "https://youtu.be/x60jHQTFCAQ"
    st.video(youtube_url)


def yangınla_mücadele():
    st.markdown('<div style="color: black;font-size: 32px;font-weight: bold;">BİLGİLENDİRME', unsafe_allow_html=True)

    # gömme kodunu gömme 1
    embed_code = """
    <iframe src="https://e.infogram.com/0b17d02d-f89d-4eba-a631-b601f9588600?src=embed" title="ormanlık alan en fazla iller" width="550" height="673" scrolling="no" frameborder="0" style="border:none;" allowfullscreen="allowfullscreen"></iframe> """
    st.markdown(embed_code, unsafe_allow_html=True)

    # gömme kodunu gömme 2
    embed_code = """
   <iframe src="https://e.infogram.com/4c3fb452-1fb6-4214-a43e-2a8a8353277c?src=embed" title="ormanlık alan iller en az" width="550" height="673" scrolling="no" frameborder="0" style="border:none;" allowfullscreen="allowfullscreen"></iframe>"""
    st.markdown(embed_code, unsafe_allow_html=True)

    # gömme kodunu gömme 3
    embed_code = """
   <iframe src="https://e.infogram.com/c3361aa6-203d-4beb-b2ce-e8d4a2a7481c?src=embed" title="ormanlık alan yüzölçüm az" width="550" height="673" scrolling="no" frameborder="0" style="border:none;" allowfullscreen="allowfullscreen"></iframe>"""
    st.markdown(embed_code, unsafe_allow_html=True)

    # gömme kodunu gömme 4
    embed_code = """
    <iframe src="https://e.infogram.com/0b17d02d-f89d-4eba-a631-b601f9588600?src=embed" title="ormanlık alan en fazla iller" width="550" height="673" scrolling="no" frameborder="0" style="border:none;" allowfullscreen="allowfullscreen"></iframe> """
    st.markdown(embed_code, unsafe_allow_html=True)

    # gömme kodunu gömme 5
    embed_code = """
    <iframe src="https://e.infogram.com/d3538700-a492-4863-b1a9-2b91b6712fc5?src=embed" title="TR ormanlık alan nüfusa göre" width="550" height="673" scrolling="no" frameborder="0" style="border:none;" allowfullscreen="allowfullscreen"></iframe>"""
    st.markdown(embed_code, unsafe_allow_html=True)

    # gömme kodunu gömme 6
    embed_code = """
   <iframe src="https://e.infogram.com/58219bf9-227f-46d6-8d66-05922249c570?src=embed" title="ormanlık alan nüfus düşük iller" width="550" height="673" scrolling="no" frameborder="0" style="border:none;" allowfullscreen="allowfullscreen"></iframe>"""
    st.markdown(embed_code, unsafe_allow_html=True)

    # gömme kodunu gömme 7
    embed_code = """
    <iframe src='http://vis.ecowest.org/interactive/wildfires-play.php#' width='700' height='550' frameborder='0' ></iframe>"""
    st.markdown(embed_code, unsafe_allow_html=True)

    # Bölge, bilgi metni ve ilgili fotoğrafları içeren bir sözlük oluşturun
    information = {
        "Biological Plant Diversity in Turkey by Regions": {
            "Text": "In our country, the trees growing in forests include poplar, oak, storax, plane tree, lime, hornbeam, birch, chestnut, storax, fir, juniper, maple, red pine, spruce, pine, cedar, oak, beech, cedar, and turkey oak.",
            "Photo": "https://ustakunduz.com/wp-content/uploads/2021/02/turkiyedekli-agac-turleri.jpg"
            # Specify the path to the photo file
        }
    }

    # Başlık
    st.title("Türkiye Orman Haritası")

    # İstockphoto'dan alınan fotoğrafın URL'si
    image_url = "/Users/kutlu/PycharmProjects/Streamlit-NASA/Ekran Resmi 2023-10-08 15.31.22.png"

    # Fotoğrafı aç
    st.image(image_url, caption="Türkiye Orman Haritası", use_column_width=True)

    text2 = """ helps the user to assess the fire risk of each pixel clicked in a thermal image based on the HSV color space. If the clicked region is within a certain color range, it is indicated that this region may be at risk of fire. This can be used for fire detection or intervention in fire zones."""

    st.text("")


    # Yazıyı beyaz renkte, arka planı kaldırmak ve yazıyı kalın yapmak için stil özellikleri kullanarak HTML kullanımı
    st.markdown(f'<div style="color: white;font-size: 22px; font-weight: bold;">{text3}</div>', unsafe_allow_html=True)


# İletişim Sayfası
def iletisim():
    page_by_img = """
             <style>
             [data-testid="stAppViewContainer"]{
             background: url("https://images.pexels.com/photos/821754/pexels-photo-821754.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2");
             background-size: cover;top: 0px}

             [data-testid="stHeader"]{
             background-color: rgba(0,0,0,0);
              }

             [data-testid="stToolbar"]{
             right: 2rem;}
             </style>
              """
    st.markdown(page_by_img, unsafe_allow_html=True)
    st.text("")
    st.text("")

    st.markdown("<h2 style='color:#8a3a3a; font-weight: bold;'>İletişim Bilgileri</h2>",
                unsafe_allow_html=True)

    st.markdown("<h2 style='color:#8a3a3a; font-weight: normal;'>E-posta</h2>",
                unsafe_allow_html=True)

    st.write("rza.kutluu@gmail.com")

    # İletişim formu eklemek için bir metin kutusu kullanabilirsiniz
    st.header("İletişim Formu")
    isim = st.text_input("İsim")
    email = st.text_input("E-posta")
    mesaj = st.text_area("Mesaj")
    gonder = st.button("Gönder")

    # Gönder düğmesine tıklanırsa işlem yapabilirsiniz
    if gonder:
        st.success("Mesajınız gönderildi!")


# Acil Durum Numaraları Sayfası
def acil_durum_numaralari():
    st.title("Acil Durum Numaraları")
    st.markdown("<h1 style='color:#ff0000;'>☎️112</h1>", unsafe_allow_html=True)


# Ana uygulama
if __name__ == "__main__":
    selected_page = st.sidebar.selectbox("Sayfa Seçin",
                                         ["Home Page", "who we are", "fire fighting systems", "About Trees",
                                          "Data-Bank", "Thermal Camera Working Principl", "Contact",
                                          "Emergency Numbers"])

    if selected_page == "Home Page":
        ana_sayfa()
    elif selected_page == "who we are":
        hakkimizda()
    elif selected_page == "fire fighting systems":
        drone()
    elif selected_page == "About Trees":
        yangin_nedir()
    elif selected_page == "Data-Bank":
        yangınla_mücadele()
    elif selected_page == "Thermal Camera Working Principl":
        termal_kamera()
    elif selected_page == "Contact":
        iletisim()
    elif selected_page == "Emergency Numbers":
        acil_durum_numaralari()
