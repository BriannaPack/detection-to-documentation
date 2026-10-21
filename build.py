"""Builds the five session pages from one shared layout.

Edit page content in PAGES below, then run `python3 build.py`.
Output: index.html and step-N/index.html.
"""
from pathlib import Path

ROOT = Path(__file__).parent

TITLE = "Detection to documentation"
SUBTITLE = "Using a ‘Revision History’ extension to support authentic student writing in the age of AI"
META = ("OLC Accelerate 2026 Discovery Session · Wed, Nov 18, 1:00–1:45 PM ET · "
        "Brianna M. Pack and Sharon K. Titus, Azusa Pacific University")
EVALUATE_URL = "https://olc.secure-platform.com/accelerate2026/gallery/rounds/82074/schedule/items/31748"

STEPS = [
    ("home", "", "Start here", "Overview"),
    ("s1", "step-1/", "Step 1", "Install"),
    ("s2", "step-2/", "Step 2", "Read the history"),
    ("s3", "step-3/", "Step 3", "Watch the replay"),
    ("s4", "step-4/", "Step 4", "Apply SHOW"),
]


def stepnav(current, base):
    items = []
    for key, path, kicker, name in STEPS:
        cur = ' aria-current="page"' if key == current else ""
        items.append(f'<a href="{base}{path}"{cur}><span>{kicker}</span>{name}</a>')
    return '<nav class="steps" aria-label="Session steps"><div class="in">' + "".join(items) + "</div></nav>"


def video(base, file, poster, label, length, captions):
    lines = "".join(f"<li>{c}</li>" for c in captions)
    return f"""<figure class="vid">
<video controls playsinline preload="metadata" poster="{base}assets/img/{poster}" aria-label="{label}">
<source src="{base}assets/video/{file}" type="video/mp4"></video>
<figcaption class="small">{length} · silent with captions on screen</figcaption>
<details class="col"><summary>Read the on-screen captions</summary><ol class="caps">{lines}</ol></details>
</figure>"""


def trybox(text):
    return f'<section class="band"><div class="in"><p class="lbl">Now try it</p><p class="try">{text}</p></div></section>'


def nextbtn(base, path, label):
    return f'<section class="sec nextrow"><div class="in center"><a class="btn" href="{base}{path}">{label} <span aria-hidden="true">→</span></a></div></section>'


SHOW_ROWS = [
    ("S", "Structure the assignment", "Set up milestones in one shared Doc, so you can see the writing process."),
    ("H", "Hold students accountable", "Enforce the requirements, like no pasting, so the process stays visible."),
    ("O", "Observe and respond", "Give feedback on the process at each milestone, so students improve."),
    ("W", "Weigh the whole picture", "Grade the whole process, not just the final product."),
]

PLAN_ROWS = [
    ("S", "Structure the assignment", "Break it into milestones in one shared Doc, and spell out the rules in the assignment itself."),
    ("H", "Hold students accountable", "Check the revision history at the first milestone, and follow through on your rules."),
    ("O", "Observe and respond", "Plan where you’ll give feedback, and have students revise in the same Doc so the history shows their growth."),
    ("W", "Weigh the whole picture", "Add the process to your rubric, such as participation and revision, not just the final product."),
]

REPLAY_CAPTIONS = [
    "Does this look like real writing?", "Real writing starts, stops, and gets revised.", "Speed changes from 1x to 2x.",
    "Two authors, each typing in bursts.", "Each author’s share of the text.", "Work happened over several sittings.",
    "Large pastes are listed with times.", "Pastes are marked on the timeline too.", "Yellow: pasted from outside the document.",
    "Green: their own text, moved. Usually fine.", "Labels are estimates, so use them as a prompt.", "Click any paste to see it happen.",
    "Or click its marker on the timeline.", "The text keeps growing a little at a time.", "Slow it to 0.25x.",
    "Jump back to just before the paste.", "Typed text builds up gradually.", "This appeared all at once.",
    "A sudden block of text is a reason to ask the student.",
]

SHOW_CAPTIONS = [
    "How do you make your students SHOW their work?", "Four rules make the process required.",
    "“Add me as an editor when your group creates this Google Doc.” Instructor sees every draft.",
    "“Do all writing directly in the Google Doc.” No pasting means a visible process.",
    "“Looking Ahead: This brainstorm is the first draft of your project proposal.” Feedback comes before the final version.",
    "“Submit the Google Doc shareable link in the Canvas submission box.” Only the original Doc keeps its history.",
    "From detection to documentation: the process is the evidence.",
]


def home(b):
    rows = "".join(f'<div class="srow"><img src="{b}assets/img/badge-{l}.png" alt="" width="64" height="64"><div><h3>{t}</h3><p>{d}</p></div></div>'
                   for l, t, d in SHOW_ROWS)
    return f"""<section class="sec"><div class="in"><h2 class="title">Make your students SHOW their work</h2>
<p class="leadc">Detection guesses from the product. Documentation shows the process.</p>
<p>AI detectors can’t show how the work was done, and they flag some students far more than others. The free ‘Revision History’ extension for Chrome replays how a Google Doc was written, so you can design assignments where the writing process is the evidence.</p></div></section>
<section class="band"><div class="in"><h2 class="sr">SHOW in four parts</h2>{rows}</div></section>
<section class="sec"><div class="in center"><p>Steps 1 to 3 show you the tool on your own Google Doc. Step 4 puts SHOW into practice.</p>
<p><a class="btn" href="{b}step-1/">Start with Step 1 <span aria-hidden="true">→</span></a></p></div></section>"""


def step1(b):
    return f"""<section class="sec"><div class="in"><h2 class="title">Install the extension</h2>
<p class="leadc">Add the free ‘Revision History’ extension to Chrome on your laptop so you can follow along in your own Google Doc. Video coming soon.</p></div></section>
{trybox('On your laptop, type <b>revisionhistory.com</b> into Chrome, click <b>Add to Chrome</b>, and pin it to your toolbar.')}
{nextbtn(b, 'step-2/', 'Next: Step 2')}"""


def step2(b):
    return f"""<section class="sec"><div class="in"><h2 class="title">Read a document’s history</h2>
<p class="leadc">Read the summary bar in a Google Doc, open Details, and see how this differs from Google Docs’ built-in version history. Video coming soon.</p></div></section>
{trybox('Open a Google Doc you’ve written over a few sittings. Read the summary bar at the top, then click <b>Details</b>.')}
{nextbtn(b, 'step-3/', 'Next: Step 3')}"""


def step3(b):
    return f"""<section class="sec"><div class="in"><h2 class="title">Watch a document being written</h2>
{video(b, 'watch-a-document-being-written.mp4', 'poster-replay.jpg', 'Video: Watch a document being written', '1 minute 53 seconds', REPLAY_CAPTIONS)}
<p class="lead">Replay a two-author document, find the pastes, and slow down to see what typed writing looks like next to text that appears all at once.</p></div></section>
{trybox('Go back to your own Google Doc. In the Revision History bar at the top, click <b>Watch Replay</b>. Try a faster speed, and if your Doc has any pastes, click a paste marker to jump to that moment.')}
{nextbtn(b, 'step-4/', 'Next: Step 4')}"""


def step4(b):
    rows = "".join(f'<div class="srow"><div class="big" aria-hidden="true">{l}</div><div><h3>{t}</h3><p>{d}</p></div></div>'
                   for l, t, d in PLAN_ROWS)
    return f"""<section class="sec"><div class="in"><h2 class="title">Make your students SHOW their work</h2>
{video(b, 'make-your-students-show-their-work.mp4', 'poster-show.jpg', 'Video: Make your students SHOW their work', '1 minute 1 second', SHOW_CAPTIONS)}
<p class="lead">A group project set up with SHOW so the revision history captures every student’s writing from the first draft.</p></div></section>
{trybox('Think of a writing assignment in one of your courses where authenticity has been a concern. How might you redesign it using the SHOW approach?')}
<section class="band band2"><div class="in"><p class="plan">As you plan, consider each part:</p>{rows}
<details class="col"><summary>Sample assignment language you can paste in</summary>
<ol class="copy"><li><b>Add me as an editor when you create this Google Doc.</b> I use the revision history to verify participation and authorship and ensure fairness. Students who do not show active involvement in the Google Doc will not receive credit.</li>
<li><b>Do all writing directly in the Google Doc.</b> The revision history is how I see your writing process, and the process is part of what this assignment asks for. Content that is written elsewhere and pasted, imported, or uploaded into the document cannot be verified, so it will receive a zero.</li></ol>
<p><b>To submit:</b> Turn on link sharing (“Anyone with the link can view”) and submit the Google Doc’s shareable link. Do not upload a Word or PDF copy.</p>
<button class="copybtn" type="button">Copy this language</button></details></div></section>"""


PAGES = [
    ("home", "", "Overview", home),
    ("s1", "step-1/", "Step 1: Install", step1),
    ("s2", "step-2/", "Step 2: Read the history", step2),
    ("s3", "step-3/", "Step 3: Watch the replay", step3),
    ("s4", "step-4/", "Step 4: Apply SHOW", step4),
]


def page(key, path, name, body):
    b = "../" if path else ""
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{name} · {TITLE}</title>
<meta name="description" content="{SUBTITLE}. OLC Accelerate 2026 Discovery Session.">
<meta property="og:title" content="{TITLE}: {name}"><meta property="og:description" content="{SUBTITLE}.">
<meta property="og:image" content="{b}assets/img/banner.jpg">
<link rel="icon" href="{b}assets/img/badge-S.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lato:wght@400;700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{b}assets/site.css"></head>
<body><a class="skip" href="#main">Skip to content</a>
<header class="hero"><div class="in"><img class="lock" src="{b}assets/img/lockup-white.png" alt="OLC Accelerate 2026 and Azusa Pacific University" width="900" height="101">
<h1>{TITLE}:</h1><p class="sub">{SUBTITLE}</p><p class="meta">{META}</p></div></header>
{stepnav(key, b)}
<main id="main">{body(b)}
<section class="take"><div class="in center"><h2 class="h2">Take it with you</h2><div class="tbtns">
<a class="tbtn" href="{b}downloads/Detection-to-Documentation-Handout.pdf">Download the handout <small>PDF</small></a>
<a class="tbtn" href="{b}downloads/Detection-to-Documentation-Slides.pdf">View the slides <small>PDF</small></a>
<a class="tbtn" href="{EVALUATE_URL}" target="_blank" rel="noopener">Evaluate this session <small>OLC</small></a>
</div></div></section></main>
<footer class="foot"><p class="names">Brianna M. Pack, MPH, MBA (<a href="mailto:bpack@apu.edu">bpack@apu.edu</a>) · Sharon K. Titus, PhD, MSN, RN (<a href="mailto:stitus@apu.edu">stitus@apu.edu</a>) · Azusa Pacific University</p>
<p>Educational session at OLC Accelerate 2026. ‘Revision History’ is a third-party tool shown for teaching; its mention here isn’t an endorsement.</p></footer>
<script src="{b}assets/site.js" defer></script>
</body></html>
"""


if __name__ == "__main__":
    for key, path, name, body in PAGES:
        out = ROOT / path / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page(key, path, name, body))
        print("wrote", out.relative_to(ROOT))
