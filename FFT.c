#include <stdio.h>
#include <stdlib.h>
#include <complex.h>
#include <math.h>
#include <string.h>

int Image1D[]={1,6,2,4};

double Image2D[3][3]={
    {0.1,0.8,1},
    {0.3,0.5,0.7},
    {0.4,0.7,0.9}
    };

double complex* TF1D(int* mat1D, int dim);
void afficheTF1D(double complex* mat1D, int dim);
void TFInverse1D();
void TF2D(); 
void TFInverse2D();

int main(int argc, char const *argv[])
{
    double complex* matTF1D;
    int choix;   
    printf("Choisir la transformee de fourrier a utiliser : \n (1)  1D\n (11) 1D Inverse\n (2)  2D\n (22) 2D Inverse\n");
    scanf("%d",&choix);
    choix=1;
    switch(choix)
    {
        case 1:         
            matTF1D = TF1D(Image1D, 4);
            afficheTF1D(matTF1D, 4);
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

double complex* TF1D(int* mat1D, int dim){

    double complex* matTF1D = (double complex*) malloc(dim*sizeof(double complex));

    //Longueur du tableau
    int N = dim;
    //Notre somme
    double complex sum;

    //On parcours notre tableau initial
    for(int u=0;u<dim;u++)
    {     
        sum=0;   
        //On applique la formule 
        for(int x=0;x<dim;x++)
        {
            sum+=mat1D[x]*cexp((-2 * I * M_PI * u * x) / dim);
        }
        matTF1D[u]=sum;
    }
    return matTF1D;
}

void afficheTF1D(double complex* mat1D, int dim){
    //Affichage Matrice
    printf("[ ");
    for(int i=0;i<dim;i++)
    {       
        if(cimag(mat1D[i])<0)
            printf("(%.2f%.2fi), ",creal(mat1D[i]),cimag(mat1D[i]));      
        else
            printf("(%.2f+%.2fi), ",creal(mat1D[i]),cimag(mat1D[i]));         
   }
   printf("]\n");
}


void TFInverse1D(){
    
}

void TF2D(){
    
}

void TFInverse2D(){
    
}



