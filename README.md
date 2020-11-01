# Trivia

Simple Trivia Game for your terminal

> Notes for reviewers:
> - My goal was to focus on implementation and structuring the program to be flexible, with isolated functionality to be able to easily upgrade/update/extend features. \
For example, the way the trivia displayed can be easily changed with any graphics lib or whatever way you want, the only constraint is to keep methods named the same, so the game class can recognise them and send message to render. As a demonstration there is a Curses renderer class (Which probably not stable but shows how renderers can be swapped)
> - I didn't focus on UIUX this time. You can check my Bechance for some visual aesthetics though :) 
> - This was done in 2 days, so forgive me for inconsistent commentaries, style, unused functionality, and luck of tests ^_^
> - But I encourage you to check out commit history to have better sense of my development process :) 

## Usage
Dependencies: `python3.7+`, `pytest==6.1.0`, `readchar==2.0.1`

Install dependencies
```bash
pip3 install -r requirements.txt
```
Run
```bash
python3 app.py
```


- You can also add custom trivias in JSON format to the `asset` folder and run the game.
game will cutch all JSONs, check them to be a valid format for the game and add them up.
- Trivias are chosen randomly.
- Note that if JSON is not valid it will be just skipped. To check the reason JSON is not valid write `True` for `asset_debug` in config:
```python
debug=False
asset_debug=True
```

To run tests use
```bash
pytest -v tests
```

> Note: Please make sure your terminal width is large enough to avoid visual bugs