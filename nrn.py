from neuron import h, gui
import math

h.load_file('import3d.hoc')

class MyCell:
    def __init__(self):
        morph_reader = h.Import3d_Neurolucida3()
        morph_reader.input('soma.asc')
        #morph_reader.input('sphere.asc')
        i3d = h.Import3d_GUI(morph_reader, 0)
        i3d.instantiate(self)

m = MyCell()

print('%d soma sections' % len(m.soma))
for seg in m.soma:
    D = seg.diam
    A = math.pi*D*seg.L
    print(f'segment: len {seg.L} diam {seg.diam} area {A}')

