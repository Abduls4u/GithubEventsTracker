#!/usr/bin/env python3

import requests
import sys


def fetch_github_events(username):
    url = f"https://api.github.com/users/{username}/events"
    headers = {"Accept": "application/vnd.github+json"}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        events = response.json()

        if not events:
            print(f"No public events found for {username}")
            return
        print(f"Here comes the recent activities of {username}")
        for i, event in enumerate(events, 1):
            event_type = event.get('type', 'Unknown')
            repo_name = event.get('repo', {}).get('name', 'Unknown Repo')
            created_at = event.get('created_at', 'Unknown Time')
            print(f"{i}. [{event_type}] on [{repo_name}] at [{created_at}]")


    except requests.exceptions.HTTPError as error:
        if error == 404:
            print(f"No user named {username}")

        else:
            print(f"HTTP Error: {error}")
    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


def main():
    if len(sys.argv) != 2:
        print('Usage: python3 githubActivity.py <user_name>')
    else:
        fetch_github_events(sys.argv[1])



if __name__ == "__main__":
    main()