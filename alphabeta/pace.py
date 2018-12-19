import time
import random
import os

import sys
sys.path.append('./alphabeta')
sys.path.append('./')
from evaluate import checkerValue

MIN = -10000

def matchChessScore_():
  __dir__ = os.path.dirname(os.path.abspath(__file__))
  dataFile = __dir__ + '/chessScore'
  
  chessScore = []
  with open(dataFile, 'r') as f:
    for line in f:
      chessScore.append(line)
  maybe = chessScore
  lastHistory = 0
  def match(history):
    l = len(history)
    nonlocal maybe, lastHistory
    if l >= 80:
      return ''
    if l <= lastHistory:
      maybe = chessScore
    lastHistory = l
    maybe_ = []
    for line in maybe:
      if line[0:len(history)] == history:
        maybe_.append(line.strip())
    maybe = maybe_
    if len(maybe) != 0:
      path = random.choice(maybe)
    else:
      path = ''
    print('[棋谱] {}'.format(path[len(history):]))
    print('（匹配棋谱数: {}）'.format(len(maybe)))
    return path[l:l+4]
  return match
matchChessScore = matchChessScore_()

def getPace(checkerboard, maxDepth, history):
  path = matchChessScore(history)
  if path != '':
    # 匹配棋谱
    nextPace = path
  else:
    # alpha-beta剪枝
    beg = time.time()
    
    if maxDepth % 2 != 0:
      maxDepth += 1

    initCheckerBoard(checkerboard)

    _, nextPace = _alphabeta(-MIN, maxDepth)

    if cb[nextPace[3]][nextPace[2]] \
      and cb[nextPace[3]][nextPace[2]].lower() == 'j':
        nextPace = None

    print('计算时间：{:.2f}s，计算深度：{}'.format(time.time()-beg, maxDepth))

  return nextPace

def _alphabeta(alpha, maxDepth):
  value, nextPace = MIN, None
  turnToAI = maxDepth % 2 == 0
  paces = getAllPace(turnToAI)
  
  for pace in paces:
    # 是否吃将
    clear = cb[pace[3]][pace[2]]
    if clear and clear.lower() == 'j':
      value, nextPace = 8888, pace
      break

    # 移动
    move(pace)
    if maxDepth == 1:
      newValue = evaluateBoard()
    else:
      newValue, _ = _alphabeta(-value, maxDepth-1)
    newValue = -newValue
    unmove(pace)

    # 更新值，剪枝
    if newValue > value:
      value, nextPace = newValue, pace
      if value >= alpha:
        break

  return value, nextPace

# CheckerBoard
cb = [
  ['C0','M0','X0','S0','J0','S1','X1','M1','C1'],
  [None,None,None,None,None,None,None,None,None],
  [None,'P0',None,None,None,None,None,'P1',None],
  ['Z0',None,'Z1',None,'Z2',None,'Z3',None,'Z4'],
  [None,None,None,None,None,None,None,None,None],
  [None,None,None,None,None,None,None,None,None],
  ['z0',None,'z1',None,'z2',None,'z3',None,'z4'],
  [None,'p0',None,None,None,None,None,'p1',None],
  [None,None,None,None,None,None,None,None,None],
  ['c0','m0','x0','s0','j0','s1','x1','m1','c1']
]

# 大写是AI，小写是玩家
# 黑色是AI，红色是玩家
# 因此所有大写字母的companion都是True，表示为电脑一方
companion = [
  [True] * 9, 
  [True] * 9, 
  [True] * 9, 
  [True] * 9, 
  [True] * 9, 
  [True] * 9, 
  [True] * 9, 
  [True] * 9, 
  [True] * 9, 
  [True] * 9
]

def initCheckerBoard(checkerboard):
  for y, line in enumerate(checkerboard):
    for x, c in enumerate(line):
      if c:
        c = c[0:1]
        companion[y][x] = c.isupper()
      cb[y][x] = c
  
def getAllPace(turnToAI:bool):
  paces = []
  for y in range(0, 10):
    for x in range(0, 9):
      if cb[y][x]:
        c = cb[y][x]
        if c.isupper() == turnToAI:
          paces += paceGetter[c](x, y)
  
  paces.sort(key=paceKey, reverse=True)

  return paces

def paceKey(pace):
  me = cb[pace[1]][pace[0]].isupper()

  value = 0
  # 动子分数
  x = pace[0]
  y = pace[1]
  x_ = pace[2]
  y_ = pace[3]

  v = checkerValue[cb[y][x].lower()]
  if me:
    value += v[9-y][8-x] - v[y_][x_]
  else:
    value += v[y][x] - v[y_][x_]
  
  # 吃子分数
  if cb[y_][x_]:
    v = checkerValue[cb[y_][x_].lower()]
    if me:
      value += v[9-y_][8-x_]
    else:
      value += v[y_][x_]

  return value

# 被吃掉的棋子的栈
clearStack = []

def move(pace):
  clearChecker = cb[pace[3]][pace[2]]
  clearStack.append(clearChecker)
  cb[pace[3]][pace[2]] = cb[pace[1]][pace[0]]
  cb[pace[1]][pace[0]] = None

  companion[pace[3]][pace[2]] = cb[pace[3]][pace[2]].isupper()
  
def unmove(pace):
  clearChecker = clearStack.pop(-1)
  cb[pace[1]][pace[0]] = cb[pace[3]][pace[2]]
  if clearChecker:
    cb[pace[3]][pace[2]] = clearChecker
    companion[pace[3]][pace[2]] = cb[pace[3]][pace[2]].isupper()
  else:
    cb[pace[3]][pace[2]] = None

  companion[pace[1]][pace[0]] = cb[pace[1]][pace[0]].isupper()

# def getFromHistory():
#   if True:
#     return None
#   else:
#     return 1

# 车
def getPace_C(x, y):
  paces = []
  me = cb[y][x].isupper()
  # 左侧检索
  for i in range(x-1, -1, -1):
    if cb[y][i]:
      if cb[y][i].isupper() != me:
        paces.append((x, y, i, y))
      break
    else:
      paces.append((x, y, i, y))
  # 右侧检索
  for i in range(x+1, 9):
    if cb[y][i]:
      if cb[y][i].isupper() != me:
        paces.append((x, y, i, y))
      break
    else:
      paces.append((x, y, i, y))
  # 上检索
  for i in range(y-1, -1, -1):
    if cb[i][x]:
      if cb[i][x].isupper() != me:
        paces.append((x, y, x, i))
      break
    else:
      paces.append((x, y, x, i))
  # 下检索
  for i in range(y+1, 10):
    if cb[i][x]:
      if cb[i][x].isupper() != me:
        paces.append((x, y, x, i))
      break
    else:
      paces.append((x, y, x, i))
  return paces

# 马
def getPace_M(x, y):
  paces = []
  me = cb[y][x].isupper()
  # 1点
  if y-2>= 0 and x+1<= 8 and not cb[y-1][x] and (not cb[y-2][x+1] or companion[y-2][x+1] != me): paces.append((x, y, x+1,y-2))
  # 2点
  if y-1>= 0 and x+2<= 8 and not cb[y][x+1] and (not cb[y-1][x+2] or companion[y-1][x+2] != me): paces.append((x, y, x+2,y-1))
  # 4点
  if y+1<= 9 and x+2<= 8 and not cb[y][x+1] and (not cb[y+1][x+2] or companion[y+1][x+2] != me): paces.append((x, y, x+2,y+1))
  # 5点
  if y+2<= 9 and x+1<= 8 and not cb[y+1][x] and (not cb[y+2][x+1] or companion[y+2][x+1] != me): paces.append((x, y, x+1,y+2))
  # 7点
  if y+2<= 9 and x-1>= 0 and not cb[y+1][x] and (not cb[y+2][x-1] or companion[y+2][x-1] != me): paces.append((x, y, x-1,y+2))
  # 8点
  if y+1<= 9 and x-2>= 0 and not cb[y][x-1] and (not cb[y+1][x-2] or companion[y+1][x-2] != me): paces.append((x, y, x-2,y+1))
  # 10点
  if y-1>= 0 and x-2>= 0 and not cb[y][x-1] and (not cb[y-1][x-2] or companion[y-1][x-2] != me): paces.append((x, y, x-2,y-1))
  # 11点
  if y-2>= 0 and x-1>= 0 and not cb[y-1][x] and (not cb[y-2][x-1] or companion[y-2][x-1] != me): paces.append((x, y, x-1,y-2))

  return paces

# 相
def getPace_X(x,y):
  paces = []
  me = cb[y][x].isupper()

  if (not me): # 红方
    # 4点半
    if y+2<= 9 and x+2<= 8 and not cb[y+1][x+1] and (not cb[y+2][x+2] or companion[y+2][x+2] != me): paces.append((x, y, x+2,y+2))
    # 7点半
    if y+2<= 9 and x-2>= 0 and not cb[y+1][x-1] and (not cb[y+2][x-2] or companion[y+2][x-2] != me): paces.append((x, y, x-2,y+2))
    # 1点半
    if y-2>= 5 and x+2<= 8 and not cb[y-1][x+1] and (not cb[y-2][x+2] or companion[y-2][x+2] != me): paces.append((x, y, x+2,y-2))
    # 10点半
    if y-2>= 5 and x-2>= 0 and not cb[y-1][x-1] and (not cb[y-2][x-2] or companion[y-2][x-2] != me): paces.append((x, y, x-2,y-2))
  else:
    # 4点半
    if y+2<= 4 and x+2<= 8 and not cb[y+1][x+1] and (not cb[y+2][x+2] or companion[y+2][x+2] != me): paces.append((x, y, x+2,y+2))
    # 7点半
    if y+2<= 4 and x-2>= 0 and not cb[y+1][x-1] and (not cb[y+2][x-2] or companion[y+2][x-2] != me): paces.append((x, y, x-2,y+2))
    # 1点半
    if y-2>= 0 and x+2<= 8 and not cb[y-1][x+1] and (not cb[y-2][x+2] or companion[y-2][x+2] != me): paces.append((x, y, x+2,y-2))
    # 10点半
    if y-2>= 0 and x-2>= 0 and not cb[y-1][x-1] and (not cb[y-2][x-2] or companion[y-2][x-2] != me): paces.append((x, y, x-2,y-2))
  
  return paces

# 士
def getPace_S(x,y):
  paces = []
  me = cb[y][x].isupper()

  if not me: # 红方
    # 4点半
    if y+1<= 9 and x+1<= 5 and (not cb[y+1][x+1] or companion[y+1][x+1] != me): paces.append((x, y, x+1,y+1))
    # 7点半
    if y+1<= 9 and x-1>= 3 and (not cb[y+1][x-1] or companion[y+1][x-1] != me): paces.append((x, y, x-1,y+1))
    # 1点半
    if y-1>= 7 and x+1<= 5 and (not cb[y-1][x+1] or companion[y-1][x+1] != me): paces.append((x, y, x+1,y-1))
    # 10点半
    if y-1>= 7 and x-1>= 3 and (not cb[y-1][x-1] or companion[y-1][x-1] != me): paces.append((x, y, x-1,y-1))
  else:
    # 4点半
    if y+1<= 2 and x+1<= 5 and (not cb[y+1][x+1] or companion[y+1][x+1] != me): paces.append((x, y, x+1,y+1))
    # 7点半
    if y+1<= 2 and x-1>= 3 and (not cb[y+1][x-1] or companion[y+1][x-1] != me): paces.append((x, y, x-1,y+1))
    # 1点半
    if y-1>= 0 and x+1<= 5 and (not cb[y-1][x+1] or companion[y-1][x+1] != me): paces.append((x, y, x+1,y-1))
    # 10点半
    if y-1>= 0 and x-1>= 3 and (not cb[y-1][x-1] or companion[y-1][x-1] != me): paces.append((x, y, x-1,y-1))
  
  return paces

# 将
def getPace_J(x,y):
  paces = []
  me = cb[y][x].isupper()

  # 两将相对
  stab = True
  black = None
  red = None
  for yy in range(0, 3):
    for xx in range(3, 6):
      if cb[yy][xx] == "J":
        black = (xx, yy)
  for yy in range(7, 10):
    for xx in range(3, 6):
      if cb[yy][xx] == "j":
        red = (xx, yy)
  if not black or not red:
    return []
  
  if black[0] != red[0]:
    stab = False
  else:
    for yy in range(black[1]+1, red[1]):
      if cb[yy][black[0]]:
        stab = False
  
  if not me: # 红方
    # 下
    if y+1<= 9 and (not cb[y+1][x] or companion[y+1][x] != me): paces.append((x, y, x,y+1))
    # 上
    if y-1>= 7 and (not cb[y-1][x] or companion[y-1][x] != me): paces.append((x, y, x,y-1))
    # 老将对老将的情况
    if stab: 
      paces.append((*red, *black))
  else:
    # 下
    if y+1<= 2 and (not cb[y+1][x] or companion[y+1][x] != me): paces.append((x, y, x,y+1))
    # 上
    if y-1>= 0 and (not cb[y-1][x] or companion[y-1][x] != me): paces.append((x, y, x,y-1))
    # 老将对老将的情况
    if stab: 
      paces.append((*black, *red))
  # 右
  if x+1<= 5 and (not cb[y][x+1] or companion[y][x+1] != me): paces.append((x, y, x+1,y))
  # 左
  if x-1>= 3 and (not cb[y][x-1] or companion[y][x-1] != me): paces.append((x, y, x-1,y))

  return paces

# 炮
def getPace_P(x,y):
  paces = []
  me = cb[y][x].isupper()

  # 左侧检索
  emplacement = False
  for i in range(x-1, -1, -1):
    if(cb[y][i]):
      if not emplacement:
        emplacement = True
      else:
        if companion[y][i] != me:
          paces.append((x, y, i, y))

        break
    else:
      if not emplacement:
        paces.append((x, y, i, y))
  # 右侧检索
  emplacement = False
  for i in range(x+1, 9):
    if(cb[y][i]):
      if not emplacement:
        emplacement = True
      else:
        if companion[y][i] != me:
          paces.append((x, y, i, y))
        break
    else:
      if not emplacement:
        paces.append((x, y, i, y))
  # 上检索
  emplacement = False
  for i in range(y-1, -1, -1):
    if(cb[i][x]):
      if not emplacement:
        emplacement = True
      else:
        if companion[i][x] != me:
          paces.append((x, y, x, i))
        break
    else:
      if not emplacement:
        paces.append((x, y, x, i))
  # 下检索
  emplacement = False
  for i in range(y+1, 10):
    if(cb[i][x]):
      if not emplacement:
        emplacement = True
      else:
        if companion[i][x] != me:
          paces.append((x, y, x, i))
        break
    else:
      if not emplacement:
        paces.append((x, y, x, i))

  return paces

# 卒
def getPace_Z(x,y):
  paces = []
  me = cb[y][x].isupper()

  if not me: # 红方
    # 上
    if y-1>= 0 and (not cb[y-1][x] or companion[y-1][x] != me): paces.append((x, y, x,y-1))
    # 右
    if x+1<= 8 and y<=4 and (not cb[y][x+1] or companion[y][x+1] != me): paces.append((x, y, x+1,y))
    # 左
    if x-1>= 0 and y<=4 and (not cb[y][x-1] or companion[y][x-1] != me): paces.append((x, y, x-1,y))
  else:
    # 下
    if y+1<= 9 and (not cb[y+1][x] or companion[y+1][x] != me): paces.append((x, y, x,y+1))
    # 右
    if x+1<= 8 and y>=6 and (not cb[y][x+1] or companion[y][x+1] != me): paces.append((x, y, x+1,y))
    # 左
    if x-1>= 0 and y>=6 and (not cb[y][x-1] or companion[y][x-1] != me): paces.append((x, y, x-1,y))
  
  return paces

paceGetter = {
  'C': getPace_C,
  'M': getPace_M,
  'X': getPace_X,
  'S': getPace_S,
  'J': getPace_J,
  'P': getPace_P,
  'Z': getPace_Z,

  'c': getPace_C,
  'm': getPace_M,
  'x': getPace_X,
  's': getPace_S,
  'j': getPace_J,
  'p': getPace_P,
  'z': getPace_Z,
}

# =============================
# 棋局评估
def evaluateBoard():
  value = 0
  for y in range(0, 10):
    for x in range(0, 9):
      if cb[y][x]:
        c = cb[y][x]
        if c.islower():
          # 红方棋子
          value -= checkerValue[c][y][x]
        else:
          # 黑方棋子
          c = c.lower()
          value += checkerValue[c][9-y][8-x]
  return value

def logCheckerBoard():
  print('================================')
  for y in range(0, 10):
    for x in range(0, 9):
      if cb[y][x]:
        print(cb[y][x], end=' ')
      else:
        print('-', end=' ')
    print('          ', end='')
    for x in range(0, 9):
      if cb[y][x]:
        if companion[y][x]:
          print(1, end=' ')
        else:
          print(0, end=' ')
      else:
        print('-', end=' ')
    print('')
  print('================================\n')
