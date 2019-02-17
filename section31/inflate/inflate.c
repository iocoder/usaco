/*
ID: iocoder1
LANG: C
TASK: inflate
*/

#include <stdio.h>
#include <stdlib.h>

/* main function */
int main() {
    
    /* declare variables */
    FILE *fin, *fout;
    int M, N, i, j;
    int *dp;
    int *Cp, *Cm;

    /* open files */
    fin  = fopen("inflate.in", "r");
    fout = fopen("inflate.out", "w");
    
    /* read M (contest length), N (number of classes) */
    fscanf(fin, "%d%d", &M, &N);

    /* initialize dynamic programming memory */
    dp = malloc(sizeof(int) * (M+1));
    for (i = 0; i <= M; i++) {
        dp[i] = 0; /* all contest length scores are zeros */
    }

    /* allocate classes stores */
    Cp = malloc(sizeof(int) * N);
    Cm = malloc(sizeof(int) * N);

    /* read initial inputs */
    for (i = 0; i < N; i++) {
        fscanf(fin, "%d%d", &Cp[i], &Cm[i]);
	if (Cm[i] <= M) {
            if (Cp[i] > dp[Cm[i]]) {
                dp[Cm[i]] = Cp[i];
	    }
	}
    }

    /* loop over dp entries */
    for (i = 0; i <= M; i++) {
	/* possible contest size? */
        if (dp[i] != 0) {
            /* dp[i] is the highest score of contest length i,
	     * try to combine two contests together (i+j)
	     * update the scores of the new contest
	     */
            for (j = 0; j <= i; j++) {
                if (i + j <= M) {
                    /* better score? */
		    if (dp[i] + dp[j] > dp[i+j]) {
                        dp[i+j] = dp[i] + dp[j]; 
		    }
		}
	    }
	}
    }

    /* print score of contest length M */
    fprintf(fout, "%d\n", dp[M]);

    /* close files */
    fclose(fin);
    fclose(fout);

    /* done */
    return 0;

}
