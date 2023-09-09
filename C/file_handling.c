#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	char file_name[255];
	printf("Enter your file name:");
	scanf("Enter file name:%s\n",file_name);
	FILE *fp;
	fp = fopen("{file_name}.txt","w");
	char ch[2000];
	fprintf(fp,"%s","First File!!\n\nWhat a surprise, C is a world of wonders!\n\nSee you in the next phase.\n");

	printf("%s",fgets(ch,500,fp));

	fclose(fp);
	return 0;
}	

