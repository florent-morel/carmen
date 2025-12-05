*** Settings ***
Resource          ../../resources/keywords.robot

*** Test Cases ***
namespaces_values
    [Tags]    endpoint  apps  namespaces_values
    ${response}    Get Namespaces    ${APPLICATION}    ${PAAS}
    Verify Response Status Code     ${response}    200
    ${engine_response}    Set Variable    ${response.json()}
    Verify Field Values Are Strings    ${engine_response}    namespaces
    Should Contain    ${engine_response}[namespaces]    ${NAMESPACE}

namespaces_and_clusters_values
    [Tags]    endpoint  apps  namespaces_and_clusters_values
    ${response}    Get Namespaces And Clusters    ${APPLICATION}
    Verify Response Status Code     ${response}    200
    ${engine_response}    Set Variable    ${response.json()}
    Verify Field Values Are Strings    ${engine_response}    namespaces    clusters   
    Should Contain    ${engine_response}[clusters]    ${PAAS}
    Should Contain    ${engine_response}[namespaces]    ${NAMESPACE}

clusters_and_applications_values
    [Tags]    endpoint  apps  clusters_and_applications_values
    ${response}    Get Resources
    Verify Response Status Code     ${response}    200
    ${engine_response}    Set Variable    ${response.json()}
    Verify Field Values Are Strings    ${engine_response}    clusters    applications
    Should Contain    ${engine_response}[clusters]    ${PAAS}
    Should Contain    ${engine_response}[applications]    ${APPLICATION}
    ${clusters_len}    Get Length    ${engine_response}[clusters]
    Should Be True    ${clusters_len} > 100
    ${apps_len}    Get Length    ${engine_response}[applications]
    Should Be True    ${apps_len} > 100