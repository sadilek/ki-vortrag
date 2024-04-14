import graphviz
from IPython.display import SVG, display
import os
import torch


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
        x = torch.relu(W @ x + b)
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
