/*
ID: iocoder1
LANG: C
TASK: castle
*/

#include <stdio.h>
#include <stdlib.h>

struct nodeptr;

typedef struct node {
    int row;
    int col;
    int cmp;
    struct nodeptr *adj;
} node_t;

typedef struct nodeptr {
    node_t *node;
    struct nodeptr *next;
} nodeptr_t;

typedef struct wall {
    node_t *src;
    node_t *dst;
    int     typ;
} wall_t;

void printGraph(node_t *nodes, int cnt) {
    int i;
    nodeptr_t *ptr;
    for (i = 0; i < cnt; i++) {
        ptr = nodes[i].adj;
        while (ptr) {
            printf("(%d,%d) -> ", nodes[i].row, nodes[i].col);
            printf("(%d, %d)\n", ptr->node->row, ptr->node->col);
            ptr = ptr->next;
        }
    }
}

void floodFill(node_t *nodes, int cnt, int new_component) {
    int num_visited = 1, i;
    nodeptr_t *ptr;
    while (num_visited != 0) {
        num_visited = 0;
        for (i = 0; i < cnt; i++) {
            if (nodes[i].cmp == -2) {
                num_visited  = num_visited + 1;
                nodes[i].cmp = new_component;
                ptr = nodes[i].adj;
                while(ptr) {
                    if (ptr->node->cmp == 0) {
                        ptr->node->cmp = -2;
                    }
                    ptr = ptr->next;
                }
            }
        }
    }
}

int findComponents(node_t *nodes, int cnt) {
    int num_components = 0, i;
    for (i = 0; i < cnt; i++) {
        nodes[i].cmp = 0;
    }
    for (i = 0; i < cnt; i++) {
        if (nodes[i].cmp == 0) {
            num_components += 1;
            nodes[i].cmp = -2;
            floodFill(nodes, cnt, num_components);
        }
    }
    return num_components;
}

int maxComp(node_t *nodes, int cnt, int num_components) {
    int *sizes = malloc(sizeof(int)*(num_components+1));
    int i;
    int max_size = 0;
    for (i = 0; i < num_components+1; i++) {
        sizes[i] = 0;
    }
    for (i = 0; i < cnt; i++) {
        sizes[nodes[i].cmp] += 1;
        if (sizes[nodes[i].cmp] > max_size) {
            max_size = sizes[nodes[i].cmp];
        }
    }
    return max_size;
}

int main() {
    FILE *fin, *fout;
    int N, M, w=0, i, j, m, cnt;
    int senw, west, nort, east, sout;
    node_t *nodes;
    wall_t *walls;
    nodeptr_t *ptr, sptr, dptr;
    int base_cmp, base_max;
    int max_cmp, max_num;
    int cur_row, cur_col;
    int cur_num_cmp, cur_max_cmp;
    int max_row, max_col, max_sid;
    /* open files */
    fin  = fopen("castle.in",  "r");
    fout = fopen("castle.out", "w");
    /* read N & M */
    fscanf(fin, "%d%d", &N, &M);
    /* allocate arrays of nodes and walls */
    cnt   = N*M;
    nodes = malloc(sizeof(node_t)*N*M);
    walls = malloc(sizeof(wall_t)*N*M*4);
    /* read castle rooms */
    for (i = 0; i < M; i++) {
        for (j = 0; j < N; j++) {
            /* read walls of current room */      
            fscanf(fin, "%d", &senw);
            west = senw & 1;
            nort = senw & 2;
            east = senw & 4;
            sout = senw & 8;
            /* add current node to list of nodes */
            nodes[i*N+j].row = i;
            nodes[i*N+j].col = j;
            nodes[i*N+j].adj = NULL;
            /* add walls between the rooms to list of walls */
            if (west == 0) {
                /* we've got no wall to the west */
                ptr = malloc(sizeof(nodeptr_t));
                ptr->node = &nodes[(i)*N+(j-1)];
                ptr->next = nodes[i*N+j].adj;
                nodes[i*N+j].adj = ptr;
            } else if (j != 0) {
                /* we've got a  wall to the west */
                walls[w].src = &nodes[i*N+j];
                walls[w].dst = &nodes[(i)*N+(j-1)];
                walls[w].typ = 'W';
                w++;
            }            
            if (nort == 0) {
                /* we've got no wall to the north */
                ptr = malloc(sizeof(nodeptr_t));
                ptr->node = &nodes[(i-1)*N+(j)];
                ptr->next = nodes[i*N+j].adj;
                nodes[i*N+j].adj = ptr;
            } else if (i != 0) {
                /* we've got a  wall to the north */
                walls[w].src = &nodes[i*N+j];
                walls[w].dst = &nodes[(i-1)*N+(j)];
                walls[w].typ = 'N';          
                w++;
            }            
            if (east == 0) {
                /* we've got no wall to the east */
                ptr = malloc(sizeof(nodeptr_t));
                ptr->node = &nodes[(i)*N+(j+1)];
                ptr->next = nodes[i*N+j].adj;
                nodes[i*N+j].adj = ptr;
            } else if (j < N-1) {
                /* we've got a  wall to the east */
                walls[w].src = &nodes[i*N+j];
                walls[w].dst = &nodes[(i)*N+(j+1)];
                walls[w].typ = 'E';          
                w++;
            }
            if (sout == 0) {
                /* we've got no wall to the south */
                ptr = malloc(sizeof(nodeptr_t));
                ptr->node = &nodes[(i+1)*N+(j)];
                ptr->next = nodes[i*N+j].adj;
                nodes[i*N+j].adj = ptr;
            } else if (i < M-1) {
                /* we've got a  wall to the south */
                walls[w].src = &nodes[i*N+j];
                walls[w].dst = &nodes[(i+1)*N+(j)];
                walls[w].typ = 'S';  
                w++;
            }
        }
    }
    /* compute base components number */
    base_cmp = findComponents(nodes, cnt);
    base_max = maxComp(nodes, cnt, base_cmp);
    /* try to add add an edge every time and see what happens. */
    max_cmp = 0;
    max_num = 1000000000;
    for (i = 0; i < w; i++) {
        /* add */
        sptr.node = walls[i].dst;
        sptr.next = walls[i].src->adj;
        dptr.node = walls[i].src;
        dptr.next = walls[i].dst->adj;
        walls[i].src->adj = &sptr;
        walls[i].dst->adj = &dptr;
        cur_row = walls[i].src->row;
        cur_col = walls[i].src->col;
        /* calculate */
        cur_num_cmp = findComponents(nodes, cnt);
        cur_max_cmp = maxComp(nodes, cnt, cur_num_cmp);
        /* compare */
        if (cur_max_cmp > max_cmp) {
            max_num = 1000000000;
            max_cmp = cur_max_cmp;
        }
        /* add to list of maxes if it is a maximum */
        if (cur_max_cmp == max_cmp) {
            /* priority first for "farthest to the west" */
            m = cur_col*M*4;
            /* then if tied, "farthest to the south" */
            m += (M-1-cur_row)*4;
            /* then if tied, N then E */
            switch (walls[i].typ) {
                case 'N':
                    m += 0;
                    break;
                case 'E':
                    m += 1;
                    break;
                case 'S':
                    m += 2;
                    break;
                case 'W':
                    m += 3;
                    break;
                default:
                    break;
            }
            /* if m < max_num, set it */
            if (m < max_num) {
                max_num = m;
            }
        }
        /* remove */
        walls[i].src->adj = sptr.next;
        walls[i].dst->adj = dptr.next;
        sptr.node = NULL;
        sptr.next = NULL;
        dptr.node = NULL;
        dptr.next = NULL;
    }
    /* extract information about maximum module */
    max_sid = "NESW"[max_num%4];
    max_num /= 4;
    max_row = M-1-(max_num%M) + 1;
    max_num /= M;
    max_col = max_num + 1;
    /* print settings */
    fprintf(fout, "%d\n", base_cmp);
    fprintf(fout, "%d\n", base_max);
    fprintf(fout, "%d\n", max_cmp);
    fprintf(fout, "%d %d %c\n", max_row, max_col, max_sid);
    /* close files */
    fclose(fin);
    fclose(fout);
    /* done */
    return 0;
}
