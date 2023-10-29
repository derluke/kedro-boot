from setuptools import find_packages, setup


def _parse_requirements(path, encoding="utf-8"):
    with open(path, encoding=encoding) as file_handler:
        requirements = [
            x.strip() for x in file_handler if x.strip() and not x.startswith("-r")
        ]
    return requirements


# get the dependencies and installs
base_requirements = _parse_requirements("requirements.txt")


# Get the long description from the README file
with open("README.md", encoding="utf-8") as file_handler:
    README = file_handler.read()

setup(
    name="kedro-boot",
    version="0.0.1",
    description="A framework that streamlines the integration of Kedro projects with various applications. It serves as a bridge that shape the interactions between an application and Kedro's resources",
    license="Apache Software License (Apache 2.0)",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/takikadiri/kedro-boot",
    author="Takieddine Kadiri",
    python_requires=">=3.7",
    packages=find_packages(exclude=["docs", "tests"]),
    include_package_data=True,
    install_requires=base_requirements,
    extras_require={
        "doc": [
            "sphinx>=4.5.0,<8.0.0",
            "sphinx_rtd_theme>=1.0,<1.4",
            "sphinx-markdown-tables~=0.0.15",
            "sphinx-click>=3.1,<5.1",
            "sphinx_copybutton~=0.5.0",
            "myst-parser>=0.17.2,<2.1.0",
        ],
        "test": [
            "pytest>=5.4.0, <8.0.0",
            "pytest-cov>=2.8.0, <5.0.0",
            "pytest-lazy-fixture>=0.6.0, <1.0.0",
            "pytest-mock>=3.1.0, <4.0.0",
            "ruff==0.1.3",
            "scikit-learn>=0.23.0, <1.4.0",
            "kedro-datasets[pandas.CSVDataSet]",
        ],
        "dev": [
            "pre-commit>=2.0.0,<4.0.0",
            "jupyter>=1.0.0,<2.0.0",
        ],
    },
    entry_points={"kedro.project_commands": ["boot =  kedro_boot.booter:commands"]},
    keywords="kedro-plugin, deployment, application integration, framework, pipelines, machine learning, data pipelines, data science, data engineering, model serving, mlops",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Kedro",
        "Intended Audience :: Developers",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
    ],
)