from pathlib import Path


def get_project_root():
    """Returns project root folder."""
    return Path(__file__).parent.parent

RT_STUDIO_TMP_PATH = "template/rt_studio/"