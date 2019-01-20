import numpy as np


def compute_cost(X, y, theta):
    # Initialize some useful values
    m = y.size
    cost = 0

    # ===================== Your Code Here =====================
    # Instructions : Compute the cost of a particular choice of theta.
    #                You should set the variable "cost" to the correct value.
    num = X.shape[0]
    cost = 0.5 * np.sum(np.square(X * theta) - y) / num
    # ==========================================================

    return cost
