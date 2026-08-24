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
    Similar to BFS and applied to matrix. Set a center point and search all of the eight surrounding cells from the center.
  - [Grid Repainting][11]

- DP(dynamic programming)
  - [Frog 1][4]
  - [Prediction and Restriction][5]

- Bit Brute Force
  - [H and V][6]
  - [ORXOR][7]

- Trig Functions
  - [Opposite][8]
    Describe some notes regarding conversion between degrees and radians. Also, about point rotation.

- Binary Search
  - [Buy an Integer][9]

- XOR (Exclusive or)
  - [Inc, Dec, Xor][10]

[1]:re/D/Double_Dots.py
[2]:C/Tour.py
[3]:E/Sensors.py
[4]:A/Frog_1.py
[5]:re/D/Prediction_and_Restriction.py
[6]:C/H_and_V.py
[7]:re/C/ORXOR.py
[8]:re/D/Opposite.py
[9]:re/C/Buy_an_Integer.py
[10]:re/C/Inc,_Dec,_Xor.py
[11]:D/Grid_Repainting.py
