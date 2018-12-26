/*
ID: iocoder1
LANG: C
TASK: ariprog
*/

#include <stdio.h>
#include <stdlib.h>

char isBi[250*250*3];
int  bisquares[250*250*3];
int  bcount = 0;
int  bmax = 0;

int compareInt (const void * a, const void * b)
{
  if ( *(int*)a <  *(int*)b ) return -1;
  if ( *(int*)a == *(int*)b ) return 0;
  if ( *(int*)a >  *(int*)b ) return 1;
}

int main() {

    FILE *fin, *fout;
    int N, M;
    int i, j;
    int a, b, n;
    int total;

    /* open files */
    fin = fopen("ariprog.in", "r");
    fout = fopen("ariprog.out", "w");
    if (!fin) {
        fprintf(stderr, "cannot open input file\n");
        return -1;
    }
    if (!fout) {
        fprintf(stderr, "cannot open output file\n");
        return -1;
    }

    /* read N and M */
    fscanf(fin, "%d%d", &N, &M);

    /* construct array of bisquares */
    for (i = 0; i < M+1; i++) {
        for (j = 0; j < M+1; j++) {
            /* calculate the bisquare */
            b = i*i + j*j;
            /* reset bmax */
            if (b > bmax) {
                bmax = b;
            }
            /* add to the array */
            if (!isBi[b]) {
                isBi[b] = 1;
                bisquares[bcount] = b;
                bcount++;
            }
        }
    }

    /* sort */
    qsort(bisquares, bcount, sizeof(bisquares[0]), compareInt);

    /* loop over every pair in bisquares */
    total = 0;
    for (b = 1; b <= bmax; b++) {
        for (i = 0; i < bcount && bisquares[i]+b*(N-1) <= bmax; i++) {
            a = bisquares[i];
            if (!isBi[a+b])
                continue;
            for (n = 2; n < N && isBi[a+b*n]; n++);
            if (n == N) {
                /* we found a bisquare progression! */
                fprintf(fout, "%d %d\n", a, b);
                total++;
                if (total == 10000)
                    break;
            }
        }
        if (total == 10000)
            break;
    }
    if (!total)
        fprintf(fout, "NONE\n");

    /* close files */
    fclose(fin);
    fclose(fout);

    /* we are done */
    return 0;
}

