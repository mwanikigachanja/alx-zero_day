#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{

	char file_name[255];
	FILE *fp;
	printf("Enter your file name:");
	scanf("%s",file_name);

	fp = fopen(file_name,"w");
	char ch[2000];
	fprintf(fp,"First File name is %s !!\n\nWhat a surprise, C is a world of wonders!\n\nSee you in the next phase.\n",file_name);
	fprintf(fp, "Your file %s is ready for use.\n",file_name);

	printf("%s",fgets(ch,500,fp));

	fclose(fp);
	return 0;
}	

