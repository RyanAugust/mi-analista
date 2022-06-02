# mi-analista

A versitile class that is designed to do that quick and dirty grunt work that you don't want to have to do yourself. Think of this as a proactive RSS feed—going and fetching information for reference later. 

`grab_info` is the core function with `execute` being an intermediary, which references a `config.ini` file as instruction.

Once `config.ini` is configured to your needs the fetching of info is executed by simply issuing a `python execute.py` command.
A cron could easily be set up by building a one line bash file (`echo "python execute.py" >> run.sh;chmod +x run.sh`) which is then referenced by cron.

Output records are stored in `./records.csv` by default, however this pathing can be customized using `write_path` within `execute.py`.
