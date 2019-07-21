program Szinkep_pr;

uses
  Forms, Interfaces,
  Szinkep in 'Szinkep.pas' {Form1};

{$R *.RES}

begin
  Application.Initialize;
  Application.CreateForm(TForm1, Form1);
  Application.Run;
end.
