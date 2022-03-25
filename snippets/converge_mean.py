#!/usr/bin/env python3


def converge_mean(data, epsilon=0.1, maxiter=1e3, bounds="both", stdev=1):
    if bounds not in ["upper", "lower", "both"]:
        raise AttributeError(
            "`bounds` must be one of `upper`, `lower` or `both`"
        )
    if maxiter < 1:
        raise AttributeError("`maxiter` must be > 1")
    if epsilon <= 0:
        raise AttributeError("`epsilon` must be > 0")

    data = np.asarray(data)
    prev_mean = np.nan
    for i in range(int(maxiter)):
        try:
            with np.errstate(all="raise"):
                mean = np.mean(data)
        except FloatingPointError:
            print(f"ERROR: Epsilon value of {epsilon} too small.")
            break
        std = np.std(data)

        if len(data) == 1 or np.abs(mean - prev_mean) < epsilon * std:
            break

        prev_mean = mean

        mask = np.ones_like(data, dtype=bool)
        if bounds != "lower":
            mask &= data <= mean + std * stdev
        if bounds != "upper":
            mask &= data >= mean - std * stdev

        data = data[mask]
    else:
        print("Did not converge")

    return mean, std
