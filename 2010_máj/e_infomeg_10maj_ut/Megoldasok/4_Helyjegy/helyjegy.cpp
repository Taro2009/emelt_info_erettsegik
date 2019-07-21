#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;

struct Tjegy{ int sorszam, hely, tol, ig; };
typedef Tjegy Tjegytomb[500];

void fszam(int i);
int fizet5(int tav_, int szakaszar_);
void beolvasas(int& db_, int& hossz_, int& osszeg_, Tjegytomb& jegy_);
void utolsovasarlo(Tjegytomb jegy_, int db_);
void vegig(Tjegytomb jegy_, int db_, int hossz_);
void bevetel(Tjegytomb jegy_, int db_, int szakaszar_);
void utolso(Tjegytomb jegy_, int db_, int hossz_);
void megallok(Tjegytomb jegy_, int db_, int hossz_);
void kihol(Tjegytomb jegy_, int db_);

int main(int argc, char *argv[])
{   
    Tjegytomb jegy;
    int db, hossz, szakaszar;
    fszam(1);
    beolvasas(db, hossz, szakaszar, jegy);
    fszam(2);
    utolsovasarlo(jegy, db);
    fszam(3);
    vegig(jegy, db, hossz);
    fszam(4);
    bevetel(jegy, db, szakaszar);
    fszam(5);
    utolso(jegy, db, hossz);
    fszam(6);
    megallok(jegy, db, hossz);
    fszam(7);
    kihol(jegy, db);
    system("PAUSE");
    return EXIT_SUCCESS;
}

void fszam(int i)
{
     cout << i << ".feladat: " << endl;
}
int fizet5(int tav_, int szakaszar_)
{
    int ar, maradek;
    if ( tav_%10==0 ) { ar=(tav_/10)*szakaszar_; } else { ar=(tav_/10+1)*szakaszar_; }
    maradek=ar%5;
    if (maradek<3) { return ar-maradek; }
    else { return ar-maradek+5; }
}
void beolvasas(int& db_, int& hossz_, int& szakaszar_, Tjegytomb& jegy_)
{
     fstream be;
     be.open("eladott.txt", ios::in);
     be >> db_ >> hossz_ >> szakaszar_;
     for (int i=0; i<db_; i++) {
         jegy_[i].sorszam=i+1;
         be >> jegy_[i].hely >> jegy_[i].tol >> jegy_[i].ig;
     }
     be.close();
}
void utolsovasarlo(Tjegytomb jegy_, int db_)
{
     cout << "Az utolo jegyvasarlo a " << endl; 
     cout << jegy_[db_-1].hely << ". helyen ult," ;
     cout << " es " << jegy_[db_-1].ig-jegy_[db_-1].tol << " km-t utazott." << endl;
}
void vegig(Tjegytomb jegy_, int db_, int hossz_)
{
     cout << "A teljes utat vegigutazo jegyvasarlok: " << endl;
     for (int i=0; i<db_; i++) {
         if ( (jegy_[i].tol==0) and (jegy_[i].ig==hossz_) ) {
              cout << i+1 << " " ;
         }
     }
     cout << endl;
}
void bevetel(Tjegytomb jegy_, int db_, int szakaszar_)
{
     long mind=0;
     for (int i=0; i<db_; i++) {
        mind+=fizet5(jegy_[i].ig-jegy_[i].tol, szakaszar_);
     }
     cout << "A tarsasag bevetele: " << mind << " Ft." << endl;
}
void utolso(Tjegytomb jegy_, int db_, int hossz_)
{
     int fel=0, le=0;
     int uthely=0;
     for (int i=0; i<db_; i++) {
        if ( jegy_[i].tol>uthely ) { uthely=jegy_[i].tol; }
        if ( (jegy_[i].ig>uthely) and (jegy_[i].ig<hossz_) ) { uthely=jegy_[i].ig; }
     }
     for (int i=0; i<db_; i++) {
        if ( jegy_[i].tol==uthely ) { fel++; }
        if ( jegy_[i].ig==uthely ) { le++; }
     }
     cout << "Az utolso megalloban " << fel << " fo szallt fel es " << le << " fo szallt le." << endl;
}
void megallok(Tjegytomb jegy_, int db_, int hossz_)
{
     int mszam=0;
     bool megallo[201]={false};
     for (int i=0; i<db_; i++) {
         megallo[jegy_[i].tol]=true;
         megallo[jegy_[i].ig]=true;
     }
     for (int i=1; i<hossz_; i++) { if (megallo[i]) { mszam++; } }
     cout << "A busz megalloinak szama: " << mszam << endl;
}
void kihol(Tjegytomb jegy_, int db_)
{
     fstream ki;
     int ules[48]={0};
     int hol;
     cout << "Adja meg, az ut mely kilometeren keri az utaslistat! ";
     cin >> hol;
     for (int i=0; i<db_; i++) {
         if ( (jegy_[i].tol<=hol) and (jegy_[i].ig>hol) ) { 
              ules[jegy_[i].hely-1]=jegy_[i].sorszam; 
         }
     }
     ki.open("kihol.txt", ios::out);
     for (int i=0; i<48; i++) {
         ki << i+1 << ". ules: " ;
         if ( ules[i]>0 ) { ki << ules[i] << ". utas" << endl;}
         else { ki << " ures" << endl; } 
     }
     ki.close();
}
