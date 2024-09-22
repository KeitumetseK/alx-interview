# 0x06 - Star Wars Characters

## Description
This project involves writing a Node.js script that interacts with the Star Wars API to print the names of all characters in a specific Star Wars movie. The movie is identified by an ID, which is passed as a positional argument to the script. The character names are printed in the order they appear in the `/films/` endpoint's `characters` list.

## Requirements
- **Node.js Version:** 10.14.x
- **Environment:** Ubuntu 20.04 LTS
- **Modules Used:** 
  - `request` (for making HTTP requests)
  - `semistandard` (for ensuring code compliance)

### Coding Standards
- All code must adhere to semistandard (Standard + semicolons).
- Code should also follow the AirBnB JavaScript style guide.
- All files must end with a new line.
- The first line of each script must be `#!/usr/bin/node`.
- Files must be executable.
- The length of files will be tested using `wc`.

## Installation

1. **Install Node 10:**
   ```bash
   curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
   sudo apt-get install -y nodejs

