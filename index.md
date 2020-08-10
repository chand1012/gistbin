# GistBin
Github Gist client allowing for quick uploads via commandline!

<sub>Currently only *nix OSes are supported </sub>

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

If you don't want others to see your gist, and you just want it for your eyes only, you can pass `--private` or `-p`.

```
octocat@octoserv:~$ cat private.txt | gistbin -n "private.txt" -p
https://gist.github.com/octocat/thisissecret
```

If you want to get the raw url for the uploaded file, such as if you want to then download the file immediately onto another machine, you can pass the `-r` or `--raw` argument.

```
octocat@octoserv:~$ cat git-author-rewrite.sh | gistbin -n "git-author-rewrite.sh" -r
https://gist.githubusercontent.com/octocat/0831f3fbd83ac4d46451/raw/c197afe3e9ea2e4218f9fccbc0f36d2b8fd3c1e3/git-author-rewrite.sh
```

You can also get the instructions for all of these commands with the help flag:

```
octocat@octoserv:~$ gistbin -h
usage: gistbin [-h] [-n NAME] [-v] [-d DESC] [--login] [-p] [-r]

A commandline tool for GitHub Gists.

optional arguments:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  Gives your gist a name. Input as a string. Default is
                        random.
  -v, --verbose         Enables verbose output.
  -d DESC, --desc DESC  Gives your gist a description. Input as a string.
  --login               Login to GitHub Gists.
  -p, --private         Sets your Gist to private so only those with the link
                        can see.
  -r, --raw             Makes Gistbin return the raw URL instead of the HTML
                        URL of the file.
```

Gistbin doesn't just work with `cat` you can pipe any terminal output (that ends) into it! For example, if you wanted to list all the files in a directory, you could use `ls -1 | gistbin -n "filelist.txt"`. If you wanted to get all the logs from yesterday from the journal, you could run `journalctl --since yesterday | gistbin -n "yesterday-today-journal.log"`. The possibilities are endless!

## Roadmap

- Windows Support.
- Multi-file uploads.
- Some more stuff probably.