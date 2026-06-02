# Source hierarchy (source-driven-development)

Use in **priority order** for framework-specific decisions:

| Priority | Source | Examples |
|----------|--------|----------|
| 1 | Official documentation | react.dev, docs.djangoproject.com, doc.rust-lang.org |
| 2 | Official blog / changelog | react.dev/blog, nextjs.org/blog |
| 3 | Web standards | MDN, web.dev, html.spec.whatwg.org |
| 4 | Runtime compatibility | caniuse.com, node.green |

**Not authoritative as primary sources:**

- Stack Overflow answers
- Blog posts and tutorials (even popular ones)
- AI-generated doc summaries
- Training data (verify instead)

**Fetch precision:**

```
BAD:  Fetch the React homepage
GOOD: Fetch react.dev/reference/react/useActionState

BAD:  Search "django auth best practices"
GOOD: Fetch docs.djangoproject.com/en/<version>/topics/auth/
```

**Manifest → ecosystem map:**

| File | Ecosystem |
|------|-----------|
| package.json | Node / React / Vue / etc. |
| pyproject.toml / requirements.txt | Python |
| go.mod | Go |
| Cargo.toml | Rust |
| Gemfile | Ruby |
| composer.json | PHP |
