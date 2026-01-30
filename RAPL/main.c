/*
 *  Análise e Teste de Software
 *  João Saraiva
 *  2016-2017
 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <powercap/powercap.h>
#include <raplcap/raplcap.h>
#include <math.h>
#include <pthread.h>
#include <unistd.h>
#include <signal.h>
#include <string.h>


int initializeRapl(raplcap *rc, int power_limit){
    printf("Running with CAP\n");
    raplcap_limit rl_short, rl_long;
    uint32_t q, j, n, d;

    // initialize
    if (raplcap_init(rc))
    {// Signal handler for SIGALRM
        perror("raplcap_init");
        return -1;
    }

    // get the number of RAPL packages
    n = raplcap_get_num_packages(NULL);
    if (n == 0)
    {
        perror("raplcap_get_num_packages");
        return -1;
    }

    // assuming each package has the same number of die, only querying for package=0
    d = raplcap_get_num_die(rc, 0);
    if (d == 0)
    {
        perror("raplcap_get_num_die");
        raplcap_destroy(rc);
        return -1;
    }

    // for each package die, set a power cap of same limit for both long and short
    // a time window of 0 leaves the time window unchanged
    rl_long.watts = power_limit;
    rl_long.seconds = 0;
    rl_short.watts = power_limit;
    rl_short.seconds = 0;

    for (q = 0; q < n; q++)
    {
        for (j = 0; j < d; j++)
        {
            if (raplcap_pd_set_limits(rc, q, j, RAPLCAP_ZONE_PACKAGE, &rl_long, &rl_short))
            {
                perror("raplcap_pd_set_limits");
            }
        }
    }

    // for each package die, enable the power caps
    // this could be done before setting caps, at the risk of enabling unknown power cap values first
    for (q = 0; q < n; q++)
    {
        for (j = 0; j < d; j++)
        {
            if (raplcap_pd_set_zone_enabled(rc, q, j, RAPLCAP_ZONE_PACKAGE, 1))
            {
                perror("raplcap_pd_set_zone_enabled");
            }
        }
    }
    return 0;
}


int main(int argc, char **argv) {
    int power_limit = 0;
    int core = 0;
    raplcap rc;

    if (argc < 2) {
        printf("Usage: %s <power_limit>\n", argv[0]);
        return -1;
    }

    power_limit = atoi(argv[1]);

    printf("power_limit %d\n", power_limit);

    fflush(stdout);

    if (power_limit != 0) {
        if(initializeRapl(&rc, power_limit))
            return -1;
    }
    printf("\n\n END of PARAMETRIZED PROGRAM: \n");

    if (power_limit != 0) {
        if (raplcap_destroy(&rc)) {
            printf("Error destroying CAP\n");
            perror("raplcap_destroy");
        } else {
            printf("Successfully destroyed CAP\n");
        }
    }
    return 0;
    
}

