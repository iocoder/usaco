/*
ID: iocoder1
LANG: C
TASK: pprime
*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

FILE *fin, *fout;
int primes[10000];
int pcount = 0;
int a, b;

int compareInt(const void * a, const void * b) {
  if ( *(int*)a <  *(int*)b ) return -1;
  if ( *(int*)a == *(int*)b ) return 0;
  if ( *(int*)a >  *(int*)b ) return 1;
}

void isPrime(int n) {
    int rn = sqrt(n)+0.5;
    int i;
    if (n > 1 && n >= a && n <= b) {
        for (i = 2; i <= rn; i++) {
            if (!(n%i))
                return;
        }
        primes[pcount++] = n;
    }
}

void genPal(int left, int right, int offset, int digits) {
    int i;
    int nleft, nright, noffset, ndigits;
    int pal;
    if (digits) {
        nleft   = left*100;
        nright  = right;
        noffset = offset*10;
        ndigits = digits-1;
        isPrime(left/10 + right);
        for (i = 0; i <= 9; i++) {
            if (i || left) {    
                isPrime(left + i*offset + nright);
                genPal(nleft+i*noffset*10, nright+i*offset, noffset, ndigits);
            }
        }
    }
}

int main() {
    int i;
    /* open files */
    fin = fopen("pprime.in", "r");
    fout = fopen("pprime.out", "w");
    /* read a and b */
    fscanf(fin, "%d%d", &a, &b);
    /* generate palindromes */
    genPal(0, 0, 1, 4);
    /* sort them */
    qsort(primes, pcount, sizeof(primes[0]), compareInt);
    /* print them */
    for (i = 0; i < pcount; i++)
        fprintf(fout, "%d\n", primes[i]);
    /* close files */
    fclose(fin);
    fclose(fout);
    /* done */
    return 0;
}
