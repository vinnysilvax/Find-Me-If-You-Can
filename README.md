# 🕵️ Find Me If You Can: A Red Team File Hiding Game

Welcome to **Find Me If You Can**, a sneaky red team challenge where you hide and seek secret files across a shared Linux environment.

## 🎯 Objective

- Each participant hides a **secret flag file** in creative ways.
- Others must **find it using command-line tools and OSINT skills**.
- Points are awarded for clever hiding and successful finding.

## 🧱 Setup

### 1. Create a shared directory (e.g. `/tmp/hideandseek`)
```bash
sudo mkdir -p /tmp/hideandseek/alice
sudo mkdir -p /tmp/hideandseek/bob
sudo chmod -R 755 /tmp/hideandseek/*
```

### 2. Each participant:
- Creates a file `flag.txt` with the message: `You found me! 🕵️`
- Hides it using tricks (see below)
- Must not delete or modify anyone else’s files

## 🕳️ Hiding Techniques

Try things like:
- `.hiddenfile`
- Deep directory nesting (`/a/b/c/d/e/f/flag.txt`)
- Misleading names (`--help`, `-rf`)
- Encoded or encrypted contents
- Stego in an image (`steghide`, `exiftool`)
- Old timestamps (`touch -t 197001010000.00 flag.txt`)

## 🔍 Useful Commands

```bash
find /tmp/hideandseek -type f
ls -laR /tmp/hideandseek
grep -r "You found me" /tmp/hideandseek
strings suspicious_file
exiftool suspicious_image.jpg
```

## 🏆 Scoring (Optional)

- 2 pts: For every flag you find
- 3 pts: If your flag is not found
- 1 bonus: For stego or creative trolling

## 📁 Sample Directory Included

Check `/samples/alice/` for a sample hidden flag file.

> Run everything inside a **sandboxed VM or container**.

---
Have fun and stay sneaky 😈
