import numpy as np
from typing import Tuple


class HypothesisFunction:
    def __init__(self, l: int, m: int, k: int) -> None:
        # TODO [1]: Initialize the function's unknown parameters
        self.l: int = l
        self.m: int = m
        self.k: int = k

        # TODO [2]: Initialize Wh and Wo matrices from a standard normal distribution
        self.Wh: np.ndarray = np.random.randn(m, l)
        self.Wo: np.ndarray = np.random.randn(k, m)

        # TODO [3]: Initialize bo and bo column vectors as zero
        self.bo: np.ndarray = np.zeros((k, 1))
        self.bh: np.ndarray = np.zeros((m, 1))

    def forward(self, x: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        # Ensure input shape matches input size
        assert x.shape[0] == self.l, f"Your input must be consistent the value l={self.l}"

        # TODO [4]: Compute a as mentioned above
        a = np.tanh(np.dot(self.Wh, x) + self.bh)

        # TODO [5]: Compute output ignoring ReLU
        y = np.dot(self.Wo, a) + self.bo

        # TODO [6]: Apply ReLU on the output with numpy boolean masking
        y[y < 0] = 0

        return y, a

    def double_forward(self, x1, x2):
        # Perform forward function for the two inputs
        y1, _ = self.forward(x1)
        y2, _ = self.forward(x2)

        # TODO [7]: Concatenate the two outputs
        z = np.concatenate((y1, y2), axis=0)

        # TODO [8]: Normalize the concatenated result
        z_bar = (z - np.mean(z, axis=0)) / np.std(z, axis=0)

        return z_bar

        # TODO [9]: Annotate all initialized variables and functions above

    def count_params(self):
        # TODO [10]: Make a lambda function num_params that takes an array z and returns np.prod(z.shape)
        def num_params(z): return np.prod(z.shape)
        # TODO [11]: return the total number of parameters by summing the function over Wh, Wo, bh, bo
        total_params = num_params(
            self.Wh) + num_params(self.Wo) + num_params(self.bh) + num_params(self.bo)
        return total_params
