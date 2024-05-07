def sort_matrix(M):
    result = []
    for i in range(len(M)):
        result.append(sum(M[i]))
    for i in range(len(M)):
        for j in range(i+1,len(M)):
            if result[i] > result[j]:
                result[i],result[j] = result[j],result[i]
                M[i],M[j] = M[j],M[i]
    return M
