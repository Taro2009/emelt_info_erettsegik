program anagram;

uses
  crt;

Type TSzavak = Array[1..300] of String[30];
Var Szavak : TSzavak;
    N, i, j, k, Db, Max : Integer;
    Szo, Szo1, Szo2, s : String;
    volt : Boolean;
    FKi : Text;

Function abcbe( Szo : String) : String;
Var i, j : byte;
    cs : char;
Begin
   for i := 1 to Length(Szo) - 1 do
     for j := i+1 to Length(Szo)  do
         if Szo[i] > Szo[j]  then
            begin
              cs := Szo[i];
              Szo[i] := Szo[j];
              Szo[j] := cs;
            end;
   abcbe := Szo;
End;

Procedure fajlbe_abcfajlki(Var N: integer; Var Szavak : TSzavak);
Var
  FBe, FKi : Text;
  i : integer;
Begin
   Assign(FBe,'szotar.txt');
   Assign(FKi, 'abc.txt');
   Reset(FBe);
   ReWrite(FKi);
   i := 1;
     While not eof(FBe) DO
       Begin
        Readln(FBe,Szo);
        Writeln(Fki,abcbe(Szo));
        Szavak[i] := Szo;
        inc(i);
       End;
     N := i-1;
   Close(FBe);
   Close(FKi);
End;

Procedure karakterszamolas(Var Db : integer; Var karakterek: String);
Var Szo : String;
      h : set of char;
      i : Byte;
Begin
  Write('Adja meg a szoveget: ');
  Readln(Szo); h := [];
  Db:= 0;
  Karakterek := '';
  for i := 1 to length(Szo) do
    Begin
       if  not (Szo[i] in h) then
         Begin
            Include(h,Szo[i]);
            inc(Db);
            karakterek := karakterek + Szo[i];
         End;
    End;
End;

Function anagrammae(Sz1,Sz2 : String) : Boolean;
Begin
  anagrammae := ( abcbe(Sz1) = abcbe(Sz2) );
End;

Procedure otodik(Szo: String; Szavak: TSzavak; N : integer; Kiir : String);
Var S : String;
    volt : Boolean;
    i : integer;
Begin
   S := abcbe(Szo);
   volt := false;
   for i := 1 to N do
     Begin
       if anagrammae(S,abcbe(Szavak[i])) then
         Begin
           Writeln(Szavak[i]);
           Volt := true;
         End;
      End;
      if not volt then Writeln(Kiir);
End;

Procedure rendez_hatodik(Szavak: TSzavak; N: integer; var Max : integer);
Var i, j, k : integer;
    seged : String;
Begin
  k := 1;
  for i := 1 to N-1 do
    for j := i+1 to N do
      Begin
        if length(Szavak[i]) < Length(Szavak[j]) then
           Begin
             seged := Szavak[i];
             Szavak[i] := Szavak[j];
             Szavak[j] := Seged;
           End;
         if anagrammae(Szavak[i],Szavak[j]) then
           Begin
             seged := Szavak[k];
             Szavak[k] := Szavak[j];
             Szavak[j] := seged;
             inc(k);
           End
         Else k := i + 1;
      End;
  i := 1; Max := Length(Szavak[i]);
  Writeln(Szavak[i]);
  While (i<=N) and (length(Szavak[i])=length(Szavak[i+1])) Do
   Begin
     Writeln(Szavak[i+1]);
     inc(i);
   End;
End;

(*-----------------------------------------------------------*)


begin
 clrscr;
(* 1. feladat  *)
  Writeln('1. feladat');
  karakterszamolas(Db,S);
  Writeln('A szoban ', Db, ' darab kulonbozo karakter szerepelt, ezek: ',S);fajlbe_abcfajlki(N,Szavak);

(* 2. és 3. feladat *)
  Writeln('2. es 3. feladat');
  fajlbe_abcfajlki(N, Szavak);
  Writeln('Kesz');

(* 4. feladat *)
  Writeln('4. feladat');
  Write('Elso szo: ');
  Readln(Szo1);
  Write('Masodik szo: ');
  Readln(Szo2);
  if anagrammae(Szo1,Szo2) then
    Writeln('Anagramma')
  else
    Writeln('Nem anagramma');

(* 5. feladat *)
   Writeln('5. feladat');
   Write('Adjon meg egy szot: ');
   Readln(Szo);
   Writeln('A(z) ', Szo, ' anagrammai:');
   otodik(Szo,Szavak,N, 'Nincs anagramma a szotarban');

(* 6. feladat *)
  Writeln('6. feladat');
  Writeln('A leghosszabb szo (szavak): ');
  rendez_hatodik(Szavak, N, Max);

(* 7. feladat *)
  Writeln('7. feladat');
  Assign(FKi,'rendezve.txt');
  Rewrite(FKi);
  for i := 2 to Max do
    Begin
      volt := false;
      for j := 1 to N do
        if length(Szavak[j])=i then
           begin
             volt := true;
             Write(FKi,Szavak[j]+' ');
             for k := 1 to N do
                 if anagrammae(Szavak[j],Szavak[k]) and (szavak[j] <> szavak[k])
                  then Begin
                      Write(FKi,Szavak[k]+' ');
                      Szavak[k] := '-';
                 End;
             Writeln(Fki);
           end;
       if volt then Writeln(Fki);
    End;
  Close(FKi);
  Writeln('Kesz');
Readln;


end.
