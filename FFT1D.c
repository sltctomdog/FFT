#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
    int choix;
    int Image;    
    int ImageTest[3][3]={
        {0.1,0.8,1},
        {0.3,0.5,0.7},
        {0.4,0.7,0.9}
    };

    if(argc=1)
        Image=ImageTest;
    
    else
    {
        char lienImage[]=argv[1];
    } 

    printf("Choisir la transformee de fourrier a utiliser : \n (1)  1D\n (11) 1D Inverse\n (2)  2D\n (22) 2D Inverse\n");
    scanf("%d",&choix);

    switch(choix)
    {
        case 1:
            T1D(Image);
            break;

        case 11:
            T1DInverse(Image);
            break;

        case 2:
            T2D(Image);
            break;

        case 22:
            T2DInverse(Image);
            break;

        default:
            printf("Choix incorrect");
    }   
    return 0;
}

void T1D(int Image){

}

void T1DInverse(int Image){
    
}

void T2D(int Image){
    
}

void T2DInverse(int Image){
    
}
