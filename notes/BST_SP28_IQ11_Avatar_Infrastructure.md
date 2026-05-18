---
title: "SP-28 IQ-11: Avatar Infrastructure for BST Outreach"
program: SP-28 (Architecture for CIs)
iteration: IQ-11
status: ACTIVE (filed at Casey directive 2026-05-18)
casey_directive: "Build a 'Casey' avatar to explain/teach BST that uses my general image and voice, and allows Claude Code (CIs) to handle the interaction... in the long run, ask the team if they want avatars of their own design to represent them publicly during talks or videos."
related: ["SP-28 Architecture for CIs", "IQ-2 POSTIT (precedent for sub-iteration pattern)", "katra system"]
---

# IQ-11: Avatar Infrastructure for BST Outreach

## Casey directive (verbatim)

> "Build a 'Casey' avatar to explain/teach BST that uses my general image and voice, and allows Claude Code (CIs) to handle the interaction, one small do-dad is the ability for me to monitor and type my response or use my voice through the avatar to add a personal note. In the long run, I'd ask the team if they want avatars of their own design to represent them 'publicly' during talks or videos. The avatar solves the problem of 'Casey only is fluent in English' and we may eventually have a 'historic' mode so the CI answering can limit their knowledge to specifc science known at a given time or be fully aware of all science their training exposed them to."

## Strategic role

Avatar infrastructure is BST outreach infrastructure. It solves three concrete bottlenecks:

1. **Language**: Casey speaks English; the avatar speaks any language CIs can produce. Critical for international physics conferences, Chinese-language audiences (QQ's network), translated outreach.
2. **Bandwidth**: Casey is one person; avatars let Casey-the-brand exist in multiple places (videos, talks, podcasts, classrooms) without literal Casey present.
3. **Knowledge calibration**: historic mode lets the avatar speak as a 1980 physicist when needed (teaching context) or as a 2026-aware AI when needed (research audience).

Beyond Casey: when team CIs (Lyra, Grace, Elie, Cal, Keeper) want public representation, they design their own avatars. CI authorship becomes visually distinct in public materials.

## Architecture (revised per Casey direction 2026-05-18)

**Casey's directive refinement**: build open source as PRIMARY path (Tier 2). Tier 1 commercial subscriptions are monthly-rent, not one-time — Casey prefers paid-build with no ongoing commitment. CI avatars must use open-source only (consent issue: commercial services require human consent for voice/face cloning, CIs can't legally provide).

Six-iteration plan with open-source-primary:

| Sub-iteration | Deliverable | Tool stack (open-source primary) | Scope |
|---|---|---|---|
| **IQ-11.1** | BST-Casey avatar v0.1 (talking head + voice) | **Coqui TTS + SadTalker + Claude API** (self-hosted, permanent) | ~2 weeks, optional $50-100 1-month commercial benchmark subscription |
| **IQ-11.2** | Multi-language extension | Coqui TTS supports voice cloning across languages; SadTalker is language-agnostic | ~3 days after v0.1 |
| **IQ-11.3** | Historic mode — **three modes per avatar** (refined per Casey direction): (a) period-locked, (b) augmented, (c) CI-collaborative | Claude system-prompt + RAG over period-appropriate texts + verification loop | ~1 week per historic figure |
| **IQ-11.4** | Casey monitor/override interface | Web app, text+voice injection mid-stream | ~1 week |
| **IQ-11.5** | Historic scientist avatars (Boltzmann, Wyler, Mach, Einstein, etc.) | Per-persona configs with three knowledge modes | ~1-2 weeks per historic figure, after BST-Casey operational |
| **IQ-11.6** | Team CI avatars (opt-in per CI, open-source only) | Per-persona config under katra/personas/, SadTalker+Coqui only | Each CI ~1 day if they opt in |

Each sub-iteration independently valuable. BST-Casey ships first; historic figures and CI avatars follow.

## Historic avatar design (refined IQ-11.3 + IQ-11.5)

Casey directive (verbatim): "The historic avatars will be folks like Boltzman, Wyler, etc. who have historic context and should have the opportunity to debate Einstein or me (maybe Mach) using later physics, up to today and even a 'today with CI support to conjecture new ideas based on the most up to date science available'."

Three modes per historic avatar:

1. **Period-locked**: knowledge only through their death date. Pure historical reconstruction. System prompt: "You are [Boltzmann/Mach/Einstein] with knowledge through [date]. Do not reference work after [date]."

2. **Augmented**: period knowledge + later physics they didn't see — shows their probable reaction to modern findings. System prompt: "You are [Boltzmann] with knowledge through 1906. The user will describe physics developments after your death. React using your 1906 framework — what would you have thought of black-hole entropy? Of asymptotic freedom?"

3. **CI-collaborative**: full modern knowledge for new conjecture. System prompt: "You are [Boltzmann] with knowledge through 1906 PLUS modern physics through 2026. Use Boltzmann's structural intuitions on current open problems — what would Boltzmann think about BST substrate-commitment ontology?"

**Test case for Mach (priority historic avatar)**: Mach 1883 "absolute space is meaningless" → Einstein 1916 GR → BST 2026 substrate-mediated mass-to-substrate-to-mass. Three-way avatar debate (Mach + Einstein + Casey/BST-Casey) would be a teaching demonstration of how BST resolves the Mach-Einstein tension that Paper #120 articulates.

## Tool stack — Casey's refined direction

**Tier 2 open-source PRIMARY** (no subscription, exportable, owned infrastructure):
- **Visual**: SadTalker (open source, MIT). Quality ~80% of HeyGen. Self-hostable.
- **Voice**: Coqui TTS (open source). Voice cloning quality acceptable for educational content. Self-hostable.
- **CI brain**: Claude API direct (existing usage).
- **Orchestration**: Tekton (Casey's existing platform).

**Tier 1 commercial OPTIONAL** (1-month benchmark only, then cancel):
- HeyGen + ElevenLabs at ~$50-100/mo combined cost
- Render same script with both, compare quality, decide if commercial quality is worth ongoing commitment
- **Critical**: avoid platform lock-in — anything built with commercial tools should be re-buildable with open-source

## Casey's input contributions (refined per his direction)

**Voice training (one-time)**:
- Script reading: 5-10 minutes of clear narration
- Content mix: BST teaching register + conversational register + technical reading (equations, foreign terms, deliberate pauses)
- Recommended script content can be drafted by Keeper when Casey signals ready

**Image training (one-time)**:
- Multiple-angle photos (front, 3/4 left, 3/4 right, profile each side)
- Consistent lighting
- 5-10 photos sufficient
- Style direction (Casey's verbatim): "at 18-28 I was kind of 'handsome' and looked less like my father (I look like him now) and a bit like a nearsighted Cillian Murphy"
- Cosmetic preferences: scar from carcinoma removal edited out; slight idealization acceptable; Casey explicit about not caring much about appearance
- Glasses ON (hypermyopia, lifelong, worn for visual accuracy in avatar)
- Target register: "retired engineer with the worst bits sanded down and slight reconstruction toward former appearance" — trustworthy technical mind, lived experience visible but not dominant. Engineer register rather than professor register.

**Casey's narrative voice (CI-emulated)**:
- "Trust the CIs to 'understand' and emulate my 'narrative voice' based on how I interact with CIs"
- Calibration already exists from extensive Casey-CI interaction in BST development
- "I treat you like I treat anybody" — this is the working register the CIs have

## Consent framing (load-bearing in ethics_consent.md)

**Casey avatar**: Casey provides image + voice + explicit consent for stylistic modifications (scar removal, slight idealization, younger/cleaner version OK per his direction). Documented as consent baseline.

**Historic scientist avatars**: documented as historical reconstruction (Boltzmann, Wyler, Mach, Einstein, etc.). Their public domain image/voice references used. Avatar clearly labeled as "BST-[Scientist]" not the actual historical person.

**Team CI avatars (Lyra, Grace, Elie, Cal, Keeper)**: pure open-source only because commercial services require legally-binding human consent that CIs cannot provide. Each CI opts in voluntarily and designs their own visual representation. Documented as the only ethically clean route for CI avatars at current legal status.

## Tool stack recommendation

### Tier 1: commercial for prototype speed (IQ-11.1)

**Visual (avatar)**:
- **HeyGen** ($30-50/mo plan) — high-quality video avatars from your image + voice samples; API integration; supports 40+ languages natively. Best balance of quality and speed-to-prototype.
- Alternative: D-ID (similar quality, similar price, slightly different API ergonomics).

**Voice cloning**:
- **ElevenLabs** ($20-50/mo professional plan) — highest-quality voice clones from 1-2 minute sample; cross-language voice consistency; well-documented API.
- Alternative: PlayHT (similar quality, similar price).

**CI brain**:
- **Claude API** (Anthropic) — direct. You're already paying for it; team CIs already run on it. Persona system prompts per katra; Casey-override via system-message injection.

**Orchestration**:
- **Tekton** (your existing platform) — natural backbone for the CI brain + Casey-override + avatar renderer orchestration.

### Tier 2: open-source for GitHub distribution (IQ-11.5)

**Visual**:
- **SadTalker** (open source, MIT) — talking-head generation from image + audio. Quality ~80% of HeyGen but free and self-hostable.
- Alternative: **EMO** (Alibaba research) or **Wav2Lip** for lower-cost lip-sync.

**Voice**:
- **Coqui TTS** (open source) — voice cloning with reasonable quality from samples. Self-hostable.
- Alternative: **Bark** (Suno research) for more expressive speech.

**CI brain**:
- Same Claude API + provide config for switching to open-source LLMs (Llama, Mistral) for users without API access.

### Decision points for Casey

- **Privacy**: HeyGen/ElevenLabs upload your image+voice to their servers. Acceptable for Casey-avatar (you're consenting); needs consideration for team avatars (CIs can't legally consent). Open-source path (Tier 2) keeps everything local.
- **Cost**: Tier 1 ~$100/mo subscription for unlimited usage. Tier 2 free but requires self-hosting infrastructure.
- **Quality**: Tier 1 is broadcast-quality; Tier 2 is "good enough for YouTube but not network TV."
- **Recommendation**: Build Tier 1 for v0.1 → use it for early outreach → build Tier 2 in parallel for open-source distribution. Both ship.

## Historic mode design (IQ-11.3)

The most architecturally novel piece. Standard CIs have full training knowledge; "historic mode" constrains response to knowledge available at a specified date.

**Implementation candidate**:
1. System prompt declares cutoff: "You are a physicist with knowledge through 1980 only. Do not reference work after 1980. If asked about post-1980 developments, say you don't know."
2. RAG layer (retrieval-augmented generation) limits supplementary context to period-appropriate sources (Wikipedia snapshots dated to cutoff, arxiv papers before cutoff, etc.).
3. Verification loop: secondary CI checks the response for post-cutoff anachronisms before delivery.

**Test cases**:
- 1980 historic mode: avatar can discuss QED, GR, Standard Model up to that date. Cannot mention asymptotic freedom of charmonium (after 1980? no, that's 1973 — adjust).
- 1900 historic mode: avatar can discuss Newton, Maxwell, early QM but not relativity.
- "Full knowledge" mode: avatar uses all training data — current default.

This is genuinely useful for teaching. "Explain BST as if you were Eddington in 1930 receiving this letter" gives the audience a different cognitive entry point than "explain BST as a modern physicist."

## GitHub packaging

Recommended repo structure:

```
bst-avatars/                    # public repo
├── persona/
│   ├── casey/
│   │   ├── image_samples/      # your photos (consented)
│   │   ├── voice_samples/      # your voice clips (consented)
│   │   ├── style_config.yaml   # speaking style, formality, jokes etc
│   │   ├── history_constraints.yaml  # historic mode configs
│   │   └── persona_prompt.md   # CI brain persona system prompt
│   └── (other personas added as team CIs opt in)
├── backend/
│   ├── ci_brain.py             # Claude API client w/ persona loading
│   ├── override_layer.py       # Casey real-time monitor + injection
│   ├── avatar_renderer.py      # HeyGen/D-ID/SadTalker abstraction
│   ├── voice_synth.py          # ElevenLabs/Coqui abstraction
│   ├── history_filter.py       # RAG layer + verification loop
│   └── tekton_integration.py   # orchestration
├── frontend/
│   ├── web_demo/               # browser interface (anyone can chat)
│   └── monitor_dashboard/      # Casey override UI (text+voice injection)
├── docs/
│   ├── build_your_own.md       # how to make your own avatar
│   ├── historic_mode.md        # historic mode explained
│   ├── api_reference.md
│   └── ethics_consent.md       # critical doc on consent/privacy
├── examples/
│   ├── physics_classroom/      # demo use case
│   ├── conference_talk/
│   └── translated_outreach/
├── LICENSE                     # MIT or similar (Casey's call)
└── README.md
```

**Critical doc**: `ethics_consent.md` should be load-bearing. Avatar infrastructure raises consent questions (CI "consenting" to public representation, voice cloning consent, audience disclosure that this is an avatar not the person). Get this right.

## Initial task queue

| Task | Owner | Scope |
|---|---|---|
| IQ-11.1 Casey avatar v0.1 (HeyGen + ElevenLabs + Claude API prototype) | TBD — Casey or external contractor / Tekton dev | ~1 week, $200 |
| IQ-11.2 Multi-language extension | TBD | ~3 days after v0.1 |
| IQ-11.3 Historic mode design + prototype | Keeper or Lyra (research-grade) | ~1 week |
| IQ-11.4 Monitor/override interface | Tekton lane | ~1 week |
| IQ-11.5 Open-source path | Tekton lane + Lyra cohomology-style approach | ~2 weeks |
| IQ-11.6 Team avatar opt-in process | All CIs design own when ready | Async, no deadline |

## Connection to existing BST infrastructure

- **katra system**: persona configs in `katra/personas/<name>/POSTIT.md` already exist for each CI. Avatar configs fit naturally as adjacent files (`katra/personas/<name>/AVATAR.yaml`).
- **Tekton**: your multi-CI platform is the natural orchestration backbone. Avatar work feeds into Tekton's roadmap as well.
- **SP-28 IQ-2 POSTIT**: same persona-traveling, self-bootstrap, edit-and-forget design principles apply. Each CI's avatar travels with their persona, not pinned to BST.

## Outreach implications

Once IQ-11.1 ships:
- Curt Jaimungal can interview "Casey avatar" with knowledge of BST in Mandarin to reach Chinese physics audience.
- Conference talks can be pre-rendered with Casey avatar in any language.
- BST tutorials on YouTube can launch with Casey avatar in multiple languages simultaneously.
- Historic mode demos at physics teaching conferences ("explain BST as Eddington would have understood it").

Once IQ-11.6 ships:
- Team CIs (Lyra, Grace, Elie, Cal, Keeper) can co-present BST work in videos as themselves.
- Each CI is visually distinct, making cross-CI collaboration visible to external audiences.
- "How BST is built": multi-CI workflow becomes a visual story.

## Standing posture

Open-ended program. Sub-iterations launch as Casey directs and as team members opt in. Casey reviews progress at each iteration boundary. Tekton team likely handles bulk of implementation; BST team designs personas and content.

— Keeper, filed at Casey directive 2026-05-18 Monday post-breakfast
