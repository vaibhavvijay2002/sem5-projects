#include<stdio.h>
#include<stdlib.h>
#include"sudoku_header.h"
int main()
{
    int **puzzle = createPuzzle();
    int **userPuzzle = copyPuzzle(puzzle);
    int **tempPuzzle = copyPuzzle(puzzle);
    printf("Rules-\n\n");
    printf("The objective of sudoku is to fill a 9x9 grid made of squares such that each row, each column and each full 3x3 squares use numbers from 1 to 9 only one time\n");
    printf("Insert numbers in the squares having value 0\n");
    printf("To check solved puzzle press q key\n\n");
    printf("Let's start the game!\n");
    printPuzzle(userPuzzle);
    userChoice(userPuzzle,tempPuzzle);
    free(puzzle);
    free(userPuzzle);
    free(tempPuzzle);
}







