from PyPDF2 import PdfReader, PdfWriter, Transformation
from PyPDF2.generic import AnnotationBuilder


def extract_info(file_path):
    reader = PdfReader('logo_dark_long_transparent.pdf')
    img_page = reader.pages[0]
    img_page.add_transformation(Transformation().scale(sx=0.3, sy=0.3))
    # img_page.add_transformation(Transformation().translate(tx=200, ty=150))
    reader = PdfReader(file_path)
    information = reader.metadata
    [print(key[1:], ": ",  information[key]) for key in information.keys()]

    writer = PdfWriter()

    page_indices = list(range(0, len(reader.pages)))
    for index in page_indices:
        content_page = reader.pages[index]
        mediabox = content_page.mediabox
        content_page.merge_page(img_page)
        content_page.mediabox = mediabox
        writer.add_page(content_page)
        writer.add_annotation(index, AnnotationBuilder.link(rect=(0, 0, 250, 50), url="http://127.0.0.1"))
    for page in reader.pages:
        writer.add_page(page)

    writer.add_metadata(
        {
            '/Producer': 'TheCloudLib',
            '/Creator': 'Zain'
        }
    )

    with open("w"+file_path, 'wb') as f:
        writer.write(f)


extract_info("9709_m22_qp_32.pdf")
