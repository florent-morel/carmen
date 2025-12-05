*** Settings ***
Resource          ../resources/keywords.robot

*** Test Cases ***
get_available_resources_endpoint
    [Tags]    endpoint  available  resources
    ${response}    Get Resources
    Verify Response Status Code     ${response}    200
    ${resources}    Set Variable    ${response.json()}
    Should Be True    ${resources} is not None

run_engine_endpoint
    [Tags]    endpoint  run  engine
    ${response}    Run Engine For App and Paas    ${APPLICATION}    ${PAAS}
    Verify Response Status Code     ${response}    200
    ${engine_response}    Set Variable    ${response.json()}
    Should Be True    ${engine_response} is not None

run_engine_hardware_endpoint
    [Tags]    endpoint run engine Hardware
    ${response}    GET   url=${HOST}/hardware/run-engine-hardware/?virtual_machine-type=Standard_E16as_v4&cpu-load=50&duration=3600
    Verify Response Status Code     ${response}    200
    ${engine_response}    Set Variable    ${response.json()}
    Should Be True    ${engine_response} is not None