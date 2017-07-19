"""Jupyter notebook compatibility with PEX

Launches Jupyter notebook with a PEX-compatible
KernelSpecManager that appropriately invokes subprocesses with PEX.
"""
import sys

from jupyter_client.kernelspec import KernelSpecManager, NATIVE_KERNEL_NAME

class PEXKernelSpecManager(KernelSpecManager):
    """KernelSpecManager that is compatible with PEX
    
    Only the native kernelspec will be present.
    The .pex file must have been invoked by absolute path,
    otherwise it won't be found.
    """
    # disable kernel search dirs. Only want the default native kernel
    kernel_dirs = []
    # ensure native kernel dir is included
    ensure_native_kernel = True

    def get_kernel_spec(self, kernel_name):
        spec = super(PEXKernelSpecManager, self).get_kernel_spec(kernel_name)
        if kernel_name == NATIVE_KERNEL_NAME:
            # rewrite native kernelspec for PEX
            # Assumes sys.argv[0] is the abspath to the .pex file,
            # otherwise this won't work.
            # If the .pex is launched with 
            spec.argv = [sys.argv[0], '-f', '{connection_file}']
            spec.env['PEX_MODULE'] = 'ipykernel_launcher'
        return spec

if __name__ == '__main__':
    from notebook.notebookapp import NotebookApp
    app = NotebookApp.instance(kernel_spec_manager_class=PEXKernelSpecManager)
    app.launch_instance()
