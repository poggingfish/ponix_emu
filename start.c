#include <stdio.h>
#include <stdlib.h>
int main(){
    printf("ponix bootstrapper v1 (%s)\n", __VERSION__);
    printf("Making pvm\n");
    system("mkdir -p binaries && clang pvm/src/pvm/pvm.c -o binaries/pvm");
}