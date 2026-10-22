# Play Data safety response data for v0.31.29

`play-data-safety-v0.31.29.csv` fills the data-type and data-handling fields in the official Google sample CSV linked from https://support.google.com/googleplay/android-developer/answer/10787469 . Sample/demo responses have been cleared. The app source reference is 0fdf8b2 (ShallWePuzzle Android v0.31.29; the data practices are unchanged since v0.31.28). The v0.31.28 filename is kept as a byte-identical compatibility download.

It selects approximate location, app interactions, crash logs, diagnostics, and device/other IDs. Crash logs are optional adult opt-in collection, analytics purpose, with processor-only Crashlytics transfer treated under the service-provider sharing exception. The other four grouped AdMob categories are collected/shared, retained rather than ephemeral, and use analytics, advertising/marketing, and fraud/security purposes. Data collection and encryption are Yes. Manual privacy/deletion requests are available through the policy contact.

This CSV is a prepared response file, not evidence that Play Console has accepted or saved it. Import can replace existing answers. The earlier file omitted the newer required account-creation question. The corrected file includes all six `PSL_SUPPORTED_ACCOUNT_CREATION_METHODS` options, selecting only `PSL_ACM_NONE=TRUE`; external account login is FALSE, data deletion requests are YES with the rights URL, and unverified badges are FALSE. It replaces the obsolete deletion boolean with the current deletion question. After importing, explicitly confirm no account creation, no outside-account login, deletion request URL https://dydxo116.github.io/shallwepuzzle-privacy/#rights , no unverified independent badges, and the remaining Preview. The optional Families promise badge is not used as a compliance certification. Age groups belong to a separate declaration and remain all six groups. No declaration or app release is submitted for review by generating this file.


## Account question import fix

The five-column machine-readable schema for the newer basic/account fields was
checked against a public current Console export example:
https://github.com/guyluz11/privacy_policy/blob/main/word_link/word_link_data_safety.csv .
Only question/response identifiers and labels were used; **none of that app's
answers were copied**. Every existing ShallWePuzzle data-type and handling answer
was preserved. New unrelated questions were left unanswered/false as appropriate.
This is still not our own authenticated Console export or proof of import acceptance.

Run `python3 -m unittest test_data_safety.py` to check account creation, external
login, deletion URL, badges and all five selected data types/handling decisions.

If Console reports another missing question, do not invent a machine response ID:
check the actual form/export and confirm the corresponding app behavior.
