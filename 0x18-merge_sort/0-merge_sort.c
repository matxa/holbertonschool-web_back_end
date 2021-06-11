
#include "sort.h"


/**
 * printArray - prints segments of the array
 * @A: array
 * @iBegin: start index
 * @iEnd: end index
 *
 * Return: void
 */
void printArray(int A[], size_t iBegin, size_t iEnd)
{
	for (; iBegin < iEnd; iBegin++)
	{
		printf("%d", A[iBegin]);
		if (iBegin < iEnd - 1)
			printf(", ");
	}
}


/**
 * TopDownMerge - sorts the segments of the array and merges them
 * @B: working array
 * @iBegin: start index
 * @iMiddle: middle index
 * @iEnd: end index
 * @A: array
 *
 * Return: void
 */
void TopDownMerge(int A[], size_t iBegin, size_t iMiddle, size_t iEnd, int B[])
{
	size_t i = iBegin, j = iMiddle, k;

	printf("[left]: ");
	printArray(A, iBegin, iMiddle);
	printf("\n");

	printf("[right]: ");
	printArray(A, iMiddle, iEnd);
	printf("\n");

	for (k = iBegin; k < iEnd; k++)
	{
		if (i < iMiddle && (j >= iEnd || A[i] <= A[j]))
		{
			B[k] = A[i];
			i = i + 1;
		}
		else
		{
			B[k] = A[j];
			j = j + 1;
		}
	}
	printf("[Done]: ");
	printArray(B, iBegin, iEnd);
	printf("\n");
}


/**
 * TopDownSplitMerge - this function recursivly splits the array then merges
 * @B: working array
 * @iBegin: start index
 * @iEnd: end index
 * @A: array
 *
 * Return: void
 */
void TopDownSplitMerge(int B[], size_t iBegin, size_t iEnd, int A[])
{
	size_t iMiddle = (iEnd + iBegin) / 2;

	if (iEnd - iBegin <= 1)
		return;
	TopDownSplitMerge(A, iBegin,  iMiddle, B);
	TopDownSplitMerge(A, iMiddle, iEnd, B);
	printf("Merging...\n");
	TopDownMerge(A, iBegin, iMiddle, iEnd, B);
}

/**
 * merge_sort - sorts an array using the merge sort algorithm
 * @array: the array we will sort
 * @size: the size of the array
 *
 * Return: void
 */
void merge_sort(int *array, size_t size)
{
	size_t k = 0;
	int *workarray = NULL;


	if (size < 2 || !array)
		return;

	workarray = malloc(size * sizeof(size));
	if (!workarray)
		return;

	for (; k < size; k++)
		workarray[k] = array[k];

	TopDownSplitMerge(workarray, 0, size, array);

	for (k = 0; k < size; k++)
		array[k] = workarray[k];
	free(workarray);
}
