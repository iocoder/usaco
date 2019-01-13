/*
ID: iocoder1
LANG: C
TASK: comehome
*/

#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define INF 1000000
typedef long long dist_t;

dist_t **edges;
dist_t **spath;
int node_count;

int char_to_idx(char node) {

    if (node >= 'A' && node <= 'Z') {
        return node-'A'+26;
    } else {
        return node-'a'+0;
    }

}

char idx_to_char(int node) {

    if (node < 26) {
        return 'a'+node;
    } else {
        return 'A'+node-26;
    }

}

void init_graph() {

    /* local vars */
    int i, j;

    /* node count is constant: 26*2 */
    node_count = 52;

    /* create edge matrix */
    edges  = malloc(sizeof(dist_t *) * node_count);
    spath  = malloc(sizeof(dist_t *) * node_count);
    for (i = 0; i < node_count; i++) {
         edges[i]  = malloc(sizeof(dist_t) * node_count);
	 spath[i]  = malloc(sizeof(dist_t) * node_count);
	 for (j = 0; j < node_count; j++) {
              if (i == j) {
                  edges[i][j] = 0;
	      } else {
                  edges[i][j] = INF;
	      }
	      spath[i][j] = INF;
	 }
    }

}

void add_edge(int i, int j, int w) {

    /* add edge between i and j */
    if (w < edges[i][j]) {
        edges[i][j] = w;
    }

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

dist_t get_shortest(int i, int j) {

    /* get shortest path between i and j */
    return spath[i][j];

}

int main() {
    
    /* declare variables */
    FILE *fin, *fout;
    char src, dst;
    int  src_idx, dst_idx;
    int  i, w, N;
    char min_node;
    int  min_path = INF;

    /* open files */
    fin  = fopen("comehome.in", "r");
    fout = fopen("comehome.out", "w");
    
    /* initialize the graph */
    init_graph();

    /* read number of edges */
    fscanf(fin, "%d", &N);

    /* read edges */ 
    for (i = 0; i < N; i++) {
	fscanf(fin, " ");
	fscanf(fin, "%c %c %d", &src, &dst, &w);
	src_idx = char_to_idx(src);
	dst_idx = char_to_idx(dst);
        add_edge(src_idx, dst_idx, w);
	add_edge(dst_idx, src_idx, w);
    }

    /* run floyd warshall once (graph size is constant = 52) */
    floyd_warshall();

    /* find shortest node */
    dst = 'Z';
    for (src = 'A'; src < dst; src++) {
        src_idx = char_to_idx(src);
	dst_idx = char_to_idx(dst);
	w = get_shortest(src_idx, dst_idx);
	if (w < min_path) {
	    min_path = w;
	    min_node = src;
	}
    }

    /* print result */
    fprintf(fout, "%c %d\n", min_node, min_path);

    /* close files */
    fclose(fin);
    fclose(fout);

    /* done */
    return 0;

}
