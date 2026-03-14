def linear_lr(step, total_steps, initial_lr, final_lr=0.0, warmup_steps=0) -> float:
    """
    Linear warmup (0→initial_lr) then linear decay (initial_lr→final_lr).
    Steps are 0-based; clamp at final_lr after total_steps.
    """
    # Write code here
    if step < warmup_steps and warmup_steps > 0:
        return float(step * initial_lr / warmup_steps)

    if step <= total_steps:
        denom = max(total_steps - warmup_steps, 1)
        return float(final_lr + (initial_lr - final_lr) * (total_steps - step) / denom)

    return float(final_lr)