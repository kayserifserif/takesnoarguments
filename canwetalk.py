from random import choice

responses = [
  "There's not much more to say.",
  "You've just been making excuses.",
  "I've heard enough from you about this.",
  "Like I've been saying, this is just the way it is.",
  "You're still going on about this?",
  "Come on, now.",
  "I don't see why.",
  "You need to be realistic.",
  "Look, we all have obligations.",
  "You should be able to do things.",
  "I expect you to be able to do things.",
  "What else is there to say?"
]

def main():
  print("\n" + choice(responses) + "\n")
  print("\033[90m\
usage: canwetalk\n\
positional arguments:\n\
optional arguments:\
\033[0m")

if __name__ == "__main__":
  main()