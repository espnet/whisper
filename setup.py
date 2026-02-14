import os
import platform
import sys

from setuptools import find_packages, setup


def read_version(fname="whisper/version.py"):
    exec(compile(open(fname, encoding="utf-8").read(), fname, "exec"))
    return locals()["__version__"]


def read_requirements(fname="requirements.txt"):
    with open(os.path.join(os.path.dirname(__file__), fname), encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]


requirements = []
if sys.platform.startswith("linux") and platform.machine() == "x86_64":
    requirements.append("triton")

setup(
    name="openai-whisper",
    py_modules=["whisper"],
    version=read_version(),
    description="Robust Speech Recognition via Large-Scale Weak Supervision",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    readme="README.md",
    python_requires=">=3.10",
    author="OpenAI",
    url="https://github.com/openai/whisper",
    license="MIT",
    packages=find_packages(exclude=["tests*"]),
    install_requires=requirements + read_requirements(),
    entry_points={
        "console_scripts": ["whisper=whisper.transcribe:cli"],
    },
    include_package_data=True,
    extras_require={"dev": ["pytest", "scipy", "black[jupyter]", "flake8", "isort"]},
)
