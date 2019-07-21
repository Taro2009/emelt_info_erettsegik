program futar;

uses crt;

type Tadat = record
            tav : byte;
             ft : word;
end; //adat record

var         t : array[1..7,1..40] of Tadat;
            N : array[1..7] of word = (0,0,0,0,0,0,0);
      Napitav : array[1..7] of word = (0,0,0,0,0,0,0);
        Nszum : word = 0;
      Elsonap : byte = 8;
    Utolsonap : byte = 0;
   Legtobbfuv : byte = 1;
    Teljesdij : longint = 0;

procedure s(a:byte);
begin
  Writeln(a,'. feladat:');
end; //s

procedure f1();
var           fv : text;
    nap, fuv, ta : byte;
              ar : word;
begin
  Assign(fv, 'tavok.txt');
  Reset(fv);
  While not eof(fv) do
    begin
      inc(Nszum);
      Read(fv, nap);
      Read(fv, fuv);
      Read(fv, ta);
      t[nap,fuv].tav:= ta;
      if ta <= 2 then ar:= 500
        else if ta<=5 then ar:= 700
               else if ta<=10 then ar:= 900
                      else if ta<=20 then ar:= 1400
                             else ar:= 2000;
      t[nap,fuv].ft:= ar;
      inc(Teljesdij, ar);
      if fuv>N[nap] then N[nap]:= fuv;
      If fuv>N[Legtobbfuv] then legtobbfuv:= nap;
      if nap<Elsonap then Elsonap:= nap;
      if nap>Utolsonap then Utolsonap:= nap;
      inc(Napitav[nap], ta);
    end; //not eof
  Close(fv);
end; //f1

procedure f2();
begin
  WriteLn('A het elso utja ',t[Elsonap,1].tav,' km hosszu volt');
end; //f2

procedure f3();
begin
  WriteLn('A het utolso utja ',t[Utolsonap,N[Utolsonap]].tav,' km hosszu volt');
end; //f3

procedure f4();
var cv : byte;
begin
  Write('Ez(ek)en a nap(ok)on nem dolgozott a futar: ');
  for cv := 1 to 7 do
    if N[cv]=0 then Write(cv, ' ');
  WriteLn;
end; //f4

procedure f5();
begin
  WriteLn('A het ', Legtobbfuv, '. napjan kellett a legtobb helyre menni.');
end; //f5

procedure f6();
var cv : byte;
begin
  for cv := 1 to 7 do
    WriteLn(cv,'. nap: ', Napitav[cv], ' km');
end; //f6

procedure f7();
var ta : byte;
    ar : word;
begin
  Write('Mekkora uthoz tartozo dijazast hatarozzam meg? ');
  Readln(ta);
  if ta <= 2 then ar:= 500
    else if ta<=5 then ar:= 700
           else if ta<=10 then ar:= 900
                  else if ta<=20 then ar:= 1400
                         else ar:= 2000;
  Writeln(ar, ' Ft');
end; //f7

procedure f8();
var       fv: text;
    nap, fuv: byte;
begin
  Assign(fv, 'dijazas.txt');
  Rewrite(fv);
  For nap := 1 to 7 do
    For fuv := 1 to N[nap] do
      Writeln(fv,nap,'. nap ', fuv, '. ut: ', t[nap,fuv].ft, ' Ft');
  Close(fv);
  WriteLn('A fajlba iras befejezodott');
end; //f8

procedure f9();
begin
  WriteLn('A futar a heti munkajaert ', Teljesdij, ' Ft-ot kap.');
end; //f9

BEGIN
  clrscr;
  s(1);  f1();
  s(2);  f2();
  s(3);  f3();
  s(4);  f4();
  s(5);  f5();
  s(6);  f6();
  s(7);  f7();
  s(8);  f8();
  s(9);  f9();
  Readkey;
END.
