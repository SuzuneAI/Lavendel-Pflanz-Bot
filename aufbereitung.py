# -*- coding: utf-8 -*-

import cv2


def aufbereiten(bild):
    # Konvertiere das Bild in den HSV-Farbraum
    hsv = cv2.cvtColor(bild, cv2.COLOR_BGR2HSV)

    # Definiere den unteren und oberen Grenzwert für Lavendel
    unterer_grenzwert = (120, 50, 50)
    oberer_grenzwert = (160, 255, 255)

    # Erstelle eine Maske, die nur die Lavendelfarben hervorhebt
    maske = cv2.inRange(hsv, unterer_grenzwert, oberer_grenzwert)

    # Wende einen Gaußschen Weichzeichner an, um das Rauschen zu reduzieren
    maske = cv2.GaussianBlur(maske, (5, 5), 0)

    # Gib die Maske zurück
    return maske


if __name__ == '__main__':
    # Lade ein Beispielbild
    bild = cv2.imread('lavendel.jpg')

    # Bereite das Bild vor
    maske = aufbereiten(bild)

    # Zeige das Originalbild und die Maske an
    cv2.imshow('Originalbild', bild)
    cv2.imshow('Maske', maske)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
