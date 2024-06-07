def nonCausalFilter(t):
    filter_table = []
    
    for i in range(len(t)):
        start = max(0, i - 1)
        end = min(len(t), i + 2)
        
        sub_table = t[start:end]
        
        filter_table.append(average(sub_table))
        
    return filter_table

def average(t):
    if not t:
        return 0
    
    avg = round(sum(t) / len(t), 1)
    if(avg.is_integer()): return int(avg)
    return avg

t = [2, 1, 4, 5, 3, 6, 3, 7]
print(nonCausalFilter(t))