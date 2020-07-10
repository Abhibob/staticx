from ..assets import copy_asset_to_tempfile
from ..errors import InternalError
from ..elf import open_elf, get_section, get_shobj_deps
from elftools.elf.gnuversions import GNUVerNeedSection
import logging
import os
from os.path import basename

def process_glibc_prog(ctx):
    if not is_linked_against_glibc(ctx.program):
        return

    try:
        nsskill = copy_asset_to_tempfile('libnsskill.so', debug=ctx.debug,
                prefix='libnsskill-', suffix='.so')
    except KeyError:
        raise InternalError("GLIBC binary detected but libnsskill.so not available")

    with nsskill:
        ctx.archive.add_fileobj('libnsskill.so', nsskill)

        # If so, add dependencies on libnss_files.so, libnss_dns.so
        # TODO: DRY with staticx.api.generate_archive
        for libpath in get_shobj_deps(nsskill.name):
            libname = basename(libpath).split('.')[0]
            if libname in ('libnss_files', 'libnss_dns'):
                ctx.archive.add_library(libpath)


def is_linked_against_glibc(prog):
    with open_elf(prog) as elf:
        sec = get_section(elf, GNUVerNeedSection)
        for verneed, vernaux_iter in sec.iter_versions():
            if not verneed.name.startswith('libc.so'):
                continue
            for vernaux in vernaux_iter:
                if vernaux.name.startswith('GLIBC_'):
                    logging.debug("Program linked with GLIBC: Found {} {}".format(
                        verneed.name, vernaux.name))
                    return True
    return False
