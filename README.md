# Homework #10: Linear Programming and Monte Carlo Integration

## Task 1: Production Optimization

**Problem:** Maximize production of Lemonade and Fruit Juice with limited resources.

**Resources:**
- Water: 100, Sugar: 50, Lemon Juice: 30, Fruit Puree: 40

**Requirements:**
- Lemonade: 2 Water + 1 Sugar + 1 Lemon Juice
- Fruit Juice: 2 Fruit Puree + 1 Water

**Result:**
- **Lemonade: 30 units**
- **Fruit Juice: 20 units**
- **Total: 50 units**

Lemon Juice and Fruit Puree are bottlenecks (100% utilized).

---

## Task 2: Monte Carlo Integration

**Problem:** Calculate ∫₀² x² dx using Monte Carlo method.

**Analytical solution:** x³/3 |₀² = **2.6666666667**

**Results:**

| Method | Result | Error % |
|--------|--------|---------|
| Analytical | 2.6666666667 | - |
| SciPy quad | 2.6666666667 | ~0% |
| Monte Carlo (1K) | 2.6798 | 0.49% |
| Monte Carlo (10K) | 2.6594 | 0.27% |
| Monte Carlo (100K) | 2.6637 | 0.11% |
| Monte Carlo (1M) | 2.6665 | 0.006% |

**Conclusions:**

1. Monte Carlo gives accurate results - 0.006% error with 1M samples
2. Accuracy improves with more samples (follows √n law)
3. Method validated - matches analytical and scipy.quad results
4. Useful when analytical solution is difficult or impossible
