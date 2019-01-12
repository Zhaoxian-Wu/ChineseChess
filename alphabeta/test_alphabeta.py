import pace

cb = [
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
  ]

def test(cb, nextPace, title, depth=4):
  p = pace.getPace(cb, depth, '0000')
  if not p in nextPace:
    print('[{}] Failed'.format(title))
    print('[expect]', nextPace)
    print('[answer]', p)
  else:
    print('[{}] Success'.format(title))

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
    'nextPace': [(5, 3, 6, 1)]
  },
'''
input = [
  {
    'title': 'test1',
    'cb': [
      [None,'z2','p0','z4',None,None,None,'z1','c1'],
      [None,None,'z3',None,None,None,None,None,'z0'],
      [None,None,None,None,None,None,None,None,None],
      [None,None,None,None,None,'M0',None,None,None],
      [None,None,None,None,None,None,None,None,None],
      [None,None,None,None,None,None,None,None,None],
      [None,None,None,None,None,None,None,None,None],
      [None,None,None,None,None,None,None,None,None],
      [None,None,None,None,None,None,None,None,None],
      [None,None,None,None,None,None,None,None,None]
    ],
    'nextPace': [(5, 3, 6, 1), (5, 3, 7, 2)],
    'depth': 3,
  },
  {
    'title': 'steb',
    'cb': [
      ['M0',None,None,None,'J0',None,None,None,None],
      [None,None,None,None,None,None,None,None,None],
      [None,None,None,None,None,None,None,None,None],
      [None,None,None,None,None,None,None,None,None],
      [None,None,None,None,None,None,None,None,None],
      [None,None,None,None,None,None,None,None,None],
      [None,None,None,None,None,None,None,None,None],
      [None,None,None,None,None,None,None,None,None],
      [None,None,None,None,None,None,None,None,None],
      [None,None,None,None,'j0',None,None,None,None]
    ],
    'nextPace': [(4, 0, 4, 9)]
  },
  {
    'title': 'deading_1',
    'cb': [
      [None,None,None,None,'J0',None,None,None,None],
      [None,None,None,None,None,None,None,None,None],
      [None,None,None,None,None,None,None,None,None],
      [None,None,None,None,None,None,None,None,None],
      [None,None,None,None,None,None,None,None,None],
      [None,None,None,None,None,None,None,None,None],
      [None,None,None,None,None,None,None,None,None],
      [None,None,None,None,None,None,None,None,None],
      ['P0',None,None,None,'s0',None,'c0',None,None],
      [None,None,None,'s1','j0',None,None,None,None]
    ],
    'nextPace': [(0, 8, 0, 9)]
  },
  {
    'title': 'eat_che',
    'cb': [
      ['C0',None,None,None,'J0',None,None,None,None],
      [None,None,None,None,None,None,None,None,None],
      [None,None,None,None,None,None,None,None,None],
      [None,None,None,None,None,None,None,None,None],
      [None,None,None,None,None,None,None,None,None],
      [None,None,None,None,None,None,None,None,None],
      [None,None,None,None,'z2',None,None,None,None],
      [None,None,None,None,None,None,None,None,None],
      [None,None,None,None,None,'c0',None,'C1',None],
      [None,None,None,'s0','j0',None,None,'c1',None]
    ],
    'nextPace': [(7, 8, 7, 9)]
  },
  {
    'title': 'take_che',
    'cb': [
      ['C0',None,None,None,'J0',None,None,None,None],
      [None,None,None,None,None,None,None,None,None],
      [None,None,None,None,None,None,None,None,None],
      [None,None,None,None,None,None,None,None,None],
      [None,None,None,None,None,None,None,'C1',None],
      [None,None,None,None,None,None,None,None,None],
      [None,None,None,None,'z2',None,None,None,'z4'],
      [None,None,None,None,None,None,None,None,None],
      [None,None,None,None,None,'c0',None,'m0',None],
      [None,None,None,None,'j0',None,None,'c1',None]
    ],
    'nextPace': [(0, 0, 0, 9)]
  },
  {
    'title': 'take_che2',
    'cb': [
      [None,None,None,None,'z2',None,None,None,None],
      ['P0',None,'P1',None,None,'J0',None,None,None],
      [None,None,None,'z0','X0','z1',None,None,'X0'],
      [None,None,None,None,None,None,None,None,None],
      [None,None,None,None,None,None,None,None,None],
      [None,None,None,None,None,None,None,None,None],
      [None,'m0',None,None,None,None,None,None,None],
      [None,None,None,None,None,None,None,None,None],
      [None,None,None,None,None,None,None,None,None],
      [None,None,None,None,None,'j0',None,None,None]
    ],
    'nextPace': [(5, 1, 4, 1)]
  },
]

if __name__ == '__main__':
  for i in input:
    if 'depth' in i:
      test(i['cb'], i['nextPace'], i['title'], depth=i['depth'])
    else:
      test(i['cb'], i['nextPace'], i['title'])