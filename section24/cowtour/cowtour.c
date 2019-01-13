/*
ID: iocoder1
LANG: C
TASK: cowtour
*/

#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <math.h>

#define INF 1e20
typedef double dist_t;

typedef struct node {
    int x;
    int y;
    dist_t diam;
    dist_t sdiam;
} node_t;

node_t *nodes;
dist_t **edges;
dist_t **spath;
int node_count;

void init_graph(int N) {

    /* local vars */
    int i, j;

    /* store N */
    node_count = N;

    /* initialize the graph */
    nodes = malloc(sizeof(node_t) * N);
    for (i = 0; i < N; i++) {
         nodes[i].x = 0;
	 nodes[i].y = 0;
    }

    /* create edge matrix */
    edges  = malloc(sizeof(dist_t *) * N);
    spath  = malloc(sizeof(dist_t *) * N);
    for (i = 0; i < N; i++) {
         edges[i]  = malloc(sizeof(dist_t) * N);
	 spath[i]  = malloc(sizeof(dist_t) * N);
	 for (j = 0; j < N; j++) {
              if (i == j) {
                  edges[i][j] = 0;
	      } else {
                  edges[i][j] = INF;
	      }
	      spath[i][j] = INF;
	 }
    }

}

void set_node(int i, int x, int y) {

    /* set node coordinates */
    nodes[i].x = x;
    nodes[i].y = y;

}

void add_edge(int i, int j) {

    /* local vars */
    double dx, dy, dist;

    /* calculate distance components */
    dx = (double) (nodes[i].x - nodes[j].x);
    dy = (double) (nodes[i].y - nodes[j].y);
    dist = sqrt(dx*dx + dy*dy);

    /* add edge between i and j */
    edges[i][j] = (dist_t) dist;

}

dist_t get_edge(int i, int j) {

    /* return edge value */
    return edges[i][j];

}

void del_edge(int i, int j) {

    /* delete edge between i and j */
    edges[i][j] = INF;

}

void floyd_warshall() {

    /* run floyd-warshall algorithm */
    int i, j, k;

    /* copy edges into spath */
    for (i = 0; i < node_count; i++) {
        for (j = 0; j < node_count; j++) {
             spath[i][j] = edges[i][j];
	}
    }

    /* the algorithm */
    for (k = 0; k < node_count; k++) {
        for (i = 0; i < node_count; i++) {
             for (j = 0; j < node_count; j++) {
                  if (spath[i][j] > spath[i][k] + spath[k][j]) {
                      spath[i][j] = spath[i][k] + spath[k][j];
		  }
	     }
	}
    }

}

void compute_diams() {

    /* local vars */
    int i, j;

    /* compute diameters for each node */
    for (i = 0; i < node_count; i++) {
        nodes[i].diam = 0;
	for (j = 0; j < node_count; j++) {
             if (spath[i][j] < INF && spath[i][j] > nodes[i].diam) {
                 nodes[i].diam = spath[i][j];
	     }
	}
    }

    /* compute subgraph diameters */
    for (i = 0; i < node_count; i++) {
        nodes[i].sdiam = 0;
	for (j = 0; j < node_count; j++) {
             if (spath[i][j] < INF) {
		 if (nodes[j].diam > nodes[i].sdiam) {
                     nodes[i].sdiam = nodes[j].diam;
		 }
	     }
	}
    }

}

double get_max(double a, double b, double c) {

    /* get max of a, b, and c */
    if (a > b && a > c) {
        return a;
    } else if (b > a && b > c) {
        return b;
    } else {
        return c;
    }

}

dist_t get_shortest(int i, int j) {

    /* get shortest path between i and j */
    return spath[i][j];

}

int main() {
    
    /* declare variables */
    FILE *fin, *fout;
    int N, x, y, i, j;
    char e;
    dist_t d, min = INF;

    /* open files */
    fin  = fopen("cowtour.in", "r");
    fout = fopen("cowtour.out", "w");
    
    /* read N */
    fscanf(fin, "%d", &N);
    init_graph(N);

    /* read nodes */ 
    for (i = 0; i < N; i++) {
	fscanf(fin, "%d%d", &x, &y);
        set_node(i, x, y);
    }

    /* read adjacency matrix */
    for (i = 0; i < N; i++) {
        fscanf(fin, " ");
	for (j = 0; j < N; j++) {
             fscanf(fin, "%c", &e);
             if (e == '1') {
		 add_edge(i, j);
	     }
	}
    }

    /* run floyd warshall once */
    floyd_warshall();

    /* compute diameters */
    compute_diams();

    /* try to add edge between each unconnected pair */
    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
             if (get_shortest(i, j) == INF) {
                 /* add edge */
		 add_edge(i, j);
		 /* new diameter */
		 d = nodes[i].diam + get_edge(i, j) + nodes[j].diam;
		 d = get_max(nodes[i].sdiam, nodes[j].sdiam, d);
		 /* minimum? */
		 if (d < min) {
                     min = d;
		 }
		 /* remove edge */
		 del_edge(i, j);
	     }
	}
    }

    /* print solution */
    fprintf(fout, "%.6lf\n", min);

    /* close files */
    fclose(fin);
    fclose(fout);

    /* done */
    return 0;

}
