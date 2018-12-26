/*
ID: iocoder1
LANG: C
TASK: money
*/

#include <stdio.h>
#include <stdlib.h>

/* recursive solution */
long long recSol(int *coinVec, int *coins, int curCoin, int coinCount, int rem, long long **dp) {
    /* declare variables */
    long long count = 0;
    int maxQu, i, newRem;
    /* solved before? */
    if (dp[curCoin][rem] != -1) {
        count = dp[curCoin][rem];
    } else {
        /* base case? */
        if (curCoin == coinCount) {
            count = (rem == 0); /* count if valid combination */
        } else {
            /* how many coins can be consumed? */
            maxQu = rem/coins[curCoin];
            newRem = rem;
            /* loop over all possible quantities */
            for (i = 0; i <= maxQu; i++) {
                coinVec[curCoin] = i;
                count += recSol(coinVec, coins, curCoin+1, coinCount, newRem, dp);
                newRem -= coins[curCoin];
            }
            /* reset */
            coinVec[curCoin] = 0;
        }
        /* store result */
        dp[curCoin][rem] = count;
    }
    /* done */
    return count;
}

int main() {
    /* declare vars */
    FILE *fin, *fout;
    int V, N, i, j;
    int *coins, *coinVec;
    long long res;
    long long **dp;
    /* open files */
    fin  = fopen("money.in", "r");
    fout = fopen("money.out", "w");
    /* read N and V */
    fscanf(fin, "%d%d", &V, &N);
    /* read coins */
    coins = (int *) malloc(sizeof(int)*V);
    for (i = 0; i < V; i++) {
        fscanf(fin, "%d", &coins[V-i-1]);
    }
    /* coin vector */
    coinVec = (int *) malloc(sizeof(int)*V);
    for (i = 0; i < V; i++) {
        coinVec[i] = 0;
    }
    /* dynamic programming */
    dp = (long long **) malloc(sizeof(int *)*(V+1));
    for (i = 0; i <= V; i++) {
        dp[i] = (long long *) malloc(sizeof(long long)*(N+1));
        for (j = 0; j <= N; j++) {
            dp[i][j] = -1;
        }
    }        
    /* solve */
    res = recSol(coinVec, coins, 0, V, N, dp);
    /* write solution */
    fprintf(fout, "%lld\n", res);
    /* close files */
    fclose(fin);
    fclose(fout);
    /* done */
    return 0;
}
