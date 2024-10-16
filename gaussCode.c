#include<stdlib.h>
#include<stdio.h>
#include<math.h>

double**A;

// Fonction pour allouer de la memoire à une matrice de taille n x m
double** allocationMemoire(int n,int m) {
    int i;
    double **mat;
    mat = (double**)malloc(n * sizeof(double*));
    if (mat == NULL) {
        fprintf(stderr, "Erreur d'allocation de memoire.\n");
        exit(EXIT_FAILURE);
    }
    for(i = 0; i < n; i++) {
        mat[i] = (double*)malloc(m * sizeof(double));
        if (mat[i] == NULL) {
            fprintf(stderr, "Erreur d'allocation de memoire.\n");
            exit(EXIT_FAILURE);
        }
    }
    return mat;
}

void triangularisation(double **A, double *B, int N)
{
    int i, j, k;
    double prod, b_av, a_av, res;
    double**L = malloc(N * sizeof(double*)); // Allouer la mémoire pour les pointeurs de ligne
    for (i = 0; i < N; i++) {
        L[i] = malloc(N * sizeof(double)); // Allouer la mémoire pour chaque ligne
    }

    for (i = 0; i < N-1; i++)
    {
        for (j = i + 1; j < N; j++)
        {
            L[j][i] = A[j][i] / A[i][i]; // Utiliser A[i][i] comme pivot
            b_av = B[j];
            B[j] = b_av - L[j][i] * B[i]; // Mettre à jour le vecteur B parallèlement
            for (k = i; k < N; k++)
            {
                prod = L[j][i] * A[i][k]; // Calculer le produit pour la mise à jour
                a_av = A[j][k];
                res = a_av - prod; // Mettre à jour A[j][k]
                A[j][k] = res;

            }
            A[j][i] = 0; // Explicitement mettre à zéro les éléments sous-diagonaux
        }
    }
}


void resolution(double **A, double *B, double *X, int N) //résolution du système Ax=B
{
	int i, j;
	double somme = 0.0;
    double prodX, som, x_save;
	for(i=N-1;i>=0;i--)
	{
		somme=0;
		for(j=i+1;j<N;j++)
		{
			prodX = A[i][j]*X[j];
            som = somme + prodX;
            somme = som;
		}
		x_save=(B[i]-somme)/A[i][i];
        X[i] = x_save;
	}
}

int main() {
    int N = 4, i;
    double *b, *x;
    A = allocationMemoire(N, N);

    // Initialisation de la matrice de Wilson
    A[0][0]=10.0; A[0][1]=7.0; A[0][2]=8.0; A[0][3]=7.0;
    A[1][0]=7.0; A[1][1]=5.0; A[1][2]=6.0; A[1][3]=5.0;
    A[2][0]=8.0; A[2][1]=6.0; A[2][2]=10.0; A[2][3]=9.0;
    A[3][0]=7.0; A[3][1]=5.0; A[3][2]=9.0; A[3][3]=10.0;

    double c;
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            c = A[i][j];
            //printf("A[%d][%d] = %20.18f ", i,j,A[i][j]); 
        }
        //printf("\n");  // Nouvelle ligne après chaque ligne de la matrice
    }

    printf("\n");

    // Initialisation du vecteur b
    b = (double*)malloc(N * sizeof(double));
    if (b == NULL) {
        fprintf(stderr, "Erreur d'allocation de memoire.\n");
        exit(EXIT_FAILURE);
    }
    b[0] = 32.0; b[1] = 23.0; b[2] = 33.0; b[3] = 31.0;
    for (int i = 0; i < 4; i++) {
        c = b[i];
        //printf("B[%d] = %20.18f ", i,b[i]);
        //printf("\n");
    }
    

    printf("\n");

    x = (double*)malloc(N * sizeof(double)); // Allouez de la mémoire pour x
    if (x == NULL) {
        fprintf(stderr, "Erreur d'allocation de memoire pour x.\n");
        exit(EXIT_FAILURE);
    }

    triangularisation(A, b, N); 
    resolution(A, b, x, N);

    // Affichage des resultats
    for (i = 0; i < N; i++) {
        printf("x[%d]=%20.18f\n", i + 1, x[i]);
    }

    // Liberation de la memoire allouee
    for (i = 0; i < N; i++) {
        free(A[i]);
    }
    free(A);
    free(b);
    free(x);

    return 0;    
}
