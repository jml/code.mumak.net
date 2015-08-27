Title: Debugging Python with gdb
Date: 2015-08-27

Here's a quick reference for getting set up to debug Python with `gdb`, aimed
at Debian and Ubuntu users.

Although I'd love to make this a full-fledged write up, it's going to have to
be a note to my future self for now.

It assumes you have `virtualenvwrapper` installed.


1. Get all of the things we need for Python debugging:

    ```
    sudo apt-get install python2.7-dbg python2.7-dev gdb
    ```

2. Make sure we use Python with debugging symbols:

    ```
    mkvirtualenv -p python2.7-dbg $PROJECT-dbg
    ```

3. Install dependencies with *their* debugging symbols:

    ```
    pip install --no-binary :all: --global-option build --global-option debug -e .
    ```

4. Make Python GDB extensions available in virtualenv:

    ```
    ln -s /usr/lib/debug/usr/bin/python2.7-gdb.py ~/.virtualenvs/$PROJECT-dbg/bin`
    ```

Once that's set up, a handy thing is to run tests in gdb over and over again
until they segfault:

```
gdb -ex r --args python ~/.virtualenvs/$PROJECT-dbg/bin/trial -u testcase
```

You might see errors about C files that can't be found. Pay them no mind. If
you had the libc6 source code in the right location, they would go away, and
you'd learn very little about your Python program.

### Core

I have literally no idea how Ubuntu handles core dumps by default. Here's
what I ended up doing:

```
$ ulimit -c unlimited
```

Then, as `root`:

```
$ echo "core" > c/proc/sys/kernel/core_pattern
```

This means core will be dumped in the current working directory.

**Note**: if you are using `trial`, the coredump will be in `_trial_temp/core`.

**Note**: for it to be any use at all, you have to have a coredump from a
debugging build of Python.

### Links

* [Debugging with GDB](https://wiki.python.org/moin/DebuggingWithGdb) on the Python wiki
* [How to use GDB Python debugging extension inside virtualenv](http://stackoverflow.com/a/22991614) on StackOverflow
