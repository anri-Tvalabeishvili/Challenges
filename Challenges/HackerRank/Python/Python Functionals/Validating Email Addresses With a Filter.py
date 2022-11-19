def fun(s):
    # return True if s is a valid email, else return False
    if "@" in s and "." in s:
        username = s.split("@")[0]
        web_ext = s.split("@")[1]
        
        if "." in s.split("@")[1] and len(username) > 0:
            websitename = web_ext.split(".")[0]
            extension = web_ext.split(".")[1]
            
            if websitename.isalnum() and extension.isalpha() and 0< len(extension) <= 3:
                checker = 0
                for i in username:
                    if i.isalnum() or i in ["_","-"]:
                        checker += 1 
                        
                if checker == len(username):
                    
                    return True
                else:
                    
                    return False
                    
                
                
            else:
                return False         
        else:
            return False            
    else:
        return False

    
def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)