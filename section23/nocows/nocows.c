/*
ID: iocoder1
LANG: C
TASK: nocows
*/

#include <stdio.h>

#define K 100
#define N 200
#define MODU 9901

/* RECURRENCE RELATION:
 *
 * NO OF TRESS OF (N nodes, K levels) =
 *   TAKE 1 NODE AS ROOT
 *   Possible childrens:
 *    subtree(1)    subtree(N-2)
 *    subtree(2)    subtree(N-3)
 *           ....
 *    subtree(N-2)  subtree(1)
 *   For each possible pair of subtrees(i,N-1-i), calculate the following:
 *     <PART 1>
 *     no_of_trees(i nodes, K-1 levels)*no_of_trees(N-1-i nodes, K-2 levels)
 *   + no_of_trees(i nodes, K-1 levels)*no_of_trees(N-1-i nodes, K-3 levels)
 *   + no_of_trees(i nodes, K-1 levels)*no_of_trees(N-1-i nodes, K-4 levels)
 *          ...
 *   + no_of_trees(i nodes, K-1 levels)*no_of_trees(N-1-i nodes,   1 level )
 *      + 
 *     <PART 2>
 *     no_of_trees(i nodes, K-2 levels)*no_of_trees(N-1-i nodes, K-1 levels)
 *   + no_of_trees(i nodes, K-3 levels)*no_of_trees(N-1-i nodes, K-1 levels)
 *   + no_of_trees(i nodes, K-4 levels)*no_of_trees(N-1-i nodes, K-1 levels)
 *          ...
 *   + no_of_trees(i nodes,   1 level )*no_of_trees(N-1-i nodes, K-1 levels)
 *      +
 *     <PART 3>
 *     no_of_trees(i nodes, K-1 levels)*no_of_trees(N-1-i nodes, K-1 levels)
 *
 *   The result of the summation of the three parts is the no of trees that should be returned
 *
 *   This can be done in a forward-dynamic programming fashion: start at 1,1
 */

int main() {
    
    /* declare variables */
    int dp[K+1][N+1] = {0}; /* dp[k][n]: no of trees of n nodes, k levels */
    int agg[K+1][N+1] = {0}; /* agg[k][n]: total no of trees of n nodes, 1-->k levels */
    int i, k, n, left_n, right_n;
    int tot_count;
    FILE *fin, *fout;
    
    /* first level can consist of only 1 node */
    dp[1][1] = 1;
    for (i = 1; i <= K; i++) {
        agg[i][1] = 1;
    }

    /* for each level k, apply the recurrence: */
    for (k = 2; k <= K; k++) {
        for (n = 3; n <= N; n++) {
            tot_count = 0;
            /* loop over possible divisions: */
            for (i = 1; i < n-1; i++) {
                left_n = i;
                right_n = n-1-i;
                /* PART1: left_k=k-1, right_k=1-->k-2 */
                tot_count = (tot_count + dp[k-1][left_n]*agg[k-2][right_n])%MODU;
                /* PART2: left_k=1-->k-2, right_k=k-1 */
                tot_count = (tot_count + agg[k-2][left_n]*dp[k-1][right_n])%MODU;
                /* PART3: left_k=k-1, right_k=k-1 */
                tot_count = (tot_count + dp[k-1][left_n]*dp[k-1][right_n])%MODU;
            }
            /* store count */
            dp[k][n] = tot_count;
            for (i = k; i <= K; i++) {
                agg[i][n] = (agg[i][n] + tot_count)%MODU;
            }
        }
    }
    
    /* open files */
    fin  = fopen("nocows.in", "r");
    fout = fopen("nocows.out", "w");
    
    /* read n & k */
    fscanf(fin, "%d%d", &n, &k);
    
    /* output dp[k][n] */
    fprintf(fout, "%d\n", dp[k][n]);

    /* close files */
    fclose(fin);
    fclose(fout);

    /* done */
    return 0;

}
