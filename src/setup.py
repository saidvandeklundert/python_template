from setuptools import setup  # type: ignore

setup(
    name="example",
    version="0.1",
    packages=["example"],
    description="This is an example package that can serve as a template.",
    url="https://github.com/saidvandeklundert/python_template",
    classifiers=["Programming Language :: Python :: 3"],
    python_requires=">=3.8, <4",
    project_urls={
        "Bug Reports": "https://github.com/saidvandeklundert/python_template/issues",
        "Source": "https://github.com/saidvandeklundert/python_template",
        "Documentation": "https://github.com/saidvandeklundert/python_template/wiki",
    },
)
