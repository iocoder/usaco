/*
ID: iocoder1
LANG: C++
TASK: humble
*/

#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <bits/stdc++.h>

/* define infinity */
#define INF LLONG_MAX

/* define integer */
typedef long long int_t; 

/* use namespace std for set */
using namespace std;

/* implementation of min-max heap */
typedef struct minmax_heap {

    /* self-balancing binary search tree */
    set<int_t> avl;

    /* heap size() operation: O(1) */
    int_t size() {
        return avl.size();
    }

    /* heap isEmpty() operation: O(1) */
    bool isEmpty() {
        return avl.size() == 0;
    }

    /* heap insert() operation: O(log N) */
    void insert(int_t n) {
        avl.insert(n);
    }

    /* heap getMin() operation: O(1) */
    int_t getMin() {
        return *(avl.begin());
    }

    /* heap getMax() operation: O(1) */
    int_t getMax() {
        return *(avl.rbegin());
    }

    /* heap delMin() operation: O(log N) */
    void delMin() {
        avl.erase(avl.begin());
    }

    /* heap delMax() operation: O(log N) */
    void delMax() {
        auto itr = avl.end();
        itr--;
        avl.erase(itr);
    }

} minmax_heap_t;

/* main function */
int main() {
    
    /* declare variables */
    FILE *fin, *fout;
    int_t N, K, i, num, new_num, max, rank;
    minmax_heap_t heap;
    int_t *primes;

    /* open files */
    fin  = fopen("humble.in", "r");
    fout = fopen("humble.out", "w");

    /* read K and N */
    fscanf(fin, "%lld%lld", &K, &N);
 
    /* initialize the heap */
    heap.insert(1);

    /* initialize primes array */
    primes = (int_t *) malloc(sizeof(int_t) * K);

    /* read the primes */
    for (i = 0; i < K; i++) {
        fscanf(fin, "%lld", &primes[i]);
    }

    /* loop until rank is N */
    rank = 0;
    while (rank <= N) {
        num = heap.getMin();
        max = heap.getMax();
        heap.delMin();
        rank++;
        for (i = 0; i < K; i++) {
            new_num = num*primes[i];
            if (heap.size() == N-rank+2) {
                if (new_num < max) {
                    heap.delMax();
                    heap.insert(new_num);
                    max = heap.getMax();
                }
            } else {
                heap.insert(new_num);
            }
        }
    }

    /* print_t result */
    fprintf(fout, "%lld\n", num);

    /* close files */
    fclose(fin);
    fclose(fout);

    /* done */
    return 0;

}
