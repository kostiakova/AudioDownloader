; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "AudioDownloader"
#define MyAppVersion "1.0"
#define MyAppPublisher "Kostinus"
#define MyAppURL "https://www.example.com/"
#define MyAppExeName "SFMLTry2.exe"
#define MyAppAssocName MyAppName + ""
#define MyAppAssocExt ".msi"
#define MyAppAssocKey StringChange(MyAppAssocName, " ", "") + MyAppAssocExt

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{7B2922CE-6DA6-4ABF-86EC-63A0F04BC82C}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppName}
ChangesAssociations=yes
DisableProgramGroupPage=yes
; Remove the following line to run in administrative install mode (install for all users.)
PrivilegesRequired=lowest
OutputBaseFilename=mysetup
SetupIconFile=C:\Users\User\PycharmProjects\ConCenter\icon.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "D:\Projects\vs c++\SFMLTry2\x64\Debug\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Projects\vs c++\SFMLTry2\x64\Debug\arial.ttf"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Projects\vs c++\SFMLTry2\x64\Debug\engine.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Projects\vs c++\SFMLTry2\x64\Debug\openal32.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Projects\vs c++\SFMLTry2\x64\Debug\sfml-graphics-2.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Projects\vs c++\SFMLTry2\x64\Debug\sfml-graphics-d-2.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Projects\vs c++\SFMLTry2\x64\Debug\sfml-system-2.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Projects\vs c++\SFMLTry2\x64\Debug\sfml-system-d-2.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Projects\vs c++\SFMLTry2\x64\Debug\SFMLTry2.pdb"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Projects\vs c++\SFMLTry2\x64\Debug\sfml-window-2.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Projects\vs c++\SFMLTry2\x64\Debug\sfml-window-d-2.dll"; DestDir: "{app}"; Flags: ignoreversion
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Registry]
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocExt}\OpenWithProgids"; ValueType: string; ValueName: "{#MyAppAssocKey}"; ValueData: ""; Flags: uninsdeletevalue
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}"; ValueType: string; ValueName: ""; ValueData: "{#MyAppAssocName}"; Flags: uninsdeletekey
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}\DefaultIcon"; ValueType: string; ValueName: ""; ValueData: "{app}\{#MyAppExeName},0"
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}\shell\open\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%1"""
Root: HKA; Subkey: "Software\Classes\Applications\{#MyAppExeName}\SupportedTypes"; ValueType: string; ValueName: ".myp"; ValueData: ""

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent
