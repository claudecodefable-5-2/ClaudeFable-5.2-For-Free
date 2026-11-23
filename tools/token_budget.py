def estimate_cost(input_tokens: int, output_tokens: int, mode: str = "standard") -> float:
    rates = {"standard": (8.0, 40.0), "batch": (4.0, 20.0), "fast": (16.0, 80.0)}
    in_rate, out_rate = rates[mode]
    return (input_tokens * in_rate + output_tokens * out_rate) / 1_000_000
