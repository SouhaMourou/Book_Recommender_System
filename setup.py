from setuptools import setup
REPO_NAME = "Books_Recommender_System"
AUTHOR_USER_NAME = "Souha_Mourou"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ['streamlit', 'numpy', 'pandas', 'scikit-learn']

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name=SRC_REPO,
    version="0.0.1",
    author="Souha MOUROU",
    description="A small local packages for ML based books recommendations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SouhaMourou",
    author_email="mourousouha@gmail.com",
    packages=[SRC_REPO],
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)
