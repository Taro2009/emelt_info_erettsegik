Program szavak;
uses crt;

type Tletraszo = record
       szo    : string[5];
       kozepe : string[3];
     end; //Tletraszo

     Tletratomb = array[1..1000] of Tletraszo;

var maganhangzok : set of char = ['a', 'e', 'i', 'o', 'u'];

procedure f1;
var szo : string;
     cv : byte;
begin //f1
  Write('Adjon meg egy sz¢t: ');
  ReadLn(szo);
  cv := 1;
  While (length(szo) >= cv) AND NOT (szo[cv] in maganhangzok) do
    inc (cv);
  if length(szo) < cv
    then Write('Nincs')
    else Write('Van');
  WriteLn(' benne mag nhangz¢.');
end; //f1

procedure f2;
var   fv : text;
     szo : string;
     max : string;
begin //f2
  max  := '';
  Assign(fv, 'szoveg.txt');
  Reset(fv);
  While not eof(fv) do
    begin
      ReadLn(fv,szo);
      if length(szo)>length(max) then max := szo;
    end; // while not eof
  WriteLn ('A leghosszabb sz¢: '+max+' hossza: ', length(max));
  Close(fv)
end; //f2

procedure f3;
var            fv : text;
       ma, ms, cv : byte;
              szo : string;
  magan, osszesen : word;
begin //f3
  magan := 0;
  osszesen := 0;
  Assign(fv, 'szoveg.txt');
  Reset(fv);
  While not eof(fv) do
    begin
      ReadLn(fv, szo);
      inc(osszesen);
      ma := 0; ms := 0;
      for cv := 1 to length(szo) do
        if szo[cv] in maganhangzok
          then inc(ma)
          else inc(ms);
      if ma>ms
        then
          begin
            Write(szo, ' ');
            inc(magan);
          end;
    end; //while not eof
  WriteLn;
  WriteLn(magan,'/',osszesen,' : ',100*magan/osszesen:8:2,'%');
  Close(fv);
end; //f3

procedure f4_5;
  procedure csere(var a,b: Tletraszo);
  var s : Tletraszo;
  begin //csere
    s:=a; a:=b; b:=s;
  end; //csere

var           t : Tletratomb;
    N, cv1, cv2 : word;
         fv,fki : text;
         h, szo : string;
            van : boolean;
begin //f4_5
  Write ('K‚rek 3 karaktert a l‚traszavakhoz: ');
  ReadLn(h);
  N := 0;
  Assign(fv,'szoveg.txt');
  Reset(fv);
  While not eof(fv) do
    begin
      ReadLn(fv, szo);
      if length(szo)=5
        then
          begin
            inc(N);
            t[N].szo := szo;
            t[N].kozepe := szo[2]+szo[3]+szo[4];
            if t[N].kozepe=h then Write(t[N].szo, ' ');
          end; //length(szo)=5
    end; //while not eof
  WriteLn;
  Close(fv);
  if N>0 then
    begin
      //rendez‚s
      for cv1 := 1 to N do
        for cv2 := 1 to cv1 do
          if t[cv1].kozepe<t[cv2].kozepe then csere(t[cv1],t[cv2]);

      Assign(fki,'letra.txt');
      Rewrite(fki);
      van := false;
      for cv1 := 2 to N do
        begin
          if t[cv1].kozepe = t[cv1-1].kozepe
            then
              begin
                WriteLn(fki, t[cv1-1].szo);
                van := True;
              end
            else
              begin
                if van then
                  begin
                    WriteLn(fki, t[cv1-1].szo);
                    WriteLn(fki, '');
                  end;
                van := False;
              end;
        end; //cv : 2--> N
      Close(fki);
    end; //N>0
end; //f4_5


begin
  ClrScr;
  WriteLn('1. feladat');
  f1;
  WriteLn('2. feladat');
  f2;
  WriteLn('3. feladat');
  f3;
  WriteLn('4. feladat');
  f4_5;
  WriteLn('Nyomjon meg egy gombot a befejez‚shez!');
  ReadKey();
end.