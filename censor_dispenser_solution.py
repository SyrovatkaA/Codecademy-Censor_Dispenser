email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

def censor_one(email, censor):
  censorer = ''
  for letter in censor:
    if letter == ' ':
      censorer += ' '
    else:
      censorer += '█'
  email_censored = email.replace(censor, censorer)
  return email_censored

print(censor_one(email_one, 'learning algorithms'))
print('\n\n')

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

def censor_two(email, proprietary_terms):
  for term in proprietary_terms:
    censorer = ''
    for letter in term:
      if letter == ' ':
        censorer += ' '
      else:
        censorer += '█'
    email = email.replace(term, censorer)
  return email

print(censor_two(email_two, proprietary_terms))
print('\n\n')

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressing", "concerning", "horrible", "horribly", "questionable"]

def censor_three(email, censored_list, negative_words):
  email_words = []
  for x in email.split(" "):
    x1 = x.split("\n")
    for word in x1:
      email_words.append(word)
  for i in range(len(proprietary_terms)):
    for j in range(len(email_words)):
      if proprietary_terms[i] in email_words[j].lower():
        censorer = ''
        for letter in proprietary_terms[i]:
          if letter == ' ':
            censorer += ' '
          else:
            censorer += '█'
        email_words[j] = email_words[j].replace(proprietary_terms[i], censorer)
  count = 0
  for i in range(len(email_words)):
    for j in range(len(negative_words)):
      if negative_words[j] in email_words[i].lower():
        count += 1
        if count > 2:
          censorer = ''
          for letter in negative_words[j]:
            if letter == ' ':
              censorer += ' '
            else:
              censorer += '█'
          email_words[i] = email_words[i].replace(negative_words[j], censorer)
  return ' '.join(email_words)
      
print(censor_three(email_three, proprietary_terms, negative_words))
print('\n\n')

def censor_four(email, censored_list, negative_words):
  censored_list += negative_words
  email_words = []
  for x in email.split(" "):
    x1 = x.split("\n")
    for word in x1:
      email_words.append(word)
  for i in range(len(email_words)):
    for j in range(len(censored_list)):
      if censored_list[j] in email_words[i].lower():
        # word before
        censorer_before = ''
        for letter in email_words[i-1]:
          if letter == ' ':
            censorer_before += ' '
          else:
            censorer_before += '█'
        email_words[i-1] = email_words[i-1].replace(email_words[i-1], censorer_before)
        # word
        censorer = ''
        for letter in email_words[i]:
          if letter == ' ':
            censorer += ' '
          else:
            censorer += '█'
        email_words[i] = email_words[i].replace(email_words[i], censorer)
        # word after
        censorer_after = ''
        for letter in email_words[i+1]:
          if letter == ' ':
            censorer_after += ' '
          else:
            censorer_after += '█'
        email_words[i+1] = email_words[i+1].replace(email_words[i+1], censorer_after)
  return ' '.join(email_words)

print('\n\n')
print(censor_four(email_four, proprietary_terms, negative_words))