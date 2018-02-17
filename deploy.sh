#!/usr/bin/zsh

source ../../env_bots/bin/activate

kill `cat /tmp/insults.pid`

rm -rf build/ dist/ bot.egg-info/
python setup.py sdist
pip install -U dist/bot*
rm -rf build/ dist/ bot.egg-info/

clear

nohup insult_bot &
