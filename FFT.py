from numbers import Real
import numpy as np
from PIL import Image, ImageOps
import cmath
import time

Image1D = np.array([1, 2, 3, 4])

def openImg(nomImage):
    imgRGB = Image.open(nomImage)
    imgGreyscale = ImageOps.grayscale(imgRGB)
    matriceGreyscale = np.asarray(imgGreyscale)
    return matriceGreyscale

def TF1D(Matrice1D):
    N=len(Matrice1D)
    # Creation d'une matrice de la taille de l'image1D 
    MatriceRes = np.zeros(N, dtype=complex)
    # On parcours notre matrice initial
    for u in range(N):
        sum = 0
        # On applique la formule
        for x in range(N):
            sum += Matrice1D[x]*cmath.exp((-2j * cmath.pi * u * x) / N)
        # On met la valeur dans la matrice resultat + on arrondi les valeurs
        MatriceRes[u]=round(sum.real, 8)+round(sum.imag, 8)*1j
    return MatriceRes

def TFI1D(Matrice1D):
    N=len(Matrice1D)
    # Creation d'une matrice de la taille de l'image1D 
    MatriceRes = np.zeros(N, dtype=complex)
    # On parcours notre matrice initial
    for u in range(N):
        sum = 0
        # On applique la formule
        for x in range(N):
            sum += Matrice1D[x]*cmath.exp((2j * cmath.pi * u * x) / N)
        sum /= N
        # On met la valeur dans la matrice resultat + on arrondi les valeurs
        MatriceRes[u]=round(sum.real, 8)+round(sum.imag, 8)*1j
    return MatriceRes

def TF2D(Matrice2D):
    # Creation d'une matrice de taille ligne*colonne de l'image2D 
    MatriceRes = np.zeros((Matrice2D.shape[0], Matrice2D.shape[1]), dtype=complex)

    # On applique la TF1D sur toute les lignes de notre image2D
    for i in range(Matrice2D.shape[0]):
        MatriceRes[i] = TF1D(Matrice2D[i])
    # On inverse les lignes et les colonnes
    MatriceRes_trans = MatriceRes.transpose()
    # On applique à nouveau la TF1D sur cette matrice (donc sur les colonnes de notre image2D)
    for i in range(MatriceRes_trans.shape[0]):
        MatriceRes_trans[i] = TF1D(MatriceRes_trans[i])
    # On remet les lignes à la place des colonnes 
    MatriceRes = MatriceRes_trans.transpose()
    np.savetxt("TF2D/matrice_TF2D.txt", MatriceRes, fmt="%.2e")
    #On créé une matrice de uint8 afin de pas avoir de problème de compatibilité lors de la création de l'image finale
    Matrice = np.zeros((MatriceRes.shape[0], MatriceRes.shape[1]), dtype=np.uint8)
    for i in range (MatriceRes.shape[0]):
        for j in range (MatriceRes.shape[1]):
            Matrice[i][j]=np.abs(MatriceRes[i][j])
    img = Image.fromarray(Matrice)
    img.save("TF2D/ImageTF2D.jpg")
    return MatriceRes

def TFI2D(Matrice2D):
    # Creation d'une matrice de taille ligne*colonne de l'image2D 
    MatriceRes = np.zeros((Matrice2D.shape[0], Matrice2D.shape[1]), dtype=complex)
    
    # On applique la TFI1D sur toute les lignes de notre image2D
    for i in range(Matrice2D.shape[0]):
        MatriceRes[i] = TFI1D(Matrice2D[i])
        
    # On inverse les lignes et les colonnes
    MatriceRes_trans = MatriceRes.transpose()
    # On applique à nouveau la TFI1D sur cette matrice (donc sur les colonnes de notre image2D)
    for i in range(MatriceRes_trans.shape[0]):
        MatriceRes_trans[i] = TFI1D(MatriceRes_trans[i])
    # On remet les lignes à la place des colonnes 
    MatriceRes = MatriceRes_trans.transpose()
    #On créé une matrice de uint8 afin de pas avoir de problème de compatibilité lors de la création de l'image finale
    Matrice = np.zeros((MatriceRes.shape[0], MatriceRes.shape[1]), dtype=np.uint8)
    for i in range (MatriceRes.shape[0]):
        for j in range (MatriceRes.shape[1]):
            Matrice[i][j]=MatriceRes[i][j].real
    np.savetxt("TF2D/matrice_TFI2D.txt", Matrice, fmt="%.1e")
    img = Image.fromarray(Matrice)
    img.save("TF2D/ImageTFI2D.jpg")
    return MatriceRes

def TF1R(Matrice1D):
    N=len(Matrice1D)

    # Si le tableau n'a qu'une seul valeur on retourne la valeur
    if N<=1:
        return Matrice1D
    else :
        # Récursivité sur les index pair et impair
        pair = TF1R(Matrice1D[0::2])
        impair = TF1R(Matrice1D[1::2])
        # On crée un nouveau tableau
        MatriceRes = np.zeros(N).astype(np.complex64)
        # On reconstitue petit à petit le tableau 1D avec la formule
        for i in range(0, N//2):
            MatriceRes[i] = pair[i]+cmath.exp(-2j*cmath.pi*i/N)*impair[i]
            MatriceRes[i+N//2] = pair[i]-cmath.exp(-2j*cmath.pi*i/N)*impair[i]
        return MatriceRes

def TFI1R_m(Matrice1D):
    N=len(Matrice1D)

    # Si le tableau n'a qu'une seul valeur on retourne la valeur
    if N<=1:
        return Matrice1D
    else :
        # Récursivité sur les index pair et impair
        pair = TFI1R_m(Matrice1D[0::2])
        impair = TFI1R_m(Matrice1D[1::2])
        # On crée un nouveau tableau
        MatriceRes = np.zeros(N).astype(np.complex64)
        # On reconstitue petit à petit le tableau 1D avec la formule et les changements de signes
        for i in range(0, N//2):
            MatriceRes[i] = pair[i]+cmath.exp(2j*cmath.pi*i/N)*impair[i]
            MatriceRes[i+N//2] = pair[i]-cmath.exp(2j*cmath.pi*i/N)*impair[i]
        return MatriceRes

# On supprime le coefficiant de chaque valeur
def TFI1R(tab):
    return [x/len(tab) for x in TFI1R_m(tab)]

def TF2R(Matrice2D):
    # Creation d'une matrice de taille ligne*colonne de l'image2D 
    MatriceRes = np.zeros((Matrice2D.shape[0], Matrice2D.shape[1]), dtype=complex)

    # On applique la TF1R sur toute les lignes de notre image2D
    for i in range(Matrice2D.shape[0]):
        MatriceRes[i] = TF1R(Matrice2D[i])
    # On inverse les lignes et les colonnes
    MatriceRes_trans = MatriceRes.transpose()
    # On applique à nouveau la TF1R sur cette matrice (donc sur les colonnes de notre image2D)
    for i in range(MatriceRes_trans.shape[0]):
        MatriceRes_trans[i] = TF1R(MatriceRes_trans[i])
    # On remet les lignes à la place des colonnes 
    MatriceRes = MatriceRes_trans.transpose()
    #On créé une matrice de uint8 afin de pas avoir de problème de compatibilité lors de la création de l'image finale
    Matrice = np.zeros((MatriceRes.shape[0], MatriceRes.shape[1]), dtype=np.uint8)
    for i in range (MatriceRes.shape[0]):
        for j in range (MatriceRes.shape[1]):
            Matrice[i][j]=np.abs(MatriceRes[i][j]) 
    np.savetxt("TF2R/matrice_TF2R.txt", MatriceRes, fmt="%.2e")
    img = Image.fromarray(Matrice)
    img.save("TF2R/ImageTF2R.jpg")
    return MatriceRes

def TFI2R(Matrice2D):
    # Creation d'une matrice de taille ligne*colonne de l'image2D 
    MatriceRes = np.zeros((Matrice2D.shape[0], Matrice2D.shape[1]), dtype=complex)
    
    # On applique la TFI1R sur toute les lignes de notre image2D
    for i in range(Matrice2D.shape[0]):
        MatriceRes[i] = TFI1R(Matrice2D[i])
        
    # On inverse les lignes et les colonnes
    MatriceRes_trans = MatriceRes.transpose()
    print(MatriceRes_trans)
    # On applique à nouveau la TFI1R sur cette matrice (donc sur les colonnes de notre image2D)
    for i in range(MatriceRes_trans.shape[0]):
        MatriceRes_trans[i] = TFI1R(MatriceRes_trans[i])       
    # On remet les lignes à la place des colonnes 
    MatriceRes = MatriceRes_trans.transpose()
    print(MatriceRes)
    #On créé une matrice de uint8 afin de pas avoir de problème de compatibilité lors de la création de l'image finale
    Matrice = np.zeros((MatriceRes.shape[0], MatriceRes.shape[1]), dtype=np.uint8)
    for i in range (MatriceRes.shape[0]):
        for j in range (MatriceRes.shape[1]):
            Matrice[i][j]=MatriceRes[i][j].real
    np.savetxt("TF2R/matrice_TFI2R.txt", Matrice, fmt="%.1e")
    img = Image.fromarray(Matrice)
    img.save("TF2R/ImageTFI2R.jpg")
    return MatriceRes

def main():
    timeResDirecte=0
    timeResRapide=0
    while True:

        print("\n1.  Demonstration de la transformee de Fourrier et de son inverse sur une matrice à une dimension \n2.  Transformee de Fourrier Directe à deux dimensions\n22. Transformee de Fourrier Inverse Directe à deux dimensions")
        print("3.  Transformee de Fourrier rapide à deux dimensions\n33. Transformee de Fourrier rapide inverse à deux dimensions\n")
        print("Temps d'éxecution Direct : ", timeResDirecte)
        print("Temps d'éxecution Rapide : ", timeResRapide, "\n")

        choix = input("Votre choix : ")
        match choix:
            case '1':
                print('Matrice en entrée')
                print(Image1D)
                print('--------------------------------------------------')
                ImageTF1D=TF1D(Image1D)
                print('Résultat de notre algorithme pour la TF1D')
                print(ImageTF1D)
                print('--------------------------------------------------')
                ImageTF1R=TF1R(Image1D)
                print('Résultat de notre algorithme pour la TF1R')
                print(ImageTF1R)
                print('--------------------------------------------------')
                print("Résultat de l'algorithme de numpy pour la TF1")
                print(np.fft.fft(Image1D))
                print('--------------------------------------------------')
                ImageTFI1D=TFI1D(ImageTF1D)
                print('Résultat de notre algorithme pour la TFI1D')
                print(ImageTFI1D)
                print('--------------------------------------------------')
                ImageTFI1R=TFI1R(ImageTF1R)
                print('Résultat de notre algorithme pour la TFI1R')
                print(ImageTFI1R)
                print('--------------------------------------------------')
                print("Résultat de l'algorithme de numpy pour la TFI1")
                print(np.fft.ifft(ImageTF1D))
                print('--------------------------------------------------')
            case '2':
                nomImage = input("Saisir le nom de l'image à ouvrir (en .jpg) : ")

                timeStart = time.time()
                TF2D(openImg(nomImage))
                timeEend = time.time()
                timeResDirecte = timeEend - timeStart

                np.savetxt("TF2D/numpy_TF2D.txt", np.fft.fft2(openImg(nomImage)),  fmt="%.2e")
                print('--------------------------------------------------------')
                print("ImageTF2D.jpg, matrice_TF2D.txt, numpy_TF2D.txt créées !")
                print('--------------------------------------------------------')
            case '22':
                nomMatrice = input("Saisir le nom de la matrice à ouvrir (en .txt) : ")
                mat = np.loadtxt(nomMatrice, dtype=complex)
                tfi2d = TFI2D(mat)
                np.savetxt("TF2D/numpy_TFI2D.txt", np.fft.ifft2(mat), fmt="%.1e")
                print('-----------------------------------------------------------')
                print("ImageTFI2D.jpg, matrice_TFI2D.txt, numpy_TFI2D.txt créées !")
                print('-----------------------------------------------------------')
            case '3':
                nomImage = input("Saisir le nom de l'image à ouvrir (en .jpg) : ")

                timeStart = time.time()
                TF2R(openImg(nomImage))
                timeEend = time.time()
                timeResRapide = timeEend - timeStart
                
                np.savetxt("TF2R/numpy_TF2R.txt", np.fft.fft2(openImg(nomImage)), fmt="%.2e")
                print('--------------------------------------------------------')
                print("ImageTF2R.jpg, matrice_TF2R.txt, numpy_TF2R.txt créées !")
                print('--------------------------------------------------------')
        
            case '33':
                nomMatrice = input("Saisir le nom de la matrice à ouvrir (en .txt) : ")
                mat = np.loadtxt(nomMatrice, dtype=complex)
                tfi2r = TFI2R(mat)
                np.savetxt("TF2R/numpy_TFI2R.txt", np.fft.ifft2(mat), fmt="%.1e")
                print('-----------------------------------------------------------')
                print("ImageTFI2R.jpg, matrice_TFI2R.txt, numpy_TFI2R.txt créées !")
                print('-----------------------------------------------------------')
            case _:
                break

            
main()