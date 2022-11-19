#include<stdio.h>
#define N 9
int row[N];
int col[N];
int box[N];
int getBox(int i,int j) 
{ 
    return i/3*3 + j/3; 
}
int isSafe(int i,int j,int number)
{
    return !((row[i] >> number) & 1) && !((col[j] >> number) & 1) && !((box[getBox(i, j)] >> number) & 1);
}
void setInitialValues(int grid[N][N])
{
    for(int i = 0;i < N;i++)
    {
        for(int j = 0;j < N;j++)
        {
            row[i] |= 1 << grid[i][j];
            col[j] |= 1 << grid[i][j];
            box[getBox(i, j)] |= 1 << grid[i][j];
        }
    }
}
int solveSudoku(int grid[N][N],int i,int j,int *seted)
{
    if(!*seted)
    {
        *seted = 1;
        setInitialValues(grid);
    }
    if(i == N-1 && j == N)
        return 1;
    if(j == N)
    {
        j = 0;
        i++;
    }
    if(grid[i][j])
        return solveSudoku(grid,i,j + 1,seted);
    for(int nr = 1;nr <= N;nr++) 
    {
        if(isSafe(i,j,nr)) 
        {
            grid[i][j] = nr;
            row[i] |= 1 << nr;
            col[j] |= 1 << nr;
            box[getBox(i, j)] |= 1 << nr;
            if(solveSudoku(grid,i,j + 1,seted))
                return 1;
            row[i] &= ~(1 << nr);
            col[j] &= ~(1 << nr);
            box[getBox(i, j)] &= ~(1 << nr);
        }
        grid[i][j] = 0;
    }
    return 0;
}
void printGrid(int arr[N][N])
{
    for(int i = 0;i < N;i++)
    {
        for(int j = 0;j < N;j++)
            printf("%d\t",arr[i][j]);
        printf("\n");
    }
}
int main()
{
    int grid[9][9] = {{ 3, 0, 6, 5, 0, 8, 4, 0, 0 },
                      { 5, 2, 0, 0, 0, 0, 0, 0, 0 },
                      { 0, 8, 7, 0, 0, 0, 0, 3, 1 },
                      { 0, 0, 3, 0, 1, 0, 0, 8, 0 },
                      { 9, 0, 0, 8, 6, 3, 0, 0, 5 },
                      { 0, 5, 0, 0, 9, 0, 6, 0, 0 },
                      { 1, 3, 0, 0, 0, 0, 2, 5, 0 },
                      { 0, 0, 0, 0, 0, 0, 0, 7, 4 },
                      { 0, 0, 5, 2, 0, 6, 3, 0, 0 }};
    int seted = 0;
    if(solveSudoku(grid,0,0,&seted))
        printGrid(grid);
    else
        printf("No solution exists");
    return 0;
}

