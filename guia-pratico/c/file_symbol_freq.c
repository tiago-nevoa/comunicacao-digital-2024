#include <stdio.h>
#include <stdlib.h>


int file_symbol_freq(char *file_name, char symbol)
{
	FILE *fp;
	int count = 0;
	int c;

	fp = fopen(file_name, "r");
	if (fp == NULL)
	{
		printf("Error opening file\n");
		exit(1);
	}

	while ((c = fgetc(fp)) != EOF)
	{
		if (c == symbol)
			count++;
    }
	fclose(fp);
	return count;
}
