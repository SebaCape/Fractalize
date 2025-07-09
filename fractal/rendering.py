import matplotlib.pyplot as plt
import io

def render_image(data, extent):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.imshow(data, cmap="inferno", extent=extent, origin="lower")
    ax.set_xticks([])
    ax.set_yticks([])
    buf = io.BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight")
    plt.close(fig)
    buf.seek(0)
    return buf
