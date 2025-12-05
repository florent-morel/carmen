*** Settings ***
Resource          ../../resources/keywords.robot


*** Test Cases ***

energy_consumed_values
    [Tags]    endpoint  run  engine  energy_consumed
    ${response}    Run Engine For App and Paas    ${APPLICATION}    ${PAAS}
    Verify Response Status Code     ${response}    200
    ${engine_response}    Set Variable    ${response.json()}
    Verify Field Exists And Value Count    ${engine_response}    energy_consumed    6

carbon_emitted_values
    [Tags]    endpoint  run  engine  carbon_emitted
    ${response}    Run Engine For App and Paas    ${APPLICATION}    ${PAAS}
    Verify Response Status Code     ${response}    200
    ${engine_response}    Set Variable    ${response.json()}
    Verify Field Exists And Value Count    ${engine_response}    carbon_emitted    6

requested_cpu_values 
    [Tags]     endpoint run engine requested_cpu_values 
    ${response}    Run Engine For App and Paas    ${APPLICATION}    ${PAAS}
    Verify Response Status Code    ${response}    200
    ${engine_response}     Set Variable     ${response.json()}
    Verify Field Exists And Value Count    ${engine_response}    requested_cpu    6

cpu_power_values 
    [Tags]     endpoint run engine cpu_power_values 
    ${response}    Run Engine For App and Paas    ${APPLICATION}    ${PAAS}
    Verify Response Status Code    ${response}    200 
    ${engine_response}    Set Variable     ${response.json()}
    Verify Field Exists And Value Count    ${engine_response}    cpu_power    6

cpu_energy_values 
    [Tags]    endpoint run engine cpu_energy_values 
    ${response}    Run Engine For App and Paas    ${APPLICATION}    ${PAAS}
    Verify Response Status Code    ${response}    200
    ${engine_response}    Set Variable    ${response.json()}
    Verify Field Exists And Value Count    ${engine_response}    cpu_energy    6








