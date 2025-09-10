import streamlit as st
from streamlit_image_comparison import image_comparison
from PIL import Image
import io
import requests


def load_image_from_url(url: str, timeout: int = 10):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        resp = requests.get(url, headers=headers, timeout=timeout)
        resp.raise_for_status()
        return Image.open(io.BytesIO(resp.content)).convert("RGB")
    except Exception:
        return None


# Ana Sayfa
def ana_sayfa():
    image = Image.open("Adsız_tasarım-4-removebg-preview.png")
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

    st.markdown('<div style="color: white;font-size: 32px;font-weight: bold;">Fire Fighting with Drone</div>',
                unsafe_allow_html=True)

    st.write("")
    text = """ is a project developed to improve fire extinguishing processes and provide a more effective fire response. 
    This project aims to control and extinguish fires with unmanned aerial vehicles (drones), especially in areas where fire types and access to fire zones are difficult. Drones can quickly reach the scene of a fire and use high-resolution cameras and equipment to monitor the spread of the fire, surveil the fire and provide data to intervene. This project aims to improve fire safety and effectiveness by providing firefighters with more information and resources. The images below are intended to illustrate the situation caused by fires in some regions in our country and around the world.
      ."""

    st.markdown(f'<div style="color: white; font-weight: bold;">{text}</div>', unsafe_allow_html=True)
    st.write("")

    st.markdown('<div style="color: white;font-size: 24px;font-weight: bold;">Marmaris</div>', unsafe_allow_html=True)

    # Use reliable HTTPS images (Wikimedia) to avoid hotlink blocks
    m1 = load_image_from_url("https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Forest_fire_aftermath.jpg/640px-Forest_fire_aftermath.jpg")
    m2 = load_image_from_url("https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Conifer_forest_before_wildfire.jpg/640px-Conifer_forest_before_wildfire.jpg")
    if m1 and m2:
        image_comparison(img1=m1, img2=m2, label1="After", label2="Before")
    else:
        if m1: st.image(m1, caption="After", use_column_width=True)
        if m2: st.image(m2, caption="Before", use_column_width=True)

    st.markdown('<div style="color: white;font-size: 24px;font-weight: bold;">Kalkan</div>', unsafe_allow_html=True)
    k1 = load_image_from_url("https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Bushfire_aftermath.jpg/640px-Bushfire_aftermath.jpg")
    k2 = load_image_from_url("https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Forest_in_Australia_before_fire.jpg/640px-Forest_in_Australia_before_fire.jpg")
    if k1 and k2:
        image_comparison(img1=k1, img2=k2, label1="After", label2="Before")
    else:
        if k1: st.image(k1, caption="After", use_column_width=True)
        if k2: st.image(k2, caption="Before", use_column_width=True)

    st.markdown('<div style="color: white;font-size: 24px;font-weight: bold;">Santa Rosa, Kaliforniya</div>',
                unsafe_allow_html=True)
    s1 = load_image_from_url("https://static01.nyt.com/newsgraphics/2017/10/09/cali-fires/6aac41a1a254730e98581e3614f8a4aaebd48ee1/coffey-park-after.jpg")
    s2 = load_image_from_url("https://static01.nyt.com/newsgraphics/2017/10/09/cali-fires/6aac41a1a254730e98581e3614f8a4aaebd48ee1/coffey-park-before.jpg")
    if s1 and s2:
        image_comparison(img1=s1, img2=s2, label1="After", label2="Before")
    else:
        if s1: st.image(s1, caption="After", use_column_width=True)
        if s2: st.image(s2, caption="Before", use_column_width=True)

    st.markdown('<div style="color: white;font-size: 24px;font-weight: bold;">Fountaingrove Round Barn</div>',
                unsafe_allow_html=True)
    f1 = load_image_from_url("https://static01.nyt.com/newsgraphics/2017/10/09/cali-fires/6aac41a1a254730e98581e3614f8a4aaebd48ee1/barn-before.jpg")
    f2 = load_image_from_url("https://static01.nyt.com/newsgraphics/2017/10/09/cali-fires/6aac41a1a254730e98581e3614f8a4aaebd48ee1/barn-after.jpg")
    if f1 and f2:
        image_comparison(img1=f1, img2=f2, label1="After", label2="Before")
    else:
        if f1: st.image(f1, caption="After", use_column_width=True)
        if f2: st.image(f2, caption="Before", use_column_width=True)

    st.markdown('<div style="color: white;font-size: 24px;font-weight: bold;">Santa Rosa, Fountaingrove bölgesi</div>',
                unsafe_allow_html=True)
    h1 = load_image_from_url("https://static01.nyt.com/newsgraphics/2017/10/09/cali-fires/6aac41a1a254730e98581e3614f8a4aaebd48ee1/hilton-after.jpg")
    h2 = load_image_from_url("https://static01.nyt.com/newsgraphics/2017/10/09/cali-fires/6aac41a1a254730e98581e3614f8a4aaebd48ee1/hilton-before.jpg")
    if h1 and h2:
        image_comparison(img1=h1, img2=h2, label1="After", label2="Before")
    else:
        if h1: st.image(h1, caption="After", use_column_width=True)
        if h2: st.image(h2, caption="Before", use_column_width=True)

    st.markdown('<div style="color: white;font-size: 24px;font-weight: bold;">Avustralya/Flinders Chase Ulusal Parkı</div>',
                unsafe_allow_html=True)
    a1 = load_image_from_url("https://ichef.bbci.co.uk/news/800/cpsprodpb/9488/production/_110542083_058989880.jpg")
    a2 = load_image_from_url("https://ichef.bbci.co.uk/news/800/cpsprodpb/12902/production/_110543067_gettyimages-186613189.jpg")
    if a1 and a2:
        image_comparison(img1=a1, img2=a2, label1="After", label2="Before")
    else:
        if a1: st.image(a1, caption="After", use_column_width=True)
        if a2: st.image(a2, caption="Before", use_column_width=True)

    st.write("Bu ana sayfadaki içerik...")


# Hakkımızda Sayfası
def hakkimizda():
    image = Image.open("biz kimiz.png")
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

    st.markdown('<div style="color: white;font-size: 32px;font-weight: bold;">front cover</div>',
                unsafe_allow_html=True)

    video_link = "https://www.youtube.com/watch?v=wCNlORnXpe8"
    st.video(video_link)

    st.markdown('<div style="color: white;font-size: 32px;font-weight: bold;">Back cover</div>',
                unsafe_allow_html=True)

    video_link = "https://www.youtube.com/watch?v=KPRjJ67nd2A&ab_channel=BurakhanAlimÇay"
    st.video(video_link)

    st.markdown('<div style="color: white;font-size: 32px;font-weight: bold;">Drone</div>', unsafe_allow_html=True)

    video_link = "https://www.youtube.com/watch?v=0SGDBw_JWAo&ab_channel=BurakhanAlim%C3%87ay"
    st.video(video_link)

    st.markdown('<div style="color: white;font-size: 32px;font-weight: bold;">Watchtower camera</div>',
                unsafe_allow_html=True)

    video_link = "https://www.youtube.com/watch?v=Hawl2DU7MB0&ab_channel=BurakhanAlim%C3%87ay"
    st.video(video_link)



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
    textd = (
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
             "<br><br><br>"
    )
    st.write("")
    st.markdown(f'<div style="color: white;font-size: 22px; font-weight: bold;">{textd}</div>', unsafe_allow_html=True)



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

    st.markdown('<div style="color: white;font-size: 32px;font-weight: bold;">Thermal camera working principle</div>',
            unsafe_allow_html=True)

    text2 = """ helps the user to assess the fire risk of each pixel clicked in a thermal image based on the HSV color space. If the clicked region is within a certain color range, it is indicated that this region may be at risk of fire. This can be used for fire detection or intervention in fire zones."""

    st.markdown(f'<div style="color: white; font-weight: bold;">{text2}</div>', unsafe_allow_html=True)
    youtube_url = "https://youtu.be/x60jHQTFCAQ"
    st.video(youtube_url)



def yangınla_mücadele():
    st.markdown('<div style="color: black;font-size: 32px;font-weight: bold;">BİLGİLENDİRME</div>', unsafe_allow_html=True)

    embed_code = """
    <iframe src="https://e.infogram.com/0b17d02d-f89d-4eba-a631-b601f9588600?src=embed" title="ormanlık alan en fazla iller" width="550" height="673" scrolling="no" frameborder="0" style="border:none;" allowfullscreen="allowfullscreen"></iframe> """
    st.markdown(embed_code, unsafe_allow_html=True)

    embed_code = """
   <iframe src="https://e.infogram.com/4c3fb452-1fb6-4214-a43e-2a8a8353277c?src=embed" title="ormanlık alan iller en az" width="550" height="673" scrolling="no" frameborder="0" style="border:none;" allowfullscreen="allowfullscreen"></iframe>"""
    st.markdown(embed_code, unsafe_allow_html=True)

    embed_code = """
   <iframe src="https://e.infogram.com/c3361aa6-203d-4beb-b2ce-e8d4a2a7481c?src=embed" title="ormanlık alan yüzölçüm az" width="550" height="673" scrolling="no" frameborder="0" style="border:none;" allowfullscreen="allowfullscreen"></iframe>"""
    st.markdown(embed_code, unsafe_allow_html=True)

    embed_code = """
    <iframe src="https://e.infogram.com/0b17d02d-f89d-4eba-a631-b601f9588600?src=embed" title="ormanlık alan en fazla iller" width="550" height="673" scrolling="no" frameborder="0" style="border:none;" allowfullscreen="allowfullscreen"></iframe> """
    st.markdown(embed_code, unsafe_allow_html=True)

    embed_code = """
    <iframe src="https://e.infogram.com/d3538700-a492-4863-b1a9-2b91b6712fc5?src=embed" title="TR ormanlık alan nüfusa göre" width="550" height="673" scrolling="no" frameborder="0" style="border:none;" allowfullscreen="allowfullscreen"></iframe>"""
    st.markdown(embed_code, unsafe_allow_html=True)

    embed_code = """
   <iframe src="https://e.infogram.com/58219bf9-227f-46d6-8d66-05922249c570?src=embed" title="ormanlık alan nüfus düşük iller" width="550" height="673" scrolling="no" frameborder="0" style="border:none;" allowfullscreen="allowfullscreen"></iframe>"""
    st.markdown(embed_code, unsafe_allow_html=True)

    embed_code = """
    <iframe src='http://vis.ecowest.org/interactive/wildfires-play.php#' width='700' height='550' frameborder='0' ></iframe>"""
    st.markdown(embed_code, unsafe_allow_html=True)

    st.title("Türkiye Orman Haritası")

    image_url = "Ekran Resmi 2023-10-08 15.31.22.png"

    st.image(image_url, caption="Türkiye Orman Haritası", use_column_width=True)

    text2 = """ helps the user to assess the fire risk of each pixel clicked in a thermal image based on the HSV color space. If the clicked region is within a certain color range, it is indicated that this region may be at risk of fire. This can be used for fire detection or intervention in fire zones."""

    st.text("")

    st.markdown(f'<div style="color: white;font-size: 22px; font-weight: bold;">{text2}</div>', unsafe_allow_html=True)


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

    st.header("İletişim Formu")
    isim = st.text_input("İsim")
    email = st.text_input("E-posta")
    mesaj = st.text_area("Mesaj")
    gonder = st.button("Gönder")

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
