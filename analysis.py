import jiwer
import numpy as np

def wer(ref, hyp):
    ref, hyp = ref.strip(), hyp.strip()
    return round(jiwer.wer(ref, hyp), 3)

#ref, hyp
def levenshtein(seq1, seq2):
    seq1, seq2 = seq1.strip(), seq2.strip()
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1
    matrix = np.zeros ((size_x, size_y))
    for x in range(size_x):
        matrix [x, 0] = x
    for y in range(size_y):
        matrix [0, y] = y

    for x in range(1, size_x):
        for y in range(1, size_y):
            if seq1[x-1] == seq2[y-1]:
                matrix [x,y] = min(
                    matrix[x-1, y] + 1,
                    matrix[x-1, y-1],
                    matrix[x, y-1] + 1
                )
            else:
                matrix [x,y] = min(
                    matrix[x-1,y] + 1,
                    matrix[x-1,y-1] + 1,
                    matrix[x,y-1] + 1
                )
    return (matrix[size_x - 1, size_y - 1])

def calculate_metrics(ref_file, hyp_file):
    temp_wer = []
    temp_levenshtein = []
    temp_response_time = []
    temp_rtf = []

    with open(ref_file) as f:
        ref = f.read().split('\n')
        ref.remove('')
        #convert ref to dictionary
        ref = [i.split(' ') for i in ref]
        ref = {i[0].strip(): ' '.join(i[1:]) for i in ref}
    
    with open(hyp_file) as f:
        hyp = f.read().split('\n')
        hyp.remove('')
        hyp = [i.split(',') for i in hyp]
        hyp = {i[0].strip(): i[1:] for i in hyp}

    for i in ref:
        temp_wer.append(wer(ref[i], hyp[i][0]))
        temp_levenshtein.append(levenshtein(ref[i], hyp[i][0]))
        temp_response_time.append(float(hyp[i][1].strip()))
        temp_rtf.append(float(hyp[i][2].strip()))
    
    return temp_wer, temp_levenshtein, temp_response_time, temp_rtf