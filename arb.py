import arbor
import math

asc = arbor.load_asc('soma.asc')
asc = arbor.load_asc('sphere.asc')

print(asc.labels)
m = asc.morphology
print(m)
nb = m.num_branches
print(f'branches {m.num_branches}')

area = 0
length = 0
for i in range(nb):
    for seg in m.branch_segments(i):
        dx = seg.prox.x - seg.dist.x
        dy = seg.prox.y - seg.dist.y
        dz = seg.prox.z - seg.dist.z
        L = pow(dx*dx+dy*dy+dz*dz, 0.5)
        D = 2*seg.prox.radius
        A = math.pi*D*L
        print(f'branch {i} segment with length {L} diam {D} area {A}')
        area = area+A
        length = length+L

print(f'total length {length} area {area}')

