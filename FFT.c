#include <stdio.h>
#include <stdlib.h>
#include <complex.h>
#include <math.h>

const double Image1D[]={30,20,10,12,5};

const double Image2D[3][3]={
    {0.1,0.8,1},
    {0.3,0.5,0.7},
    {0.4,0.7,0.9}
    };

void T1D();
void T1DInverse();
void T2D();
void T2DInverse();
void AfficherMatric1D(double complex Image[], int size);

int main(int argc, char const *argv[])
{
    int choix;   

    printf("Choisir la transformee de fourrier a utiliser : \n (1)  1D\n (11) 1D Inverse\n (2)  2D\n (22) 2D Inverse\n");
    //scanf("%d",&choix);
    choix=1;
    switch(choix)
    {
        case 1:
            T1D();
            break;

        case 11:
            T1DInverse();
            break;

        case 2:
            T2D();
            break;

        case 22:
            T2DInverse();
            break;

        default:
            printf("Choix incorrect\n");
    }   
    return 0;
}

void T1D(){
    int N=sizeof(Image1D)/sizeof(double);
    double complex ImageRes[N];

    for(int u=0;u<N-1;u++)
    {      
        double sum=0; 
        double complex z;     
        for(int x=0;x<N-1;x++)
        {
            z = (-2 * I * M_PI * u * x) / N;
            z+=Image1D[x]*cexp(z);
        }
        ImageRes[u]=z;
    }

   AfficherMatric1D(ImageRes,N);
}

void T1DInverse(){
    
}

void T2D(){
    
}

void T2DInverse(){
    
}

void AfficherMatric1D(double complex Image[], int size)
{
    int N=size;
    for(int i=0;i<N-1;i++)
    {
        if(i==0)
            printf("[%f + %f I, ", creal(Image[i]),cimag(Image[i]));        
        if(i==N-2)
            printf("%f + %f I] ", creal(Image[i]),cimag(Image[i]));        
        else
            printf("%f + %f I, ", creal(Image[i]),cimag(Image[i]));        
    }
}



