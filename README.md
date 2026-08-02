# python-reference

My personal notes about algorithms during self-study.

## Set up the environment

```
$ git clone https://github.com/TakamichiOsumi/python-reference.git
$ cd python-reference
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
```

Optionally, prepare the snippets in different repo.
```
$ git clone https://github.com/TakamichiOsumi/Env.git
$ cp Env/.emacs ~/.emacs
$ mkdir -p ~/.emacs.d/snippets/python-mode
$ cp Env/snippets/python-mode/* ~/.emacs.d/snippets/python-mode
```

## Run a local interactive reference

Execute 'python3' to start the console. Load the reference file.
This enables key shortcuts such as Cntrl-a and Cntrl-d, while
the direct execution of reference.py disables them.

```
>>> import reference
>>> help(string)
```

## Notes

Tested on only Mac OS X.

## Algorithms links

- BFS(breadth-first search)
  - [Double Dots][1]
  - [Tour][2]
  - [Sensors][3]
    This is the BFS for matrix. Set a center point and search all of the 8 surrounding cells
    from the center.

[1]:re/D/Double_Dots.py
[2]:C/Tour.py
[3]:E/Sensors.py
