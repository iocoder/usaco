/*
ID: iocoder1
LANG: C
TASK: ttwo
*/

#include <stdio.h>
#include <stdlib.h>

#define MAX_STEP 100000

#define DIR_NORTH  0
#define DIR_EAST   1
#define DIR_SOUTH  2
#define DIR_WEST   3

typedef struct {
    int row;
    int col;
    int dir;
} obj_t;

char map[10][10];
obj_t farmer, cow;

int meet(obj_t *obj1, obj_t *obj2) {

    /* two objects meeting? */
    if (obj1->row == obj2->row && obj1->col == obj2->col) {
        return 1;
    } else {
        return 0;
    }

}

void move(obj_t *obj) {

    /* move depending on the direction */
    switch(obj->dir) {

	case DIR_NORTH:
            if (obj->row == 0 || map[obj->row-1][obj->col] == '*') {
                obj->dir = (obj->dir + 1) % 4;
	    } else {
                obj->row--;
	    }
	    break;

	case DIR_EAST:
	    if (obj->col == 9 || map[obj->row][obj->col+1] == '*') {
                obj->dir = (obj->dir + 1) % 4;
	    } else {
                obj->col++;
	    }
            break;

	case DIR_SOUTH:
	    if (obj->row == 9 || map[obj->row+1][obj->col] == '*') {
                obj->dir = (obj->dir + 1) % 4;
	    } else {
                obj->row++;
	    }
	    break;

	case DIR_WEST:
            if (obj->col == 0 || map[obj->row][obj->col-1] == '*') {
                obj->dir = (obj->dir + 1) % 4;
	    } else {
                obj->col--;
	    }
	    break;

    }

}

void print_map() {

    /* loop counters */
    int i, j;

    /* print map */
    for (i = 0; i < 10; i++) {
        for (j = 0; j < 10; j++) {
             if (farmer.row == i && farmer.col == j) {
                 printf("F");
	     } else if (cow.row == i && cow.col == j) {
                 printf("C");
	     } else {
                 printf("%c", map[i][j]);
	     }
	}
	printf("\n");
    }
    printf("\n");

}

int main() {
    
    /* declare variables */
    FILE *fin, *fout;
    int i, j, step;

    /* open files */
    fin  = fopen("ttwo.in", "r");
    fout = fopen("ttwo.out", "w");

    /* read map */
    for (i = 0; i < 10; i++) {
        fscanf(fin, " ");
	for (j = 0; j < 10; j++) {
	    /* read map */
            fscanf(fin, "%c", &map[i][j]);
	    /* farmer? */
	    if (map[i][j] == 'F') {
                farmer.row = i;
		farmer.col = j;
		farmer.dir = DIR_NORTH;
		map[i][j] = '.';
	    }
	    /* cow? */
	    if (map[i][j] == 'C') {
                cow.row = i;
		cow.col = j;
		cow.dir = DIR_NORTH;
		map[i][j] = '.';
	    }
	}
    }

    /* simulation */
    step = 0;
    while (step < MAX_STEP && !meet(&farmer, &cow)) {
	move(&farmer);
	move(&cow);
        step++;
    }

    /* max? */
    if (step == MAX_STEP) {
        step = 0;
    }

    /* print number of steps */
    fprintf(fout, "%d\n", step);

    /* close files */
    fclose(fin);
    fclose(fout);

    /* done */
    return 0;

}
