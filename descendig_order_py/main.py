def descending_order(num):
    if num != int(num):
        return "that shit is not a number"
    try:
        new_arr=[]
        tmp_arr = [i for i in str(num)] if num > 0 else False
        n_max, n_min = (max(tmp_arr)), (min(tmp_arr))
        c_min, c_max = (tmp_arr.count(str(n_min))), (tmp_arr.count(n_max))
        limit_values = [[c_max, n_max], [c_min,n_min]]
        for i in limit_values:
            c = 0
            while c < i[0]:
                c+=1
                new_arr.append(int(i[1]))
        first = int(n_min)
        for i in tmp_arr: 
            if n_max != i and n_min != i:
                if int(i) >= first:
                    ins = new_arr[-1]
                    new_arr.insert(ins+1, int(i))
                    first = int(i)
                else:
                    pass
        return new_arr
            
    except TypeError as e:
        print("Value can't be below 0")
        return e
    except ValueError as e:
        print("Value is any shit")
        return e

print(descending_order(9911323))