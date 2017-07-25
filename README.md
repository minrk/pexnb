# pexnb

Entrypoint for launching jupyter notebooks from a pex

Modifies the default KernelSpecManager to:

1. only list the native kernel (same interpreter as the notebook server)
2. launch the IPython kernel via the pex entrypoint

Use it:

    pip install pex
    pex pexnb -m pexnb -o ./nb.pex

    ./nb.pex
