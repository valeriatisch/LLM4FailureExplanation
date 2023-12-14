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
    # TODO:
    #  idea1: explain failed workflow as comment in PR
    #  idea2: if user comments on GPTs answer with question, answer, otherwise ignore
    #   -> preserve conversation context for asynchronous conversations
    #      Allows us to preprocess the context before resuming the conversation
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
            github_client.set_gpt_response(latest_issue, response)
            github_client.post_comment(
                latest_issue,
                f"This is an automated comment by ChatGPT (version: gpt-3.5-turbo). \n\n"
                f"{response}",
            )
            logging.info("Response generated and posted")
            last_checked_issue = latest_issue
        issues = github_client.issues
        # TODO: track issues that have been responded to for new comments
        if issues:
            for issue_number in issues:
                comments = github_client.get_issue_comments(issue_number)
                user_response = github_client.find_user_response(comments)
                print(user_response)
                # TODO: put whole conversation together, give to GPT & it should only respond if it's a question
        time.sleep(2)


if __name__ == "__main__":
    main()
