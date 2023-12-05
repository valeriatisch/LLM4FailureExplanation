from typing import Optional

import requests
import logging


class GitHubClient:
    def __init__(self, token: str, repo: str):
        self.token = token
        self.api_url = f"https://api.github.com/repos/{repo}/issues"

    def get_latest_issue_number(self) -> int:
        try:
            response = requests.get(
                self.api_url, headers={"Authorization": f"token {self.token}"}
            )
            response.raise_for_status()
            issues = response.json()
            return issues[0]["number"] if issues else 0
        except requests.RequestException as e:
            logging.error(f"Error fetching issue: {e}")
            return 0

    def post_comment(self, issue_number: int, comment: str) -> Optional[int]:
        url = f"{self.api_url}/{issue_number}/comments"
        try:
            response = requests.post(
                url,
                json={"body": comment},
                headers={"Authorization": f"token {self.token}"},
            )
            response.raise_for_status()
            return response.status_code
        except requests.RequestException as e:
            logging.error(f"Error posting comment: {e}")
            return None

    def get_issue_content(self, issue_number: int) -> str:
        url = f"{self.api_url}/{issue_number}"
        try:
            response = requests.get(
                url, headers={"Authorization": f"token {self.token}"}
            )
            response.raise_for_status()
            issue = response.json()
            return issue["body"] if "body" in issue else ""
        except requests.RequestException as e:
            logging.error(f"Error fetching issue content: {e}")
            return ""
