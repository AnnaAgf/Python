*** Settings ***
Library  BuiltIn
Library  OperatingSystem
Library  Process
Library  MyLib.py

Test Setup  Run Server And Check
Test Teardown  Stop Server And Check

*** Variables ***
${file}
${host} =  localhost
${port} =  9090

*** Test Cases ***
Hello
    [Tags]  DEBUG
    Hello  Ann

Send Hello To The Server
    [Tags]
    Start
    Send File  hello  ${host}  ${port}
    Wait

*** Keywords ***
Run Server And Check
    Run Server
    Check Process Running

Stop Server And Check
    Stop Server
    Check Process Stopped

Run Server
    ${handle} =  Start Process  python3  server.py  --host\=${host}  --port\=${port}  alias=RunServer

Check Process Running
    #${output_process} =  Wait Until Keyword Succeeds  10 sec  2 sec  Run  ps -a | grep python3
    Sleep  1s
    ${output_port} =  Run  netstat -a | grep ${host}:${port}
    Should Contain Any  ${output_port}   ${host}  ${port}  LISTEN
    ${output_process} =  Run  ps -x | grep python3
    Log  ${output_process}
    Should Contain Any  ${output_process}  python3  ${host}  ${port}

Stop Server
    Switch Process  RunServer
    ${result} =  Terminate Process
    Should Be Equal As Integers  ${result.rc}  -15

Check Process Stopped
    ${output_process} =  Run  ps -a | grep python3
    Should Not Contain  ${output_process}  ${host}  ${port}
    ${output_port} =  Run  netstat -a | grep ${host}:${port}
    Should Not Contain Any  ${output_port}   ${host}  ${port}  LISTEN
