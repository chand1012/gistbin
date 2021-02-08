# GistBin
[![](https://img.shields.io/pypi/l/gistbin)](https://pypi.org/project/gistbin/) [![](https://img.shields.io/pypi/pyversions/gistbin)](https://pypi.org/project/gistbin/) ![Upload Python Package](https://github.com/chand1012/gistbin/workflows/Upload%20Python%20Package/badge.svg)

Github Gist client allowing for quick uploads via commandline!

## Installing

Via pip: 

```
pip3 install gistbin
```

Manually:

```
git clone https://github.com/chand1012/gistbin.git
cd gistbin
pip install .
```

## Using

### Authentication

Because Gistbin uses the GitHub API, authentication is required. This requires a Github Personal Access Token, instructions of where to find and how to generate can be found [here](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token). To authenticate, simply run `gistbin --login` after installing and enter the prompted information. Here is an example:

```
octocat@octoserv:~$ gistbin --login
Enter GitHub username: octocat
Enter GitHub access token: ****************
Keyfile saved.
octocat@octoserv:~$ 
```

The key file is saved at `$HOME/.gistbin/auth.json`.

### Usage

To use, simply pipe the file you want to upload into Gistbin like so:

```
octocat@octoserv:~$ cat hello_world.rb | gistbin
https://gist.github.com/octocat/6cad326836d38bd3a7ae
```

By default, the gist that you upload is given a random name and a `.txt` extension with a blank description. You can edit this later on the gist's webpage, or you can also pass the `--name` and `--desc` to add a name and description respectively. You can also use the shortcut parameters, `-n` and `-d`.

```
octocat@octoserv:~$ cat test.cs | gistbin -n "test.cs"
https://gist.github.com/octocat/1305321
```

Another option is by adding file metadata. Here is an example:

```Python
# name: test.py
# desc: this is a test
# public: true

print("Hello world!")
```

```bash
octocat@octoserv:~$ cat test.py | gistbin
https://gist.github.com/chand1012/4d47f84d9c7b61c99ea9d310e92c7a17
```

Here are a few more examples of metadata in files:

```javascript
// name: test.js
// desc: This is a test
// public: false

console.log("Hello world!");
```

```C++
#include <iostream>

// name: test.cpp
// desc: Hello World in C++
// public: true

int main() {
  std::cout << "Hello world!" << std::endl;
  return 0;
}
```

```lua
-- name: test.lua
-- desc: test program
-- public: false

print("test")
```


If you want to make your gists public, just pass the `-p` or `--public` flag.

```
octocat@octoserv:~$ cat requirements.txt | gistbin -p -n "requirements.txt" -d "Gistbin requirements"
https://gist.github.com/chand1012/75b92e8a17906a0f7f7b330154fccbc2

```

If you want to get the raw url for the uploaded file, such as if you want to then download the file immediately onto another machine, you can pass the `-r` or `--raw` argument.

```
octocat@octoserv:~$ cat git-author-rewrite.sh | gistbin -n "git-author-rewrite.sh" -r
https://gist.githubusercontent.com/octocat/0831f3fbd83ac4d46451/raw/c197afe3e9ea2e4218f9fccbc0f36d2b8fd3c1e3/git-author-rewrite.sh
```

If you are on a platform that does not support piping in to STDIN, you can instead give GistBin a path to a file with the `-f` or `--file` command. This works with a single file or multiple files, but will not work with the `--raw` flag. This is also the only way to get GistBin working on Windows.

```
octocat@octoserv:~$ gistbin -f singleBrick.scad singleBrick.stl # this is an ASCII STL, GistBin does not work with binary files.
https://gist.github.com/chand1012/c8f4d8094d6e0b48c8e97e89a2530fad
```

You can also get the instructions for all of these commands with the help flag:

```
octocat@octoserv:~$ gistbin -h
usage: gistbin [-h] [-n NAME] [-v] [-d DESC] [--login] [-p] [-r] [-f FILES [FILES ...]]

A commandline tool for GitHub Gists.

optional arguments:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  Gives your gist a name. Input as a string. Default is random.
  -v, --verbose         Enables verbose output.
  -d DESC, --desc DESC  Gives your gist a description. Input as a string.
  --login               Login to GitHub Gists.
  -p, --public          Sets your Gist to public.
  -r, --raw             Makes Gistbin return the raw URL instead of the HTML URL of the file.
  -f FILES [FILES ...], --file FILES [FILES ...]
                        Gives Gistbin a list of files to upload. Also works with a single file.
```

Gistbin doesn't just work with `cat` you can pipe any terminal output (that ends) into it! For example, if you wanted to list all the files in a directory, you could use `ls -1 | gistbin -n "filelist.txt"`. If you wanted to get all the logs from yesterday from the journal, you could run `journalctl --since yesterday | gistbin -n "yesterday-today-journal.log"`. The possibilities are endless!
