# NASA 2023 – Fire Fighting with Drones (Streamlit)

Bu proje, orman yangınlarına insansız hava araçlarıyla (drone) müdahaleyi anlatan interaktif bir Streamlit uygulamasıdır. Marmaris, Kalkan ve Kaliforniya örnekleriyle önce/sonra görüntü karşılaştırmaları, termal kamera çalışma prensibi ve bilgilendirici görselleştirmeler içerir.

## Özellikler
- Görsel karşılaştırmalar (before/after)
- Termal kamera çalışma prensibi (video)
- Bilgilendirme grafikleri ve gömülü içerikler
- Basit, taşınabilir kurulum

## Kurulum
```bash
pip install -r requirements.txt
streamlit run main.py
```

## Gereksinimler
- Python 3.9+
- Streamlit, Pillow, streamlit-image-comparison

## Notlar
- Görseller repo içinden relative path ile kullanılır; harici mutlak path yoktur.
- Kod sadeleştirildi (kullanılmayan importlar temizlendi, küçük hatalar düzeltildi).

## Lisans
Bu depo eğitim amaçlı örnek bir projedir.
