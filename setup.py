import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fdroid_build_checker",
    version="0.0.3",
    author="Tobias Preuss",
    author_email="tobias.preuss+fdroid-build-checker@googlemail.com",
    description="Python code to check if F-Droid recent build has succeeded or failed.",
    long_description="The scripts check if your custom packages occur on the recent changes page and then inspect the associated last build pages for the build result.",
    long_description_content_type="text",
    url="https://github.com/johnjohndoe/fdroid-build-checker",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Operating System :: OS Independent",
    ],
)
