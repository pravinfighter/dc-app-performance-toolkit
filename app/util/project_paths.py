import datetime
import os
from pathlib import Path


def __get_jira_yml():
    return Path(__file__).parents[1] / "jira.yml"


def __get_datasets():
    return Path(__file__).parents[1] / "datasets"


def __get_jira_datasets():
    return __get_datasets() / "jira"


def __get_jira_dataset(file_name):
    return __get_jira_datasets() / file_name


def __get_confluence_yml():
    return Path(__file__).parents[1] / "confluence.yml"


def __get_bitbucket_yml():
    return Path(__file__).parents[1] / "bitbucket.yml"


def __get_bitbucket_datasets():
    return __get_datasets() / "bitbucket"


def __get_confluence_datasets():
    return __get_datasets() / "confluence"


def __get_confluence_dataset(file_name):
    return __get_confluence_datasets() / file_name


def __get_bitbucket_dataset(file_name):
    return __get_bitbucket_datasets() / file_name


def __get_taurus_artifacts_dir():
    if 'TAURUS_ARTIFACTS_DIR' in os.environ:
        return Path(os.environ.get('TAURUS_ARTIFACTS_DIR'))
    else:
        results_dir_name = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        local_run_results = Path(f'results/{results_dir_name}_local')
        local_run_results.mkdir(parents=True)
        return local_run_results


JIRA_YML = __get_jira_yml()
JIRA_DATASETS = __get_jira_datasets()
JIRA_DATASET_JQLS = __get_jira_dataset('jqls.csv')
JIRA_DATASET_SCRUM_BOARDS = __get_jira_dataset('scrum-boards.csv')
JIRA_DATASET_KANBAN_BOARDS = __get_jira_dataset('kanban-boards.csv')
JIRA_DATASET_USERS = __get_jira_dataset('users.csv')
JIRA_DATASET_ISSUES = __get_jira_dataset('issues.csv')
JIRA_DATASET_PROJECTS = __get_jira_dataset('projects.csv')
JIRA_DATASET_CUSTOM_ISSUES = __get_jira_dataset('custom-issues.csv')
JIRA_DATASET_VERSIONS = __get_jira_dataset('versions.csv')


CONFLUENCE_YML = __get_confluence_yml()
CONFLUENCE_DATASETS = __get_confluence_datasets()
CONFLUENCE_USERS = __get_confluence_dataset('users.csv')
CONFLUENCE_PAGES = __get_confluence_dataset('pages.csv')
CONFLUENCE_BLOGS = __get_confluence_dataset('blogs.csv')
CONFLUENCE_STATIC_CONTENT = __get_confluence_dataset('static-content/files_upload.csv')
CONFLUENCE_CUSTOM_PAGES = __get_confluence_dataset('custom_pages.csv')

BITBUCKET_YML = __get_bitbucket_yml()
BITBUCKET_DATASETS = __get_bitbucket_datasets()
BITBUCKET_USERS = __get_bitbucket_dataset('users.csv')
BITBUCKET_PROJECTS = __get_bitbucket_dataset('projects.csv')
BITBUCKET_REPOS = __get_bitbucket_dataset('repos.csv')
BITBUCKET_PRS = __get_bitbucket_dataset('pull_requests.csv')

ENV_TAURUS_ARTIFACT_DIR = __get_taurus_artifacts_dir()