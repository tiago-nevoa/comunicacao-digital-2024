#include <stdio.h>

void count_bits(int val);
void print_fibonacci(int n);
int file_symbol_freq(char *file_name, char symbol);
void file_histogram(char *file_name);
void reverse_file(char *input_file_name, char *output_file_name);

int main()
{
	int n = 42;
	char my_input_file[] = "test-in.txt";
	char my_output_file[] = "test-out.txt";
	char symbol = 'e';

	printf("\n ------------------ \n");
	printf("\ncount_bits(%d):\n", n);
	count_bits(n);

	printf("\n ------------------ \n");
	printf("\nprint_fibonnaci(%d):\n", n);
	print_fibonacci(n);

	printf("\n ------------------ \n");
	printf("\nfile_symbol_freq('%c') : %d\n", symbol, file_symbol_freq(my_input_file, symbol));
	printf("\n ------------------ \n");

	printf("\n ------------------ \n");
	printf("\nfile_histogram('%s') :\n", my_input_file);
	file_histogram(my_input_file);
	printf("\n ------------------ \n");

	printf("\n ------------------ \n");
	printf("\nreverse_file('%s', '%s') :\n", my_input_file, my_output_file);
	reverse_file(my_input_file, my_output_file);
	printf("\n ------------------ \n");

	return 0;
}
