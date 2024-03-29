#include <stdio.h>
#include <stdlib.h>

void file_histogram(char *file_name)
{
	FILE *f_in;
	f_in = fopen(file_name, "r");
	if (f_in == NULL)
	{
		printf("Error opening file\n");
		exit(1);
	}

	int histogram[256] = {0}; // Inicializa o histograma com zeros para cada caractere ASCII

	// Lê o arquivo e atualiza o histograma
	int c;
	while ((c = fgetc(f_in)) != EOF)
	{
		histogram[c]++;
	}

	// Imprime o histograma
	printf("Histograma do arquivo '%s':\n", file_name);
	for (int i = 0; i < 256; i++)
	{
		if (histogram[i] > 0)
			printf("'%c' (%d) : %d\n", (char)i, i, histogram[i]);
	}
}
