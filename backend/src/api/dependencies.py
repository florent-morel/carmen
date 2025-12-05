"""
Dependencies of the app, currently, auth_strategies to Argos
"""

import os
from backend.src.crud.crud_thanos_app import CrudThanosApp
from backend.src.core.yaml_config_loader import config
from backend.src.crud.auth_strategies.aad_auth import AAD
from backend.src.crud.auth_strategies.none_auth import NoAuth


def get_app_dao() -> CrudThanosApp | None:
    """
    Function to get an instance of CrudApp, which is a data access object (DAO).

    Returns:
        CrudThanosApp: An instance of CrudApp representing the data access object.
    """
    api_config = config.carmen_api
    if not api_config:
        return
    # Use NoAuth during testing to avoid real HTTP requests to Azure AD
    if os.getenv("TEST_ENV", "False").lower() in ("true", "1", "t"):
        return CrudThanosApp(api_config.thanos_url, NoAuth(), api_config.verify_ssl)

    if api_config.authentication == "azure":
        return CrudThanosApp(
            api_config.thanos_url, AAD(api_config), api_config.verify_ssl
        )
    return CrudThanosApp(api_config.thanos_url, NoAuth(), api_config.verify_ssl)


# AppDao = Annotated[CrudApp, Depends(get_app_dao)] DO: Apply this dependency function for a better practise
AppDao = get_app_dao()
