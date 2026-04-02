from heapq     import heapify, heappush, heappop
from itertools import count

def huffman_tree(seq, freq):
  """ ref: Magnus Hetland, 'Python Algorithms', chapter 7 """
  num = count()
  trees = list(zip(freq, num, seq))             # «num» ensures a valid ordering
  heapify(trees)                                # min-heap based on frequencies
  while len(trees) > 1:                         # until there's just one tree:
    fa, _, a = heappop(trees)                   #  get the two 'smallest' trees
    fb, _, b = heappop(trees)
    heappush(trees, (fa+fb, next(num), [a, b])) #  combine and add new tree
  return trees[0][-1]





seq = "abcdefghi"  #alterar para todas as letras
frq = [4, 5, 6, 9, 11, 12, 15, 16, 20] # alterar para as frequências de cada letra
huffman_tree(seq, frq)


#saber o codigo de cada letra
def codes(tree, prefix=""):
  """ ref: Magnus Hetland, 'Python Algorithms', chapter 7 """
  if len(tree) == 1:
    yield (tree, prefix)                      # a leaf with its code
  else:
    for bit, child in zip("01", tree):        # left is 0, right is 1
      yield from codes(child, prefix + bit)   # get codes recursively
      
      
list(codes(huffman_tree(seq, frq)))



from collections import Counter

def encoding_map(msg):
  """ return unique letters from 'msg' and their frequencies """
  data = Counter(msg).items()
  seq, freq = ''.join(map(lambda p:p[0], data)), list(map(lambda p:p[1], data))
  return {letter:code for letter, code in codes(huffman_tree(seq, freq))}

def huffman_encode(msg, encoding):
  """ apply Huffman encoding to msg """
  return ''.join(map(lambda c: encoding[c], msg))


msg = 'an example sentence with only lowercase letters that can be used to test the algorithm we are explaining'
encoding = encoding_map(msg)
msg_huffman = huffman_encode(msg, encoding)
msg_huffman




def decoding_map(encoding):
  """ just invert encoding dictionary """
  return {v:k for k,v in encoding.items()}

def huffman_decode(bits, decoding):
  """ apply decoding to binary message 'bits' """
  key, res = '', []
  for bit in bits:
    key += bit
    if key in decoding:
      res.append(decoding[key])
      key = ''
  return ''.join(res)

huffman_decode(msg_huffman, decoding_map(encoding))