#! /bin/bash
python scripts/Discord.py
python scripts/CHNRoute.py
git add rules
git commit -m "Rules auto update. `date +"%Y-%m-%d"`"
git push
