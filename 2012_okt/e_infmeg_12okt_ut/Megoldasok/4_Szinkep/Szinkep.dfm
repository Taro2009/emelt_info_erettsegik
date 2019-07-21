object Form1: TForm1
  Left = 319
  Height = 275
  Top = 125
  Width = 428
  Caption = 'Színkép feladat'
  ClientHeight = 275
  ClientWidth = 428
  Color = clBtnFace
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'MS Sans Serif'
  LCLVersion = '0.9.30.4'
  object Image1: TImage
    Left = 16
    Height = 50
    Top = 16
    Width = 50
  end
  object Label1: TLabel
    Left = 80
    Height = 20
    Top = 16
    Width = 46
    Alignment = taCenter
    AutoSize = False
    Caption = 'Vörös:'
    Font.CharSet = EASTEUROPE_CHARSET
    Font.Color = clWindowText
    Font.Height = -13
    Font.Name = 'Times New Roman'
    Layout = tlCenter
    ParentColor = False
    ParentFont = False
  end
  object Label2: TLabel
    Left = 80
    Height = 20
    Top = 40
    Width = 46
    Alignment = taCenter
    AutoSize = False
    Caption = 'Zöld:'
    Font.CharSet = EASTEUROPE_CHARSET
    Font.Color = clWindowText
    Font.Height = -13
    Font.Name = 'Times New Roman'
    Layout = tlCenter
    ParentColor = False
    ParentFont = False
  end
  object Label3: TLabel
    Left = 80
    Height = 20
    Top = 64
    Width = 46
    Alignment = taCenter
    AutoSize = False
    Caption = 'Kék:'
    Font.CharSet = EASTEUROPE_CHARSET
    Font.Color = clWindowText
    Font.Height = -13
    Font.Name = 'Times New Roman'
    Layout = tlCenter
    ParentColor = False
    ParentFont = False
  end
  object Image2: TImage
    Left = 192
    Height = 50
    Top = 16
    Width = 50
  end
  object Kepbeolvas_Button: TButton
    Left = 280
    Height = 25
    Top = 8
    Width = 121
    Caption = '1. feladat Képbeolvasás'
    OnClick = Kepbeolvas_ButtonClick
    TabOrder = 0
  end
  object Kepment_Button: TButton
    Left = 280
    Height = 25
    Top = 168
    Width = 121
    Caption = '6. feladat Képment'
    Enabled = False
    OnClick = Kepment_ButtonClick
    TabOrder = 1
  end
  object Voros_Edit: TEdit
    Left = 128
    Height = 21
    Top = 16
    Width = 49
    TabOrder = 2
    Text = '0'
  end
  object Zold_Edit: TEdit
    Left = 128
    Height = 21
    Top = 40
    Width = 49
    TabOrder = 3
    Text = '0'
  end
  object Kek_Edit: TEdit
    Left = 128
    Height = 21
    Top = 64
    Width = 49
    TabOrder = 4
    Text = '0'
  end
  object Pixelkeres_Button: TButton
    Left = 280
    Height = 25
    Top = 40
    Width = 121
    Caption = '2. feladat Pixelkeres'
    Enabled = False
    OnClick = Pixelkeres_ButtonClick
    TabOrder = 5
  end
  object Pixelszamol_Button: TButton
    Left = 280
    Height = 25
    Top = 72
    Width = 121
    Caption = '3. feladat Pixelszámol'
    Enabled = False
    OnClick = Pixelszamol_ButtonClick
    TabOrder = 6
  end
  object SzinMax_Button: TButton
    Left = 280
    Height = 25
    Top = 104
    Width = 121
    Caption = '4. feladat Színmaximum'
    Enabled = False
    OnClick = SzinMax_ButtonClick
    TabOrder = 7
  end
  object Memo1: TMemo
    Left = 8
    Height = 121
    Top = 112
    Width = 241
    TabOrder = 8
  end
  object Keret_Button: TButton
    Left = 280
    Height = 25
    Top = 136
    Width = 121
    Caption = '5. feladat Keret'
    Enabled = False
    OnClick = Keret_ButtonClick
    TabOrder = 9
  end
  object Sarga_Button: TButton
    Left = 280
    Height = 25
    Top = 200
    Width = 121
    Caption = '7. feladat Sárga'
    Enabled = False
    OnClick = Sarga_ButtonClick
    TabOrder = 10
  end
  object SaveDialog1: TSaveDialog
    FileName = 'keretes.txt'
    left = 16
    top = 68
  end
  object OpenDialog1: TOpenDialog
    left = 48
    top = 72
  end
end
