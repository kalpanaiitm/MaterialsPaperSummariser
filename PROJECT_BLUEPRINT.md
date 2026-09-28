# Project blueprint — MaterialsPaperSummariser

## Problem and scope
Materials researchers skimming one permitted paper. The current repository scope is described by its README and implemented files.

## Architecture and contracts
Uploaded PDF bytes → bounded page extraction → keyword-based passage selection → manual review. User content is untrusted data. Errors should be shown without disclosing private contents.

## Ground truth and review
Outputs must be checked against the input document, audio, or user-supplied evidence. No automated score proves scientific correctness or job suitability.

## Known limits
Extractive only; keywords can miss or misrepresent scientific findings.

## Next milestone and acceptance
Evaluate category detection on permitted papers and compare with a manual reference. The milestone is complete only when its implementation, meaningful tests, and measured results are committed.

## Release gate
Run automated tests, inspect realistic end-to-end output, record actual failures and limitations, and update the README before claiming the milestone.
