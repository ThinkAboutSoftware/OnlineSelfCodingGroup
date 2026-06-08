"""
One-time script to get Google Calendar OAuth2 refresh token.

Prerequisites:
  1. Google Cloud Console에서 OAuth2 Client ID 생성 (유형: Desktop app)
  2. pip install google-auth-oauthlib

Usage:
  python get_calendar_oauth_token.py <client_id> <client_secret>

After running:
  출력된 세 값을 GitHub repo secrets에 추가:
  - GOOGLE_OAUTH2_CLIENT_ID
  - GOOGLE_OAUTH2_CLIENT_SECRET
  - GOOGLE_OAUTH2_REFRESH_TOKEN
"""
import sys
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/calendar']


def main():
    if len(sys.argv) != 3:
        print("Usage: python get_calendar_oauth_token.py <client_id> <client_secret>")
        sys.exit(1)

    client_id, client_secret = sys.argv[1], sys.argv[2]

    flow = InstalledAppFlow.from_client_config(
        {
            "installed": {
                "client_id": client_id,
                "client_secret": client_secret,
                "redirect_uris": ["http://localhost"],
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
            }
        },
        SCOPES,
    )

    creds = flow.run_local_server(port=0)

    print("\n--- GitHub Secret Values ---")
    print(f"GOOGLE_OAUTH2_CLIENT_ID:     {client_id}")
    print(f"GOOGLE_OAUTH2_CLIENT_SECRET: {client_secret}")
    print(f"GOOGLE_OAUTH2_REFRESH_TOKEN: {creds.refresh_token}")


if __name__ == "__main__":
    main()
