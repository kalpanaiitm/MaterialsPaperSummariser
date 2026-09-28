# Architecture

Uploaded PDF bytes → bounded page extraction → keyword-based passage selection → manual review.

The README names the runnable entry point. Components should keep validation separate from the core operation and presentation. The existing code is the source of truth; this page does not claim planned capabilities as implemented.

## Failure and privacy boundaries
Extractive only; keywords can miss or misrepresent scientific findings. Use non-sensitive or permitted inputs for demos. Do not commit user documents, audio, credentials, or generated outputs.
