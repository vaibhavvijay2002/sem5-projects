#include<stdio.h>
#include<stdlib.h>
#include "sudoku_header.h"
int **createPuzzle()
{
    int **puzzle;
    int arrayPuzzle[9][9] = {{ 3, 0, 6, 5, 0, 8, 4, 0, 0 },
                             { 5, 2, 0, 0, 0, 0, 0, 0, 0 },
                             { 0, 8, 7, 0, 0, 0, 0, 3, 1 },
                             { 0, 0, 3, 0, 1, 0, 0, 8, 0 },
                             { 9, 0, 0, 8, 6, 3, 0, 0, 5 },
                             { 0, 5, 0, 0, 9, 0, 6, 0, 0 },
                             { 1, 3, 0, 0, 0, 0, 2, 5, 0 },
                             { 0, 0, 0, 0, 0, 0, 0, 7, 4 },
                             { 0, 0, 5, 2, 0, 6, 3, 0, 0 }};
    puzzle = (int**)malloc(sizeof(int*) * 9);
    for(int i = 0;i < 9;i++)
    {
        puzzle[i] = (int*)malloc(sizeof(int) * 9);
        for(int j = 0;j < 9;j++)
            puzzle[i][j] = arrayPuzzle[i][j];
    }
    return puzzle;
}
void printPuzzle(int **puzzle)
{
    printf("\n");
    printf(" 0 | 1  2  3 | 4  5  6 | 7  8  9 | X\n");
    printf(" ---------------------------------\n");
    for(int i = 0,a = 1;i < 9;i++,a++)
    {
        for(int j = 0;j < 9;j++)
        {
            if(j == 0)
                printf(" %d |", a);
            else if(j%3 == 0)
                printf("|");
            printf(" %d ", puzzle[i][j]);
            if(j == 8)
                printf("|");
        }
        printf("\n");
        if((i + 1) % 3 == 0)
            printf(" ---------------------------------\n");
    }
    printf(" Y\n");
}
int checkAvailable(int **puzzle,int *row,int *column)
{
    for(int i = 0;i < 9;i++)
    {
        for(int j = 0;j < 9;j++)
        {
            if(puzzle[i][j] == 0)
            {
                *row = i;
                *column  = j;
                return 1;
            }
        }
    }
    return 0;
}
int checkBox(int **puzzle,int row,int column,int val)
{
    for(int i = 0;i < 9;i++)
    {
        if(puzzle[i][column] == val)
            return 0;
    }
    for(int j = 0;j < 9;j++)
    {
        if(puzzle[row][j] == val)
            return 0;
    }
    int squareRow;
    int squareColumn;
    squareRow = row - row % 3;
    squareColumn = column - column % 3;
    for(int i = 0;i < 3;i++)
    {
        for(int j = 0;j < 3;j++)
        {
            if(puzzle[squareRow + i][squareColumn + j] == val)
                return 0;
        }
    }
    return 1;
}
int solvePuzzle(int **puzzle)
{
    int i;
    int j;
    if(!checkAvailable(puzzle,&i,&j))
        return 1;
    for(int val = 1;val < 10;val++)
    {
        if(checkBox(puzzle,i,j,val))
        {
            puzzle[i][j] = val;
            if(solvePuzzle(puzzle))
                return 1;
            else
                puzzle[i][j] = 0;
        }
    }
    return 0;
}
int **copyPuzzle(int **puzzle)
{
    int **newPuzzle;
    newPuzzle = (int**)malloc(sizeof(int*) * 9);
    for (int i = 0;i < 9;i++)
    {
        newPuzzle[i] = (int*)malloc(sizeof(int) * 9);
        for(int j = 0;j < 9;j++)
            newPuzzle[i][j] = puzzle[i][j];
    }
    return newPuzzle;
}
void userChoice(int **userPuzzle,int **tempPuzzle)
{
    int positionX;
    int positionY;
    int userVal;
    char c;
    int i;
    int j;
    while(1)
    {
        if(!checkAvailable(userPuzzle,&i,&j))
        {
            printf("\nsuccessfully solved the puzzle!\n");
            return;
        }
        while(1)
        {
            printf("\npress enter to continue or press q to quit\n");
            c = getchar();
            if((c == 'q') || (c == 'Q'))
            {
                getchar();
                solvePuzzle(userPuzzle);
                printf("\nsolved puzzle:\n");
                printPuzzle(userPuzzle);
                return;
            }
            else if((c != '\n') && (c != 'q'))
                getchar();
            else
                break;
        }
        printf("\nenter coordinate for the square to insert value as X Y:\n");
        scanf("%d %d",&positionX,&positionY);
        while(1)
        {
            if((positionX > 9) || (positionX < 1) || (positionY > 9) || (positionY < 1) || (userPuzzle[positionY - 1][positionX - 1] != 0))
            {
                printf("\ncan't insert value to this coordinate, so enter new coordinate\n");
                scanf("%d %d",&positionX,&positionY);
            }
            else 
            {
                positionX -= 1;
                positionY -= 1;
                break;
            }
        }
        printf("\nenter value from 1 to 9\n");
        scanf("%d",&userVal);
        while(1)
        {
            if((userVal > 9) || (userVal < 1))
            {
                printf("\nenter valid value:\n");
                scanf("%d",&userVal);
            }
            else 
                break;
        }
        if(checkBox(userPuzzle,positionY,positionX,userVal))
            userPuzzle[positionY][positionX] = userVal;
        else
            printf("\nvalue entered is already present in that row or column or box, so try again\n",positionX + 1,positionY + 1);
        for(int i = 0;i < 9;i++)
        {
            for(int j = 0;j < 9;j++)
                tempPuzzle[i][j] = userPuzzle[i][j];
        }
        if(!solvePuzzle(tempPuzzle))
        {
            printf("\nvalue entered is not leading to the solution, so try again\n",positionX + 1,positionY + 1);
            userPuzzle[positionY][positionX] = 0;
        }
        getchar();
        printPuzzle(userPuzzle);
    }
    return;
}