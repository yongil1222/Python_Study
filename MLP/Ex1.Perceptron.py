import numpy as np

class Perceptron():
    def __init__(self, thresholds=0.0, eta=0.01, n_iter=10):
        self.thresholds = thresholds
        self.eta = eta
        self.n_iter = n_iter

    def fit(self, x, y):
        self.w_ = np.zeros(1+x.shape[1])
        self.errors_ = []

        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(x,y):
                update = self.eta * (target-self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update!=0.0)
            self.errors_.append(errors)
            print(self.w_)

    def net_input(self, x):
        return np.dot(x, self.w_[1:]) + self.w_[0]

    def predict(self, x):
        return np.where(self.net_input(x) > self.thresholds, 1, -1)

if __name__ == '__main__':
    x = np.array([[0,0], [0,1], [1,0], [1,1]])
    y = np.array([-1,-1,-1,1])

    ppn = Perceptron(eta=0.1)
    ppn.fit(x,y)
    print(ppn.errors_)