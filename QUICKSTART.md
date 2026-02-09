# Quick Start - TOML Address Book

## 🚀 Get Started in 3 Steps

### Step 1: Start the Container
```bash
docker-compose up -d
```

### Step 2: Open Your Browser
```
http://localhost:5000
```

### Step 3: Add Contacts!
Your data is automatically saved to TOML files in `./data/`

---

## 💾 Where Your Data Lives

**TOML Files Location:**
```
./data/individuals.toml    ← Individual contacts
./data/companies.toml      ← Company contacts
```

✅ Data persists across container restarts
✅ Human-readable format
✅ Easy to backup (just copy `./data/` folder)
✅ Can be edited manually in any text editor

---

## 📝 What's TOML?

TOML is a simple, readable configuration format. Your contacts look like this:

```toml
[contact_1]
firstName = "John"
lastName = "Doe"
email = "john.doe@example.com"
phone = "+1-555-0123"
company = "Tech Corp"
notes = "Met at conference"
```

**Benefits:**
- 👁️ Human-readable
- ✏️ Easy to edit manually
- 📦 Simple to backup
- 🔍 Great for version control (Git)
- 🚀 No database needed

---

## 🎯 Key Features

### Add Contacts
- Click **👤 Individuals** or **🏢 Companies** tab
- Fill in the form
- Click **Add** button
- Data automatically saved to TOML

### Search Contacts
- Use the search box to filter instantly
- Searches all fields

### Export Your Data
- **📝 Export TOML**: Download the raw TOML file
- **📊 Export Excel**: Get a spreadsheet (.xlsx)
- **📄 Export PDF**: Get a formatted PDF report

### Edit & Delete
- **Edit**: Click yellow "Edit" button → make changes → save
- **Delete**: Click red "Delete" button → confirm

---

## 💾 Backup Your Data

### Quick Backup
```bash
cp -r ./data ./data-backup
```

### Dated Backup
```bash
cp -r ./data ./data-backup-$(date +%Y%m%d)
```

### Restore from Backup
```bash
cp -r ./data-backup/* ./data/
docker-compose restart
```

---

## 🔧 Common Commands

**Start:**
```bash
docker-compose up -d
```

**Stop:**
```bash
docker-compose down
```

**Restart:**
```bash
docker-compose restart
```

**View logs:**
```bash
docker-compose logs -f
```

**Rebuild after changes:**
```bash
docker-compose up -d --build
```

---

## 📂 View Your TOML Files

You can open and edit the TOML files directly!

**On Linux/Mac:**
```bash
cat ./data/individuals.toml
nano ./data/individuals.toml
```

**On Windows:**
```cmd
notepad data\individuals.toml
```

**After manual edits:**
```bash
docker-compose restart
```

---

## 🆚 Why TOML Storage?

| Feature | TOML Files | Database |
|---------|-----------|----------|
| Setup | ✅ Zero config | ❌ Complex |
| Readable | ✅ Human-readable | ❌ Binary |
| Backup | ✅ Copy files | ⚠️ Export/Import |
| Edit | ✅ Any text editor | ❌ SQL/Tools |
| Portable | ✅ Copy anywhere | ⚠️ Depends |
| Version Control | ✅ Perfect for Git | ❌ Difficult |

---

## 🎨 Customizing Fields

Want to add custom fields?

1. **Edit** `static/index.html` → add form field
2. **Edit** `app.py` → add field to API
3. **Rebuild**: `docker-compose up -d --build`

See the full README.md for detailed instructions!

---

## 🐛 Troubleshooting

### Port already in use?
Edit `docker-compose.yml`:
```yaml
ports:
  - "3000:5000"  # Change to any available port
```

### Data not saving?
```bash
# Check data directory exists
ls -la ./data/

# Check permissions
chmod -R 755 ./data/

# Restart
docker-compose restart
```

### Container won't start?
```bash
docker-compose logs
docker-compose up -d --build
```

### Want to reset everything?
```bash
docker-compose down
rm -rf ./data/*
docker-compose up -d
```

---

## 💡 Pro Tips

1. **Regular backups**: Copy `./data/` folder weekly
2. **Version control**: Add to Git for history tracking
3. **Manual edits**: Edit TOML files directly when needed
4. **Share data**: Just share the `./data/` folder
5. **Migration**: Export TOML → copy to new system

---

## 🎉 That's It!

You now have a fully functional address book with:
- ✅ TOML file storage
- ✅ Beautiful web interface
- ✅ Export to Excel/PDF
- ✅ Full CRUD operations
- ✅ Persistent data storage

**Need more details?** Check the full **README.md**

**Happy organizing!** 📇
