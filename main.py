
####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('book', 'back'), ('kookaburra', 'kookybird-'), ('relev-ant','-elephant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T), MED(S[1:],T[1:])))
  

def fast_MED(S, T):
  memo = [[0 for col in range(len(T)+1)] for row in range(len(S)+1)]
  # memo[1:][0] = range(1, len(S)+1)
  # memo[0][1:] = range(1, len(T)+1)
  for i in range(len(S) + 1):
    for j in range(len(T) +1):
      if i==0:
        memo[i][j] = j
      elif j==0:
        memo[i][j] = i
      elif S[i-1] == T[j-1]:
        memo[i][j] = memo[i-1][j-1]
      else:
        memo[i][j] = 1 + min(memo[i][j-1], memo[i-1][j], memo[i-1][j-1])
  return memo[len(S)][len(T)]

  
#def fast_MED(S, T, MED={}):

 # if (S == ""):
    #return(len(T))
  #if (T == ""):
   # return(len(S))
#  if (len(S), len(T)) in MED:
 #   return MED[(len(S), len(T))]
 # if (S[0] == T[0]):
#  result = fast_MED(S[1:], T[1:], MED)
 # else:
  #  result = 1 + min(fast_MED(S, T[1:], MED), fast_MED(S[1:], T, MED), fast_MED(S[1:],T[1:], MED))
  #MED[(len(S), len(T))] = result
  #return result



def fast_align_MED(S, T, MED={}):
  S_align = ""
  T_align = ""
    memo = [[0 for col in range(len(T)+1)] for row in range(len(S)+1)]
  # memo[1:][0] = range(1, len(S)+1)
  # memo[0][1:] = range(1, len(T)+1)
  for i in range(len(S) + 1):
    for j in range(len(T) +1):
      if i==0:
        memo[i][j] = j
      elif j==0:
        memo[i][j] = i
      elif S[i-1] == T[j-1]:
        memo[i][j] = memo[i-1][j-1]
      else:
        memo[i][j] = 1 + min(memo[i][j-1], memo[i-1][j], memo[i-1][j-1])
  i = 0
  j = 0
  while(i <= len(S) or j <= len(T)):
    if i==len(S) and j==len(T):
      return S_align, T_align
    if 
  #right (i+1, j) = gap for S and add letter to T
  #left (i, j+1) = letter for S and gap for T
  #diagonal = letter for both
  

def test_MED():
    for S, T in test_cases:
        assert fast_MED(S, T) == MED(S, T)
                                 
def test_align():
    for i in range(len(test_cases)):
        S, T = test_cases[i]
        align_S, align_T = fast_align_MED(S, T)
        assert (align_S == alignments[i][0] and align_T == alignments[i][1])
