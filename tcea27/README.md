# TCEA 2027 presenter decks

Open https://mguhlin.github.io/webdecks/tcea27/math-tools.html . The same encrypted deck is included in the MG Learn conference site and its protected offline packet.

Twenty slides allocate exactly fifty minutes: graph prediction 0–5; number representations 5–15; GraphSplat investigation 15–35; retrieval and feedback 35–45; ACE planning 45–50. Every slide has about 100 words of teleprompter notes and pacing guidance in the speaker notes. Activity and tool links open in separate tabs. Facilitation design follows the supplied Professional Learning Facilitator Guide's progression from learner needs and a focused priority through modeling, discussion, reflection, and a concrete next step.

The deck follows canonical Web Deck v5. Project-local framework copies are in assets/ and are also inlined inside the encrypted HTML. The only framework customization is the exit link to the session hub; shared framework behavior is unchanged. The project skin uses system fonts for offline operation. V opens the two-monitor presenter window, F fullscreen, S notes, P audience-slide PDF; presenter A−/A+ resize notes. Speaker notes do not appear in the audience PDF.

Current content is encrypted with AES-256-GCM and a PBKDF2-SHA256 key (600,000 iterations). The password and private authoring sources are not in this repository. Enter the separately supplied presenter password. Uncheck Remember access for temporary access, or use Forget access and lock. On HTTPS a presenter window opened by an already-open deck can receive that opener's decrypted document in memory after same-origin, path, window-name, and opener checks. No password or decrypted document is persisted. Optional thirty-day remembered access stores a non-exportable PBKDF2 CryptoKey in IndexedDB and an opaque SameSite=Strict cookie; Forget access and lock removes both. Each host requires its own initial unlock. The standard framework separately stores only slide index and notes font size. Local file presenter windows may require password entry again.

To update, edit the private source outside public Git, regenerate the deck using canonical framework copies, seal it with the conference project's seal-presenter.cjs, copy the encrypted output here, and run the conference presenter tests against both hosts. Do not commit plaintext notes, a password, decrypted screenshots, or a notes PDF.

Beyond the Rollout: Project Management That Works in K–12: https://mguhlin.github.io/webdecks/tcea27/project-management.html — twenty slides in fifty minutes, including a school project case, paired planning, stakeholder/dependency analysis, risk and change leadership, feedback, and revision.

Both decks use a photorealistic title image, Miguel Guhlin facilitator profile on slide two, a session overview, success criteria, and locally embedded infographic-style diagrams. Future-session design instructions: https://mglearn.github.io/tcea27/design-system/deck-guidelines.md . The reusable project skin is assets/tcea27-deck-theme.css.

Beyond the Rollout is presenter-led and uses a shared district case and completed worked framework. No attendee project or preparation is required. Brief decision discussions fit the fifty-minute plan. Original ADKAR, Kotter, KPI, milestone, and risk infographics follow the user-supplied infographic instructions; sources appear on model slides.

Slides six through twenty of Beyond the Rollout now combine photorealistic fictional school scenes with explanations of who acts, what they do, and what evidence they check. ADKAR and Kotter each have case-based explanations. The math deck has its own graph comparisons, number-line arrows, graph-selection pathway, sampling, reasoning, retrieval, and ACE infographics. Both retain twenty slides and fifty minutes. Warm, direct language is the default in the canonical spec and standalone instructions.

Access controls stay off projected slides. Use keyboard help (?) or the separate presenter toolbar for Forget access and lock. The generated-image disclosure is on the public workshop page rather than under slide photographs.

## Play, Explore, Explain: Cooperative Learning in Action

Open https://mguhlin.github.io/webdecks/tcea27/play-explore-explain.html . Twenty slides and exactly fifty minutes: concept Bingo0–9; cooperative routines9–18; two exploration rounds18–34; sharing34–42; classroom adaptation42–47; recall and closure47–50. Six requested tools: Bingo Card Generator/Caller, Quiz and Flashcard Studio, Meme Puzzle, Story Wheel, Dicebreaker Creator, Fortune Wheel. All slides have an original illustrative photo or native infographic; warm first-person speaker notes, facilitator second, clear success criteria.

Public companion, tasks, starter files, four PDF/HTML handouts: https://mglearn.github.io/tcea27/sessions/play-explore-explain/ . Remembered presenter access uses the same gate and stays off audience slides. External tools require internet access; the local Bingo and protected deck are in the offline packet.
