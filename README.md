# pexnb

Entrypoint for launching notebooks with PEX

Modifies the default KernelSpecManager to:

1. only list the native kernel (same interpreter as the notebook server)
2. launch the IPython kernel via the pex entrypoint

Use it:

    pip install pex
    pex notebook pexnb -m pexnb -o ./nb.pex

    $PWD/nb.pex

Notes:

- Resulting .pex **must** be invoked by absolute path, otherwise the .pex file cannot be found.
