import setuptools

with open("README.md","r",encoding = "utf-8") as f:
    long_description = f.read()


__version__ ="0.0.0"

REPO_NAME = "Text_Summarizer"
AUTHOR_USER_NAME = "dorasambhrant"
SRC_REPO = "Text_Summarizer"
AUTHOR_EMAIL = "ssambhrant2001@gmail.com"


setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "Text Summarizer using Natural Language Processing",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_url = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    },
    packages = setuptools.find_packages(where="src"),
    package_dir = {"": "src"}
)
