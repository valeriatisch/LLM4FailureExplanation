from typing import Optional

import requests
import logging


class GitHubClient:
    def __init__(self, token: str, repo: str):
        self.headers = {"Authorization": f"token {token}"}
        self.api_url = f"https://api.github.com/repos/{repo}/issues"
        self.issues = {}

    def get_latest_issue_number(self) -> int:
        try:
            response = requests.get(self.api_url, headers=self.headers)
            response.raise_for_status()
            issues = response.json()
            issue_number = 0
            if issues:
                issue_number = issues[0]["number"]
            return issue_number
        except requests.RequestException as e:
            logging.error(f"Error fetching issue: {e}")
            return 0

    def add_issue_to_cache(self, issue_number: int) -> None:
        self.issues[issue_number] = {
            "body": None,
            "comments": None,
        }

    def post_comment(self, issue_number: int, comment: str) -> Optional[int]:
        url = f"{self.api_url}/{issue_number}/comments"
        try:
            response = requests.post(
                url,
                json={"body": comment},
                headers=self.headers,
            )
            response.raise_for_status()
            return response.status_code
        except requests.RequestException as e:
            logging.error(f"Error posting comment: {e}")
            return None

    def get_issue_content(self, issue_number: int) -> str:
        url = f"{self.api_url}/{issue_number}"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            issue = response.json()
            body = ""
            if "body" in issue:
                body = issue["body"]
                self.issues[issue_number]["body"] = body
            return body
        except requests.RequestException as e:
            logging.error(f"Error fetching issue content: {e}")
            return ""

    def update_comments(self, issue_number: int, comments: list = None) -> None:
        comments = comments or self.get_issue_comments(issue_number)
        self.issues[issue_number]["comments"] = comments

    def get_issue_comments(self, issue_number: int) -> list:
        comments_url = f"{self.api_url}/{issue_number}/comments"
        response = requests.get(comments_url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            logging.error(
                f"Failed to fetch comments for issue {issue_number}: {response.status_code}, {response.text}"
            )
            return []
