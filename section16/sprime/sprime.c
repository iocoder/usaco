/*
ID: iocoder1
LANG: C
TASK: sprime
*/

#include <stdio.h>
#include <math.h>

int isPrime(int n) {
    int rn = sqrt(n)+0.5;
    int i;
    if (n < 2)
        return 0;
    for (i = 2; i <= rn; i++) {
        if (!(n%i))
            return 0;
    }
    return 1;
}

void genSPrime(int n, int digits, FILE *f) {
    int i, nn, ndigits;
    if (digits) {
        nn = n*10-1;
        ndigits = digits - 1;
        for (i = 0; i <= 9; i++)
            if (isPrime(++nn))
                genSPrime(nn, ndigits, f);
    } else {
        /* just print the number */
        fprintf(f, "%d\n", n);
    }
}

int main() {
    FILE *fin, *fout;
    int n;
    /* open files */
    fin = fopen("sprime.in", "r");
    fout = fopen("sprime.out", "w");
    /* read n */
    fscanf(fin, "%d", &n);
    /* generate numbers */
    genSPrime(0, n, fout);
    /* close files */
    fclose(fin);
    fclose(fout);
    /* done */
    return 0;
}
