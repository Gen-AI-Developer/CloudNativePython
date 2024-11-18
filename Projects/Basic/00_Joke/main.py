# This is simple program that prompt only jokes
print('Joke Master')
Prompt: str = "What you want me todo!"
JOKE: str = "this is simple joke"
Again: str = "Again"

# Define a Function
def _joke_bot():
    user_input = input(Prompt)
    print(user_input)
    if user_input.lower() == "joke":
        print(JOKE)
        if input(Again).lower() == "again":
            _again(True)
        else:
            _again(False)
    else:
        print("sorry ! there, I only tell Jokes...")

def _again(again:bool):
    if again:
        _joke_bot()
    else:
        print('Thanks')

_joke_bot()