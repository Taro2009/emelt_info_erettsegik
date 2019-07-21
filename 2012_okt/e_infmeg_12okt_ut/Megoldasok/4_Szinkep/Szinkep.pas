unit Szinkep;

interface

uses
  Windows, SysUtils, Classes, Graphics, Controls, Forms, Dialogs,
  StdCtrls, ExtCtrls;

type
  TPixel = Record
    R,G,B : byte;
  end;
  TPict = Array[0..49,0..49] of TPixel;
  TForm1 = class(TForm)
    Kepbeolvas_Button: TButton;
    Image1: TImage;
    Image2: TImage;
    SaveDialog1: TSaveDialog;
    Kepment_Button: TButton;
    OpenDialog1: TOpenDialog;
    Label1: TLabel;
    Voros_Edit: TEdit;
    Label2: TLabel;
    Zold_Edit: TEdit;
    Label3: TLabel;
    Kek_Edit: TEdit;
    Pixelkeres_Button: TButton;
    Pixelszamol_Button: TButton;
    SzinMax_Button: TButton;
    Memo1: TMemo;
    Keret_Button: TButton;
    Sarga_Button: TButton;
    procedure FajlBeolvas(Var Kep : TPict);
    procedure KepFajlba(Kep : TPict);
    Function VanPixel(BeP: TPixel; Kep : TPict) : Boolean;
    Function PixelHasonlit(a,b :TPixel) : Boolean;
    procedure Kepbeolvas_ButtonClick(Sender: TObject);
    procedure Kepment_ButtonClick(Sender: TObject);
    procedure Pixelkeres_ButtonClick(Sender: TObject);
    procedure Pixelszamol_ButtonClick(Sender: TObject);
    procedure SzinMax_ButtonClick(Sender: TObject);
    procedure Keret_ButtonClick(Sender: TObject);
    procedure Sarga_ButtonClick(Sender: TObject);

  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form1 : TForm1;
    Kep : TPict;
implementation

{$R *.DFM}

procedure TForm1.Kepbeolvas_ButtonClick(Sender: TObject);
Var i, j : integer;
Begin
 FajlBeolvas(Kep);
 for i := 0 to 49 Do
   for j := 0 to 49 Do
     Image1.Canvas.Pixels[j,i] := RGB(Kep[i,j].r,Kep[i,j].g,Kep[i,j].b);
  Pixelkeres_Button.Enabled := true;
  Pixelszamol_Button.Enabled := true;
  SzinMax_Button.Enabled := true;
  Keret_Button.Enabled := true;
  Kepment_Button.Enabled := true;
  Sarga_Button.Enabled := true;
  Memo1.Lines.Add('1. feladat - fájlbeolvasás - KÉSZ!');
end;

procedure TForm1.KepFajlba(Kep: TPict);
Var FN : Textfile;
    i,j : Byte;
begin
  if SaveDialog1.Execute then
    Begin
      Assignfile(FN,SaveDialog1.FileName);
      Rewrite(FN);
        For i := 0 to 49 Do
           For j := 0 to 49 Do
             Begin
               Write(FN, Kep[i,j].R);
               Write(FN,' ');
               Write(FN, Kep[i,j].G);
               Write(FN,' ');
               Writeln(FN, Kep[i,j].B);
             End;
      CloseFile(FN);
    End;
end;

procedure TForm1.Kepment_ButtonClick(Sender: TObject);
begin
 KepFajlba(Kep);
 Memo1.Lines.Add('-----------------------------------------');
 Memo1.Lines.Add('6. feladat - Kép mentése - KÉSZ!');
end;

procedure TForm1.FajlBeolvas(var Kep: TPict);
Var FN : TextFile;
    i,j :Integer;
begin
 if OpenDialog1.Execute then
    Begin
      Assignfile(FN,OpenDialog1.FileName);
      Reset(FN);
        For i := 0 to 49 Do
          Begin
           For j := 0 to 49 Do
             Begin
               Read(FN,kep[i,j].R);
               Read(FN,kep[i,j].G);
               Read(FN,kep[i,j].B);
             End;
          End;
      CloseFile(FN);
    End;
end;

Function Tform1.Pixelhasonlit(a,b :TPixel) : Boolean;
Var egyezik : Boolean;
Begin
  egyezik := false;
  If (a.R = b.R) AND (a.G = b.G) AND (a.B = b.B) then egyezik := true;
  PixelHasonlit := egyezik;
End;

Function Tform1.VanPixel(BeP: TPixel; Kep : TPict) : Boolean;
Var i, j : Byte;
    Van : Boolean;
Begin
  i := 0;
  Van := false;
  While (i<=49) AND not van Do
    Begin
      j := 0;
      While (j<=49) AND Not PixelHasonlit(BeP, Kep[i,j]) do
        inc(j);
      Van := (j<=49) AND PixelHasonlit(BeP, Kep[i,j]);
      inc(i);
    End;
  VanPixel := van;

End;
procedure TForm1.Pixelkeres_ButtonClick(Sender: TObject);
Var BePixel : TPixel;
begin
 Memo1.Lines.Add('-----------------------------------------');
 Memo1.Lines.Add('2. feladat');
   With BePixel DO
     Begin
       R := StrToInt(Voros_Edit.Text);
       G := StrToInt(Zold_Edit.Text);
       B := StrToInt(Kek_Edit.Text);
     End;
   if VanPixel(BePixel, kep) then
      Memo1.Lines.Add('A megadott szín megtalálható a képen')
   else
      Memo1.Lines.Add('A megadott szín nincs a képen');
end;

procedure TForm1.Pixelszamol_ButtonClick(Sender: TObject);
Var P : TPixel;
    sordb, oszlopdb, i : Byte;
begin
 Memo1.Lines.Add('-----------------------------------------');
 Memo1.Lines.Add('3. feladat');
  P := Kep[35-1,8-1];
  sordb := 0; oszlopdb := 0;
  for i := 0 to 49 Do
   Begin
    If PixelHasonlit(P,Kep[35-1,i]) then inc(sordb);
    If PixelHasonlit(P,Kep[i,8-1]) then inc(oszlopdb);
   End;
  Memo1.Lines.Add('Sorban: ' + IntToStr(sordb) +
                    ' Oszlopban: ' + IntToStr(oszlopdb));
end;

procedure TForm1.SzinMax_ButtonClick(Sender: TObject);
Var Max : Array[1..3] of integer;
    maxind : Integer;
    i,j : Byte;
    P : TPixel;
begin
 Memo1.Lines.Add('-----------------------------------------');
 Memo1.Lines.Add('4. feladat');
   for i := 1 to 3 do Max[i] := 0;
   for i := 0 to 49 Do
        for j := 0 to 49 Do
           Begin
             P.R := 255; P.G := 0; P.B := 0;
             If PixelHasonlit(P,Kep[i,j]) then
                 inc(Max[1]);
             P.R := 0; P.G := 255;
             if PixelHasonlit(P,Kep[i,j]) then
                 inc(Max[2]);
             P.G := 0; P.B := 255;
             if PixelHasonlit(P,Kep[i,j]) then
                 inc(Max[3]);
           End;
   maxind := 1;
   for i := 2 to 3 do if Max[i] > Max[Maxind] then Maxind := i;
   Case maxind of
     1 : Memo1.Lines.Add('Vörös');
     2 : Memo1.Lines.Add('Zöld');
     3 : Memo1.Lines.Add('Kék');
   End;
end;

procedure TForm1.Keret_ButtonClick(Sender: TObject);
Var i, j : Byte;
begin
 Memo1.Lines.Add('-----------------------------------------');
 Memo1.Lines.Add('5. feladat - Keret kész!');

  for i := 0 to 49 do
    for j := 0 to 49 do
       begin
         if (i<3) OR (i>46) OR (j<3) OR (j>46) then
           Begin
             Kep[i,j].R := 0;
             Kep[i,j].G := 0;
             Kep[i,j].B := 0;
           End;
         Image2.Canvas.Pixels[j,i] := RGB(Kep[i,j].r,Kep[i,j].g,Kep[i,j].b);
       end;
end;

procedure TForm1.Sarga_ButtonClick(Sender: TObject);
Var i, j, SDB : Integer;
    kpj, vpj, kpi, vpi : Byte;
    Sarga : TPixel;
begin
 Memo1.Lines.Add('-----------------------------------------');
 Memo1.Lines.Add('7. feladat');

   Sarga.R := 255; Sarga.G := 255; Sarga.B := 0;
   i := 0; j := 0;
   While not PixelHasonlit(Sarga, Kep[i,j]) DO
     Begin
       j := 0;
       While (j <=49) AND not PixelHasonlit(Sarga, Kep[i,j]) DO inc(j);
       if not PixelHasonlit(Sarga, Kep[i,j]) then inc(i);
     End;
   Memo1.Lines.Add('Kezd: ' + inttostr(i+1) + ', ' + inttostr(j+1));
   kpj := j; kpi := i;
   i := 49 ; j := 49;
   While not PixelHasonlit(Sarga, Kep[i,j]) DO
     Begin
       j := 49;
       While (j>=0) AND not PixelHasonlit(Sarga, Kep[i,j]) DO dec(j);
       if not PixelHasonlit(Sarga, Kep[i,j]) then dec(i);
     End;
   Memo1.Lines.Add ('Vége: ' + inttostr(i+1) + ', ' + inttostr(j+1));
   vpj := j; vpi := i;
   SDB := (vpi-kpi+1)*(vpj-kpj+1);
   Memo1.Lines.Add ('Képpontok száma: ' + inttostr(SDB));
end;

end.
