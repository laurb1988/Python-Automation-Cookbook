import fpdf
from random import randint

document = fpdf.FPDF()
document.set_font('Times', 'B', 14)
document.set_text_color(19, 83, 173)
document.add_page()
document.cell(0, 5, 'Pdf test document')
document.ln()
document.set_font('Times', '', 12)
document.set_text_color(0)
document.multi_cell(0, 5, 'This is an example of a long paragraph. ' * 10)
document.ln()
document.multi_cell(0, 5, 'Another long paragraph. Lorem ipsum dolor sit amet, consectetur adispiscing sit amet, consectetur adipiscing elit.' * 20)

#document.output('report.pdf')

######################STRUCTURING PDF######################
print('######################STRUCTURING PDF######################')

class StructuredPDF(fpdf.FPDF):
    LINE_HEIGHT = 5
    def footer(self):
        self.set_y(5)
        self.set_font('Times', 'I', 8)
        page_number = 'Page {number}/{{nb}}'.format(number=self.page_no())
        self.cell(0, self.LINE_HEIGHT, page_number, 0, 0, 'R')

    def chapter(self, title, paragraphs):
        self.add_page()
        link = self.title_text(title)
        page = self.page_no()
        for paragraph in paragraphs:
            self.multi_cell(0, self.LINE_HEIGHT, paragraph)
            self.ln()
        return link, page

    def title_text(self, title):
        self.set_font('Times', 'B', 15)
        self.cell(0, self.LINE_HEIGHT, title)
        self.set_font('Times', '', 12)
        self.line(10, 17, 110, 17)
        link = self.add_link()
        self.set_link(link)
        self.ln()
        self.ln()

        return link

    def get_full_line(self, head, tail, fill):
        '''
        It returns the line up to the width with the proper number
        of fill elements.
        '''
        WIDTH = 120
        width = 0
        number = 1
        while width < WIDTH:
            number += 1
            line = '{} '.format(head) + '.' * number + '  {}'.format(tail)
            width = self.get_string_width(line)

        return line

    def toc(self, links):
        self.add_page()
        self.title_text('Table of contents')
        self.set_font('Times', 'I', 12)

        for title, page, link in links:
            line = self.get_full_line(title, page, '.')
            self.cell(0, self.LINE_HEIGHT, line, link=link)
            self.ln()


LOREM_IPSUM = ('Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
               'Donec a diam sem. Sed ac nulla consequat, tempus tortor eget, '
               'fermentum turpis. Class aptent taciti sociosqu ad litora '
               'torquent per conubia nostra, per inceptos himenaeos. Fusce '
               'fermentum nibh ligula, sed dignissim risus hendrerit mollis. '
               'Fusce aliquam semper odio, in convallis mi sagittis et. Proin '
               'ac neque non massa lobortis maximus a quis turpis. Vestibulum '
               'vitae justo elit. Fusce hendrerit, libero in auctor auctor, '
               'risus velit fermentum dui, sed placerat urna augue vel lorem.'
               ' Praesent in enim porta, blandit lorem vulputate, semper '
               'nulla. Duis placerat neque vitae magna pulvinar elementum. '
               'Proin in velit pellentesque, tempus dolor vel, tincidunt '
               'turpis. Quisque vel sem metus. Nullam aliquet risus vel arcu '
               'tempus elementum.')


def main():
    document = StructuredPDF()
    document.alias_nb_pages()
    links = []
    num_chapters = randint(5, 40)
    for index in range(1, num_chapters):
        chapter_title = 'Chapter {}'.format(index)
        num_paragraphs = randint(10, 15)
        link, page = document.chapter(chapter_title,
                                      [LOREM_IPSUM] * num_paragraphs)
        links.append((chapter_title, page, link))

    document.toc(links)

    document.output('structured_report.pdf')


if __name__ == '__main__':
    main()

