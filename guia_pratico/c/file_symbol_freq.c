#include <stdio.h>
#include <stdlib.h>

int file_symbol_freq(char *file_name, char symbol)
{
	FILE *f_in;
	int count = 0;
	int c;

	f_in = fopen(file_name, "r");
	if (f_in == NULL)
	{
		printf("Error opening file\n");
		exit(1);
	}

	while ((c = fgetc(f_in)) != EOF)
	{
		if (c == symbol)
			count++;
	}
	fclose(f_in);
	return count;
}
