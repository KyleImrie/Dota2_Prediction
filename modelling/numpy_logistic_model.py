import time
import numpy as np


class LogisticRegression(object):

    learning_rate = None
    number_of_iterations = None

    @classmethod
    def setup(cls, learning_rate=0.001, number_of_iterations=10000):
        cls.learning_rate = learning_rate
        cls.number_of_iterations = number_of_iterations

    @classmethod
    def train(cls, x_train, y_train):
        assert isinstance(x_train, np.ndarray)
        assert isinstance(y_train, np.ndarray)
        assert x_train.shape[0] == y_train.shape[0]
        number_of_samples = x_train.shape[0]

        parameters = np.zeros((x_train.shape[1], 1))
        offset = 0

        # sizes = [10, 100, 1000, 10000, 50000]
        # for size in sizes:
        #     x_test = x_train[:size]
        #     y_test = y_train[:size]
        #     parameters = np.zeros((x_test.shape[1], 1))
        #
        #     estimate = cls._sigmoid(np.dot(x_test, parameters) + offset)
        #     tic = time.time()
        #     cost = -np.sum(y_test*np.log(estimate)+(1-y_test)*np.log(1-estimate))/size
        #     toc = time.time()
        #     print("Time to run was %0.3f" % (toc-tic))

        for iteration in range(cls.number_of_iterations):
            estimate = cls._sigmoid(np.dot(x_train, parameters) + offset)
            cost = -np.sum(y_train*np.log(estimate)+(1-y_train)*np.log(1-estimate))/number_of_samples
            d_params = np.dot(x_train.T, (estimate - y_train)) / number_of_samples
            d_offset = np.sum(estimate - y_train) / number_of_samples
            parameters -= cls.learning_rate * d_params
            offset -= cls.learning_rate * d_offset

            if iteration % 100 == 0:
                print("cost: %0.3f" % cost)

        return parameters, offset

    @staticmethod
    def _sigmoid(z):
        return 1 / (1 + np.exp(-z))


def main():
    x = np.genfromtxt('data/x.data', delimiter=',')
    y = np.genfromtxt('data/y.data', delimiter=',').reshape(50000, 1)
    LogisticRegression.setup()
    tic = time.time()
    parameters, offset = LogisticRegression.train(x, y)
    toc = time.time()
    print("Time elapsed: %0.3f" % (toc-tic))
    print(parameters)
    print(offset)


if __name__ == '__main__':
    main()
