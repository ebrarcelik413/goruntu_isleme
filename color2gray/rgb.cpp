#include <opencv2/opencv.hpp>
#include <iostream>
using namespace cv;
using namespace std;

int main() {
    string path = "test.png";
    cout << "Dosya yolu: " << path << endl;

    Mat image = imread(path);
    if (image.empty()) {
        cout << "Resim yüklenemedi! Lütfen dosya yolunu kontrol et." << endl;
        system("dir"); 
        return -1;
    }

    cout << "Orijinal resim boyutu: " << image.cols << "x" << image.rows << endl;

    // ---- Renkli resmi griye dönüştür ----
    Mat grayImage;
    cvtColor(image, grayImage, COLOR_BGR2GRAY);

    // ---- Sonuçları göster ----
    imshow("Orijinal", image);
    imshow("Siyah Beyaz", grayImage);

    waitKey(0);
    return 0;
}
