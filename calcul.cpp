#include <iostream>
#include <fstream>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <time.h>
#include <math.h> 

using namespace std;

const int iteration = 2000;
const double times = 0.3;
const double g = 4.;
const int numberofplanet = 100;
const double e = 25.0;
const double e2 = 700;
const double e3 = pow(e2, 2);
double p[numberofplanet][10];


void planet() { //donne une position et une masse  aleatoire au planet

	srand((unsigned)time(0));
	int randomx, randomy, randomz, randommasse;
	for (int index = 0; index < numberofplanet; index++) {
		randomx = (rand() % 2000) - 1000;
		randomy = (rand() % 2000) - 1000;
		randomz = (rand() % 2000) - 1000;
		randommasse = (rand() % 9) + 1;
		p[index][0] = randomx;
		p[index][1] = randomy;
		p[index][2] = randomz;
		p[index][9] = randommasse;
		//cout << randomx << " x " << index << endl << randomy << " y " << index << endl << randomz << " z " << index << endl;
	}
}

ofstream fichier("gravity.cvs");
void calcul() {
	for (int k = 0;k < numberofplanet;k++) {
		p[k][6] = 0.0;
		p[k][7] = 0.0;
		p[k][8] = 0.0;
	}
	for (int i = 0;i < numberofplanet;i++) {
		for (int j = i;j < numberofplanet;j++) {
			double r_2 = pow(p[i][0] - p[j][0], 2) + pow(p[i][1] - p[j][1], 2) + pow(p[i][2] - p[j][2], 2);
			if (r_2 == 0 || r_2 > e3) continue;
			double Fx = g * p[j][9] * p[i][9] * (p[i][0] - p[j][0]) / (pow(r_2 + e, 1.5));
			double Fy = g * p[j][9] * p[i][9] * (p[i][1] - p[j][1]) / (pow(r_2 + e, 1.5));
			double Fz = g * p[j][9] * p[i][9] * (p[i][2] - p[j][2]) / (pow(r_2 + e, 1.5));
			p[j][6] += Fx;
			p[j][7] += Fy;
			p[j][8] += Fz;
			p[i][6] -= Fx;
			p[i][7] -= Fy;
			p[i][8] -= Fz;
		}
	}
	for (int h = 0;h < numberofplanet;h++) {
		p[h][3] += p[h][6] / p[h][9] * times;
		p[h][4] += p[h][7] / p[h][9] * times;
		p[h][5] += p[h][8] / p[h][9] * times;
		p[h][0] += p[h][3] * times;
		p[h][1] += p[h][4] * times;
		p[h][2] += p[h][5] * times;
		fichier << p[h][0] << "," << p[h][1] << "," << p[h][2] << endl;
	}
}


int main() {
	planet();
	clock_t tStart = clock();
	for (int w = 0;w < iteration;w++) {
		calcul();
		cout << endl;
		cout << w + 1;
	}
	cout << endl;
	cout << (double(clock() - tStart) / 1000) << " seconde";
}