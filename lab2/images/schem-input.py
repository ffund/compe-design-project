import schemdraw
import schemdraw.elements as elm

d = schemdraw.Drawing()
V = d.add(elm.Vdd(label='3.3V'))
S = d.add(elm.Button(d='down', label='S'))
d.push()
R1 = d.add(elm.Resistor(d='left', label='R1'))
P = d.add(elm.Tag(d='left', label='GPIO'))
d.pop()
R2 = d.add(elm.Resistor(d='down', label='R2'))
G = d.add(elm.Ground)

d.save('schem-input.svg')

d = schemdraw.Drawing()
V = d.add(elm.Vdd(label='3.3V'))
S = d.add(elm.Button(d='down', label='S'))
R1 = d.add(elm.Resistor(d='left', label='R1'))
P = d.add(elm.Tag(d='left', label='GPIO'))

d.save('schem-floating.svg')

