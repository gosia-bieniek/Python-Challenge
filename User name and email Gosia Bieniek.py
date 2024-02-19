while True:

    user_name = input("Please provide your user name:").strip()
    email = input('Please provide your email address:').strip().lower()

    if any(char.isdigit()for char in user_name):
        print('Whoops! It looks like your user name does not meet the following requirements: User name can not include numeric characters.')
        continue
    if len(user_name) > 15:
        print('Whoops!It looks like your user name does not meet the following rquirements: User name can not exceed 15 characters.')
        continue
    if not email.startswith(user_name):
        print('Whoops! It looks like your email does not meet the following requirements: email address must starts with your user name.')
        continue
    if not email.endswith('@ubs.com'):
        print("Whoops! It looks like your email does not meet the following requirements: email address must ends with @ubs.com")
        continue
    if '_' not in email:
        print("Whoops! It looks like your email does not meet the following requirements: email address must contain _")
        continue
    if ' ' in email:
        print('Whoops! It looks like your email does not meet the following requirements: address can not contain the white spaces.')
        continue
    break
print('Registration successful!')




