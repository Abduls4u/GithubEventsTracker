
# GitHub Activity CLI

A simple command-line Python app that fetches and displays the **most recent public GitHub activities** of a specified user using the GitHub REST API.

## 🛠 Features

- Fetches the latest public events (activities) of any GitHub user
- Outputs event type, repository name, and timestamp
- Lightweight and easy to run from the terminal
- No authentication required (up to 60 requests/hour)

## 🚀 How to Use

### 1. Clone or Download This Repository

```bash
git clone https://github.com/Abduls4u/GithubEventsTracker.git
cd GithubEventsTracker
````

### 2. Ensure You Have Python Installed

```bash
python3 --version
```

### 3. Install Requirements

This script uses the `requests` library. Install it if you don't have it:

```bash
pip install requests
```

### 4. Run the Script

```bash
python3 githubActivity.py <github_username>
```

**Example:**

```bash
python3 githubActivity.py torvalds
```

## 📌 Sample Output

```
Here comes the recent activities of torvalds
1. [PushEvent] on [torvalds/linux] at [2025-06-22T10:45:12Z]
2. [CreateEvent] on [torvalds/test-repo] at [2025-06-20T14:12:05Z]
3. [WatchEvent] on [some/repo] at [2025-06-19T18:03:33Z]
```

## ⚠️ Notes

* The script fetches up to 30 events by default, but only the top few are typically recent and relevant.
* GitHub rate-limits unauthenticated API calls to **60 requests per hour per IP**. For higher usage, you can modify the script to use a personal access token.

## 📄 License

MIT License

Here's a link to the project on roadmap.sh (https://roadmap.sh/projects/github-user-activity)
```

