/* 
	A simple kalman filter example by Adrian Boeing
		www.adrianboeing.com
*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>


double frand() 
{
	return 2*((rand() / (double)RAND_MAX) - 0.5);
}

int main() 
{
	int i = 0;
	float x_est_last = 0, P_last = 0;	//initial values for the kalman filter	
	float Q = 0.022, R = 0.617;			//the noise in the system

	float K, P, P_temp;
	float x_temp_est, x_est;
	float z_measured; 			//the 'noisy' value we measured
	float z_real = 200; 		//the ideal value we wish to measure

	float sum_error_kalman = 0, sum_error_measure = 0;
	 
	srand(0);	 
	x_est_last = z_real + frand() * 0.09;		//initialize with a measurement 
	for (i = 0; i < 30; i++) 
	{
		x_temp_est 	= x_est_last;
		P_temp 		= P_last + Q;
		K 			= P_temp * (1.0/(P_temp + R));		//calculate the Kalman gain
		//z_measured needs to be read from console
		z_measured 	= z_real + frand() * 0.09; 	//the real measurement plus noise
		
		x_est 	= x_temp_est + K * (z_measured - x_temp_est);
		P 		= (1- K) * P_temp;
		sum_error_kalman 	+= fabs(z_real - x_est);
		sum_error_measure 	+= fabs(z_real-z_measured);

		P_last 		= P;
		x_est_last 	= x_est;
	}
	 
	printf("Total error if using raw measured:  %f\n", sum_error_measure);
	printf("Total error if using kalman filter: %f\n", sum_error_kalman);
	printf("Reduction in error: %d%% \n", 100-(int)((sum_error_kalman / sum_error_measure) * 100));
	 
	return 0;
}
