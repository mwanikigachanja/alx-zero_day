#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	FILE *fp;
	fp = fopen("first_file.txt","w");
	char ch[2000];
	fprintf(fp,"%s","First File!!\n\nWhat a surprise, C is a world of wonders!\n\nSee you in the next phase.\n");

	printf("%s",fgets(ch,500,fp));

	fclose(fp);
	return 0;
}	

