# Personal Discord Music bot

![Status badge](https://img.shields.io/badge/Status-Archived-important)

**Update** (30 Nov. 2021): Try using Selenium to do Youtube scrapping for video link

## Dataset Information

🎼 A trivial bot to play music and other trivial stuff

## Requirements

There are some general library requirements for the project and some which are specific to individual methods. The general requirements are as follows.

- `discord`
- `asyncio`
- `pytube`
- `json`

**Note**: It is recommended to use **Replit** for deploying bot

## Usage

### Bot commands

1. Run `v/album` to display list of song tracks
2. Run `v/play` + `[name]` to play songs in the album
3. If cannot find song in **album**, use `v/download` + `[name]` to update new song to the album
4. `v/pause`, `v/stop`, `v/skip`, `v/leave`, `v/join` are used as usual

More features are being developed, takes time, duhh 😅🌠

## Information about other files

- `scrapping.py`: Youtube scrapping
- `ytvids.py`: Download `.mp3` files
