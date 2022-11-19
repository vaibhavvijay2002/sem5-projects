#include <stdio.h>
int findUnassignedLocation(int N,int grid[N][N],int *row,int *col)
{
	int i;
	int j;
	for(i = 0;i < N;i++)
	{
		for(j = 0;j < N;j++)
		{
			if(grid[i][j] == 0)
			{
				*row = i;
				*col = j;
				return 1;
			}
		}
	}
	*row = i;
	*col = j;
	return 0;
}
int usedInRow(int N,int grid[N][N],int row,int num)
{
	for(int col = 0;col < N;col++)
	{
		if (grid[row][col] == num)
			return 1;
	}
	return 0;
}
int usedInCol(int N,int grid[N][N],int col,int num)
{
	for(int row = 0;row < N;row++)
	{
		if(grid[row][col] == num)
			return 1;
	}
	return 0;
}
int usedInBox(int N,int grid[N][N],int boxStartRow,int boxStartCol,int num)
{
	for(int row = 0; row < 3; row++)
	{
		for(int col = 0; col < 3; col++)
		{
			if(grid[row + boxStartRow][col + boxStartCol] == num)
				return 1;
		}
	}
	return 0;
}
int isSafe(int N,int grid[N][N],int row,int col,int num)
{
		return !usedInRow(N,grid,row,num) && !usedInCol(N,grid,col,num) && !usedInBox(N,grid,row - row % 3,col - col % 3,num) && grid[row][col] == 0;
}
int solveSudoku(int N,int grid[N][N])
{
	int row;
	int col;
	if (!findUnassignedLocation(N,grid,&row,&col))
		return 1;
	for(int num = 1;num <= N;num++)
	{
		if(isSafe(N,grid,row,col,num))
		{
			grid[row][col] = num;
			if(solveSudoku(N,grid))
				return 1;
			grid[row][col] = 0;
		}
	}
	return 0;
}
void printGrid(int N,int grid[N][N])
{
	for(int row = 0;row < N;row++)
	{
		for(int col = 0;col < N;col++)
			printf("%d\t",grid[row][col]);
		printf("\n");
	}
}
int main()
{
	int N = 9;
	int grid[9][9] = {{ 3, 0, 6, 5, 0, 8, 4, 0, 0 },
                      { 5, 2, 0, 0, 0, 0, 0, 0, 0 },
                      { 0, 8, 7, 0, 0, 0, 0, 3, 1 },
                      { 0, 0, 3, 0, 1, 0, 0, 8, 0 },
                      { 9, 0, 0, 8, 6, 3, 0, 0, 5 },
                      { 0, 5, 0, 0, 9, 0, 6, 0, 0 },
                      { 1, 3, 0, 0, 0, 0, 2, 5, 0 },
                      { 0, 0, 0, 0, 0, 0, 0, 7, 4 },
                      { 0, 0, 5, 2, 0, 6, 3, 0, 0 }};
	if(solveSudoku(N,grid))
		printGrid(N,grid);
	else
		printf("No solution exists");
	return 0;
}
 