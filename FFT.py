from pickle import TRUE
import numpy as np
import cmath

Image1D = [1, 6, 2, 4]
Image2D = [[1, 2, 4, 14], [5, 2, 14, 12], [4, 4, 88, 2], [11, 4, 2, 15]]

def TF1D(Image1D):
    
    # Notre tableau de retour
    ImageRes = []
    # La longueur de notre tableau
    N=len(Image1D)

    # On parcours notre tableau initial
    for u in range(N):
        sum = 0
        # On applique la formule
        for x in range(N):
            sum += Image1D[x]*cmath.exp((-2j * cmath.pi * u * x) / N)
        # On met la valeur dans le tableau
        ImageRes.append(sum)

    return [round(value.real, 8)+round(value.imag, 8)*1j for value in ImageRes]

def TFI1D(Image1D):
    return 0

def TF2D(Image2D):
    return 0

def TFI2D(Image2D):
    return 0

def main():

    while True:
        choix = input("Choisir la transformee de fourrier a utiliser : \n (1)  1D\n (11) 1D Inverse\n (2)  2D\n (22) 2D Inverse\n")
        
        print('Tableau des entrées')
        print(Image1D)
        print('--------------------------------------------------')

        match choix:
            case '1':
                ImageTransforme=TF1D(Image1D)
                print('Résultat de notre algorithme')
                print(ImageTransforme)
                print('--------------------------------------------------')
                print("Résultat de l'algorithme de numpy")
                A =  np.fft.fft(Image1D)
                print(A)
                print('--------------------------------------------------')
            case 11:
                TFI1D(Image1D)
            case 2:
                TF2D(Image2D)
            case 22:
                TFI2D(Image2D)
            case _:
                print("Choix incorrect\n")
                break
        
main()