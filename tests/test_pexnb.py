"""Tests """
import os
import sys
from subprocess import check_call as sh, check_output
import tempfile
from unittest import mock

import jupyter_client
import pytest

import pexnb

PEXNB_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))


def build_pex(pexnb='./nb.pex'):
    sh(['pex', PEXNB_DIR, '-m', 'pexnb', '-o', pexnb])
    return pexnb


@pytest.fixture(scope='session')
def pexfile():
    with tempfile.TemporaryDirectory() as td:
        yield build_pex(os.path.join(td, 'nb.pex'))


@pytest.fixture
def kernel(request):
    ksm = pexnb.PEXKernelSpecManager()
    km = jupyter_client.KernelManager(
        kernel_name=pexnb.NATIVE_KERNEL_NAME,
        kernel_spec_manager=ksm,
    )
    km.start_kernel()
    kc = km.client()
    kc.start_channels()
    try:
        kc.wait_for_ready()
        yield kc
    finally:
        kc.stop_channels()
        km.shutdown_kernel()


@pytest.mark.local
def test_kernel_spec():
    ksm = pexnb.PEXKernelSpecManager()
    assert list(ksm.get_all_specs()) == [pexnb.NATIVE_KERNEL_NAME]
    spec = ksm.get_kernel_spec(pexnb.NATIVE_KERNEL_NAME)
    assert spec.argv[0] == os.path.abspath(sys.argv[0])


@pytest.mark.local
def test_main():
    from notebook.notebookapp import NotebookApp
    with mock.patch.object(NotebookApp, 'start', lambda self: None):
        pexnb.main([])
    app = NotebookApp.instance()
    NotebookApp.clear_instance()
    assert isinstance(app.kernel_spec_manager, pexnb.PEXKernelSpecManager)


@pytest.mark.local
def test_launch_kernel(kernel, capsys):
    reply = kernel.execute_interactive('import sys; print(sys.argv[0])')
    assert reply['content']['status'] == 'ok'
    out, err = capsys.readouterr()
    assert os.path.abspath(sys.argv[0]) in out


@pytest.mark.pex
def test_help_smoke(pexfile):
    help_out = check_output([pexfile, '-h']).decode('utf8', 'replace')
    assert 'Jupyter' in help_out

