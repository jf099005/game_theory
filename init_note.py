import os
import shutil
from pathlib import Path
from pdf2image import convert_from_path
from argparse import ArgumentParser
# pdf_path = 'lecture1.pdf'
# note_name = "0310"

def parse_args():
    args = ArgumentParser()
    args.add_argument('input_path', type=str)
    args.add_argument('--note_name', default = None, type=str)

    return args.parse_args()

def main(args):
    pdf_path = Path(args.input_path)
    pdf_name = pdf_path.stem

    pages = convert_from_path(pdf_path)

    note_name = args.note_name

    if note_name is None:
        note_name = pdf_name

    note_name += '.md'
    target_folder = os.path.join(pdf_path.parent, f'.{pdf_name}')
    os.makedirs(target_folder, exist_ok=True)

    note_default = ""

    for i_page in range(len(pages)):
        img_path = os.path.join(target_folder, f"{pdf_name}_{i_page}.png")
        pages[i_page].save(img_path, "PNG")
        note_default += f'![Page {i_page}]({img_path})\n'
        note_default += '<div style="background-color: #4a90e2; color: #ffffff; padding: 20px; border-radius: 10px; margin-bottom: 30px;">\n\n'
        note_default += f'##### 📝 Notes\n'
        # note_default += '在此輸入筆記，支援 LaTeX：$E = mc^2$\n\n'
        note_default += '\n\n'
        note_default += '</div>\n\n---\n\n' # 分隔線
        # note_default += "<!-- add notes here -->\n\n\n\n"    
    # shutil.move( pdf_path, os.path.join(target_folder, f"{pdf_name}.pdf") )

    note_path = note_name

    with open(note_path, 'w') as f:
        f.write(note_default)

if __name__ == "__main__":
    args = parse_args()
    main(args)