#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

struct egyjarmu {
	int ora, perc, mperc;
	string rendszam;
};

int idomp(egyjarmu j)
{
	return (j.ora*60+j.perc)*60+j.mperc;
}
string ir(int ertek)
{
	stringstream szam;
	if (ertek<10) { szam << 0; }
	szam << ertek;
	return szam.str();
}
int main(int argc, char **argv)
{
	egyjarmu jarmu[1000];
	// 1. feladat beolvasás
	ifstream be;
	be.open("jarmu.txt");
	int i=0;
	while (be >> jarmu[i].ora >> jarmu[i].perc >> jarmu[i].mperc >> jarmu[i].rendszam)
	{
		i++;
	}
	int db=i;
	be.close();

	// 2. feladat
	cout << "2. feladat" << endl;
	cout << "A munkaido hossza: " << jarmu[db-1].ora-jarmu[0].ora+1 << " ora" << endl;
	
	// 3. feladat
	cout << "3. feladat" << endl;
	int aktora=-1; 
	for (int i=0; i<db; i++)
	{
		if (jarmu[i].ora>aktora)
		{
			aktora=jarmu[i].ora;
			cout << aktora << " ora: " << jarmu[i].rendszam << endl;
		}
	}
	
	// 4. feladat
	cout << "4. feladat" << endl;
	int busz=0, kamion=0, motor=0;
	for (int i=0; i<db; i++)
	{
		if ( jarmu[i].rendszam[0]=='B') busz++;
		if ( jarmu[i].rendszam[0]=='K') kamion++;
		if ( jarmu[i].rendszam[0]=='M') motor++;
	}
	cout << "busz " << busz << "db" << endl
			<< "kamion " << kamion << "db" << endl
			<< "motor " << motor << "db" << endl
			<< "szemelygepkocsi " << db-busz-kamion-motor << "db" << endl;

	// 5. feladat
	cout << "5. feladat" << endl;
	int max=0; // feltételezzük, hogy az első az
	for (int i=1; i<db-1; i++)
	{
		if ( (idomp(jarmu[i+1])-idomp(jarmu[i])) > (idomp(jarmu[max+1])-idomp(jarmu[max]) ) )
		{
			max=i;
		}
	}
	cout << "A leghosszabb forgalommentes idoszak "
			<< jarmu[max].ora << ":" << jarmu[max].perc << ":" << jarmu[max].mperc << " - "
			<< jarmu[max+1].ora << ":" << jarmu[max+1].perc << ":" << jarmu[max+1].mperc << endl;

	// 6. feladat
	cout << "6. feladat" << endl;
	string keresett;
	cout << "Add meg a keresett rendszamot! ";
	cin >> keresett;
	for (int i=0; i<db; i++)
	{
		bool illik=true;
		for (int j=0; j<keresett.size(); j++)
		{
			illik = illik and 
					( (keresett[j]==jarmu[i].rendszam[j]) or (keresett[j]=='*') );
		}
		if (illik)
		{
			cout << jarmu[i].rendszam << endl;
		}
	}
	
	// 7. feladat
	cout << "7. feladat" << endl;
	ofstream ki;
	ki.open("vizsgalt.txt");
	int vizsgkezd=-300;
	int v=0;
	while (v<db)
	{
		if(vizsgkezd+300<=idomp(jarmu[v]))
		{
			ki << ir(jarmu[v].ora) << " " << ir(jarmu[v].perc) << " " << ir(jarmu[v].mperc)
			<< " " << jarmu[v].rendszam << endl;
			vizsgkezd=idomp(jarmu[v]);
		}
		v++;
	}
	ki.close();
	return 0;
}
