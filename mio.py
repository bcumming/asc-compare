from morphio import Morphology

#m = Morphology('soma.asc')
m = Morphology('sphere.asc')

s = m.soma
print(s.type)
print(s.diameters)
print(s.points)
