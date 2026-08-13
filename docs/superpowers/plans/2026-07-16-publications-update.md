# Homepage Publications Update Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Update the homepage to show HPFA as accepted at COLM 2026 and keep StackPlanner's EMNLP 2026 submission in News only while preserving the correct author roles.

**Architecture:** Keep the existing single-page Jekyll structure and paper-card markup. Change only `_pages/about.md`, reusing the existing untracked `images/publication4.jpg`, then validate the source and generated homepage before opening the local preview.

**Tech Stack:** Jekyll, Markdown, Liquid, HTML, Bundler

---

### Task 1: Define the expected homepage content

**Files:**
- Test: shell assertions against `_pages/about.md`

- [ ] **Step 1: Run a failing source-content check**

Run:

```bash
ruby -e 's=File.read("_pages/about.md"); abort "missing COLM card" unless s.include?(%q{<div class="badge">COLM 2026</div>}); abort "missing publication4" unless s.include?(%q{images/publication4.jpg}); abort "missing HPFA title" unless s.include?("HPFA: Hypergraph-Based Paired Failure Attribution for LLM Reasoning"); abort "missing EMNLP news" unless s.include?(%q{EMNLP 2026}); abort "StackPlanner publication remains" if s.include?(%q{alt="StackPlanner"})'
```

Expected: FAIL with `missing COLM card` because the requested content has not been added yet.

### Task 2: Update homepage content

**Files:**
- Modify: `_pages/about.md:18-70`

- [ ] **Step 1: Add the July 2026 COLM announcement**

Insert this first News entry:

```markdown
- **Jul 2026**: &nbsp;🎉 Our paper **HPFA** is accepted by <span class="highlight">COLM 2026</span> (<u>Co-first Author</u>).
```

- [ ] **Step 2: Replace StackPlanner's News status**

Use this wording:

```markdown
- **Jul 2026**: &nbsp;🍀 Our paper **StackPlanner** is submitted to <span class="highlight">EMNLP 2026</span>, under review (<u>Co-author</u>).
```

- [ ] **Step 3: Add the HPFA publication card**

Insert this card first in Publications:

```html
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">COLM 2026</div><img src='images/publication4.jpg' alt="HPFA" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

<span class="paper-title">HPFA: Hypergraph-Based Paired Failure Attribution for LLM Reasoning</span>

<span class="paper-meta">Co-first Author</span>
</div>
</div>
```

- [ ] **Step 4: Remove the StackPlanner publication card**

Delete the full paper card containing:

```html
<img src='images/publication3.jpg' alt="StackPlanner" width="100%">
```

Retain the News role:

```html
<span class="paper-meta">Co-author</span>
```

- [ ] **Step 5: Run the source-content check again**

Run the Ruby command from Task 1.

Expected: exit status 0 with no output.

### Task 3: Build and preview the site

**Files:**
- Verify: `_site/index.html`

- [ ] **Step 1: Build the Jekyll site**

Run:

```bash
bundle exec jekyll build
```

Expected: exit status 0 and a generated `_site/index.html`.

- [ ] **Step 2: Verify rendered content**

Run:

```bash
ruby -e 's=File.read("_site/index.html"); %w[HPFA COLM EMNLP].each { |term| abort "missing #{term}" unless s.include?(term) }; abort "missing publication4" unless s.include?("images/publication4.jpg"); abort "missing HPFA title" unless s.include?("HPFA: Hypergraph-Based Paired Failure Attribution for LLM Reasoning"); abort "StackPlanner publication remains" if s.include?(%q{alt="StackPlanner"})'
```

Expected: exit status 0 with no output.

- [ ] **Step 3: Start the local GitHub Pages-style preview**

Run:

```bash
bundle exec jekyll serve --host 127.0.0.1 --port 4000
```

Expected: the server remains running and reports `Server address: http://127.0.0.1:4000/`.

- [ ] **Step 4: Inspect the homepage in the in-app browser**

Open `http://127.0.0.1:4000/` and confirm the news order, publication-card order, image rendering, full HPFA title, StackPlanner's absence from Publications, and author-role labels visually.
