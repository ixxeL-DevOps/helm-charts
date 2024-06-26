#!/usr/bin/env python3

import subprocess
import yaml
import re
import os
import git
import github
from github import Auth

_gh = None

DEFAULT_CONFIG = {
    'groups': [
        {
            'title': "💥 Breaking changes",
            'regexp': r'^.*?(feat|chore|fix)!(?:\(\w+\))?!?: .+$',
        },
        {
            'title': "🚀 New Features",
            'regexp': r'^.*?feat(?:\(\w+\))?!?: .+$',
        },
        {
            'title': "📦 Dependency updates",
            'regexp': r'^.*?chore(?:\(\w+\))?!?: .+$',
        },
        {
            'title': "⚠️ Security updates",
            'regexp': r'^.*?sec(?:\(\w+\))?!?: .+$',
        },
        {
            'title': "🐛 Bug fixes",
            'regexp': r'^.*?(fix|refactor)(?:\(\w+\))?!?: .+$',
        },
        {
            'title': "🔨 Refactoring",
            'regexp': r'^.*?refactor(?:\(\w+\))?!?: .+$',
        },
        {
            'title': "♻️ Revert changes",
            'regexp': r'^.*?revert(?:\(\w+\))?!?: .+$',
        },
        {
            'title': "📚 Documentation updates",
            'regexp': r'^.*?docs(?:\(\w+\))?!?: .+$',
        },
        {
            'title': "🏗️ Build process updates",
            'regexp': r'^.*?(build|ci)(?:\(\w+\))?!?: .+$',
        }
    ]
}

def classify_commits(commits: dict[git.Commit, list[git.TagReference]], groups: list[dict[str, str]]) -> dict[str, list[tuple[git.Commit, list[git.TagReference]]]]:
    classified_commits = {group['title']: [] for group in groups}
    classified_commits['🧰 Other work'] = []

    for commit, tags in commits.items():
        commit_message = (commit.message.split('\n', 1)[0]).strip() if commit else None

        matched_group = next((group for group in groups if group.get('regexp') and re.match(group['regexp'], commit_message)), None)

        if matched_group:
            classified_commits.get(matched_group['title']).append((commit, tags))
            print(f"Commit identified as: {commit_message}")
            print(f"Group: {matched_group}\n")
        else:
            classified_commits.get('🧰 Other work').append((commit, tags))

    return classified_commits


def replace_pull_requests(message: str, repo_url: str) -> str:
    def replace(match):
        pull_number = match.group(1)
        return f'in ({repo_url}/pull/{pull_number})'

    return re.sub(r'\(#(\d+)\)$', replace, message)

def gh_instantiate(token: str) -> github.Github:
    if token:
        auth = Auth.Token(token)
        gh = github.Github(auth=auth)
        return gh
    else:
        gh = github.Github()
        return gh


def get_gh_username(author: str, gh_users: dict, email: str = "", access_token: str = "") -> str:
    global _gh

    if not _gh:
        _gh = gh_instantiate(access_token)
    if author in gh_users:
        return ""
    if author == "dependabot[bot]":
        return "dependabot[bot]"
    users = _gh.search_users(author)
    try:
        if len(list(users)) > 1:
            gh_user = users[0].login
            return gh_user
        else:
            gh_user = users[0].login
            return gh_user
    except IndexError:
        print(f"No user found for author: {author}")
        return ""


def generate_markdown(classified_commits: dict[str, list[tuple[git.Commit, list[git.TagReference]]]], lower_tag: str, upper_tag: str, repo_url: str, access_token: str = "") -> str:
    markdown = "## Changelog\n"
    gh_user_dict = {}

    for title, commits_data_list in classified_commits.items():
        if commits_data_list:
            markdown += "### {}\n".format(title)
            for commit, tags in commits_data_list:
                gh_author = get_gh_username(commit.author.name, gh_user_dict, commit.author.email, access_token)
                if gh_author:
                    gh_user_dict[commit.author.name] = gh_author

                tags_info = " {}".format(' '.join(
                    [f'[🏷 {str(tag)}]({repo_url}/tree/{str(tag)})' for tag in
                    tags])) if tags else ""

                commit_msg = (commit.message.split('\n', 1)[0]).strip()
                print(f"SHA: {commit.hexsha}, MSG: {commit_msg}, AUTHOR: {gh_user_dict[commit.author.name]}, EMAIL: {commit.author.email}, TAGS: {tags_info}")
                markdown += "* {}: {} by (@{}){}\n".format(commit.hexsha, commit_msg, gh_user_dict[commit.author.name], tags_info)
            markdown += "\n"
    markdown += "**Full Changelog**: {}/compare/{}...{}".format(repo_url, lower_tag, upper_tag)
    return markdown


def load_user_config(file_path: str) -> dict:
    try:
        with open(file_path, 'r') as config_file:
            return yaml.safe_load(config_file)
    except FileNotFoundError:
        return {}

def merge_configs(default_config: dict, user_config: dict) -> dict:
    merged_config = default_config.copy()
    merged_config.update(user_config)
    return merged_config

def main():
    lower_tag = "aio-1.0.3"
    upper_tag = "aio-1.0.4"
    repo_url = "https://github.com/ixxeL-DevOps/demo-web-py.git"
    access_token = ""

    config_file = ".config.yaml"

    repo = git.Repo(os.getcwd())
    tagmap = {}

    for tag in repo.tags:
        tagmap.setdefault(repo.commit(tag), []).append(tag)

    commits_data = {commit: tagmap.get(commit, []) for commit in repo.iter_commits(f"{lower_tag}...{upper_tag}")}

    for commit, tags in commits_data.items():
        commit_msg = commit.message.split('\n', 1)[0]
        print(f"Commit : {commit} Msg: {commit_msg} Tags: {tags}")

    config = merge_configs(DEFAULT_CONFIG, load_user_config(config_file))

    classified_commits = classify_commits(commits_data, config['groups'])

    final_markdown = generate_markdown(classified_commits, lower_tag, upper_tag, repo_url, access_token)

    print(final_markdown)

    with open('CHANGELOG.md', 'w') as file:
        file.write(final_markdown)

if __name__ == "__main__":
    main()
