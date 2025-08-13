import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

def significance_pairs(data, cat_col, value_col, alpha=0.05):
    """Return list of (catA, catB, pval) that are significant by Welch t-test."""
    cats = list(data[cat_col].unique())
    sig = []
    for i in range(len(cats)):
        for j in range(i + 1, len(cats)):
            a = data.loc[data[cat_col] == cats[i], value_col].dropna()
            b = data.loc[data[cat_col] == cats[j], value_col].dropna()
            if len(a) >= 2 and len(b) >= 2:
                _, p = ttest_ind(a, b, equal_var=False)
                if p < alpha:
                    sig.append((cats[i], cats[j], p))
    return sig

def add_sig_bar(ax, x1, x2, y, h=1.0, text="*", lw=1.5):
    """Draw a bracket and asterisk between bars at positions x1 and x2."""
    ax.plot([x1, x1, x2, x2], [y, y + h, y + h, y], lw=lw, c="k")
    ax.text((x1 + x2) / 2, y + h, text, ha="center", va="bottom", fontsize=20)

def main(csv_path):
    df = pd.read_csv(csv_path, sep="\t")

    # Optional: fix any comma-as-decimal issues just in case
    def to_float_series(s):
        return pd.to_numeric(s.astype(str).str.replace(",", ".", regex=False), errors="coerce")

    df["theta (ellipse)"] = to_float_series(df["theta (ellipse)"])
    
    # Create new column for 180 - theta
    df["180-theta"] = 180 - df["theta (ellipse)"]

    # --- Derive category from 'image' (prefix before first underscore) ---
    df["category"] = df["image"].astype(str).str.split("_").str[0]

    # --- Compute stats using 180-theta instead of theta ---
    stats = df.groupby("category")["180-theta"].agg(["mean", "std"]).reset_index()
    categories = list(stats["category"])
    x = np.arange(len(categories))
    means = stats["mean"].to_numpy()
    stds = stats["std"].to_numpy()

    # --- Plot ---
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(x, means, yerr=stds, capsize=10)

    ax.set_ylabel(r"180° - $\theta_{\mathrm{ellipse}}$", fontsize=20)  # Updated label
    ax.set_xticks(x)
    ax.set_xticklabels(categories, fontsize=16)
    ax.tick_params(axis="y", labelsize=16, direction="out", length=6, width=1.5)
    ax.tick_params(axis="x", direction="out", length=6, width=1.5)
    ax.grid(False)

    # --- Significance annotations using 180-theta ---
    sig_pairs = significance_pairs(df, "category", "180-theta", alpha=0.05)
    cat_to_x = {cat: xi for xi, cat in enumerate(categories)}

    top_y = np.max(means + stds)
    step = 2.0
    current_level = 0
    for a, b, p in sig_pairs:
        x1, x2 = cat_to_x[a], cat_to_x[b]
        y = top_y + 1.0 + current_level * step
        add_sig_bar(ax, x1, x2, y, h=0.8, text="*")
        current_level += 1

    plt.tight_layout()
    plt.savefig("category_180-theta_barplot_significance.png", dpi=300)
    plt.show()


path = "contactAngles.csv"
main(path)
