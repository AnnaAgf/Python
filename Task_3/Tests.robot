*** Settings ***
Library  BuiltIn
Library  OperatingSystem
Library  Process
Library  Player.py

Test Setup  Run Server And Check
Test Teardown  Stop Server And Check

*** Variables ***
${file} =  chain_cfu_B.pcap
${host} =  localhost
${port} =  9090
${python} =  python3

*** Test Cases ***
Play Pcap File
    [Tags]
    Start
    Send File  ./${file}  ${host}  ${port}
    Wait

*** Keywords ***
Run Server And Check
    Run Server
    Check Process Running

Stop Server And Check
    Stop Server
    Check Process Stopped

Run Server
    ${handle} =  Start Process  ${python}  server.py  --host\=${host}  --port\=${port}  alias=RunServer

Check Process Running
    ${output_port} =  Wait Until Keyword Succeeds  2 s  50ms  Check Opened Port
    ${output_process} =  Run  ps -x | grep ${python}
    Should Contain Any  ${output_process}  ${python}  ${host}  ${port}

Check Opened Port
    ${output_port} =  Run  netstat -a | grep ${host}:${port}
    Should Contain Any  ${output_port}   ${host}  ${port}  LISTEN

Stop Server
    Switch Process  RunServer
    ${result} =  Terminate Process
    Should Be Equal As Integers  ${result.rc}  -15

Check Process Stopped
    ${output_process} =  Run  ps -a | grep ${python}
    Should Not Contain  ${output_process}  ${host}  ${port}
    ${output_port} =  Run  netstat -a | grep ${host}:${port}
    Should Not Contain Any  ${output_port}   ${host}  ${port}  LISTEN
