#include <stdio.h>
#include <stdlib.h>

void reverse_file(char *input_file_name, char *output_file_name)
{
	FILE *fp_in;
	FILE *fp_out;

	fp_in = fopen(input_file_name, "r");
	if (fp_in == NULL)
	{
		printf("Error opening input file\n");
		exit(1);
	}

	fp_out = fopen(output_file_name, "w");
	if (fp_out == NULL)
	{
		printf("Error opening output file\n");
		fclose(fp_in);
		exit(1);
	}

	fseek(fp_in, 0, SEEK_END);	   // Move para o final do arquivo de entrada
	long file_size = ftell(fp_in); // Obtem o tamanho do arquivo
	fseek(fp_in, 0, SEEK_SET);	   // Move de volta para o início do arquivo de entrada

	char *buffer = (char *)malloc(file_size * sizeof(char)); // Aloca memória para armazenar o conteúdo do arquivo

	if (buffer == NULL)
	{
		printf("Memory allocation error\n");
		fclose(fp_in);
		fclose(fp_out);
		exit(1);
	}

	// Write the content of the buffer to the output file in reverse order
	for (long i = file_size - 1; i >= 0; i--)
		fwrite(&buffer[i], sizeof(char), 1, fp_out);

	free(buffer); // Free the memory allocated for the buffer
	fclose(fp_in);
	fclose(fp_out);

	printf("Input file '%s' has been reversed and saved as '%s'.\n", input_file_name, output_file_name);
}
