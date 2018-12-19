import pace

def test(cb, title, turnToAI):
  pace.initCheckerBoard(cb)
  
  paces = pace.getAllPace(turnToAI)

  paces.sort(key=pace.paceKey)

  print('turn to ai:', turnToAI)
  for p in paces:
    print(p)
'''
  {
    'title': 'test1',
    'cb': [
      [None,None,None,None,None,None,None,None,None],
      [None,None,None,None,None,None,None,None,None],
      [None,None,None,None,None,None,None,None,None],
      [None,None,None,None,None,None,None,None,None],
      [None,None,None,None,None,None,None,None,None],
      [None,None,None,None,None,None,None,None,None],
      [None,None,None,None,None,None,None,None,None],
      [None,None,None,None,None,None,None,None,None],
      [None,None,None,None,None,None,None,None,None],
      [None,None,None,None,None,None,None,None,None]
    ],
    'nextPace': (5, 3, 6, 1)
  },
'''
input = [
  # {
  #   'title': 'test1',
  #   'cb': [
  #     [None,'z2','p0','z4',None,None,None,'z1','c1'],
  #     [None,None,'z3',None,None,None,None,None,'z0'],
  #     [None,None,None,None,None,None,None,None,None],
  #     [None,None,None,None,None,'M0',None,None,None],
  #     [None,None,None,None,None,None,None,None,None],
  #     [None,None,None,None,None,None,None,None,None],
  #     [None,None,None,None,None,None,None,None,None],
  #     [None,None,None,None,None,None,None,None,None],
  #     [None,None,None,None,None,None,None,None,None],
  #     [None,None,None,None,None,None,None,None,None]
  #   ],
  #   'nextPace': (5, 3, 6, 1)
  # },
  {
    'title': 'test2',
    'cb': [
      ['C0',None,'X0','S0','J0','S1','X1',None,None],
      [None,None,None,None,None,None,None,None,None],
      [None,'P0','M0',None,'P1',None,'M1',None,None],
      ['Z0',None,'Z1',None,'Z2',None,'Z3',None,'Z4'],
      [None,None,None,None,None,None,None,'C0',None],
      [None,None,'z1',None,None,None,None,None,None],
      ['z0',None,None,None,'z2',None,'z3',None,'z4'],
      [None,'m0','p0',None,None,None,'m1','p1',None],
      [None,None,None,None,None,'c0',None,None,None],
      [None,None,'x0','s0','j0','s1','x1','c1',None]
    ],
    'turnToAI': True
  },
]

if __name__ == '__main__':
  for i in input:
    test(i['cb'], i['title'], i['turnToAI'])