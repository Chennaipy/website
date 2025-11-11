# Contributing to Chennaipy

Thanks for your interest in contributing to the Chennaipy website. This site is built with Hugo (Extended) and the Hextra theme.

## Setup for local development

Follow the steps in the README:

- See [Setup for local development](README.md#setup-for-local-development)
- Prerequisite: Hugo v0.150.0 (Extended) and Git
- Start the dev server locally with:

```bash
hugo server -D
```

Preview at <http://localhost:1313> (hot reload enabled).

## Workflow (Issues and Pull Requests)

1. Pick or open an Issue describing the change you plan to make.
2. Fork the repo and create a feature branch in your fork.
3. Make your changes and verify locally (`hugo server -D`).
4. Commit and push your branch, then open a Pull Request.

For more on Pull Requests, see GitHub docs: <https://help.github.com/articles/using-pull-requests/>

---

## Contributing Minutes of Meeting (MoM)

Meeting minutes live under `content/meeting_minutes/` organized by year.

- Location: `content/meeting_minutes/<year>/`
- File name: `YYYY-MM-mom.md`

### Front matter (required)

Use Hugo front matter at the top of the file (YAML format):

```yaml
---
title: "April 2015 Meetup Minutes"
date: 2015-04-26T19:00:00+05:30
tags: ["Meeting Minutes"]
summary: "Brief summary of the meetup (1–2 sentences)."
---
```

- title: Clear and descriptive
- date: Date/time of the meetup (with timezone preferred)
- tags: Always include `Meeting Minutes` (you may add more if relevant)
- summary: A one- or two-sentence overview (shown in lists/search)

### Full file template (front matter + content)

```markdown
---
title: "April 2015 Meetup Minutes"
date: 2015-04-26T19:00:00+05:30
tags: ["Meeting Minutes"]
summary: "Brief summary of the meetup (1–2 sentences)."
---

## Summary
A short summary of the meetup.

## Talk 1: {Talk Title}
### Speaker: {Speaker Name}
Details of talk 1.

## Talk 2: {Talk Title}
### Speaker: {Speaker Name}
Details of talk 2.

## Lightning Talks
Highlights of lightning talks.

Meeting minutes contributed by [your_name](your_preferred_link)
```

> You may write in your own words and style. We discourage the use of generative AI tools to produce MoM content.

> Refer [this page](https://imfing.github.io/hextra/docs/guide/markdown/) for more about format and styles


### Preview locally

Run the site locally to ensure formatting, titles, dates, and links are correct:

```bash
hugo server -D
```

---

## Add Upcoming Event

The homepage shows an upcoming event using data from `data/upcoming_event.yaml`

- Data file: `data/upcoming_event.yaml`


### Fields

- `title` (required): A short call-to-action.
  - Example: `"Join our upcoming October meetup"`
- `date` (required): Event date in `DD-MM-YYYY` format (zero‑padded day and month). Used to automatically hide the button on/after the event date.
  - Example: `"26-10-2025"`
- `venue` (optional): Venue name.
- `venue_details` (optional): Venue details like Room name and Floor.
- `venue_link` (optional): A Google Maps URL or venue page.
- `link` (required): The full URL to the Meetup event.

> Ensure `date` uses leading zeros (e.g., `05-09-2025`, not `5-9-2025`).

### Example

```yaml
upcoming:
  title: "Join our upcoming October meetup - Saturday, October 26, 2025 at 3:00 PM (IST)"
  date: "26-10-2025"
  venue: "The Institute of Mathematical Sciences (IMSc), Chennai"
  venue_link: "https://maps.app.goo.gl/koek7CfmSa95Adbm8"
  link: "https://www.meetup.com/chennaipy/events/311517051/"
```

### Behavior

- Before the event date: shows a button linking to the Meetup event, plus the formatted date/time and venue.
- After the event date: the upcoming-event button is hidden and a general "Join Our Meetup" link is shown instead.
---

## Other content changes

For other content changes, follow the same process: update the relevant Markdown files or data files, then preview and test your changes locally.
