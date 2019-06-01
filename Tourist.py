from itertools import combinations

infile = open("tourist_sample_input.txt")
outfile = open("out.txt", "w")

T = int(next(infile))

for i in range(T):
    line = next(infile).split()
    N, K, V = int(line[0]), int(line[1]), int(line[2])
    ls = []
    for j in range(N):
        ls.append(next(infile).rstrip())
    out = []
    if N == K:
        lin_out = ' '.join(ls)
        outfile.write("Case #" + str(i + 1) + ": " + lin_out + "\n")
        continue
    comb = combinations(ls, K)
    for a in range(((V - 1) % N) + 1):
        b = next(comb)
    lin_out = ' '.join(b)
    outfile.write("Case #" + str(i + 1) + ": " + lin_out + "\n")
