import os

import graphviz
import numpy as np
import seaborn as sns
import torch
from IPython.display import SVG, display


def plot_f(f, x_min=-10, x_max=10, n_points=100):
    if f == torch.relu:
        x = torch.linspace(x_min, x_max, n_points)
        y = f(x)
        sns.lineplot(x=x.numpy(), y=y.numpy())
    else:
        x = np.linspace(x_min, x_max, n_points)
        y = [f(x) for x in x]
        sns.lineplot(x=x, y=y)


def edge_format(weight, max_weight):
    return {
        "color": "#c00" if weight < 0 else "#0c0",
        "penwidth": str(abs(weight) / max_weight),
        "arrowhead": "none",
    }


def plot_network(sample, layers):
    dot = graphviz.Digraph()

    x = sample.flatten()
    input_range = range(300, 320) if len(x) == 784 else range(0, len(x))

    for i in input_range:
        dot.node("input_%d" % i, label="%.2f" % x[i].item())

    for l in range(len(layers)):
        layer = layers[l]
        W, b = layer
        x = W @ x + b
        if l < len(layers) - 1:
            x = torch.relu(x)
        max_weight = torch.max(torch.abs(W)).item()
        for i in range(len(x)):
            label = (
                "%d: %.2f" % (i, x[i].item())
                if l == len(layers) - 1
                else "%.2f" % x[i].item()
            )
            dot.node("node_%d_%d" % (l, i), label=label)
            if l == 0:
                for j in input_range:
                    dot.edge(
                        "input_%d:e" % j,
                        "node_%d_%d:w" % (l, i),
                        **edge_format(W[i, j].item(), max_weight)
                    )
            else:
                prev_layer = layers[l - 1]
                for j in range(len(prev_layer[1])):
                    dot.edge(
                        "node_%d_%d:e" % (l - 1, j),
                        "node_%d_%d:w" % (l, i),
                        **edge_format(W[i, j].item(), max_weight)
                    )

    dot.attr(rankdir="LR", splines="false", ranksep="3", ordering="out")
    dot.render("network", format="svg", cleanup=True)
    display(SVG(filename="network.svg"))
    os.remove("network.svg")

    return x


def lookup_tokens(tokenizer, ids):
    if type(ids) == int:
        ids = [ids]
    return [fix_encoding(tok) for tok in tokenizer.convert_ids_to_tokens(ids)]


def fix_encoding(s: str):
    def recode(s: str):
        return str(bytes(s, "latin-1"), "utf-8")

    if s.startswith("Ġ"):
        return " " + recode(s[1:])
    if s.startswith("Ċ"):
        return "\n" + recode(s[1:])
    return recode(s)
