#include <iostream>
#include <fstream>
#include <sstream>
using namespace std;

struct egyhivas
{
	int kezd, befejez;
};

int mpbe(int o, int p, int mp)
{
	return (o*60+p)*60+mp;
}
string idopont(int mp)
{
	stringstream puffer;
	puffer << mp/3600 << " " << (mp%3600)/60 << " " << mp%60;
	string ido;
	getline(puffer, ido);
	return ido;
}
int main(int argc, char **argv)
{
	// F2. beolvasas
	ifstream be;
	be.open("hivas.txt");
	egyhivas hivas[2000];
	int db=0;
	int ko, kp, kmp, vo, vp, vmp;
	while(be >> ko >> kp >> kmp >> vo >> vp >> vmp)
	{
		hivas[db].kezd=mpbe(ko, kp, kmp);
		hivas[db].befejez=mpbe(vo, vp, vmp);
		db++;
	}
	// F3. orankent
	cout << endl << "3. feladat" << endl;
	int ora[24]={0};
	for(int i=0; i<db; i++)
	{
		ora[hivas[i].kezd/3600]++;
	}
	for(int i=0; i<24; i++)
	{
		if(ora[i]>0)
		{
			cout << i << " ora " << ora[i] << " hivas" << endl;
		}
	}
	
	// F4. 
	cout << endl << "4. feladat" << endl;
	int maxhivo=0;
	for(int i=1; i<db; i++)
	{
		if ( hivas[i].befejez-hivas[i].kezd > hivas[maxhivo].befejez-hivas[maxhivo].kezd)
		{
			maxhivo=i;
		}
	}
	cout << "A leghosszabb ideig vonalban levo hivo " << maxhivo+1 << ". sorban szerepel, " 
			<< "a beszelgetes hossza: " << hivas[maxhivo].befejez-hivas[maxhivo].kezd << " masodperc."<< endl;
	
	// F5. 
	cout << endl << "5. feladat" << endl;
	int o, p, mp;
	cout << "Adjon meg egy idopontot! (ora perc masodperc) ";
	cin >> o >> p >> mp;
	int keresett=mpbe(o, p, mp);
	int varakozo=0, beszelo=-1;
	for(int i=db-1; i>=0; i--)
	{
		if(hivas[i].kezd<=keresett and keresett<hivas[i].befejez)
		{
			varakozo++;
			beszelo=i;
		}
	}
	if(beszelo>-1)
	{
		cout << "A varakozok szama: " << varakozo-1;
		cout << " a beszelo a " << beszelo+1 << ". hivo." << endl;
	}
	else
	{
		cout << "Nincs beszelo" << endl;
	}
	
	// F6. 
	cout << endl << "6. feladat" << endl;
	int mbefejez=mpbe(12, 0, 0);

	int vegso=0, vegsoelott=0;
	for(int i=0; i<db; i++)
	{
		if( (hivas[i].kezd<mbefejez) and (hivas[i].befejez>hivas[vegso].befejez))
		{
			vegsoelott=vegso;
			vegso=i;
		}
	}
	cout << "Az utolso hivo adatai a(z) " << vegso+1 << ". sorban vannak, " 
			<< max(0,hivas[vegsoelott].befejez-hivas[vegso].kezd) << " masodpercig vart." << endl;
	
	// F7.
	int mkezd=mpbe(8, 0, 0);
	ofstream ki;
	ki.open("sikeres.txt");
	int beszel=0;
	while(hivas[beszel].befejez<=mkezd) { beszel++; }
	ki << beszel+1 << " " << idopont(max(mkezd, hivas[beszel].kezd)) << " " << idopont(hivas[beszel].befejez) << endl;
	for(int i=0; i<db; i++)
	{
		if( (hivas[i].befejez>hivas[beszel].befejez) and (hivas[i].kezd<=mbefejez))
		{
			ki << i+1 << " " << idopont(max(hivas[i].kezd, hivas[beszel].befejez)) << " " << idopont(hivas[i].befejez) << endl;
			beszel=i;
		}
	}
	ki.close();
	
	return 0;
}
