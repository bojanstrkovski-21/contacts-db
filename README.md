# Address Book Manager - TOML Storage Edition

A modern, containerized address book application that stores all contacts in **TOML files** for easy human-readable configuration and backup.

## 🎯 Key Features

### 💾 **TOML File Storage**
- All contacts stored in `.toml` files
- Human-readable format
- Easy to edit manually if needed
- Stored in Docker volume for persistence

### 📋 **Dual Contact Types**
- **Individuals**: Name, email, phone, mobile, job title, company, birthday, address, notes
- **Companies**: Company name, industry, email, phone, fax, website, contact person, tax ID, address, notes

### ✨ **Core Functionality**
- ✅ Add, edit, and delete contacts
- ✅ Real-time search/filter
- ✅ Export to **TOML** (native format)
- ✅ Export to **Excel** (.xlsx)
- ✅ Export to **PDF** (formatted tables)
- ✅ RESTful API backend
- ✅ Persistent Docker volume storage

## 📁 Where Contacts Are Stored

Contacts are stored in **TOML files** inside the Docker container at `/data/`:

```
/data/
  ├── individuals.toml    # All individual contacts
  └── companies.toml      # All company contacts
```

These files are **persisted** in a Docker volume mapped to `./data/` on your host machine, so:
- ✅ Data survives container restarts
- ✅ Data survives container rebuilds
- ✅ You can backup by copying the `./data/` folder
- ✅ You can edit TOML files directly if needed
- ✅ Data is portable and human-readable

## 🚀 Quick Start

### 1. Start the Application

```bash
docker-compose up -d
```

### 2. Access the Application

Open your browser to: **http://localhost:5000**

### 3. Your Data

Your TOML files are stored in: `./data/`

## 📝 TOML File Format

Contacts are stored in TOML format like this:

### individuals.toml
```toml
[contact_1]
firstName = "John"
lastName = "Doe"
email = "john.doe@example.com"
phone = "+1-555-0123"
mobile = "+1-555-0124"
jobTitle = "Software Engineer"
company = "Tech Corp"
birthday = "1990-05-15"
street = "123 Main St"
city = "San Francisco"
state = "CA"
postalCode = "94102"
country = "USA"
notes = "Met at conference 2024"
created_at = "2025-02-08T15:30:00"
updated_at = "2025-02-08T15:30:00"

[contact_2]
firstName = "Jane"
lastName = "Smith"
email = "jane.smith@example.com"
# ... more fields
```

### companies.toml
```toml
[contact_1]
companyName = "Acme Corporation"
industry = "Technology"
email = "info@acme.com"
phone = "+1-555-9999"
website = "https://acme.com"
contactPerson = "John Doe"
contactTitle = "Account Manager"
taxId = "12-3456789"
# ... more fields
created_at = "2025-02-08T15:30:00"
updated_at = "2025-02-08T15:30:00"
```

## 🔧 Management Commands

**Start:**
```bash
docker-compose up -d
```

**Stop:**
```bash
docker-compose down
```

**View logs:**
```bash
docker-compose logs -f
```

**Rebuild:**
```bash
docker-compose up -d --build
```

**Backup your data:**
```bash
cp -r ./data ./data-backup-$(date +%Y%m%d)
```

**Restore from backup:**
```bash
cp -r ./data-backup-20250208/* ./data/
docker-compose restart
```

## 📤 Export Options

### 1. **Export to TOML** (Native Format)
Click "📝 Export TOML" to download the raw TOML file
- Perfect for backups
- Can be edited and re-imported
- Human-readable

### 2. **Export to Excel**
Click "📊 Export Excel" for spreadsheet format
- Good for data analysis
- Compatible with Excel, Google Sheets, etc.

### 3. **Export to PDF**
Click "📄 Export PDF" for formatted reports
- Professional looking
- Ready to print or share

## 🔌 API Endpoints

The application provides a RESTful API:

### Individuals
- `GET /api/individuals` - Get all individuals
- `POST /api/individuals` - Add new individual
- `PUT /api/individuals/<id>` - Update individual
- `DELETE /api/individuals/<id>` - Delete individual
- `GET /api/export/individuals/toml` - Export to TOML

### Companies
- `GET /api/companies` - Get all companies
- `POST /api/companies` - Add new company
- `PUT /api/companies/<id>` - Update company
- `DELETE /api/companies/<id>` - Delete company
- `GET /api/export/companies/toml` - Export to TOML

## 🛠️ Customizing Fields

To add or modify fields:

1. **Update the frontend form** (`static/index.html`):
```html
<div class="form-group">
    <label>New Field</label>
    <input type="text" name="newField">
</div>
```

2. **Update the backend API** (`app.py`):
```python
contact_data = {
    # ... existing fields ...
    'newField': formData.get('newField')
}
```

3. **Rebuild:**
```bash
docker-compose up -d --build
```

## 🔍 Technical Stack

**Backend:**
- Python 3.11
- Flask (web framework)
- TOML library for parsing/writing

**Frontend:**
- HTML5/CSS3/JavaScript
- SheetJS (Excel export)
- jsPDF (PDF export)

**Infrastructure:**
- Docker
- Docker Compose
- Volume-based persistence

**Storage:**
- TOML files in `/data/`
- Mapped to `./data/` on host

## 📊 Data Structure

Each contact is stored with:
- Unique ID (e.g., `contact_1`, `contact_2`)
- All user-entered fields
- `created_at` timestamp (ISO 8601)
- `updated_at` timestamp (ISO 8601)

## 🔐 Data Security

- All data stored locally on your machine
- No external API calls (except CDN for libraries)
- No telemetry or tracking
- Full control over your data

## 🆚 Advantages of TOML Storage

✅ **Human-Readable**: Easy to read and edit manually
✅ **Version Control Friendly**: Great for Git
✅ **Simple Format**: No complex database setup
✅ **Portable**: Copy files anywhere
✅ **Backup-Friendly**: Just copy the `./data/` folder
✅ **Debuggable**: Open files in any text editor
✅ **No Database**: No PostgreSQL/MySQL needed

## 📦 File Locations

```
addressbook-toml/
├── app.py                  # Flask backend API
├── requirements.txt        # Python dependencies
├── Dockerfile             # Docker build instructions
├── docker-compose.yml     # Docker orchestration
├── static/
│   └── index.html        # Frontend application
└── data/                 # TOML data files (created on first run)
    ├── individuals.toml  # Individual contacts
    └── companies.toml    # Company contacts
```

## 🐛 Troubleshooting

**Port already in use?**
Edit `docker-compose.yml`:
```yaml
ports:
  - "3000:5000"  # Change 3000 to any available port
```

**Data not persisting?**
Check that `./data/` directory exists and has write permissions:
```bash
ls -la ./data/
```

**Can't access the application?**
Check if container is running:
```bash
docker-compose ps
docker-compose logs
```

**Want to reset all data?**
```bash
docker-compose down
rm -rf ./data/*
docker-compose up -d
```

## 💡 Tips & Tricks

1. **Backup regularly**: `cp -r ./data ./data-backup-$(date +%Y%m%d)`
2. **Edit TOML manually**: Open `./data/individuals.toml` in any text editor
3. **Version control**: Add `./data/*.toml` to Git for versioning
4. **Import data**: Place your TOML files in `./data/` and restart
5. **Export for migration**: Use "Export TOML" to move data between systems

## 📄 License

Free to use and modify for personal or commercial purposes.

## 🤝 Support

For issues:
1. Check Docker logs: `docker-compose logs`
2. Verify data files exist: `ls -la ./data/`
3. Check file permissions
4. Try rebuilding: `docker-compose up -d --build`

---

**Enjoy your TOML-powered address book!** 📇✨
# contacts-db
