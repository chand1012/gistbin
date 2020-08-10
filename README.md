# GistBin
Github Gist client allowing for quick uploads via commandline!

<sub>Currently only *nix OSes are supported </sub>

## Installing

Via pip: `pip3 install gistbin`

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

