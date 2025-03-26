time_capsule_hosts_lock_tool/
├── hosts_lock_tool
│   ├── cli.py                 # CLI argument parsing & main commands
│   ├── config.py              # Handles persistent lock state and configuration
│   ├── __init__.py            # Python package initialization
│   ├── lock_control.py        # Locking logic using chattr immutable flag
│   ├── password_storage.py    # Secure password handling
│   ├── scheduler.py           # Automatic unlocking using 'at'
│   └── utils.py               # Helper functions (time parsing, etc.)
├── README.md                  # (this file)
└── layout.md                  # additional project layout documentation

