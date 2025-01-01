import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description=f.read()
    
__version__="0.0.0"

REPO_NAME = "garbage-classification-using-mlflow-and-dvc"
AUTHORE_USER_NAME = "GauravBosamiya"
SRC_REPO = "GarbageCassification"
AUTHOR_EMAIL = "gauravbosamiya9@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHORE_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for CNN app",
    long_description_content_type="text/markdown",
    url=f"https://github.com{AUTHORE_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker":f"https://github.com/{AUTHORE_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
    
)