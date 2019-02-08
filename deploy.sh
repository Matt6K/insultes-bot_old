#!/usr/bin/zsh

source ../bots_venv/bin/activate

kill `cat /tmp/insults.pid`

rm nohup.out
rm -rf build/ dist/ bot.egg-info/
python setup.py sdist
pip install -U dist/bot*
rm -rf build/ dist/ bot.egg-info/
sleep 1
rehash
clear
insult_bot
