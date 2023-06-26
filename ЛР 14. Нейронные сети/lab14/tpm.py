from update_rules import hebbian, anti_hebbian, random_walk
import numpy as np


class TPM:
    def __init__(self, k=3, n=4, l=6):
        self.k = k
        self.n = n
        self.l = l
        self.W = np.random.randint(-l, l + 1, [k, n])

    def get_output(self, X):
        k = self.k
        n = self.n
        W = self.W
        X = X.reshape([k, n])

        sigma = np.sign(np.sum(X * W, axis=1))
        tau = np.prod(sigma)

        self.X = X
        self.sigma = sigma
        self.tau = tau

        return tau

    def __call__(self, X):
        return self.get_output(X)

    def update(self, tau2, update_rule='hebbian'):
        X = self.X
        tau1 = self.tau
        sigma = self.sigma
        W = self.W
        l = self.l

        if (tau1 == tau2):
            if update_rule == 'hebbian':
                hebbian(W, X, sigma, tau1, tau2, l)
            elif update_rule == 'anti_hebbian':
                anti_hebbian(W, X, sigma, tau1, tau2, l)
            elif update_rule == 'random_walk':
                random_walk(W, X, sigma, tau1, tau2, l)
            else:
                raise Exception("Invalid update rule. Valid update rules are: " +
                    "\'hebbian\', \'anti_hebbian\' and \'random_walk\'.")