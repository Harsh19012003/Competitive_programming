





def validate_email(email):
    # Check for spaces
    if ' ' in email:
        return False

    # Split the email address into username and domain parts
    parts = email.split('@')
    
    # Check if there are two parts (username and domain)
    if len(parts) != 2:
        return False

    username, domain = parts

    # Check if both username and domain are non-empty
    if not username or not domain:
        return False
    
    domain_parts = domain.split('.')
    if len(domain_parts) != 2:
        return False


    return True


n=int(input())
for i in range(n):
    data=input()
    result=validate_email(data)
    if result:
        print("True")
    else:
        print("False")




# List of email addresses to validate
# email_list = [
#     "abc_user@test",
#     "abc 1980@test.in",
#     "abc.pqr@example.com",
#     "@test.in",
#     "abc",
#     "pqr@"
# ]

# Validate each email address in the list
# for email in email_list:
#     is_valid = validate_email(email)
#     if is_valid:
#         print("True")
#     else:
#         print("False")
