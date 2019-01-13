/*
ID: iocoder1
LANG: C
TASK: fracdec
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char str[100000];
int visited[100001];

int main() {
    
    /* declare variables */
    FILE *fin, *fout;
    long long N, D;
    long long digits, factor, part;
    int count = 0, i, j, k;
    int flt = 0, rep = -1;
    int partition, slice, eq;

    /* open files */
    fin  = fopen("fracdec.in", "r");
    fout = fopen("fracdec.out", "w");

    /* read N and D */
    fscanf(fin, "%lld%lld", &N, &D);

    /* initialize visited */
    for (i = 0; i < 100001; i++) {
         visited[i] = -1;
    }

    /* calculate number of digits per computation */
    if (D < 10) {
        digits = 1;
	factor = 10;
    } else if (D < 100) {
        digits = 2;
	factor = 100;
    } else if (D < 1000) {
        digits = 3;
	factor = 1000;
    } else if (D < 10000) {
        digits = 4;
	factor = 10000;
    } else if (D < 100000) {
        digits = 5;
	factor = 100000;
    } else if (D < 1000000) {
        digits = 6;
	factor = 1000000;
    }

    /* loop until N is zero */
    while (N) {
        if (N >= D) {
	    /* print the integral part */
            count += sprintf(&str[count], "%lld", N/D);
	    N = N%D;
	} else {
            /* first, print floating point if not printed */
	    if (!flt) {
		if (count == 0) {
                    count += sprintf(&str[count], "0.");
		} else {
                    count += sprintf(&str[count], ".");
	        }
		flt = 1;
	    }
	    /* visited before? */
            if (visited[N] != -1) {
                /* done */
	        rep = visited[N];
		N = 0;
	    } else {
                /* mark as visited */
		visited[N] = count;
	        /* calculate frac part */
	        part = N*factor/D;
	        /* print it */
	        switch (digits) {
		    case 1:
	    	        count += sprintf(&str[count], "%01lld", part);
	                break;
	            case 2:
	    	       count += sprintf(&str[count], "%02lld", part);
	               break;
		    case 3:
	    	       count += sprintf(&str[count], "%03lld", part);
	               break;
		    case 4:
	    	       count += sprintf(&str[count], "%04lld", part);
	               break;
		    case 5:
	    	       count += sprintf(&str[count], "%05lld", part);
	               break;
		    case 6:
	    	       count += sprintf(&str[count], "%06lld", part);
	               break;
	        }
                /* continue fracting */
	        N = (N*factor)%D;
            }
        }

    }

    /* need floating point? */
    if (!flt) {
        count += sprintf(&str[count], ".0");
    } else {
        /* remove trailing 0s */
	if (rep == -1) {
	    while (str[count-1] == '0') {
                str[--count] = 0;
	    }
	}
    }

    /* has rep? */
    if (rep != -1) {
	/* first, adjust rep */
        while (str[rep-1] == str[count-1]) {
            rep--;
	    str[--count] = 0;
	}
	/* rep could be partitioned? */
	partition = 1;
	while (partition) {
            partition = 0;
            for (i = 2; i <= count-rep; i++) {
		/* not sliceable? */
		if ((count-rep)%i) {
                    continue;
		}
                /* calculate slice size */
                slice  = (count-rep)/i;
		eq = 1;
	        /* compare all slices to first slice */
                for (j = 1; j < i; j ++) {
		    /* comparing slice j to slice 0 */
                    for (k = 0; k < slice; k++) {
                        if (str[rep+k] != str[rep+j*slice+k]) {
                            eq = 0;
			    break;
			}
		    }
		    if (!eq) {
                        break;
		    }
	        }
		if (eq == 1) {
                    partition = i;
		    break;
		}
	    }
	    /* paritition? */
	    if (partition) {
                count = rep + (count-rep)/partition;
		str[count] = 0;
	    }
	}

	/* add ( and ) */
        for (i = count; i > rep; i--) {
             str[i] = str[i-1];
	}
	count = count + 2;
	str[rep] = '(';
	str[count-1] = ')';
	str[count] = 0;
    }

    /* print the number */
    for (i = 0; i < count; i++) {
	 if (i > 0 && !(i%76)) {
             fprintf(fout, "\n");
	 }
         fprintf(fout, "%c", str[i]);
    }
    fprintf(fout, "\n");

    /* close files */
    fclose(fin);
    fclose(fout);

    /* done */
    return 0;

}
