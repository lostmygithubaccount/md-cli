"""Tests for the dkdc-md-cli Python bindings."""

from dkdc_md_cli import run, main


class TestImports:
    def test_import_run(self):
        assert callable(run)

    def test_import_main(self):
        assert callable(main)

    def test_run_has_docstring(self):
        assert run.__doc__ is not None

    def test_main_has_docstring(self):
        assert main.__doc__ is not None
