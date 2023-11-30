import os
import time
import logging

from dotenv import load_dotenv

from bugxplainer.ghclient import GitHubClient
from bugxplainer.gptclient import ChatGPTClient

logging.basicConfig(level=logging.INFO)

load_dotenv()
repo = os.getenv("REPO")
gh_token = os.getenv("GITHUB_TOKEN")
api_key = os.getenv("OPENAI_API_KEY")


def main():
    logging.info("Starting BugXplainer")
    github_client = GitHubClient(gh_token, repo)
    chatgpt_client = ChatGPTClient(api_key)

    last_checked_issue = github_client.get_latest_issue_number()
    while True:
        latest_issue = github_client.get_latest_issue_number()
        if latest_issue > last_checked_issue:
            logging.info(f"New issue found: {latest_issue}")
            issue_content = github_client.get_issue_content(latest_issue)
            if issue_content == "":
                logging.info(f"Empty issue, skipping {latest_issue}")
                continue
            response = chatgpt_client.generate_response(issue_content)
            github_client.post_comment(
                latest_issue,
                f"This is an automated comment by ChatGPT (version: gpt-3.5-turbo). \n\n"
                f"{response}",
            )
            logging.info("Response generated and posted")
            last_checked_issue = latest_issue
        time.sleep(2)


if __name__ == "__main__":
    main()
