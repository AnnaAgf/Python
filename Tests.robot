*** Settings ***
Library  Process
Library  MyLib.py

Test Setup  Run Server
Test Teardown  Stop Server

*** Variables ***
${file}
${host} =  localhost
${port} =  9090

*** Test Cases ***
Hello
    [Tags]
    Log  Hello
    Hello  Ann

Send Hello To The Server
    [Tags]  DEBUG

*** Keywords ***
Run Server
    ${result} =  Start Process  python  C:${/}Users${/}Anna.Agafonova${/}PycharmProjects${/}Python${/}Robot${/}server.py  --host\=${host}  --port\=${port}
    ${cancel_process} =  Terminate Process  ${result}
    Should Be Equal As Integers  ${cancel_process.rc}  0


Stop Server
