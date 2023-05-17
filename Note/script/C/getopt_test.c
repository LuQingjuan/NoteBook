#include <stdio.h>
#include <stdlib.h>
#include <getopt.h>
/*
*/
int main(int argc, char *argv[])
{
  char optc;
  int i;
  int cnt = 1;

 // print('0', argc, argv, optind);

  while ((optc = getopt(argc, argv, "ab:c:de::")) != -1) {
    printf("%02d: optc - '%c'\toptarg : %s\n\targv: ", cnt++, optc, optarg);
   for (i = 0; i < argc; i++) {
     printf("%s ", argv[i]);
   }
    printf("---- optind = %d\n", optind);

    switch (optc) {
      default:
        break;
    }
  }

  //print('0', argc, argv, optind);

  exit(EXIT_SUCCESS);
}