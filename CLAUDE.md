# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Django 5.1.5 project ("mysite") with two applications:
- **polls/** - Tutorial polling app demonstrating Django basics (Q&A voting system)
- **lcc_entries/** - Lightsaber Choreography Competition archive system (main application)

## Common Commands

```bash
# Activate virtual environment first
source env/bin/activate

# Run development server
python manage.py runserver

# Database migrations
python manage.py makemigrations
python manage.py migrate

# Run tests
python manage.py test
python manage.py test polls           # Test specific app
python manage.py test polls.tests.QuestionModelTests  # Single test class

# Django shell for debugging
python manage.py shell

# Create admin superuser
python manage.py createsuperuser
```

## Architecture

### URL Routing

Root URLs (`mysite/urls.py`) delegate to app-specific routers:
- `/polls/` → polls app (generic class-based views)
- `/lcc_entries/` → lcc_entries app (function-based views)
- `/admin/` → Django admin

### LCC Entries App Models

```
LCCComp (competition) ──┐
                        ├──> LCCEntry (main entry with YouTube link)
LCCCreator (choreographer) ─┘
                        │
LCCCompany (production) ─┘ (optional relationship)
```

Key model behaviors:
- `LCCCreator` and `LCCCompany` auto-generate slugs from names in `save()`
- `LCCEntry` status choices: Pending, Accepted, Rejected, Disqualified, Withdrawn, Live
- Competition names are hardcoded in `COMP_NAMES` tuple (LCC01-LCC12, LCC2015-2018, SC19-SC24)

### Polls App Models

Simple two-model relationship: `Question` has many `Choice` objects (CASCADE delete).

### Template Tags

Custom filter in `lcc_entries/templatetags/custom_filters.py`:
- `youtube_embed` - Converts YouTube URLs to embeddable format

## Code Patterns

- **URL namespacing**: Use `polls:detail` or `lcc_entries:entry` for reverse lookups
- **Templates**: Located in `<app>/templates/<app>/` directories
- **Admin inlines**: LCCCreatorAdmin and LCCCompAdmin use LCCEntry inlines for batch management
