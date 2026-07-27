from pathlib import Path

import click

from pdf_names_conversion import PdfPath
from pdf_sanitize_info import del_info, pdf_update_metadata
from PdfManifestEntry import PdfManifestEntry

# --------------------------------------------
# public functions
#
# --------------------------------------------


def single_pdf_action_with_path(pdf_path, entry: PdfManifestEntry, sanitize_info=False):
    if not Path(pdf_path).exists():
        return f"pdf not found {str(pdf_path)}"
    p: PdfPath = PdfPath(pdf_path)
    if sanitize_info:
        del_info(p)
        pdf_update_metadata(p, entry)


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------


@click.command()
@click.argument("pdf_path", type=click.Path(exists=True, dir_okay=False))
@click.option(
    "--sanitize-info",
    is_flag=True,
    default=False,
    help="sanitize info",
)
def main(pdf_path: str, sanitize_info: bool) -> None:
    entry: PdfManifestEntry = PdfManifestEntry.new_empty_manifest_entry()
    entry.author="test author"
    entry.isbn="123456"
    entry.title="test title"
    single_pdf_action_with_path(pdf_path, entry, sanitize_info=sanitize_info)


if __name__ == "__main__":
    main()


# python pdf_actions.py /tmp/tmp80tnmer3/ml-linearized-sanitized.pdf --legacy-info
# /bin/python pdf_actions.py  /home/sd/tmp/1-sanitized2/Concise\ Guide\ to\ Software\ Testing\ by\ Gerard\ ORegan-y2019-linearized-sanitized.pdf    --print-values
