*** Settings ***
Library           RequestsLibrary
Variables         variables.py

Library    ${PYTHONLIBPATH}/site-packages/robot/libraries/Collections.py
Library    ${PYTHONLIBPATH}/site-packages/robot/libraries/String.py

*** Keywords ***
Verify Response Status Code
    [Arguments]    ${response}    ${expected_status_code}
    Should Be Equal As Strings    ${response.status_code}    ${expected_status_code}

Get Resources
    ${response}    GET    ${HOST}/apps/
    RETURN    ${response}

Get Namespaces
    [Arguments]    ${app}    ${paas}
    ${response}    GET    url=${HOST}/apps/?app=${app}&paas=${paas}
    RETURN    ${response}

Get Namespaces and Clusters
    [Arguments]    ${app}
    ${response}    GET    url=${HOST}/apps/?app=${app}
    RETURN    ${response}

Run Engine For App and Paas
    [Arguments]    ${app}    ${paas}
    ${response}    GET    url=${HOST}/apps/run-engine/?app=${app}&paas=${paas}
    RETURN    ${response}

Verify Field Exists And Value Count
    [Arguments]    ${engine_response}    ${field_name}    ${expected_count}    
    # Verify that engine_response is a valid list and contains at least one item

    Should Be True    ${engine_response} is not None
    Should Be True    len(${engine_response}) > 0
    # Retrieve the first item from the list
    ${first_item}    Set Variable    ${engine_response}[0]
    # Verify that the specified field is present in the first item
    Dictionary Should Contain Key    ${first_item}    ${field_name}
    # Retrieve the specified field
    ${field_values}    Set Variable    ${first_item}[${field_name}]
    # New: Handle both list and single value cases
    ${is_list}    Evaluate    isinstance($field_values, list)
    IF    ${is_list}
        # Iterate over each value in the field value list
        FOR    ${value}    IN    @{field_values}
        # Check if the value is a float and greater than 0
            Should Be True    isinstance(${value}, float)
            Should Be True    ${value} >= 0
        END
        # Verify the number of items in the specified field
        ${field_count}    Get Length    ${field_values}
    ELSE
        # Handle single value case - but log a warning
        Should Be True    isinstance(${field_values}, float)
        Should Be True    ${field_values} >= 0
        ${field_count}    Evaluate     1
    END
    # Convert the expected count to an integer
    ${expected_count_int}    Evaluate    int(${expected_count})
    # Compare the actual count with the expected count
    Should Be Equal    ${field_count}    ${expected_count_int}

Verify Field Values Are Strings
    [Arguments]    ${engine_response}    @{field_names}
    # Verify that engine_response is a valid list and contains at least one item
    Should Be True    ${engine_response} is not None
    Should Be True    len(${engine_response}) > 0
    # Iterate over each field_name provided
    FOR    ${field_name}    IN    @{field_names}
        # Verify that the specified field is present in the engine_response
        Dictionary Should Contain Key    ${engine_response}    ${field_name}
        # Retrieve the specified field
        ${field_values}    Set Variable    ${engine_response['${field_name}']}
        # Iterate over each value in the field value list
        FOR    ${value}    IN    @{field_values}
            # Verify if the value is a string
            Should Be String    ${value}    Value should be a string, but it was ${value}
        END
    END