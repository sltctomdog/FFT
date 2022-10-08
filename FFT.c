#include <stdio.h>
#include <stdlib.h>
#include <complex.h>
#include <math.h>

const int Image1D[]={1,6,2,4};

const double Image2D[3][3]={
    {0.1,0.8,1},
    {0.3,0.5,0.7},
    {0.4,0.7,0.9}
    };

void TF1D();
void TFInverse1D();
void TF2D(); 
void TFInverse2D();

int main(int argc, char const *argv[])
{
    int choix;   

    printf("Choisir la transformee de fourrier a utiliser : \n (1)  1D\n (11) 1D Inverse\n (2)  2D\n (22) 2D Inverse\n");
    scanf("%d",&choix);
    choix=1;
    switch(choix)
    {
        case 1:
            TF1D();
            break;

        case 11:
            TFInverse1D();
            break;

        case 2:
            TF2D();
            break;

        case 22:
            TFInverse2D();
            break;

        default:
            printf("Choix incorrect\n");
    }   
    return 0;
}

void TF1D(){
    //Longueur du tableau
    unsigned short N = *(&Image1D + 1) - Image1D;
    //Notre tableau vide de retour
    double complex ImageRes[N];
    //Notre somme
    double complex sum;

    //On parcours notre tableau initial
    for(int u=0;u<N;u++)
    {     
        sum=0;   
        //On applique la formule 
        for(int x=0;x<N;x++)
        {
            sum+=Image1D[x]*cexp((-2 * I * M_PI * u * x) / N);
        }
        ImageRes[u]=sum;
    }

    //Affichage Matrice
    printf("[ ");
    for(int i=0;i<N;i++)
    {       
        if(cimag(ImageRes[i])<0)
            printf("(%.2f%.2fi), ",creal(ImageRes[i]),cimag(ImageRes[i]));      
        else
            printf("(%.2f+%.2fi), ",creal(ImageRes[i]),cimag(ImageRes[i]));         
   }
   printf("]\n");
}

void TFInverse1D(){
    
}

void TF2D(){
    
}

void TFInverse2D(){
    
}



