def z_per_element(x, y):
    z = np.exp(x**2 + np.cos(y)) + 2
    return z

def row_dot(x, y):
    z = np.sum(np.matmul(x, y), axis=1)
    return z

def shrink(x):
    x = np.transpose(x[0::2,1::2])
    return x

def multiplier(x, y):
    result = (x.T * y).T
    return result

def double_quadrant(x):
    z = np.copy(x)
    z[:z.shape[0]//2:,:z.shape[1]//2:] *= 2 
    return z


