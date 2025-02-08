import numpy as np


def prod_non_zero_diag(x):
    """Compute product of nonzero elements from matrix diagonal.

    input:
    x -- 2-d numpy array
    output:
    product -- integer number


    Vectorized implementation.
    """

    pass


def are_multisets_equal(x, y):
    """Return True if both vectors create equal multisets.

    input:
    x, y -- 1-d numpy arrays
    output:
    True if multisets are equal, False otherwise -- boolean

    Vectorized implementation.
    """

    pass


def max_after_zero(x):
    """Find max element after zero in array.

    input:
    x -- 1-d numpy array
    output:
    maximum element after zero -- integer number

    Vectorized implementation.
    """

    pass


def convert_image(img, coefs):
    """Sum up image channels with weights from coefs array

    input:
    img -- 3-d numpy array (H x W x 3)
    coefs -- 1-d numpy array (length 3)
    output:
    img -- 2-d numpy array

    Vectorized implementation.
    """

    pass


def run_length_encoding(x):
    """Make run-length encoding.

    input:
    x -- 1-d numpy array
    output:
    elements, counters -- integer iterables

    Vectorized implementation.
    """

    pass


def pairwise_distance(x, y):
    """Return pairwise object distance.

    input:
    x, y -- 2d numpy arrays
    output:
    distance array -- 2d numpy array

    Vctorized implementation.
    """

    pass
    
def numpy_method(a):
    diagonal_elements = np.diag(a)
    ans = np.prod(diagonal_elements[diagonal_elements != 0])
    return ans


    pass

def vec_solve(x, y):
    unique_x, countx = np.unique(x, return_counts=True)
    unique_y, county = np.unique(y, return_counts=True)
    if np.array_equal(unique_x, unique_y) and np.array_equal(countx, county):
        return 0  # Совпали

    pass

def vec_solve3(x):
    x = np.array(x)
    mask = (x[:-1] == 0) 
    mb = x[1:][mask]
    if mb.size ==0:
        return "have not answer"
    else:
        return mb.max()

    pass

def vec_solve5(x):
    x = np.array(x)
    changes = np.diff(a)
    change_indices = np.where(changes != 0)[0] + 1  # +1, потому что diff уменьшает размер на 1

    cx = np.insert(a[change_indices], 0, a[0])

    cy = np.diff(np.concatenate(([0], change_indices, [len(a)])))

    return(cx)
    return(cy)

    pass