
# change directory to your package
<code>

    cd your_package_path
</code>


<br>
<br>


# create folder named 'tests'
<code> **tests/ is a placeholder for unit test files. leave it empty.**</code>
<code>

    mkdir tests
</code>


<br>
<br>


# create MANIFEST.in
<code> **write this to your manifest file**</code>
<code>

    recursive-include $your_package_name *.json *.wav *.txt *.md
</code>


<br>
<br>


# create README.md
<code>

    # project name bla bla
    some quick description
    [some image]

</code>


<br>
<br>


# create setup.py
<code> **change these variables**</code>

<code>

    1. name (will be the one that you are ~pip install package-name~)
    2. version
    3. author
    4. author_email
    5. description
    6. url
    7. install_requires (all external dependencies installed with pip long time ago)
</code>

**warning**
<br>
`include_package_data must be 'True' in order to include all the additional files from your package`

<br>
<br>


<code> **paste this code to your file**</code>
<code>

    import setuptools

    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()

    setuptools.setup(
        name="python-core-alexzander36", # Replace with your own username
        version="2.0",
        author="alexzander",
        author_email="alexxander18360@gmail.com",
        description="python core package, created especially for lazy developers",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="",
        include_package_data=True,
        install_requires=[
            'pydub',
            'SpeechRecognition',
            'requests',
            "numpy"
        ],
        platforms="any",
        packages=setuptools.find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        python_requires='>=3.7',
    )
</code>
<br>

# create LICENSE
<code> **MIT LICENSE**</code>
<code>

    Copyright (c) 2018 The Python Packaging Authority

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
</code>

`not quite a big deal but its working`


<br>
<br>


# before building
<code> **you MUST have this tree format in your current working dir**</code>

<code>

    . (doesnt matter what name has this folder)
    ├── tests
    ├── MANIFEST.in
    ├── README.md
    ├── setup.py
    ├── LICENSE
    ├── your_package_name (the one that you want to import after pip install)
    │   ├── __init__.py
    │   ├── another_python_file.py
    │   ├── another_folder
    │   │   ├── ...
    │   │   └── ...
    │   └── ...
    └── ...
</code>


<br>
<br>


# install/upgrade python setuptools
<code>

    python -m pip install --user --upgrade setuptools wheel
</code>


<br>
<br>


# build
<code>

    python setup.py sdist bdist_wheel
</code>

**this command will add these folders to your current working dir**

<code>

    dist
</code>

<code> **under dist/ will be\
&nbsp;&nbsp;&nbsp;&nbsp;~your_package_name-version.whl~\
&nbsp;&nbsp;&nbsp;&nbsp;~your_package_name-version.tar.gz~** </code>

**these files will be uploaded to pypi.org or test.pypi.org**
<br>
**they contain all the zipped files from your package**


<br>
<br>



<code>

    build


    build/bdist.win-amd64
    build/lib/your_package_name/ (here will be everything that you upload to pypi.org or test.pypi.org, but unzipped form)

</code>

<br>

<code>

    your_package_name.egg-info


    this folder contains metadata about
        - what dependencies should be installed (requires.txt)
        - name of the package that should be imported after install (top_level.txt)
        - a tree list with all installed files (SOURCES.txt)
        - package info (PKG-INFO)
        - dependency links file (dependency_links.txt)

</code>



<br>
<br>


# after building
<code> **you SHOULD have this tree format in your current working dir**</code>

<code>

    . (doesnt matter what name has this folder)
    ├── tests
    ├── MANIFEST.in
    ├── README.md
    ├── setup.py
    ├── LICENSE
    ├── your_package_name (the one that you want to import after pip install)
    │   ├── __init__.py
    │   ├── another_python_file.py
    │   ├── another_folder
    │   │   ├── ...
    │   │   └── ...
    │   └── ...
    ├── build
    ├── dist
    ├── your_package_name.egg-info (the name from setup.py not the one that you import)
</code>

<code> **three new folders added at the bottom** </code>


<br>
<br>


# create an api token (if you dont have)
1. login to test.pypy.org or pypi.org
2. go to your account settings
3. api token section
4. generate api token key


<br>
<br>


# .pypirc
create a file at path
<code>

    C:/Users/$username/.pypirc
</code>
and paste inside:

<br>
<br>

for **test.pypi.org**
<code>

    [testpypi]
        username = __token__
        password = $your_api_token
</code>

<br>

for **pypi.org**
<code>

    [pypi]
        username = __token__
        password = $your_api_token
</code>

**leave the file there**

* this file will help you login to pypi.org or test.pypi.org api end point to upload your package


<br>
<br>


# install/upgrade twine
* twine is a python program that helps you upload your files remote

<br>

<code>

    python -m pip install --user --upgrade twine
</code>

<br/><br/>

# upload your package to test.pypi.org
**test.pypi.org**
<code>

    cd current_working_dir
    python -m twine upload --repository testpypi dist/*
</code>

uploading url will be `https://test.pypi.org/legacy/`

<br>
<br>

**pypi.org**
<code>

    python -m twine upload dist/*
</code>



<br>
<br>


# install your package
from `test.pypi.org`

<code>

    pip install -i https://test.pypi.org/simple/ $package_name
</code>

<br>

from `pypi.org`
<code>

    pip install $your_package_name
</code>


<br>

# uninstall your package
<code>

    pip uninstall $your_package_name
</code>