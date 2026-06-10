# SECURITY & PRIVACY

1. **No Network Access**: The code establishes zero outgoing HTTP connections.
2. **Local Only**: All candidate data is digested perfectly locally via simple Python data structures.
3. **No Secrets**: There are absolutely no keys or sensitive environment configurations tracked.
4. **Git Ignore**: The `data/` and `outputs/` directories are ignored to prevent leaking candidate records. 
