# COS802 report package

Author: Makungu Ndlovu, student 16153970, University of Pretoria.

The report uses the official SIGKDD Explorations LaTeX class downloaded from https://www.kdd.org/formats/sigkddExp.cls on 17 November 2026. The course requirement is 6–8 pages; the report is seven pages including references. No journal submission is implied.

Compile `COS802_Ndlovu_Report.tex` twice with pdfLaTeX from this directory. The checked PDF is included separately. Figures are already supplied; regenerating them is optional and requires pandas and matplotlib. `prepare_figures.py` does not train models.

## Template compatibility adjustment

The original class is preserved in `evidence/sigkddExp_original.cls`. Its legacy negative 14-point skip after numbered headings produced overlap under current LaTeX. That one skip was removed in the working class. The two-column layout, 9-point body text and template typography are retained. The PDF has no page numbers or footers. A manual column break within the references balances the final page approximately.

## Evidence and scope

All reported model results come from the canonical Drive project, seed 16153970, with 2,344 development and 586 test rows. Older local baseline outputs outside this package were not used. Supporting exports, reusable source and executed notebooks 02, 04, 05 and 06 are preserved in `evidence/`. Notebook files are evidence, not automatically executable report-build dependencies.

The report documents an audited limitation: Notebook 04's original arm passes raw features to imputation, whereas the engineered arm applies explicit structural-absence handling as well as feature creation. The main comparison is therefore a pipeline comparison. Notebook 06 retains structural-absence handling during feature removal and is post-hoc. These caveats do not alter the frozen final test scores.

Main evidence sources in Drive:

- Model comparisons: file 1-xD9WdRzSlHYYW4C11_FS7AEDuVVn4w_
- Selected configuration: file 1ps5pS2ImcfZKpHCWyjzwx0EjD4Fh7n2F
- Held-out metrics: file 1a8C-apsyG7HmtQr3zdDZrkOAGxSZTggy
- Bootstrap intervals: file 1k2LJg-z7lUTbYWEQ9lgzJ_bU9ph9ynrj
- Price quartiles: file 1mWYuE6EGCOOEUFKvCiMhZP6FO2uWxkPw
- Global SHAP: file 1qFxzo7eK7W7adQ_Thwne5cxtehawp8xy
- Local SHAP: file 1vJaDC78I0GvT0pEFqve2VmPazzaKANuD
- Notebook 04: file 1kjJjc90gwHhuPXYAfy6LPXfU_Hn8RN27
- Notebook 05: file 16O1QFlbj8bQRwwHksod3A6uDjImA3QPq
- Notebook 06: file 1TJFI_yhER7IL8Z5KlZqsNUWsE1ejTWTb

The current package is a report draft for author review. It does not claim a new clean execution of the full project, an external validation, or course submission.

