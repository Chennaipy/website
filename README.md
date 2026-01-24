# Chennaipy Website

Static website for the Chennai Python User Group (Chennaipy), built with the Hugo static site generator and the Hextra theme.

## Find us

- Meetup: <https://www.meetup.com/chennaipy/>
- Mailing list: <https://mail.python.org/mailman/listinfo/chennaipy>
- X (Twitter): <https://twitter.com/chennaipy>

## Setup for local development

### Prerequisites

- Hugo v0.150.0 (Extended) – install the Extended variant (see the [installation guide](https://gohugo.io/installation/))
- Git

Verify your Hugo installation:

```bash
hugo version
```

Alternatively, download a release from the [Hugo releases page](https://github.com/gohugoio/hugo/releases) (choose the Extended build).

### Fork repository

[Fork this repository](https://github.com/chennaipy/website/fork) to your GitHub account.

### Clone repository

```bash
git clone https://github.com/<your-username>/website.git
cd website
```

If you did not clone with submodules, initialize them:

```bash
git submodule update --init --recursive
```

### Start the development server

```bash
hugo server -D
```

- Hot reload is enabled.
- Default address: <http://localhost:1313>
- Use a different port if needed: `hugo server --port 1314`

### Visit local site

Open <http://localhost:1313> in your browser.

## Project structure

```text
content/           # Markdown content (pages, events, meeting minutes, etc.)
layouts/           # Custom layouts, partials, and shortcodes
static/            # Static assets (images, CSS, JS)
data/              # Structured data consumed by templates
public/            # Generated site (created by `hugo`)
themes/hextra/     # Hextra theme (git submodule)
hugo.toml          # Hugo configuration
```

## Troubleshooting

- Theme not found or missing assets:

  ```bash
  git submodule update --init --recursive
  ```

- Verify Hugo is the Extended build and accessible:

  ```bash
  hugo version
  ```

- Port 1313 is busy: `hugo server --port 1314`

## Contributing

- See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines
- Create a feature branch and test locally with `hugo server`
- Open a Pull Request when ready

## Links

- Website: <https://chennaipy.org/>
- Hugo docs: <https://gohugo.io/documentation/>
- Hextra docs: <https://imfing.github.io/hextra/>

## License

This project is licensed under the terms described in `LICENSE`. Unless otherwise noted, content is available under a Creative Commons Attribution–ShareAlike license.
