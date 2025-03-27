import msal

def authenticate_to_azure():
    app = msal.ConfidentialClientApplication(
        "client_id",
        authority="https://login.microsoftonline.com/tenant_id",
        client_credential="client_secret"
    )

    result = app.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])

    if "access_token" in result:
        print("Authentication successful!")
        return result["access_token"]
    else:
        print("Authentication failed")
        return None

if __name__ == "__main__":
    authenticate_to_azure()
