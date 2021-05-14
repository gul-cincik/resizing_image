import cv2

def main():
    image = cv2.imread('cicek.png')
    print(image.shape  )
    ekran_cozunurlukleri = 1280, 720

    skala_genislik = ekran_cozunurlukleri[0]/image.shape[1]
    skala_yukseklik = ekran_cozunurlukleri[1]/image.shape[0]
    skala = min(skala_genislik,skala_yukseklik )

    pencere_genislik = int(image.shape[1] * skala)
    pencere_yukseklik = int(image.shape[0] * skala)

    cv2.namedWindow('Boyutlanabilir Pencere', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Boyutlanabilir Pencere', pencere_genislik,pencere_yukseklik)

    cv2.imshow('Boyutlanabilir Pencere', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()