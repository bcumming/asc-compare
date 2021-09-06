Removing everything except the soma makes no difference to how the soma is represented in either Neuron or Arbor.

Arbor creates two segments
NEURON creates a single segment

Below are the dimensions of the soma (in arbor the length is the sum of the two cylinder lengths)

```
        length  diam    area
Arbor    6.587  6.587   136.314
Neuron   8.708  4.667   127.667
```

The area was calculated using the formula for area of a cylinder `π⋅D⋅L`.

The MorphIO library, installed with `pip install morphio`, does not try to interpret the soma as cylinders. Instead, it records the points, and marks it as `SOMA_SIMPLE_CONTOUR`.

Whatever NEURON is doing, it isn't following the policy for "soma as a contour" prescribed by NeuroMorpho (http://neuromorpho.org/SomaFormat.html), and followed by Arbor.

# how to test

```
python -m venv env
source env/bin/activate
pip install --upgrade pip
pip install numpy neuron arbor morphio
```
