def prod_non_zero_diag(x):
    """Compute product of nonzero elements from matrix diagonal.

    input:
    x -- 2-d numpy array
    output:
    product -- integer number


    Not vectorized implementation.
    """

    pass


def are_multisets_equal(x, y):
    """Return True if both vectors create equal multisets.

    input:
    x, y -- 1-d numpy arrays
    output:
    True if multisets are equal, False otherwise -- boolean

    Not vectorized implementation.
    """

    pass


def max_after_zero(x):
    """Find max element after zero in array.

    input:
    x -- 1-d numpy array
    output:
    maximum element after zero -- integer number

    Not vectorized implementation.
    """

    pass


def convert_image(img, coefs):
    """Sum up image channels with weights from coefs array

    input:
    img -- 3-d numpy array (H x W x 3)
    coefs -- 1-d numpy array (length 3)
    output:
    img -- 2-d numpy array

    Not vectorized implementation.
    """

    pass


def run_length_encoding(x):
    """Make run-length encoding.

    input:
    x -- 1-d numpy array
    output:
    elements, counters -- integer iterables

    Not vectorized implementation.
    """

    pass


def pairwise_distance(x, y):
    """Return pairwise object distance.

    input:
    x, y -- 2d numpy arrays
    output:
    distance array -- 2d numpy array

    Not vectorized implementation.
    """

    pass

def classic_method(a, x, y):
    ans = 1
    for i in range(min(x, y)):
        if a[i][i] != 0:
            ans *= a[i][i]
    return ans
    pass
def notvec_solve(x, y):
    cntx = Counter(x)
    cnty = Counter(y)
    if cntx == cnty:
        return 0  # Совпали

    pass
def notvec_solve3(x):
    ans=-6
    for i in range(1, len(x)):
        if x[i-1]==0:
            ans=max(ans, x[i])

    if ans==None:
        return "have not answer"

    pass

def notvec_solve5(x):
    cx=[]
    cy=[]
    for i in range(1, len(x)):
        if a[i]==a[i-1]:
            ++cy.back()
        else:
            cx.append(a[i])
    return(cx)
    return(cy) 

    pass