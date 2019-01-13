/*
ID: iocoder1
LANG: C
TASK: maze1
*/

#include <stdio.h>
#include <stdlib.h>

#define INF 1000000

struct node;
struct edge;

typedef struct edge {
    int row;
    int col;
    struct edge *next;
} edge_t;

typedef struct node {
    int row;
    int col;
    int distance;
    int hindex;
    int best;
    struct edge *edges;
} node_t;

typedef struct source {
    int row;
    int col;
    struct source *next;
} source_t;

int main() {
    
    /* declare variables */
    FILE *fin, *fout;
    int W, H;
    int row, col, prow, pcol;
    int i, j;
    char inp;
    node_t **maze = NULL, *node_u, *node_v, *node_h;
    source_t *sources = NULL, *cur_src;
    edge_t *cur_edge;
    node_t **heap = NULL;
    int heap_size, next_h;
    node_t *max_node = NULL;
    int max_dist = -1;

    /* open files */
    fin  = fopen("maze1.in", "r");
    fout = fopen("maze1.out", "w");

    /* first of all, we read W and H separated */
    fscanf(fin, "%d%d", &W, &H);

    /* allocate the nodes */
    maze = malloc(sizeof(node_t *) * H);
    for (row = 0; row < H; row++) {
         maze[row] = malloc(sizeof(node_t) * W);
	 for (col = 0; col < W; col++) {
              maze[row][col].row   = row;
	      maze[row][col].col   = col;
	      maze[row][col].best  = INF;
	      maze[row][col].edges = NULL;
	 }
    }

    /* allocate the heap */
    heap = malloc(sizeof(node_t *) * H * W);

    /* read the maze */
    fscanf(fin, " ");
    for (i = 0; i < 2*H; i++) {
         if (i%2 == 0) {
             /* this is a row border */
             row  = i/2;
	     prow = row-1;
             for (col = 0; col < W; col++) {
                 fscanf(fin, "%*c%c", &inp);
		 if (inp != '-') {
                     if (prow == -1) {
			 cur_src = malloc(sizeof(source_t));
			 cur_src->row = row;
			 cur_src->col = col;
			 cur_src->next = sources;
			 sources = cur_src;
		     } else {
			 cur_edge = malloc(sizeof(edge_t));
			 cur_edge->row = row;
			 cur_edge->col = col;
			 cur_edge->next = maze[prow][col].edges;
			 maze[prow][col].edges = cur_edge;
			 cur_edge = malloc(sizeof(edge_t));
			 cur_edge->row = prow;
			 cur_edge->col = col;
			 cur_edge->next = maze[row][col].edges;
			 maze[row][col].edges = cur_edge;
		     }
		 }
	     }
	     fscanf(fin, "%*c"); /* the last + */
	 } else {
             /* this is an actual row description */
             for (col = 0; col < W; col++) {
		 pcol = col - 1;
                 fscanf(fin, "%c%*c", &inp);
		 if (inp != '|') {
                     if (pcol == -1) {
			 cur_src = malloc(sizeof(source_t));
			 cur_src->row = row;
			 cur_src->col = col;
			 cur_src->next = sources;
			 sources = cur_src;
		     } else {
			 cur_edge = malloc(sizeof(edge_t));
			 cur_edge->row = row;
			 cur_edge->col = col;
			 cur_edge->next = maze[row][pcol].edges;
			 maze[row][pcol].edges = cur_edge;
			 cur_edge = malloc(sizeof(edge_t));
			 cur_edge->row = row;
			 cur_edge->col = pcol;
			 cur_edge->next = maze[row][col].edges;
			 maze[row][col].edges = cur_edge;
		     }
		 }
	     }
	     fscanf(fin, "%c", &inp); /* the last | */
	     col--;
	     if (inp != '|') {
		 cur_src = malloc(sizeof(source_t));
	         cur_src->row = row;
		 cur_src->col = col;
		 cur_src->next = sources;
		 sources = cur_src;
	     }
	 }
	 /* read \n */
	 fscanf(fin, "%*c");
    }

    /* last input line is special */
    for (col = 0; col < W; col++) {
         fscanf(fin, "%*c%c", &inp);
         if (inp != '-') {
             cur_src = malloc(sizeof(source_t));
	     cur_src->row = row;
	     cur_src->col = col;
	     cur_src->next = sources;
	     sources = cur_src;
	 }
    }
    fscanf(fin, "%*c"); /* the last + */

    /* dijkstra -- first loop over source nodes */
    cur_src = sources;
    while(cur_src != NULL) {
        /* first, set all the distances with inf, except the source */
        i = 1;
 	for (row = 0; row < H; row++) {
             for (col = 0; col < W; col++) {
                  if (row == cur_src->row && col == cur_src->col) {
		      maze[row][col].distance = 0;
		      heap[0] = &maze[row][col];
		      heap[0]->hindex = 0;
		      max_node = heap[0];
		  } else {
		      maze[row][col].distance = INF;
		      heap[i] = &maze[row][col];
		      heap[i]->hindex = i;
		      i++;
		  }
	     }
	}
	heap_size = W*H;
        /* we keep looping until heap size is 0 O(V)*/
	while (heap_size) {
            /* we take the top node */
            node_u = heap[0];
	    /* decrease heap size */
	    heap_size--;
            /* now make a new root O(log(V))*/
	    if (heap_size) {
		/* take the last heap element */
	    	heap[0] = heap[heap_size];
		heap[0]->hindex = 0;
		/* push down the heap until balanced */
		next_h = 0;
		while(next_h != -1) {
                    if (((next_h*2)+1 < heap_size && 
		         heap[next_h]->distance > heap[next_h*2+1]->distance) ||
	                ((next_h*2)+2 < heap_size &&
			 heap[next_h]->distance > heap[next_h*2+2]->distance)
		       ) {
                        /* swap with the smallest child */
                        if ((next_h*2)+2 < heap_size &&
			    heap[(next_h*2)+2]->distance < heap[next_h*2+1]->distance) {
			    /* swap with the right child */
                            node_h = heap[next_h*2+2];
			    heap[next_h*2+2] = heap[next_h];
			    heap[next_h] = node_h;
			    heap[next_h*2+2]->hindex = next_h*2+2;
			    heap[next_h]->hindex = next_h;
			    next_h = next_h*2+2;
		        } else {
			    /* swap with the left child */
			    node_h = heap[next_h*2+1];
			    heap[next_h*2+1] = heap[next_h];
			    heap[next_h] = node_h;
			    heap[next_h*2+1]->hindex = next_h*2+1;
			    heap[next_h]->hindex = next_h;
			    next_h = next_h*2+1;
			}
		    } else {
                        /* we're done */
			next_h = -1;
		    }
		}
	    }
	    /* node_u distance is settled */
	    //printf("(%d,%d) %d\n", node_u->row, node_u->col, node_u->distance);
            if (node_u->distance < node_u->best) {
                node_u->best = node_u->distance;
            }
	    /* last round? */
	    if (cur_src->next == NULL) {
                /* max? */
		if (node_u->best > max_dist) {
                    max_dist = node_u->best;
		    max_node = node_u;
		}
	    }
	    /* loop over the edges of u O(E/V) */
            cur_edge = node_u->edges;
	    while (cur_edge) {
		node_v = &maze[cur_edge->row][cur_edge->col];
		if (node_u->distance + 1 < node_v->distance) {
                    /* update node_v */
	            node_v->distance = node_u->distance + 1;
		    /* now update the heap */
		    next_h = node_v->hindex;
                    while (next_h) {
                        if (heap[(next_h-1)/2]->distance > heap[next_h]->distance) {
                            /* swap */
			    node_h = heap[(next_h-1)/2];
			    heap[(next_h-1)/2] = heap[next_h];
			    heap[next_h] = node_h;
			    heap[(next_h-1)/2]->hindex = (next_h-1)/2;
		  	    heap[next_h]->hindex = next_h;
			    next_h = (next_h-1)/2;
			} else {
                            /* we are done */
			    next_h = 0;
			}
		    }
		}
                cur_edge = cur_edge->next;
	    }
	}
        cur_src = cur_src->next;
    }

    /* print result */
    fprintf(fout, "%d\n", max_dist+1);

    /* close files */
    fclose(fin);
    fclose(fout);

    /* done */
    return 0;

}
