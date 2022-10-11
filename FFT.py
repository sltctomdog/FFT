from numbers import Real
import numpy as np
import cmath


Image1D = np.array([1, 6, 2, 4])
Image2D = np.array([[0, 0, 0], [1, 1, 1], [0, 0, 0]])

def TF1D(Image1D):
    
    # Creation d'une matrice de la taille de l'image1D 
    MatriceRes = np.zeros(Image1D.shape[0], dtype=complex)
    # On parcours notre matrice initial
    for u in range(Image1D.shape[0]):
        sum = 0
        # On applique la formule
        for x in range(Image1D.shape[0]):
            sum += Image1D[x]*cmath.exp((-2j * cmath.pi * u * x) / Image1D.shape[0])
        # On met la valeur dans la matrice + on arrondi les valeurs
        MatriceRes[u]=round(sum.real, 8)+round(sum.imag, 8)*1j
    return MatriceRes

def TFI1D(ImageTransforme):
    # Creation d'une matrice de la taille de l'image1D 
    MatriceRes = np.zeros(Image1D.shape[0], dtype=complex)

    # On parcours notre matrice initial
    for u in range(Image1D.shape[0]):
        sum = 0
        # On applique la formule
        for x in range(Image1D.shape[0]):
            sum += ImageTransforme[x]*cmath.exp((2j * cmath.pi * u * x) / Image1D.shape[0])
        # On met la valeur dans la matrice
        sum /= Image1D.shape[0]
        # On arrondi les valeurs
        MatriceRes[u]=round(sum.real, 8)+round(sum.imag, 8)*1j
    return MatriceRes

def TF2D(Image2D):
    # Creation d'une matrice de taille ligne*colonne de l'image2D 
    MatriceRes = np.zeros((Image2D.shape[0], Image2D.shape[1]), dtype=complex)

    # On applique la TF1D sur toute les lignes de notre image2D
    for i in range(Image2D.shape[0]):
        MatriceRes[i] = TF1D(Image2D[i])
    # On inverse les lignes et les colonnes
    MatriceRes_trans = MatriceRes.transpose()
    # On applique à nouveau la TF1D sur cette matrice (donc sur les colonnes de notre image2D)
    for i in range(MatriceRes_trans.shape[0]):
        MatriceRes_trans[i] = TF1D(MatriceRes_trans[i])
    # On remet les lignes à la place des colonnes 
    MatriceRes = MatriceRes_trans.transpose()
    return MatriceRes


def TFI2D(Image2D):
    return 0

def main():

    while True:
        choix = input("Choisir la transformee de fourrier a utiliser : \n (1)  1D\n (11) 1D Inverse\n (2)  2D\n (22) 2D Inverse\n")
        match choix:
            case '1':
                print('Tableau des entrées')
                print(Image1D)
                print('--------------------------------------------------')
                ImageTF1D=TF1D(Image1D)
                print('Résultat de notre algorithme pour la TF1D')
                print(ImageTF1D)
                print('--------------------------------------------------')
                print("Résultat de l'algorithme de numpy pour la TF1D")
                print(np.fft.fft(Image1D))
                print('--------------------------------------------------')

            case '11':
                print('Tableau des entrées')
                print(Image1D)
                print('--------------------------------------------------')
                ImageTF1D=TF1D(Image1D)
                print('Matrice resultante de la TF1D')
                print(ImageTF1D)
                print('--------------------------------------------------')
                ImageTFI1D=TFI1D(ImageTF1D)
                print('Résultat de notre algorithme pour la TFI1D')
                print(ImageTFI1D)
                print('--------------------------------------------------')
                print("Résultat de l'algorithme de numpy pour la TFI1D")
                print(np.fft.ifft(ImageTF1D))
                print('--------------------------------------------------')

            case '2':
                print('Tableau des entrées')
                print(Image2D)
                print('--------------------------------------------------')
                ImageTF2D=TF2D(Image2D)
                print('Résultat de notre algorithme pour la TF2D')
                print(ImageTF2D)
                print('--------------------------------------------------')
                print("Résultat de l'algorithme de numpy pour la TF2D")
                print(np.fft.fft2(Image2D))
                print('--------------------------------------------------')
            case '22':
                TFI2D(Image2D)
            case _:
                print("Choix incorrect\n")
                break
        
main()