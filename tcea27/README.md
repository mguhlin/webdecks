# TCEA 2027 math presenter deck

Open https://mguhlin.github.io/webdecks/tcea27/math-tools.html . The same encrypted deck is included in the MG Learn conference site and its protected offline packet.

Eighteen slides allocate exactly fifty minutes: graph prediction 0–5; number representations 5–15; GraphSplat investigation 15–35; retrieval and feedback 35–45; ACE planning 45–50. Every slide has about 100 words of teleprompter notes and a visible pacing window. Activity and tool links open in separate tabs. Facilitation design follows the supplied Professional Learning Facilitator Guide's progression from learner needs and a focused priority through modeling, discussion, reflection, and a concrete next step.

The deck follows canonical Web Deck v5. Project-local framework copies are in assets/ and are also inlined inside the encrypted HTML. The only framework customization is the exit link to the session hub; shared framework behavior is unchanged. The project skin uses system fonts for offline operation. V opens the two-monitor presenter window, F fullscreen, S notes, P audience-slide PDF; presenter A−/A+ resize notes. Speaker notes do not appear in the audience PDF.

Current content is encrypted with AES-256-GCM and a PBKDF2-SHA256 key (600,000 iterations). The password and private authoring sources are not in this repository. Enter the separately supplied presenter password. Reload or close a tab to lock it. On HTTPS a presenter window opened by an already-open deck can receive that opener's decrypted document in memory after same-origin, path, window-name, and opener checks. No password or decrypted document is persisted; the standard framework stores only slide index and notes font size. Local file presenter windows may require password entry again.

To update, edit the private source outside public Git, regenerate the deck using canonical framework copies, seal it with the conference project's seal-presenter.cjs, copy the encrypted output here, and run the conference presenter tests against both hosts. Do not commit plaintext notes, a password, decrypted screenshots, or a notes PDF.
