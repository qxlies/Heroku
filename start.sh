#!/bin/bash
source /venv/bin/activate
nohup python -m hikka --root --no-web > bot.log 2>&1 &
echo $! > bot.pid
