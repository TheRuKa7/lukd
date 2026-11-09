# Mangaka analysis recovery

Observed 8 November 2026. This is a diagnostic record, not a provider incident report or a claim that the manga has been produced.

## Observed failure

The original [22-chapter project](https://higgsfield.ai/mangaka/649e59e2-9ac9-51f3-9cce-f9fab6389b0c/analyze) accepted the32-document-page manuscript and displayed **17,135 script words**. Its exact initial input PDF is preserved in [the upload archive](../../output/production/archive/OMEN_Mangaka_22_Chapter_Manuscript_initial_upload_20261108.pdf), SHA256 `b2061a4535bab6e8b09847a38b212b7fea726b5a2a2c25d82a4c9a2347fc740d`; later editorial rebuilds do not change what that project received. Analysis repeatedly stopped. The latest inspected stopped state found **no chapters**, kept Cast and Generate & read locked, disabled Export and displayed **0 credits spent**. Its interface showed no actionable error code or explanation.

Repeated resumes accumulated duplicate identities: Vendor/Breakfast vendor/the vendor, Collector/the Collector, Debt Hound/Debt Hounds, several schoolchildren and ward-worker groups, and repeated locations/props. Extraction also misidentified Ofuku as a spirit. Ofuku is an elderly human shrine keeper. Do not generate assets from this uncorrected cast list or treat resuming as a repair.

The manuscript combines story, production instructions, continuity references and later chapter blocks. Input complexity is a plausible contributor; the visible stopped state does **not** establish a word limit, context-window overflow or provider root cause. File acceptance and content analysis are different stages.

## Separate text-field issue

In a fresh unsent Describe test, the intended6,945-character Chapter01 input became3,979 visible characters and ended halfway through page16. That truncation was caught before submitting; the text was cleared. This is an observed constraint of that form/session, not a verified universal API limit. Do not paste a whole manuscript into Describe without checking the actual retained text and final beat.

## Controlled smaller test

The [archived original Chapter01 source](../../art/manga/mangaka/inputs/ch01_diagnostic_20261108.md) was rendered as a [small upload PDF](../../output/production/OMEN_Chapter_01_Story_Only.pdf): three document pages,75,423 bytes, all30 numbered comic-page beats. PDF SHA256 is `7c8b33a87ecea3da82f155b6f77ea4750acd6670b058ec1fc0d612f00a86ab1c`; source SHA256 is `9c8a30e682781309819500d9c5f620be3b07a06a1120291d67c5183b968a3ad1`. Document pagination is separate from manga pagination. That source contains about1,110 whitespace-counted words; Mangaka reports1,128 extracted script words. The current [clean input source](MANGAKA_CH01_CLEAN_INPUT.md) is a later editorial revision, not the exact running input.

A separate [Chapter01 pilot project](https://higgsfield.ai/mangaka/a5ee44de-fadf-568b-9d4e-a2e1f3faa5fe/analyze) was started once with B&W manga,2:3,English, free single-chapter mode and Auto generate off. Its short optional prompt preserves the page order, emotional acting, rescue hook and final spoon reveal. The original project remains preserved.

The pilot found one correctly ordered chapter, ten extracted character labels, twelve props and six locations. It reached the visible **Script analyzed** state and unlocked Cast and Generate & read. Its Cast workspace contained nine character cards, twelve props and six locations, plus additional looks; no duplicate aliases were present at that review. This is partial evidence that the cleaner input improves extraction, not a completed chapter.

NIL's native description was corrected to the established1.74m height, orange hair streak in monochrome values, RIGHT-wrist decoder, longer LEFT tail, three RIGHT-side clasps and NaN/resonance distinction. The existing selected NIL turnaround was uploaded through **Upload sheet**, producing a ready base reference at0 credits spent. The injured-hand look remains a separate unrendered variant. No story page or cast image was generated in this diagnostic.

After moving into Cast and saving/uploading that reference, the UI reverted to **Analysis stopped** and locked Generate & read again, while retaining the chapter and the reference. Whether the editing transition caused that reversal is unknown. Therefore a small input alone has **not** established a stable recovery, and script size cannot be treated as the sole cause. One controlled Resume was started on the smaller project; its final state must be recorded before further retry or production. Console inspection exposed no actionable analysis error, only an unrelated dialog accessibility warning.

Both uploaded PDFs are far below the official25MB upload limit. That rules out exceeding the documented byte-size cap; it does not prove that a17,135-word mixed manuscript is within an undocumented analysis budget. Do not invent a provider word/token limit, promise that splitting fixes the service, or claim the660-page comic is complete.

## Production after a successful test

Use [the lean series digest](MANGAKA_SERIES_DIGEST.md) for the overall22-chapter spine, subject to native plan review. Keep the full production manuscript as the editorial reference. Supply detailed chapter beats at the native chapter-editing stage only if the actual UI supports it; do not assume a private import endpoint or that separate projects share cast identities.

Before scaling, correct canonical aliases and reveal timing, approve recurring Cast & World references, and generate/review Chapter01. Count exactly30 exported story pages per chapter; Medium is approximate. Reconcile actual page order, acting, dialogue, geography and last-page hook. No generation or export count substitutes for story acceptance. No ordinary image generator may replace the requested Mangaka story pages.

Official workflow reference: [Higgsfield's Mangaka guide](https://higgsfield.ai/blog/higgsfield-introduces-mangaka). Native UI state and exported files are the evidence for this production attempt.
