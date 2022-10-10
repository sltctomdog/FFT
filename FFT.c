#include <stdio.h>
#include <stdlib.h>
#include <complex.h>
#include <math.h>
#include <string.h>

double Image1D[]={1,6,2,4};

double complex* TF1D(double* mat1D, int dim);
void afficheMat1D(double* mat1D, int dim);
void afficheTF1D(double complex* mat1D, int dim);
double* TFInverse1D(double complex* matTF1D, int dim);

double** getMat2D();
double complex** TF2D(double** mat2D, int dim); 
void afficheMat2D(double** mat2D, int dim);
//void afficheTF2D(double complex** mat2D, int dim);


int main(int argc, char const *argv[])
{
    double complex* matTF1D;
    double* mat1D;
    double** mat2D;
    int choix;   
    //printf("Choisir la transformee de fourrier a utiliser : \n (1)  1D\n (11) 1D Inverse\n (2)  2D\n (22) 2D Inverse\n");
    //scanf("%d",&choix);
    choix=2;
    switch(choix)
    {
        case 1:        
            afficheMat1D(Image1D, 4); 
            matTF1D = TF1D(Image1D, 4);
            afficheTF1D(matTF1D, 4);
            free(matTF1D);
            break;

        case 11:
            afficheMat1D(Image1D, 4); 
            matTF1D = TF1D(Image1D, 4);
            afficheTF1D(matTF1D, 4);
            mat1D = TFInverse1D(matTF1D, 4);
            afficheMat1D(mat1D, 4);
            free(matTF1D);
            free(mat1D);
            break;

        case 2:
            mat2D = getMat2D();
            afficheMat2D(mat2D, 3);
            break;

        case 22:
            //TFInverse2D();
            break;

        default:
            printf("Choix incorrect\n");
    }   
    return 0;
}

double complex** TF2D(double** mat2D, int dim){

    double complex** matTF2D = (double complex**)malloc((dim)*sizeof(double complex*));
    for(int i=0;i<dim;i++){
        double complex* ligne = (double complex*)calloc(dim, sizeof(double complex*));    
    } 

    double complex sum;

    for(int k=0;k<dim;k++){
        for(int l=0;l<dim;l++){
            sum=0;
            for(int m=0;m<dim;m++){
                for(int n=0;n<dim;n++){
                    sum+=mat2D[m][n]*cexp(-2 * I * M_PI * ((k*m/dim) + (l*n/dim)));
                }
            }
            matTF2D[k][l]=sum;
        }
    }
    return matTF2D;
}

void afficheMat2D(double** mat2D, int dim){
    printf("[ ");
    for(int i=0;i<dim;i++){
        for(int j=0;j<dim;j++){
            printf("%.02f, ", mat2D[i][j]);
        }
        printf("\n");
    }
    printf(" ]\n");
}

double** getMat2D(){
    int dim = 3;
    double** mat2D = (double**)malloc(3*sizeof(double*));
    for(int i=0;i<dim;i++){
        double* ligne = (double*)malloc(3*sizeof(double*));    
    } 
    printf("azeffeza\n");
    mat2D[0][0] = 0.00; 
    mat2D[0][1] = 0.00; 
    mat2D[0][2] = 0.00;
    mat2D[1][0] = 1.00; 
    mat2D[1][1] = 1.00; 
    mat2D[1][2] = 1.00;  
    return mat2D;
}

double complex* TF1D(double* mat1D, int dim){

    double complex* matTF1D = (double complex*) malloc(dim*sizeof(double complex));

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


double* TFInverse1D(double complex* matTF1D, int dim)
{
    double* mat1D = (double*) malloc(dim*sizeof(double));

    //Notre somme
    double sum;

    //On parcours notre tableau initial
    for(int u=0;u<dim;u++)
    {     
        sum=0;   
        //On applique la formule 
        for(int x=0;x<dim;x++)
        {
            sum+=matTF1D[x]*cexp((2 * I * M_PI * u * x) / dim);
        }
        mat1D[u]=sum;
    }
    return mat1D;
}

void afficheMat1D(double* mat1D, int dim){
    printf("[");
    for(int i=0;i<dim;i++){
        printf("%.2f, ", mat1D[i]);
    }
    printf(" ]\n");
}



void TFInverse2D(){
    
}



