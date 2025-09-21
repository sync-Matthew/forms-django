from profiles.models import UserProfile
from syncqb.json_quickbase import JsonQuickbaseClient
from typing import Any, List

class ExtendedJsonQuickbaseClient(JsonQuickbaseClient):
    """
    Extended JSON Quickbase Client with additional methods.
    """

    def clone_user_token(self) -> dict[str, Any]:
        """
        Clones the existing user token for this JSON client.

        Quickbase JSON API - Clone User Token
        https://developer.quickbase.com/operation/cloneUserToken
        """
        return self._request(
            "https://api.quickbase.com/v1/usertoken/clone",
            "post",
            self.headers,
            data={
                "name": "SyncBot",
                "label": "SyncBot's User Token",
            },
            json=True,
        )


    def delete_user_token(self) -> dict[str, Any]:
        """
        Deletes the user token for this JSON client.

        Quickbase JSON API - Delete User Token
        https://developer.quickbase.com/operation/deleteUserToken
        """
        return self._request(
            "https://api.quickbase.com/v1/usertoken",
            "delete",
            self.headers,
            json=True,
        )


    def list_apps(self, profile: UserProfile) -> List[dict[str, Any]]:
        """
        Lists all Quickbase apps for the user associated with this client.
        """
        # The response from cloning a user token includes all apps associated with the token being cloned
        # This is a workaround to get the list of apps since there's no direct API to list apps with just a user token
        clone_response = self.clone_user_token()
        
        # Clean up the cloned token after use
        updated_client = ExtendedJsonQuickbaseClient(
            realmhost=f"{profile.realm}.quickbase.com",
            base_url=f"https://{profile.realm}.quickbase.com",
            user_token=clone_response.get('token'),
        )
        updated_client.delete_user_token()

        return clone_response.get('apps', [])


    def list_tables(self, app_id: str) -> List[dict[str, Any]]:
        """
        Lists all Quickbase tables for a Quickbase app.
        """
        return self._request(
            f"https://api.quickbase.com/v1/tables?appId={app_id}",
            "get",
            self.headers,
            json=True,
        )


    def list_fields(self, table_id: str) -> List[dict[str, Any]]:
        """
        Lists all fields for a Quickbase table.
        """
        return self._request(
            f"https://api.quickbase.com/v1/fields?tableId={table_id}",
            "get",
            self.headers,
            json=True,
        )


def get_quickbase_client(realm: str, user_token: str) -> ExtendedJsonQuickbaseClient:
    return ExtendedJsonQuickbaseClient(
        realmhost=f"{realm}.quickbase.com",
        base_url=f"https://{realm}.quickbase.com",
        user_token=user_token,
    )
