import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-authsimple",
    version="0.3",
    author="asad2200",
    author_email="asadjakhavala92@gmial.com",
    description="A Django app to implement basic authentication in django project.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/asad2200/authsimple",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
