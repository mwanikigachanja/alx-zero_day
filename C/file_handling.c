#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	FILE *fp;
	fp = fopen("first_file.txt","w");

	fprintf(fp,"%s","First File!!");

	fclose(fp);
	return 0;
}	

