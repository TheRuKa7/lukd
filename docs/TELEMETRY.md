# ZERO-SUM: OMEN — Evidence and future telemetry

Updated 7 November 2026 IST. **No runtime telemetry/network calls in the jam.** Local explicit replay export and observer notes are sufficient initial evidence. This page specifies a possible post-jam system, not a deployed service or legal-compliance certificate.

## 1. Jam evidence

Record build/content/rules hashes, named browser/device, local accepted-command replay, results/round counts and opt-in playtest observations. Export only through a deliberate user action and tell the player what the filecontains. Do not upload install IDs, raw inputs, settings or story choices automatically. The reference replay is an in-memory experiment, not a complete production exporter.

## 2. Post-jam service gate T-SERVICE

Before collection: define exact purpose/fields, consent UI(defaultoff), retention/deletion process, security/access controls, backend/CDN logging behaviour and a published privacy notice appropriate to target regions. Verify requirements with appropriate review; do not state that “anonymous” or a random ID guarantees legal compliance or no IP processing. No purchases or external account setup follow merely from this design.

Consent state and schema versions are saved; declining has no gameplay penalty. Withdrawal stops new uploads and explains deletion scope. Do not collect accessibility setting usage by default: it can expose sensitive inferences and is unnecessary for initial balance questions. Aggregate route/round statistics where possible, avoid persistent identity, and collect no free-text/chat/content without a separate justified purpose and consent.

## 3. Candidate minimal event schema

|Event |Fields |Purpose |
|---|---|---|
|fight_end |build/rules/content version, encounter ID, mode, outcome, rounds, pattern counts |Difficulty/length distribution |
|offer_choice |offer Set ID, candidate IDs, chosen ID |Dead/overpowered offers; include opportunity denominator |
|progress_stop |coarse checkpoint ID, elapsed bucket |Where sessions end; no guaranteed quit event |
|error |errorcode, build, coarse platform |Crashes/soft-locks; sanitize payloads |

Chosen digit/party composition is optional schema expansion only if needed and disclosed. No raw timestamps beyond what the justified analysis needs. No assumptions that browsers deliver quit events reliably. Idempotent event IDs and retry-safe ingestion avoid duplicate rewards/statistics; telemetry never authorizes or computes gameplay rewards.

## 4. Analysis and limits

Compare model assumptions with observed frequencies only after defining comparable parties, input modes and build versions. Pickrate alone is not power: account for offer frequency, unlock availability, player skill and survivorship. Treat apparent boss/charm outliers as investigation triggers, not automatic balance patches. Human playtests remain needed to understand confusion and enjoyment.

Gate acceptance: explicit declined-consent networktrace empty; consented payloadexact; withdrawal/deletion tested; server logs audited; retention job verified; outage never blocks game; security/privacy review recorded. These are future production tasks; no server or dashboard exists here.
