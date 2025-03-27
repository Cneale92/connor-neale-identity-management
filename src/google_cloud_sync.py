from google.cloud import iam
from google.auth import compute_engine

def sync_users_to_google_workspace():
    credentials = compute_engine.Credentials()
    client = iam.iam_v1.IdentityAwareProxyOAuthClient(credentials=credentials)

    # Example: Create a user (this would typically be more advanced, syncing users or fetching them)
    user = client.create_user(name="newuser@example.com", password="password")
    print(f"User {user['name']} created successfully")

if __name__ == "__main__":
    sync_users_to_google_workspace()