import numpy as np


def n_size_ndarray_creation(n, dtype=np.int):
    return np.array(range(n**2), dtype=dtype).reshape(n,n)

print('n_size_ndarray_creation')
print(n_size_ndarray_creation(3))
print()


def zero_or_one_or_empty_ndarray(shape, type=0, dtype=np.int):
    if type==0:
        return np.zeros(shape=shape, dtype=dtype)
    if type==1:
        return np.ones(shape=shape, dtype=dtype)
    if type==99:
        return np.empty(shape=shape, dtype=dtype)

print('zero_or_one_or_empty_ndarray')
print(zero_or_one_or_empty_ndarray(shape=(2,2), type=0))
print(zero_or_one_or_empty_ndarray(shape=(2,2), type=1))
print(zero_or_one_or_empty_ndarray(shape=(2,2), type=99))
print()


def change_shape_of_ndarray(X, n_row):
    return X.flatten() if n_row==1 else X.reshape(n_row,-1)

print('change_shape_of_ndarray')
X=np.ones((32,32), dtype=np.int)
print(change_shape_of_ndarray(X,2))
print()


def concat_ndarray(X_1, X_2, axis):
    try:
        if X_1.ndim == 1:
            X_1 = X_1.reshape(1,-1)
        if X_2.ndim == 1:
            X_2 = X_2.reshape(1,-1)
        return np.concatenate((X_1, X_2), axis=axis)
    except ValueError as e:
        return False

print('concat_ndarray')
a=np.array([[1,2],[3,4]])
b=np.array([5,6])
print(concat_ndarray(a,b,1))
print(concat_ndarray(a,b,0))
print()


def normalize_ndarray(X, axis=99, dtype=np.float32):
    X = X.astype(np.float32)
    n_row, n_column = X.shape
    if axis == 99:
        x_mean = np.mean(X)
        x_std = np.std(X)
        Z = (X-x_mean) / x_std
    if axis == 0:
        x_mean = np.mean(X, 0).reshape(1,-1)
        x_std = np.std(X, 0).reshape(1,-1)
        Z = (X-x_mean) / x_std
    if axis == 1:
        x_mean = np.mean(X, 1).reshape(n_row,-1)
        x_std = np.std(X, 1).reshape(n_row,-1)
        Z = (X-x_mean) / x_std
    return Z

print('normalize_ndarray')
X = np.arange(12, dtype=np.float32).reshape(6,2)
print(X)
print(normalize_ndarray(X))
print(normalize_ndarray(X, 1))
print(normalize_ndarray(X, 0))
print()

def save_ndarray(X, filename="test.npy"):
    pass


def boolean_index(X, condition):
    pass


def find_nearest_value(X, target_value):
    pass


def get_n_largest_values(X, n):
    pass
