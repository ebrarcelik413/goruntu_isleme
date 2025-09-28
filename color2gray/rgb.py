import cv2

# Fotoğrafın tam yolu
img_path = r"C:\Users\Ebrar Celik\Desktop\goruntu_renklendirme\goruntu_isleme\color2gray\siyah_beyaz.png"

# Siyah-beyaz fotoğrafı oku
gray = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

deneme deneme

if gray is None:
    print("⚠️ Fotoğraf bulunamadı! Dosya yolunu kontrol et.")
else:
    print("✅ Fotoğraf yüklendi, boyut:", gray.shape)
    # Colormap uygula
    color_img = cv2.applyColorMap(gray, cv2.COLORMAP_JET)

    # Sonucu göster
    cv2.imshow("Renklendirilmis", color_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

