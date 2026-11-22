from pathlib import Path
from pypdf import PdfReader
import json, zipfile
root=Path(__file__).resolve().parent
r=PdfReader(root/'COS802_Ndlovu_Report.pdf')
assert 6 <= len(r.pages) <= 8
text='\n'.join(p.extract_text() for p in r.pages)
for x in ['13,885','25,354','22,195','16153970','REFERENCES']:
    assert x in text, x
fonts={}
for page in r.pages:
    for font in page['/Resources'].get('/Font',{}).values():
        f=font.get_object()
        for ff in f.get('/DescendantFonts',[f]):
            ff=ff.get_object()
            fd=ff.get('/FontDescriptor')
            if fd:
                fd=fd.get_object()
                embedded=any(k in fd for k in ['/FontFile','/FontFile2','/FontFile3'])
                fonts[str(ff.get('/BaseFont'))]=embedded
                assert embedded
            assert ff.get('/Subtype')!='/Type3'
log=(root/'COS802_Ndlovu_Report.log').read_text(errors='replace')
assert 'Overfull' not in log
assert 'undefined' not in log
print(json.dumps({'pages':len(r.pages),'words':len(text.split()),'fonts':fonts},indent=2))
(root/'evidence'/'pdf_validation.json').write_text(json.dumps({'pages':len(r.pages),'embedded_fonts':fonts,'overfull_boxes':0,'undefined_references':0},indent=2))
with zipfile.ZipFile(root.parent/'COS802_Ndlovu_Report_Source.zip','w',zipfile.ZIP_DEFLATED) as z:
    for p in root.rglob('*'):
        if p.is_file() and p.suffix not in ['.aux','.log','.out'] and p.name != 'COS802_Ndlovu_Report.pdf':
            z.write(p,Path('COS802_Report')/p.relative_to(root))
