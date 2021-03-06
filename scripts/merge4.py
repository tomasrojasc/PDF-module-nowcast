
'''
Credits: https://github.com/pmaupin/pdfrw/blob/master/examples/4up.py
usage:   4up.py my.pdf
Creates 4up.my.pdf with a single output page for every
4 input pages.
'''


from pdfrw import PdfReader, PdfWriter, PageMerge


def get4(srcpages):
    scale = 0.5
    srcpages = PageMerge() + srcpages
    x_increment, y_increment = (scale * i for i in srcpages.xobj_box[2:])
    for i, page in enumerate(srcpages):
        page.scale(scale)
        page.x = x_increment if i & 1 else 0
        page.y = 0 if i & 2 else y_increment
    return srcpages.render()


inpfn = 'output.pdf'
outfn = 'output.pdf'
pages = PdfReader(inpfn).pages
writer = PdfWriter(outfn)
for index in range(0, len(pages), 4):
    writer.addpage(get4(pages[index:index + 4]))
writer.write()
