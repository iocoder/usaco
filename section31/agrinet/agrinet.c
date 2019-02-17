/*
ID: iocoder1
LANG: C
TASK: agrinet
*/

#include <stdio.h>
#include <stdlib.h>

/* maximum possible weight */
#define INF 100001

/* a graph node */
typedef struct node {
    int source;   /* parent node in the tree */
    int distance; /* current distance from tree */
    int intree;   /* in tree or not? */
} node_t;

/* the graph */
node_t *nodes;
int **weights;
int node_count;

/* solution of MST */
int tree_size;
int tree_weight;

/* initialize the graph based on its size */
void init_graph(int N) {
    
    /* local variables */
    int i, j;

    /* store N */
    node_count = N;

    /* allocate nodes */
    nodes = malloc(sizeof(node_t) * node_count);

    /* initialize nodes */
    for (i = 0; i < node_count; i++) {
        nodes[i].source   = -1;
	nodes[i].distance = INF;
	nodes[i].intree   = 0;
    }

    /* allocate adjacency matrix */
    weights = malloc(sizeof(int *) * node_count);
    for (i = 0; i < node_count; i++) {
        weights[i] = malloc(sizeof(int) * node_count);
	for (j = 0; j < node_count; j++) {
            weights[i][j] = INF;
	}
    }

    /* initialize MST vars */
    tree_size = 0;
    tree_weight = 0;

}

/* set weight of edge(src,dst) */
void set_weight(int src, int dst, int weight) {

    /* update adjacency matrix */
    weights[src][dst] = weight;

}

/* execute Prim's algorithm */
int run_prim() {

    /* loop counters */
    int i, curnode, curdist;

    /* start with one node */
    tree_size = 1;
    tree_weight = 0;

    /* choose first node as root of the tree */
    nodes[0].source = -1;
    nodes[0].distance = 0;
    nodes[0].intree = 1;

    /* update its neightbours */
    for (i = 1; i < node_count; i++) {
        /* update distance */
	nodes[i].source = 0;
	nodes[i].distance = weights[0][i];
    }

    /* keep looping until we have all nodes in MST */
    while (tree_size < node_count) {

        /* find node with smallest distance */
	curdist = INF;
        for (i = 0; i < node_count; i++) {
            if (nodes[i].intree == 0 && nodes[i].distance < curdist) {
                curdist = nodes[i].distance;
		curnode = i;
	    }
	}

	/* update MST parameters */
	tree_size++;
	tree_weight += curdist;

	/* insert node into tree */
	nodes[curnode].intree = 1;

	/* update neighbors */
	for (i = 0; i < node_count; i++) {
             if (nodes[i].intree == 0) {
                 if (nodes[i].distance > weights[curnode][i]) {
                     nodes[i].distance = weights[curnode][i];
		     nodes[i].source   = curnode;
		 }
	     }
	}

    }

    /* return MST weight */
    return tree_weight;

}

/* main function */
int main() {
    
    /* declare variables */
    FILE *fin, *fout;
    int N, i, j, w, res;

    /* open files */
    fin  = fopen("agrinet.in", "r");
    fout = fopen("agrinet.out", "w");
    
    /* read N */
    fscanf(fin, "%d", &N);

    /* initialize graph */
    init_graph(N);

    /* read adjacency matrix */
    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
            fscanf(fin, "%d", &w);
	    set_weight(i, j, w);
	}
    }

    /* run Prim's algorithm */
    res = run_prim();

    /* print result */
    fprintf(fout, "%d\n", res);

    /* close files */
    fclose(fin);
    fclose(fout);

    /* done */
    return 0;

}
