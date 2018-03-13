def randomization(df, n_repeat=1):
    s = set(Series.tolist(df['syllable'])) #data is set 
    res = []
    for n in range(n_repeat):
        if res:
            # Avoid the last placed element
            lst = list(s.difference({res[-1]}))
            # Shuffle
            random.shuffle(lst) 
            #df.sample(frac=1)
    
            lst.append(res[-1])
            # Shuffle once more to avoid obvious repeating patterns in the last position
            lst[1:] = random.sample(lst[1:], len(lst)-1)
        else:
            lst = df[:]
            random.shuffle(lst) 
            #df.sample(frac=1)
            
        res.extend(lst)

    return res


    def compareConsecutive(x):
        for i in x:
            if i== x[x.index(i)+1]:   #check if two consecutive values in a list x are the same 
                return False

    while compareConsecutive(ans) == False  #if the same, then shuffle' elif stop random.shuffle
            random.shuffle(ans)



