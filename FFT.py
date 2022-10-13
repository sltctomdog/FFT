from numbers import Real
import numpy as np
from PIL import Image, ImageOps
import cmath


Image1D = np.array([1, 6, 2, 4])
Image2D = np.array([[0, 0, 0], [1, 1, 1], [0, 0, 0]])

def openImg(nomImage):
    imgRGB = Image.open(nomImage)
    imgGreyscale = ImageOps.grayscale(imgRGB)
    matriceGreyscale = np.asarray(imgGreyscale)
    return matriceGreyscale

def TF1D(Matrice1D):
    
    # Creation d'une matrice de la taille de l'image1D 
    MatriceRes = np.zeros(Matrice1D.shape[0], dtype=complex)
    # On parcours notre matrice initial
    for u in range(Matrice1D.shape[0]):
        sum = 0
        # On applique la formule
        for x in range(Matrice1D.shape[0]):
            sum += Matrice1D[x]*cmath.exp((-2j * cmath.pi * u * x) / Matrice1D.shape[0])
        # On met la valeur dans la matrice resultat + on arrondi les valeurs
        MatriceRes[u]=round(sum.real, 8)+round(sum.imag, 8)*1j
    return MatriceRes

def TFI1D(Matrice1D):
    # Creation d'une matrice de la taille de l'image1D 
    MatriceRes = np.zeros(Matrice1D.shape[0], dtype=complex)
    # On parcours notre matrice initial
    for u in range(Matrice1D.shape[0]):
        sum = 0
        # On applique la formule
        for x in range(Matrice1D.shape[0]):
            sum += Matrice1D[x]*cmath.exp((2j * cmath.pi * u * x) / Matrice1D.shape[0])
        sum /= Matrice1D.shape[0]
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
    np.savetxt("matrice_TF2D.txt", MatriceRes)
    #On créé une matrice de uint8 afin de pas avoir de problème de compatibilité lors de la création de l'image finale
    Matrice = np.zeros((MatriceRes.shape[0], MatriceRes.shape[1]), dtype=np.uint8)
    for i in range (MatriceRes.shape[0]):
        for j in range (MatriceRes.shape[1]):
            Matrice[i][j]=np.abs(MatriceRes[i][j])
    img = Image.fromarray(Matrice)
    img.save("ImageTF2D.jpg")
    return MatriceRes

def TFI2D(Matrice2D):
    # Creation d'une matrice de taille ligne*colonne de l'image2D 
    MatriceRes = np.zeros((Matrice2D.shape[0], Matrice2D.shape[1]), dtype=complex)
    
    # On applique la TFI1D sur toute les lignes de notre image2D
    for i in range(Matrice2D.shape[0]):
        MatriceRes[i] = TFI1D(Matrice2D[i])
        
    # On inverse les lignes et les colonnes
    MatriceRes_trans = MatriceRes.transpose()
    print(MatriceRes_trans)
    # On applique à nouveau la TFI1D sur cette matrice (donc sur les colonnes de notre image2D)
    for i in range(MatriceRes_trans.shape[0]):
        MatriceRes_trans[i] = TFI1D(MatriceRes_trans[i])
    # On remet les lignes à la place des colonnes 
    MatriceRes = MatriceRes_trans.transpose()
    print(MatriceRes)
    #On créé une matrice de uint8 afin de pas avoir de problème de compatibilité lors de la création de l'image finale
    Matrice = np.zeros((MatriceRes.shape[0], MatriceRes.shape[1]), dtype=np.uint8)
    for i in range (MatriceRes.shape[0]):
        for j in range (MatriceRes.shape[1]):
            Matrice[i][j]=MatriceRes[i][j].real
    np.savetxt("matrice_TFI2D.txt", Matrice, fmt="%.1e")
    img = Image.fromarray(Matrice)
    img.save("ImageTFI2D.jpg")
    return MatriceRes

def TF1R(Matrice1D):
    N=Matrice1D.shape[0]
    MatriceRes = np.zeros(N, dtype=complex)
    
    # On parcours notre matrice initial
    for u in range(N):
        sumpair = 0
        sumimpair = 0
        sumres = 0
        if(N%2==0):
            for x in range(int(N/2)):
                sumpair += Matrice1D[2*x]*cmath.exp((-2j * cmath.pi * u * x) / (N/2))        
                sumimpair += Matrice1D[2*x+1]*cmath.exp((-2j * cmath.pi * u * x) / (N/2))
        else:
            for x in range(int((N+1)/2)):
                sumpair += Matrice1D[2*x]*cmath.exp((-2j * cmath.pi * u * x) / (N/2))   
            for x in range(int((N-1)/2)):
                sumimpair += Matrice1D[2*x+1]*cmath.exp((-2j * cmath.pi * u * x) / (N/2))

        sumres = sumpair+cmath.exp((-2j * cmath.pi * u) / N)*sumimpair

        # On met la valeur dans la matrice resultat + on arrondi les valeurs
        MatriceRes[u]=round(sumres.real, 8)+round(sumres.imag, 8)*1j  

    return MatriceRes

def TFI1R(Matrice1D):
    N=Matrice1D.shape[0]
    MatriceRes = np.zeros(N, dtype=complex)
    
    # On parcours notre matrice initial
    for u in range(N):
        sumpair = 0
        sumimpair = 0
        sumres = 0
        if(N%2==0):
            for x in range(int(N/2)):
                sumpair += Matrice1D[2*x]*cmath.exp((2j * cmath.pi * u * x) / (N/2))        
                sumimpair += Matrice1D[2*x+1]*cmath.exp((2j * cmath.pi * u * x) / (N/2))
        else:
            for x in range(int((N+1)/2)):
                sumpair += Matrice1D[2*x]*cmath.exp((2j * cmath.pi * u * x) / (N/2))   
            for x in range(int((N-1)/2)):
                sumimpair += Matrice1D[2*x+1]*cmath.exp((2j * cmath.pi * u * x) / (N/2))

        sumres = sumpair+cmath.exp((-2j * cmath.pi * u) / N)*sumimpair
        sumres /= N

        # On met la valeur dans la matrice resultat + on arrondi les valeurs
        MatriceRes[u]=round(sumres.real, 8)+round(sumres.imag, 8)*1j  

    return MatriceRes

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
    np.savetxt("matrice_TF2R.txt", MatriceRes)
    #On créé une matrice de uint8 afin de pas avoir de problème de compatibilité lors de la création de l'image finale
    Matrice = np.zeros((MatriceRes.shape[0], MatriceRes.shape[1]), dtype=np.uint8)
    for i in range (MatriceRes.shape[0]):
        for j in range (MatriceRes.shape[1]):
            Matrice[i][j]=np.abs(MatriceRes[i][j])
    img = Image.fromarray(Matrice)
    img.save("ImageTF2R.jpg")
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
    np.savetxt("matrice_TFI2R.txt", Matrice, fmt="%.1e")
    img = Image.fromarray(Matrice)
    img.save("ImageTFI2R.jpg")
    return MatriceRes

def main():

    mat = np.loadtxt("matrice_TF2D.txt", dtype=complex)
    print('--------------------------------------------------')
    tfi2d = TFI2D(mat)
    #print(tfi2d)
    print('--------------------------------------------------')
    tfi2R = TFI2R(mat)
    #print(tfi2R)
    print('--------------------------------------------------')
    print("Résultat de l'algorithme de numpy pour la TF2D")
    print(np.fft.ifft2(mat))
    print('--------------------------------------------------')

    """    
    while True:
        print("1. Demonstration de la transformee de Fourrier et de son inverse sur une matrice à une dimension \n2. Transformee de Fourrier discrete à deux dimensions\n22. Transformee de Fourrier inverse discrete a deux dimensions")
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
                print("Résultat de l'algorithme de numpy pour la TF1D")
                print(np.fft.fft(Image1D))
                print('--------------------------------------------------')
                ImageTFI1D=TFI1D(ImageTF1D)
                print('Résultat de notre algorithme pour la TFI1D')
                print(ImageTFI1D)
                print('--------------------------------------------------')
                print("Résultat de l'algorithme de numpy pour la TFI1D")
                print(np.fft.ifft(ImageTF1D))
                print('--------------------------------------------------')
            case '11':
                print('Matrice en entrée')
                print(Image1D)
                print('--------------------------------------------------')
                ImageTF1R=TF1R(Image1D)
                print('Résultat de notre algorithme pour la TF1R')
                print(ImageTF1R)
                print('--------------------------------------------------')
                print("Résultat de l'algorithme de numpy pour la TF1R")
                print(np.fft.fft(Image1D))
                print('--------------------------------------------------')
                ImageTFI1R=TFI1R(ImageTF1R)
                print('Résultat de notre algorithme pour la TFI1R')
                print(ImageTFI1R)
                print('--------------------------------------------------')
                print("Résultat de l'algorithme de numpy pour la TFI1R")
                print(np.fft.ifft(ImageTF1R))
                print('--------------------------------------------------')
            case '2':
                nomImage = input("Saisir le nom de l'image à ouvrir (en .jpg) : ")
                tf2d = TF2D(openImg(nomImage))
                print("ImageTF2D.jpg et matrice_TF2D.txt créées !")
                print('Résultat de notre algorithme pour la TF2D')
                print(tf2d)
                print('--------------------------------------------------')
                print("Résultat de l'algorithme de numpy pour la TF2D")
                print(np.fft.fft2(openImg(nomImage)))
                print('--------------------------------------------------')
            case '22':
                nomMatrice = input("Saisir le nom de la matrice à ouvrir (en .txt) : ")
                mat = np.loadtxt(nomMatrice, dtype=complex)
                tfi2d = TFI2D(mat)
                print("ImageTFI2D.jpg et matrice_TFI2D.txt créées !")
                print('Résultat de notre algorithme pour la TFI2D')
                print(tfi2d)
                print('--------------------------------------------------')
                print("Résultat de l'algorithme de numpy pour la TFI2D")
                print(np.fft.ifft2(mat))
                print('--------------------------------------------------')
            case _:
                break
    """  
main()